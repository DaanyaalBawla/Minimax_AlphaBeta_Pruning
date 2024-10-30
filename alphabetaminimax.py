import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, alpha=float('-inf'), beta=float('inf')):
    # Base case: targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        maxeva = float('-inf')
        leftnum = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth, alpha, beta)
        maxeva = max(maxeva, leftnum)
        alpha = max(alpha, maxeva)

        # Alpha-Beta pruning
        if beta <= alpha:
            return maxeva

        rightnum = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth, alpha, beta)
        maxeva = max(maxeva, rightnum)
        alpha = max(alpha, maxeva)

        return maxeva

    else:
        mineva = float('inf')
        leftnum = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth, alpha, beta)
        mineva = min(mineva, leftnum)
        mineva = min(beta, mineva)

        # Alpha-Beta pruning
        if beta <= alpha:
            return mineva

        rightnum = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth, alpha, beta)
        mineva = min(mineva, rightnum)
        beta = min(beta, mineva)

        return mineva



scores = [3, 5, 17, 8, -2, 5, -1, 7]
treeDepth = math.log(len(scores), 2)
print("Optimal Value: ", end="")
print(minimax(0, 0, True, scores, treeDepth))
