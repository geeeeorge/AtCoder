from collections import defaultdict

def hamiltonian_path_exists(graph, vertex_count):
    visited = [False] * vertex_count
    paths = [None] * vertex_count

    def hamiltonian_path(v):
        visited[v] = True
        paths[position[0]] = v

        if position[0] + 1 == vertex_count:
            return True

        position[0] += 1
        for neighbor in graph[v]:
            if not visited[neighbor] and hamiltonian_path(neighbor):
                return True

        visited[v] = False
        position[0] -= 1
        return False

    position = [0]
    for start_vertex in range(vertex_count):
        if hamiltonian_path(start_vertex):
            return True
    return False


def one_character_diff(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1


def main():
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]

    graph = defaultdict(list)
    for i in range(N):
        for j in range(i + 1, N):
            if one_character_diff(words[i], words[j]):
                graph[i].append(j)
                graph[j].append(i)

    if hamiltonian_path_exists(graph, N):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
