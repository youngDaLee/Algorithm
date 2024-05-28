from collections import deque

def bfs(n, k, dp):
    queue = deque([n])
    dp[n] = 0

    while queue:
        v = queue.popleft()
        if v == k:
            break

        if v*2 < len(dp) and dp[v*2] > dp[v]:
            dp[v*2] = dp[v]
            queue.append(v*2)
        if v+1 < len(dp) and dp[v+1] > dp[v]+1:
            dp[v+1] = dp[v]+1
            queue.append(v+1)
        if v-1 >= 0 and dp[v-1] > dp[v]+1:
            dp[v-1] = dp[v]+1
            queue.append(v-1)

    print(dp[k])

dp = [100000] * 200000
n, k = map(int, input().split())
bfs(n, k, dp)
