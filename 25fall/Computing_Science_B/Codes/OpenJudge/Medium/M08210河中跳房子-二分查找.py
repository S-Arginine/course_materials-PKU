def is_possible(distance, rocks, M):
    removed = 0
    prev = 0
    for rock in rocks:
        if rock - prev < distance:
            removed += 1
        else:
            prev = rock
    return removed <= M
def max_shortest_distance(L, N, M, rocks):
    left, right = 1, L
    result = 0
    while left <= right:    #二分查找
        mid = left + (right - left) // 2
        if is_possible(mid, rocks, M):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
L, N, M = map(int, input().split())
rocks = [int(input()) for _ in range(N)]
print(max_shortest_distance(L, N, M, rocks))