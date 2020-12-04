class Node:
    def __init__(self, s_data, i_data):
        self.s_data = s_data
        self.i_data = i_data
        self.left = None
        self.right = None


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            if self.root.s_data > node.s_data:
                if self.root.left is None:
                    self.root.left = node
                    return
                cur = self.root.left
                while cur:
                    if cur.s_data > node.s_data:
                        if cur.left is None:
                            cur.left = node
                            return
                        cur = cur.left
                    else:
                        if cur.right is None:
                            cur.right = node
                            return
                        cur = cur.right
            else:
                if self.root.right is None:
                    self.root.right = node
                    return
                cur = self.root.right
                while cur:
                    if cur.s_data > node.s_data:
                        if cur.left is None:
                            cur.left = node
                            return
                        cur = cur.left
                    else:
                        if cur.right is None:
                            cur.right = node
                            return
                        cur = cur.right

    def search(self, value):
        cur = self.root
        while cur:
            if cur.s_data == value:
                return f'{cur.s_data}, {cur.i_data}'
            else:
                if cur.s_data > value:
                    cur = cur.left
                else:
                    cur = cur.right

    def breadth_first_traversal(self):
        """
        Traverses the binary tree and appends by level
        A breadth first search returns each node on each level and it will
        goes down the tree by level.
        :return: appends the name data to a list
        """
        travel = [self.root]
        bft_order = []
        while travel:
            cur = travel.pop(0)
            bft_order.append(cur.s_data)
            if cur.left:
                travel.append(cur.left)
            if cur.right:
                travel.append(cur.right)
        return bft_order

    def print_inorder(self, node):
        """
        inorder traverses the tree by starting at the left most node going
        to its root printing whatever is on the right and so on so forth.
        :param node: The root node
        :return: should print left, root, right
        """
        if node:
            self.print_inorder(node.left)
            print(node.s_data)
            self.print_inorder(node.right)

    def print_postorder(self, node):
        """
        postorder goes left, right and then root
        :param node: the root node
        :return: should print left, right and root
        """
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.s_data)

    def print_preorder(self, node):
        """
        preorder goes root, left and then right
        :param node: the node root
        :return: prints the list root first and then left and finally right
        """
        if node:
            print(node.s_data),
            self.print_preorder(node.left)
            self.print_preorder(node.right)


if __name__ == '__main__':
    william_node = Node('William', 5)
    ethan_node = Node('Ethan', 6)
    james_node = Node('James', 7)
    noah_node = Node('Noah', 1)
    liam_node = Node('Liam', 2)
    mason_node = Node('Mason', 3)
    jacob_node = Node('Jacob', 4)
    alex_node = Node('Alexander', 8)
    michael_node = Node('Michael', 9)
    benjamin_node = Node('Benjamin', 10)
    boys_name_tree = Bst()
    boys_name_tree.insert(william_node)
    boys_name_tree.insert(james_node)
    boys_name_tree.insert(ethan_node)
    boys_name_tree.insert(noah_node)
    boys_name_tree.insert(liam_node)
    boys_name_tree.insert(mason_node)
    boys_name_tree.insert(jacob_node)
    boys_name_tree.insert(alex_node)
    boys_name_tree.insert(michael_node)
    boys_name_tree.insert(benjamin_node)
    # searching a name in the list
    print(boys_name_tree.search('Jacob'))
    print(boys_name_tree.search('William'))
    print(boys_name_tree.search('Ethan'))
    print(boys_name_tree.search('James'))
    print(boys_name_tree.search('Liam'))
    print(boys_name_tree.search('Mason'))
    print(boys_name_tree.search('Alexander'))
    print(boys_name_tree.search('Michael'))
    print(boys_name_tree.search('Benjamin'))
    # searching my name in the list
    print(boys_name_tree.search('Noah'))
    # searching a name not in the list
    print(boys_name_tree.search('Shaun'))
    # girls name list
    # making my nodes
    isabella_node = Node('Isabella', 5)
    mia_node = Node('Mia', 6)
    abigail_node = Node('Abigail', 7)
    emma_node = Node('Emma', 1)
    olivia_node = Node('Olivia', 2)
    sophia_node = Node('Sophia', 3)
    ava_node = Node('Ava', 4)
    emily_node = Node('Emily', 8)
    charlotte_node = Node('Charlotte', 9)
    harper_node = Node('Harper', 10)
    girls_name_tree = Bst()
    # inserting my nodes
    girls_name_tree.insert(isabella_node)
    girls_name_tree.insert(mia_node)
    girls_name_tree.insert(abigail_node)
    girls_name_tree.insert(emma_node)
    girls_name_tree.insert(olivia_node)
    girls_name_tree.insert(sophia_node)
    girls_name_tree.insert(ava_node)
    girls_name_tree.insert(emily_node)
    girls_name_tree.insert(charlotte_node)
    girls_name_tree.insert(harper_node)
    # searching the names in the list
    print(girls_name_tree.search('Emily'))
    print(girls_name_tree.search('Emma'))
    print(girls_name_tree.search('Olivia'))
    print(girls_name_tree.search('Isabella'))
    print(girls_name_tree.search('Mia'))
    print(girls_name_tree.search('Abigail'))
    print(girls_name_tree.search('Sophia'))
    print(girls_name_tree.search('Ava'))
    print(girls_name_tree.search('Charlotte'))
    print(girls_name_tree.search('Harper'))
    # searching my name in the list
    print(girls_name_tree.search('Noah'))
    # searching a name not in the list
    print(girls_name_tree.search('Madelyn'))
    # Making my breadth first search
    print("\n")
    print(boys_name_tree.breadth_first_traversal())
    # Making my breadth first search
    print("\n")
    print(girls_name_tree.breadth_first_traversal())
    # depth first search in-order
    print("\n")
    boys_name_tree.print_inorder(isabella_node)
    # depth first search post-order
    print("\n")
    boys_name_tree.print_postorder(isabella_node)
    # depth first search preorder
    print("\n")
    boys_name_tree.print_preorder(isabella_node)