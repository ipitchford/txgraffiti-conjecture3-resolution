#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>

namespace {
constexpr int kVariables = 15;
constexpr int kClauses = 20;
constexpr int kVertices = 50;
constexpr int kExpectedEdges = 75;
constexpr int kDegree = 3;

// A positive integer j denotes x_j; a negative integer -j denotes not-x_j.
constexpr int clauses[kClauses][3] = {
    {1, 9, -11}, {-4, -10, -13}, {1, -9, -14}, {2, 6, 14},
    {-5, -6, 15}, {2, -3, 15}, {3, 5, -9}, {-6, -12, -15},
    {-1, 5, -11}, {4, -7, -15}, {-2, 8, -12}, {3, 9, 11},
    {-4, -8, 10}, {7, -8, 13}, {4, 7, -13}, {-2, -7, 14},
    {-3, 11, -14}, {8, 10, 12}, {-10, 12, 13}, {-1, -5, 6}
};

struct Graph {
    std::array<std::uint64_t, kVertices> open{};
    std::vector<std::pair<int, int>> edges;

    void add_edge(int u, int v) {
        if (u < 0 || v < 0 || u >= kVertices || v >= kVertices || u == v) {
            throw std::runtime_error("invalid edge");
        }
        if ((open[u] >> v) & 1ULL) {
            throw std::runtime_error("duplicate edge");
        }
        open[u] |= 1ULL << v;
        open[v] |= 1ULL << u;
        edges.emplace_back(std::min(u, v), std::max(u, v));
    }
};

Graph build_graph() {
    Graph g;
    for (int j = 0; j < kVariables; ++j) {
        g.add_edge(2 * j, 2 * j + 1);
    }
    for (int c = 0; c < kClauses; ++c) {
        const int clause_vertex = 30 + c;
        for (int p = 0; p < 3; ++p) {
            const int literal = clauses[c][p];
            const int variable = std::abs(literal) - 1;
            const int literal_vertex = 2 * variable + (literal > 0 ? 1 : 0);
            g.add_edge(literal_vertex, clause_vertex);
        }
    }
    std::sort(g.edges.begin(), g.edges.end());
    return g;
}

int graph_girth(const Graph& g) {
    int answer = std::numeric_limits<int>::max();
    for (int source = 0; source < kVertices; ++source) {
        std::array<int, kVertices> distance;
        std::array<int, kVertices> parent;
        distance.fill(-1);
        parent.fill(-1);
        std::queue<int> q;
        distance[source] = 0;
        q.push(source);
        while (!q.empty()) {
            const int u = q.front();
            q.pop();
            std::uint64_t neighbours = g.open[u];
            while (neighbours) {
                const int v = __builtin_ctzll(neighbours);
                neighbours &= neighbours - 1;
                if (distance[v] == -1) {
                    distance[v] = distance[u] + 1;
                    parent[v] = u;
                    q.push(v);
                } else if (parent[u] != v) {
                    answer = std::min(answer, distance[u] + distance[v] + 1);
                }
            }
        }
    }
    return answer;
}

bool verify_structure(const Graph& g) {
    if (static_cast<int>(g.edges.size()) != kExpectedEdges) return false;
    for (int v = 0; v < kVertices; ++v) {
        if (__builtin_popcountll(g.open[v]) != kDegree) return false;
    }
    std::array<int, kVariables> positive{};
    std::array<int, kVariables> negative{};
    for (int c = 0; c < kClauses; ++c) {
        for (int p = 0; p < 3; ++p) {
            const int literal = clauses[c][p];
            if (literal > 0) ++positive[literal - 1];
            else ++negative[-literal - 1];
        }
    }
    for (int j = 0; j < kVariables; ++j) {
        if (positive[j] != 2 || negative[j] != 2) return false;
    }

    std::array<bool, kVertices> seen{};
    std::queue<int> q;
    seen[0] = true;
    q.push(0);
    int reached = 0;
    while (!q.empty()) {
        const int u = q.front();
        q.pop();
        ++reached;
        std::uint64_t neighbours = g.open[u];
        while (neighbours) {
            const int v = __builtin_ctzll(neighbours);
            neighbours &= neighbours - 1;
            if (!seen[v]) {
                seen[v] = true;
                q.push(v);
            }
        }
    }
    return reached == kVertices;
}

bool verify_independent_dominating_set(
    const Graph& g, const int* vertices, std::size_t count
) {
    std::uint64_t witness = 0;
    for (std::size_t i = 0; i < count; ++i) {
        const int v = vertices[i];
        if (v < 0 || v >= kVertices || ((witness >> v) & 1ULL)) return false;
        witness |= 1ULL << v;
    }
    if (__builtin_popcountll(witness) != 16) return false;
    for (const auto& [u, v] : g.edges) {
        if (((witness >> u) & 1ULL) && ((witness >> v) & 1ULL)) return false;
    }
    for (int v = 0; v < kVertices; ++v) {
        if (((witness >> v) & 1ULL) == 0 && (g.open[v] & witness) == 0) return false;
    }
    return true;
}

bool verify_independent_dominating_witness(const Graph& g) {
    constexpr int simple_witness[] = {
        0, 3, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 47
    };
    constexpr int public_witness[] = {
        0, 2, 5, 7, 8, 13, 15, 30, 31, 32, 33, 35, 37, 42, 46, 48
    };
    return verify_independent_dominating_set(
               g, simple_witness, sizeof(simple_witness) / sizeof(simple_witness[0])
           ) &&
           verify_independent_dominating_set(
               g, public_witness, sizeof(public_witness) / sizeof(public_witness[0])
           );
}

bool verify_maximal_matching(const Graph& g) {
    std::uint64_t matched_vertices = 0;
    for (int j = 0; j < kVariables; ++j) {
        const int u = 2 * j;
        const int v = 2 * j + 1;
        if (((g.open[u] >> v) & 1ULL) == 0) return false;
        if ((matched_vertices >> u) & 1ULL) return false;
        if ((matched_vertices >> v) & 1ULL) return false;
        matched_vertices |= (1ULL << u) | (1ULL << v);
    }
    // A matching is maximal iff no graph edge has two unmatched endpoints.
    for (const auto& [u, v] : g.edges) {
        if (((matched_vertices >> u) & 1ULL) == 0 &&
            ((matched_vertices >> v) & 1ULL) == 0) return false;
    }
    return true;
}

// Direct exact branch-and-bound on the graph.  The state D is the union of
// closed neighbourhoods of the selected independent vertices.  A vertex
// outside D is therefore addable without violating independence.
struct IndependentDominationSearch {
    const Graph& g;
    std::array<std::uint64_t, kVertices> closed{};
    const std::uint64_t full = (1ULL << kVertices) - 1ULL;
    int best = 16;  // established by the explicit witness
    std::uint64_t nodes = 0;

