import collections

def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
    if n <= 1:
        return [0]

    # 무방향(양방향) 그래프 생성
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    # 첫 번째 리프 노드 추가
    leaves = []
    for i in range(n+1):
        if len(graph[i]) == 1:
            leaves.append(i)

    # 루트 노드만 남을 때까지 반복 제거
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            # 양방향이므로 제거도 두 번
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves

    return leaves