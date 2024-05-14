def longest_common_subsequence(s1, s2):
    """
    Find and return the longest common subsequence between 's1' and 's2'.
    """
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    lcs = [''] * lcs_length
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs[lcs_length - 1] = s1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)


def knapsack(weights, values, W):
    """
    Solve the 0/1 knapsack problem and return the maximum total value that can be obtained with the given weights and values and a knapsack of capacity 'W'.
    """
    number_of_weights = len(weights)
    dp = [[0] * (W + 1) for _ in range(number_of_weights + 1)]

    for i in range(1, number_of_weights + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[number_of_weights][W]

def coin_change(coins, amount):
    """
    Given different coin denominations in 'coins' and a total amount 'amount', find the minimum number of coins that make up that amount.
    Return -1 if that amount cannot be made up by any combination of the coins.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins are needed for 0 

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]
