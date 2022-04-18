# Main function to call the Add and Print functions to display the sorted tree.

def main():
        nums = [5,3,7]
        bst = Node()
        for num in nums:
            bst.insert(num)
        print(bst.PrintOrder([]))

# Binary Search Tree Class Nodes

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

# This function inserts values into the list to be sorted. 
# Value, left and right nodes will determine where the inserted value will go

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right = Node(val)

# Fuction to print out the tree

    def PrintOrder(self, vals):
        if self.left is not None:
            self.left.PrintOrder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.PrintOrder(vals)
        return vals

main()






