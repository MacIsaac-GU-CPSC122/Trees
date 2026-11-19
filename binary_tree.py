from typing import Any
import numpy as np

class _Node:
    def __init__(self, item:Any, left: Any=None, right:Any=None):
        self._item = item
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def __str__(self) -> str:
        # in-order string
        # For PA8, you should be 
        # returning a pre-order traversal
        return self._str_helper(self._root, 0)

    def _str_helper(self, curr_node: _Node, level:int) -> str:
        if curr_node is None:
            return ""

        # In-order traversal
        # left, visit node, right
        s = "" 
        s += self._str_helper(curr_node._left, level + 1)
        # adds spacing based on the level of the node, for pretty printing
        s += f"{" "*level}{curr_node._item}\n"
        s += self._str_helper(curr_node._right, level + 1)
        return s

    def __len__(self) -> int:
        return 0 # TODO: fix this
    
    def height(self) -> int:
        return -1 # TODO: fix this

    def clear(self) -> None:
        pass # TODO: finish this
        
    def is_empty(self) -> bool:
        return False # TODO: fix this
    
    def search(self, item) -> bool:
        return False # TODO: fix this

    def add_to_first_open_spot(self, item) -> None:
        pass # TODO: finish this

    def pre_order(self) -> list[Any]:
        return [] # TODO: fix this

    def post_order(self) -> list[Any]:
        return [] # TODO: fix this

    def in_order(self) -> list[Any]:
        return [] # TODO: fix this

    def level_order(self) -> list[Any]:
        return [] # TODO: fix this
    
    # for BONUS task
    def delete(self, item) -> None:
        pass # TODO: finish this

if __name__ == "__main__":
    a = _Node("A")
    b = _Node("B")
    c = _Node("C")
    d = _Node("D")
    e = _Node("E")
    f = _Node("F")
    a._left = b
    a._right = c
    b._left = d
    b._right = e
    c._left = f
    #   A
    #  / \
    # B   C
    bt = BinaryTree()
    bt._root = a
    print(bt)

    # Code below is taking the in-order traversal code, 
    # turning it into a matrix, transposing it
    # and printing it out so it looks like a tree.
    # This was done for fun, there are much better ways
    # (ie. using level by level traversal) to 
    # do a "pretty print"
    st = str(bt)
    matrix_tree = []
    st = st.split("\n")
    n = len(st[0])
    # create a matrix based on the string
    for line in st:
        row = list(line)
        # add padding when needed
        for i in range(n-len(row)):
            row.append(" ")
        matrix_tree.append(row)
    print(matrix_tree)
    arr = np.array(matrix_tree)
    print("Matrix")
    print(arr)
    # transpose
    arr = arr.T
    st = ""
    print("Transposed Matrix")
    print(arr)
    # matrix to pretty print
    for row in arr:
        for item in row:
            st += item
        st += "\n"
    print(st)
