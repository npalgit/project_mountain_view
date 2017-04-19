class BTNode:
    def __init__(self, val=None, l_child=None, r_child=None):
        self.val = val
        self.left = l_child
        self.right = r_child

    @staticmethod
    def print_nodes(n):
        if not n:
            return

        lhs = n.left.val if n.left else None
        rhs = n.right.val if n.right else None
        print('n={n_val}, {n_val}.left={lhs}, {n_val}.right={rhs}'.format(n_val=n.val, lhs=lhs, rhs=rhs))
        BTNode.print_nodes(n.left)
        BTNode.print_nodes(n.right)

