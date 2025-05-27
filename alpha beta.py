def alphabeta(depth, node_index, is_maximizing, values, alpha, beta):
    # Terminal condition: leaf node
    if depth == 3:
        return values[node_index]
    
    if is_maximizing:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Prune
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            # Prune
            if beta <= alpha:
                break
        return best

# Leaf values (simulate a simple game tree)
values = [3, 5, 6, 9, 1, 2, 0, -1]

def alphabeta(depth, node_index, is_maximizing, values, alpha, beta):
    # Terminal condition: leaf node
    if depth == 3:
        return values[node_index]
    
    if is_maximizing:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Prune
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            # Prune
            if beta <= alpha:
                break
        return best

# Leaf values (simulate a simple game tree)
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Run alpha-beta pruning
optimal_value = alphabeta(0, 0, True, values, float('-inf'), float('inf'))

print("🎯 The optimal value is:", optimal_value)
# Run alpha-beta pruning
optimal_value = alphabeta(0, 0, True, values, float('-inf'), float('inf'))

print("🎯 The optimal value is:", optimal_value)
