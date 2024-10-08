
# program 1:
def minimax(node, depth, maximizingPlayer):
    if depth == 0 or not node.children:
        return node.value
    
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval


# program 2:
def minimax_alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or not node.children:
        return node.value
    
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node.children:
            eval = minimax_alpha_beta(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return maxEval
    else:
        minEval = float('inf')
        for child in node.children:
            eval = minimax_alpha_beta(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return minEval


# creating class that will be used to create the tree with its child that can be used in both programs
class Node:
    def __init__(self, value=None, children=None):
        self.value = value  # Value of the node (useful for leaf nodes)
        self.children = children if children is not None else []  # List of child nodes

# Creating the leaf nodes
leaf1 = Node(value=3)
leaf2 = Node(value=5)
leaf3 = Node(value=6)
leaf4 = Node(value=9)

# Creating intermediate nodes
nodeD = Node(children=[leaf1, leaf2])
nodeE = Node(children=[leaf3, leaf4])
nodeF = Node(children=[leaf1, leaf2]) 
nodeG = Node(children=[leaf3, leaf4])  

# Creating the higher-level nodes
nodeB = Node(children=[nodeD, nodeE])
nodeC = Node(children=[nodeF, nodeG])

# Creating the root node
root = Node(children=[nodeB, nodeC])

#  Running Minimax Algorithm
minimax_value = minimax(root, depth=3, maximizingPlayer=True)
print("Minimax Value:", minimax_value)

# Creating the leaf nodes for alpha-beta-pruning 
leaf1 = Node(value=3)
leaf2 = Node(value=5)
leaf3 = Node(value=6)
leaf4 = Node(value=9)
leaf5 = Node(value=11)
leaf6 = Node(value=14)
leaf7 = Node(value=16)
leaf8 = Node(value=21)
# Creating intermediate nodes
nodeD = Node(children=[leaf1, leaf2])
nodeE = Node(children=[leaf3, leaf4])
nodeF = Node(children=[leaf5, leaf6])  
nodeG = Node(children=[leaf7, leaf8])  

# Creating the higher-level nodes
nodeB = Node(children=[nodeD, nodeE])
nodeC = Node(children=[nodeF, nodeG])

# Creating the root node
root = Node(children=[nodeB, nodeC])

#Running Minimax with Alpha-Beta Pruning
minimax_ab_value = minimax_alpha_beta(root, depth=3, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True)
print("Minimax with Alpha-Beta Pruning Value:", minimax_ab_value)
