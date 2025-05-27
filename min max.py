# Min-Max Algorithm for Gaming

def min_max(depth, node_index, is_max, scores, h):
    if depth == h:
        return scores[node_index]

    if is_max:
        best = -float('inf')
        for i in range(2):
            value = min_max(depth + 1, node_index * 2 + i, False, scores, h)
            best = max(best, value)
        return best
    else:
        best = float('inf')
        for i in range(2):
            value = min_max(depth + 1, node_index * 2 + i, True, scores, h)
            best = min(best, value)
        return best

# Example usage
scores = [3, 5, 2, 9, 12, 5, 23, 23]
h = 3  # Height of the tree
result = min_max(0, 0, True, scores, h)
print("The optimal value is:", result)
