#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>

namespace {
constexpr int kVariables = 15;
constexpr int kClauses = 20;
constexpr int kVertices = 50;
constexpr int kTarget = 15;
constexpr int kDegree = 3;

constexpr int clauses[kClauses][3] = {
    {1, 9, -11}, {-4, -10, -13}, {1, -9, -14}, {2, 6, 14},
    {-5, -6, 15}, {2, -3, 15}, {3, 5, -9}, {-6, -12, -15},
    {-1, 5, -11}, {4, -7, -15}, {-2, 8, -12}, {3, 9, 11},
    {-4, -8, 10}, {7, -8, 13}, {4, 7, -13}, {-2, -7, 14},
    {-3, 11, -14}, {8, 10, 12}, {-10, 12, 13}, {-1, -5, 6}
};

struct Stats {
    std::uint64_t nodes = 0;
    std::uint64_t branches = 0;
    std::uint64_t bound_leaves = 0;
    std::uint64_t cardinality_leaves = 0;
    std::uint64_t dead_leaves = 0;
};

class CertificateGenerator {
public:
    CertificateGenerator() {
        for (int j = 0; j < kVariables; ++j) {
            add_edge(2 * j, 2 * j + 1);
        }
        for (int c = 0; c < kClauses; ++c) {
            const int clause_vertex = 30 + c;
            for (int p = 0; p < 3; ++p) {
                const int literal = clauses[c][p];
                const int variable = std::abs(literal) - 1;
                const int literal_vertex = 2 * variable + (literal > 0 ? 1 : 0);
                add_edge(literal_vertex, clause_vertex);
            }
        }
        for (int v = 0; v < kVertices; ++v) {
            closed_[v] = open_[v] | (1ULL << v);
            if (__builtin_popcountll(open_[v]) != kDegree) {
                throw std::runtime_error("constructed graph is not cubic");
            }
        }
    }

    void write(const std::string& output_path) {
        std::ofstream out(output_path, std::ios::binary);
        if (!out) throw std::runtime_error("cannot open output file");
        out << "IDS15_TREE_V1\n";
        emit(out, 0, 0);
        if (!out) throw std::runtime_error("write failure");
    }

    const Stats& stats() const { return stats_; }

private:
    std::array<std::uint64_t, kVertices> open_{};
    std::array<std::uint64_t, kVertices> closed_{};
    const std::uint64_t full_ = (1ULL << kVertices) - 1ULL;
    Stats stats_{};

    void add_edge(int u, int v) {
        if (u < 0 || v < 0 || u >= kVertices || v >= kVertices || u == v) {
            throw std::runtime_error("invalid edge");
        }
        if (((open_[u] >> v) & 1ULL) != 0) {
            throw std::runtime_error("duplicate edge");
        }
        open_[u] |= 1ULL << v;
        open_[v] |= 1ULL << u;
    }

    void emit(std::ofstream& out, std::uint64_t dominated, int size) {
        ++stats_.nodes;

        // The certificate proves that no independent dominating set has size
        // at most kTarget. Once a branch has selected kTarget+1 vertices, it is
        // closed regardless of what remains undominated.
        if (size > kTarget) {
            out << "C\n";
            ++stats_.cardinality_leaves;
            return;
        }

        if (dominated == full_) {
            throw std::runtime_error("found an independent dominating set of size <= target");
        }

        const std::uint64_t undominated = full_ & ~dominated;
        const int remaining = __builtin_popcountll(undominated);
        const int additions_needed = (remaining + kDegree) / (kDegree + 1);
        if (size + additions_needed > kTarget) {
            out << "B\n";
            ++stats_.bound_leaves;
            return;
        }

        int witness = -1;
        int fewest = std::numeric_limits<int>::max();
        std::uint64_t candidates = 0;
        std::uint64_t scan = undominated;
        while (scan) {
            const int w = __builtin_ctzll(scan);
            scan &= scan - 1;
            const std::uint64_t c = closed_[w] & ~dominated;
            const int count = __builtin_popcountll(c);
            if (count < fewest) {
                fewest = count;
                witness = w;
                candidates = c;
                if (count == 0) break;
            }
        }
        if (witness < 0) throw std::runtime_error("failed to select branch witness");

        if (candidates == 0) {
            out << "X " << witness << '\n';
            ++stats_.dead_leaves;
            return;
        }

        out << "P " << witness << '\n';
        ++stats_.branches;
        while (candidates) {
            const int x = __builtin_ctzll(candidates);
            candidates &= candidates - 1;
            emit(out, dominated | closed_[x], size + 1);
        }
    }
};
}  // namespace

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: " << argv[0] << " OUTPUT_TREE\n";
        return 2;
    }
    try {
        CertificateGenerator generator;
        generator.write(argv[1]);
        const Stats& s = generator.stats();
        std::cout << "CERTIFICATE_GENERATED nodes=" << s.nodes
                  << " branches=" << s.branches
                  << " bound_leaves=" << s.bound_leaves
                  << " cardinality_leaves=" << s.cardinality_leaves
                  << " dead_leaves=" << s.dead_leaves << '\n';
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "ERROR: " << e.what() << '\n';
        return 1;
    }
}
