def fractional_knapsack(values, weights, capacity):
    """
    Solve the fractional knapsack problem and return the maximum value that can be obtained.
    """
    ratios = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    
    ratios.sort(reverse=True)
    
    max_value = 0
    
    for ratio, weight, value in ratios:
        if capacity >= weight:
            max_value += value
            capacity -= weight
        else:
            max_value += ratio * capacity
            break
    
    return max_value

def coin_change_greedy(coins, amount):
    """
    Using a greedy approach, determine the minimum number of coins needed to make the given amount.
    If it's not possible to make the amount using the given coin denominations, return -1.
    """
    coins.sort(reverse=True)
    num_coins = 0
    i = 0
    
    while amount > 0 and i < len(coins):
        if coins[i] <= amount:
            num_coins += amount // coins[i] 
            amount %= coins[i]
        i += 1
    
    if amount == 0:
        return num_coins
    else:
        return -1

def activity_selection(activities):
    """
    Given a list of 'activities' where each activity is represented as a tuple (start_time, end_time),
    determine the maximum number of activities that can be scheduled without any conflicts.
    Return the list of selected activities.
    """
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    end_time = -1
    
    for activity in activities:
        start_time, curr_end_time = activity
        if start_time >= end_time:
            selected_activities.append(activity)
            end_time = curr_end_time
    
    return selected_activities
