class BinaryTree:
    def __init__(self, node):
        self.node = node
        self.count = 1
        self.left_child = None
        self.right_child = None

    def insert_child(self, child):
        count = 0
        current = self
        while True:
            if child > current.node:
                count += current.count
                if current.right_child is not None:
                    current = current.right_child
                else: 
                    current.right_child = BinaryTree(child)
                    return count
            else:
                current.count += 1
                if current.left_child is not None:
                    current = current.left_child
                else: 
                    current.left_child = BinaryTree(child)
                    return count
        
def smaller(arr):
    tree, res = BinaryTree(arr[-1]), [0]
    for i in range(len(arr) - 2, -1, -1):
        res.append(tree.insert_child(arr[i]))
    return res[::-1]