    explicit IndependentDominationSearch(const Graph& graph) : g(graph) {
        for (int v = 0; v < kVertices; ++v) closed[v] = g.open[v] | (1ULL << v);
    }

    void search(std::uint64_t dominated, int size) {
        ++nodes;
        if (size >= best) return;
        if (dominated == full) {
            best = size;
            return;
        }
        const std::uint64_t undominated = full & ~dominated;
        const int remaining = __builtin_popcountll(undominated);
        const int lower_bound = (remaining + kDegree) / (kDegree + 1);
        if (size + lower_bound >= best) return;

        int fewest = std::numeric_limits<int>::max();
        std::uint64_t branch_candidates = 0;
        std::uint64_t scan = undominated;
        while (scan) {
            const int w = __builtin_ctzll(scan);
            scan &= scan - 1;
            const std::uint64_t candidates = closed[w] & ~dominated;
            const int count = __builtin_popcountll(candidates);
            if (count < fewest) {
                fewest = count;
                branch_candidates = candidates;
                if (count <= 1) break;
            }
        }

        std::vector<std::pair<int, int>> ordered;
        while (branch_candidates) {
            const int x = __builtin_ctzll(branch_candidates);
            branch_candidates &= branch_candidates - 1;
            const int gain = __builtin_popcountll(closed[x] & ~dominated);
            ordered.emplace_back(-gain, x);
        }
        std::sort(ordered.begin(), ordered.end());
        for (const auto& [negative_gain, x] : ordered) {
            (void)negative_gain;
            search(dominated | closed[x], size + 1);
        }
    }
};

struct BilateralReceipt {
    std::uint64_t total = 0;
    std::uint64_t bilateral = 0;
    std::uint64_t violations = 0;
    std::array<std::uint64_t, kVariables + 1> counts{};
    std::array<int, kVariables + 1> min_unsatisfied{};
};

BilateralReceipt verify_bilateral_lemma() {
    BilateralReceipt r;
    r.min_unsatisfied.fill(std::numeric_limits<int>::max());
    std::uint64_t assignments = 1;
    for (int j = 0; j < kVariables; ++j) assignments *= 3;
    r.total = assignments;

    std::array<int, kVariables> value{};  // 0=unassigned, 1=false, 2=true
    for (std::uint64_t code = 0; code < assignments; ++code) {
        std::uint64_t z = code;
        int unassigned = 0;
        for (int j = 0; j < kVariables; ++j) {
            value[j] = static_cast<int>(z % 3);
            z /= 3;
            if (value[j] == 0) ++unassigned;
        }

        std::uint32_t residual = 0;
        for (int c = 0; c < kClauses; ++c) {
            bool satisfied = false;
            for (int p = 0; p < 3; ++p) {
                const int literal = clauses[c][p];
                const int j = std::abs(literal) - 1;
                if (value[j] == 0) continue;
                const bool truth = value[j] == 2;
                if ((literal > 0 && truth) || (literal < 0 && !truth)) {
                    satisfied = true;
                    break;
                }
            }
            if (!satisfied) residual |= 1U << c;
        }

        bool bilateral = true;
        for (int j = 0; j < kVariables && bilateral; ++j) {
            if (value[j] != 0) continue;
            bool positive = false;
            bool negative = false;
            for (int c = 0; c < kClauses; ++c) {
                if (((residual >> c) & 1U) == 0) continue;
                for (int p = 0; p < 3; ++p) {
                    if (clauses[c][p] == j + 1) positive = true;
                    if (clauses[c][p] == -(j + 1)) negative = true;
                }
            }
            if (!positive || !negative) bilateral = false;
        }

        if (bilateral) {
            const int unsatisfied = __builtin_popcount(residual);
            ++r.bilateral;
            ++r.counts[unassigned];
            r.min_unsatisfied[unassigned] =
                std::min(r.min_unsatisfied[unassigned], unsatisfied);
            if (unsatisfied <= unassigned) ++r.violations;
        }
    }
    return r;
}

bool matches_expected_bilateral_receipt(const BilateralReceipt& r) {
    constexpr std::uint64_t expected_counts[kVariables + 1] = {
        32768, 68864, 105066, 131296, 141302, 134321, 114282, 87592,
        60260, 36402, 18335, 7151, 1967, 338, 30, 1
    };
    constexpr int expected_min[kVariables + 1] = {
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20
    };
    if (r.total != 14348907ULL || r.bilateral != 939975ULL || r.violations != 0) return false;
    for (int u = 0; u <= kVariables; ++u) {
        if (r.counts[u] != expected_counts[u] || r.min_unsatisfied[u] != expected_min[u]) return false;
    }
    return true;
}
}  // namespace

