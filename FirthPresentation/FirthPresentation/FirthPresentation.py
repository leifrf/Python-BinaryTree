
class Node:

    def __init__(self, value):
        self._value = value
        self.left = None
        self.right = None
        
# This is a BinaryTree
# Note that it is not a BALANCED Binary Tree
class BinaryTree:

    def __init__(self, root):
        """
        Creates a binary tree with the given node as the root.
        Does not sanitize "root" to be a Node.

        root -- the Node to act as the root of the tree.
        """
        self.root = root

    def addNode(newValue):
        """
        Add the given value to the tree as a node.
        If it is already there, a string stating that it already exists is returned.
        If it does not already exist, the value is added as a node from the appropriate parent.

        value -- The integer to look for.
        """

        # Empty tree! Add this as the root node
        if self.root == None:
            self.root = Node(newValue)
            return

        current = self.root       
        while True:
            if current.value == newValue:
                return "Already in the tree!"
            elif current.value > newValue:
                # Found the spot to add (left)
                if current.left == None:
                    current.left = Node(newValue)
                    return "Added "+ str(newValue) +" to the tree!"
                else:
                    current = current.left
            # Implicitly, current.value < newValue
            else: 
                # Found the spot to add (right)
                if current.right == None:
                    current.right = Node(newValue)
                    return "Added "+ str(newValue) +" to the tree!"
                else:
                    current = current.right

    def hasValue(value):
        """
        Checks if the given value is in the tree.
        Returns a string stating whether or not the value was found.

        value -- The integer to look for.
        """

        current = self.root
        while current != None:
            if current.value == value:
                return "It's in the tree!"
            elif current.value > value:
                current = current.left
            # Implicitly, current.value < value
            else:
                current = current.right
        
        return "It's not in the tree!"