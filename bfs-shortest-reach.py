#!/usr/bin/env python3

from collections import defaultdict


def bfs_shortest_reach(graph, start, num_vertices):
    q, marked, distances = [start], set([start]), [-1] * num_vertices
    distances[start] = 0

    while q:
        vertex = q.pop(0)

        if vertex not in graph:
            break

        for neighbor in graph[vertex]:
            if neighbor not in marked:
                distances[neighbor] = distances[vertex] + 1
                marked.add(neighbor)
                q.append(neighbor)

    del distances[start]

    print(' '.join(
        [str(distance * 6) if distance > 0 else '-1' for distance in distances]
    ))


num_queries = int(input())

for _ in range(num_queries):
    graph = defaultdict(list)

    num_vertices, num_edges = [int(value) for value in input().strip().split()]

    for _ in range(num_edges):
        u, v = [int(vertex) - 1 for vertex in input().strip().split()]

        # Add edges (u, v) and (v, u) to graph.
        graph[u].append(v)
        graph[v].append(u)

    start = int(input().strip()) - 1
    bfs_shortest_reach(graph, start, num_vertices)