int main() {
    try {
        const Graph graph = build_graph();
        const bool structure_ok = verify_structure(graph);
        const int girth = graph_girth(graph);
        const bool witness_ok = verify_independent_dominating_witness(graph);
        const bool matching_ok = verify_maximal_matching(graph);

        IndependentDominationSearch direct_search(graph);
        const auto ids_start = std::chrono::steady_clock::now();
        direct_search.search(0, 0);
        const double ids_seconds = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - ids_start).count();

        const auto bilateral_start = std::chrono::steady_clock::now();
        const BilateralReceipt bilateral = verify_bilateral_lemma();
        const double bilateral_seconds = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - bilateral_start).count();
        const bool bilateral_ok = matches_expected_bilateral_receipt(bilateral);

        std::cout << "STRUCTURE n=" << kVertices
                  << " m=" << graph.edges.size()
                  << " degree=" << kDegree
                  << " connected=" << structure_ok
                  << " girth=" << girth << '\n';
        std::cout << "WITNESSES independent_dominating_size=16 explicit_sets=2 verified=" << witness_ok << '\n';
        std::cout << "MATCHING size=15 maximal=" << matching_ok
                  << " cubic_edge_domination_lower_bound="
                  << ((kExpectedEdges + (2 * kDegree - 2)) / (2 * kDegree - 1)) << '\n';
        std::cout << "DIRECT_IDS optimum=" << direct_search.best
                  << " search_nodes=" << direct_search.nodes
                  << " seconds=" << ids_seconds << '\n';
        std::cout << "BILATERAL checked=" << bilateral.total
                  << " bilateral=" << bilateral.bilateral
                  << " violations=" << bilateral.violations
                  << " seconds=" << bilateral_seconds << '\n';
        std::cout << "u bilateral_assignments minimum_residual_clauses\n";
        for (int u = 0; u <= kVariables; ++u) {
            std::cout << u << ' ' << bilateral.counts[u] << ' '
                      << bilateral.min_unsatisfied[u] << '\n';
        }

        const bool all_ok = structure_ok && girth == 5 && witness_ok && matching_ok &&
                            direct_search.best == 16 && bilateral_ok;
        if (!all_ok) {
            std::cerr << "VERIFICATION FAILED\n";
            return 1;
        }
        std::cout << "GRAPH_CHECK_PASSED result=mu_star_15_i_16\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "ERROR: " << e.what() << '\n';
        return 2;
    }
}
