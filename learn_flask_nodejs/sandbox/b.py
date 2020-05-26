import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random
import heapq


def test_case():
    c, d = list(map(int, input().split()))
    edges = [[] for i in range(d)]
    graph = [[] for i in range(c + 1)]
    status = list(map(int, input().split()))
    timestamp = [1001] * (c + 1)
    times = []
    ranks = []
    vis = [0] * (c + 1)
    vis[1] = 1

    for i in range(2, c + 1):
        x = int(input())
        if x < 0:
            ranks.append([-x, i])
        else:
            times.append([x, i])

    qtimes = heapq.heapify(times)
    qranks = heapq.heapify(ranks)

    for i in range(d):
        u, v = list(map(int, input().split()))
        edges[i] = [u, v, 1001]
        graph[u].append(v)
        graph[v].append(u)

    gap = 0
    count = 1
    it = 0
    ir = 0
    q = []
    rang = 0
    t = 1

    while qtimes and qranks:
        if qranks[0] < count:
            rank, idx = heapq.heappop(qranks)
            ok = False
            for i in graph[idx]:
                if timestamp[i] != 1001:
                    if not ok:
                        edges[idx][i] = t - timestamp[i]
                        timestamp[i] = t
                    else:
                        edges[idx][i] = 1000
            count += 1

        elif qranks[0] == count:
            rank, idx = heapq.heappop(qranks)
            ok = False
            for i in graph[idx]:
                if timestamp[i] != 1001:
                    if not ok:
                        t += 1
                        edges[idx][i] = t - timestamp[i]
                        timestamp[i] = t
                    else:
                        edges[idx][i] = 1000
            count += 1

        else:
            while qranks[0] > count:
                temp, idx = heapq.heappop(qtimes)
                ok = False
                for i in graph[idx]:
                    if not ok:
                        t = temp
                        edges[idx][i] = t - timestamp[i]
                        timestamp[i] = t
                    else:
                        edges[idx[i] = 1000
                        count += 1
    while qtimes:


def main():
    T = int(input())
    for i in range(1, T + 1):
        print("Case #{}: ".format(i), end="")
        test_case()


if __name__ == "__main__":
    main()

