#!python


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    # def __repr__(self):
    #     """Return a string representation of this binary tree node."""
    #     return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""

        if self.is_leaf():
            return 0

        return 1 + max(self.left.height() if self.left is not None else 0,
                       self.right.height() if self.right is not None else 0)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: O(1) when tree is empty, or absurdly unbalanced
        Worst case running time: O(log(n)) when parent node is the second to last"""

        new_node = BinaryTreeNode(item)

        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = new_node
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item)
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            # set the parent's left child to the new node
            parent.left = new_node
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            # set the parent's right child to the new node
            parent.right = new_node
        # Increase the tree size
        self.size += 1

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: O(log(n)),
        TODO: Worst case running time: O(log(n)), """
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent


    def _find_parent_node_recursive(self, item, node="None", parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: O(log(n)),
        TODO: Worst case running time: O(log(n)), """
        # Start with the root node and keep track of its parent

        if node == "None":
            node = self.root
            parent = None

        # Check if the given item matches the node's data
        if node is  None:
            return parent

        if item == node.data:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Update the parent and descend to the node's left child
            parent = node
            return self._find_parent_node_recursive(item, node.left, parent)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Update the parent and descend to the node's right child
            parent = node
            return self._find_parent_node_recursive(item, node.right, parent)


    # This space intentionally left blank (please do not delete this comment)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    # def _traverse_in_order_recursive(self, node, visit):
    #     """Traverse this binary tree with recursive in-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse left subtree, if it exists
    #     ...
    #     # TODO: Visit this node's data with given function
    #     ...
    #     # TODO: Traverse right subtree, if it exists
    #     ...
    #
    # def _traverse_in_order_iterative(self, node, visit):
    #     """Traverse this binary tree with iterative in-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse in-order without using recursion (stretch challenge)
    #
    # def items_pre_order(self):
    #     """Return a pre-order list of all items in this binary search tree."""
    #     items = []
    #     if not self.is_empty():
    #         # Traverse tree pre-order from root, appending each node's item
    #         self._traverse_pre_order_recursive(self.root, items.append):
    #     # Return pre-order list of all items in tree
    #     return items
    #
    # def _traverse_pre_order_recursive(self, node, visit):
    #     """Traverse this binary tree with recursive pre-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Visit this node's data with given function
    #     ...
    #     # TODO: Traverse left subtree, if it exists
    #     ...
    #     # TODO: Traverse right subtree, if it exists
    #     ...
    #
    # def _traverse_pre_order_iterative(self, node, visit):
    #     """Traverse this binary tree with iterative pre-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse pre-order without using recursion (stretch challenge)
    #
    # def items_post_order(self):
    #     """Return a post-order list of all items in this binary search tree."""
    #     items = []
    #     if not self.is_empty():
    #         # Traverse tree post-order from root, appending each node's item
    #         self._traverse_post_order_recursive(self.root, items.append):
    #     # Return post-order list of all items in tree
    #     return items
    #
    # def _traverse_post_order_recursive(self, node, visit):
    #     """Traverse this binary tree with recursive post-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse left subtree, if it exists
    #     ...
    #     # TODO: Traverse right subtree, if it exists
    #     ...
    #     # TODO: Visit this node's data with given function
    #     ...
    #
    # def _traverse_post_order_iterative(self, node, visit):
    #     """Traverse this binary tree with iterative post-order traversal (DFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Traverse post-order without using recursion (stretch challenge)
    #
    # def items_level_order(self):
    #     """Return a level-order list of all items in this binary search tree."""
    #     items = []
    #     if not self.is_empty():
    #         # Traverse tree level-order from root, appending each node's item
    #         self._traverse_level_order_iterative(self.root, items.append):
    #     # Return level-order list of all items in tree
    #     return items
    #
    # def _traverse_level_order_iterative(self, start_node, visit):
    #     """Traverse this binary tree with iterative level-order traversal (BFS).
    #     Start at the given node and visit each node with the given function.
    #     TODO: Running time: ??? Why and under what conditions?
    #     TODO: Memory usage: ??? Why and under what conditions?"""
    #     # TODO: Create queue to store nodes not yet traversed in level-order
    #     queue = ...
    #     # TODO: Enqueue given starting node
    #     ...
    #     # TODO: Loop until queue is empty
    #     while ...:
    #         # TODO: Dequeue node at front of queue
    #         node = ...
    #         # TODO: Visit this node's data with given function
    #         ...
    #         # TODO: Enqueue this node's left child, if it exists
    #         ...
    #         # TODO: Enqueue this node's right child, if it exists
    #         ...


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root.data))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
