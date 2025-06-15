# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree: Node) -> int:
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    if tree.get_left_child() == None and tree.get_right_child() == None:
        return 0
    elif tree.get_left_child() != None and tree.get_right_child() == None:
        return 1 + find_tree_height(tree.get_left_child())
    elif tree.get_right_child() != None and tree.get_left_child() == None:
        return 1 + find_tree_height(tree.get_right_child())
    else:
        return 1 + max(find_tree_height(tree.get_right_child()), find_tree_height(tree.get_left_child()))

def is_heap(tree: Node, compare_func: callable) -> bool:
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    if tree.get_left_child() == None and tree.get_right_child() == None:
        return True
    elif tree.get_left_child() != None and tree.get_right_child() == None:
        if not compare_func(tree.get_left_child().get_value(), tree.get_value()):
            return False
        else:
            return is_heap(tree.get_left_child(), compare_func)
    elif tree.get_right_child() != None and tree.get_left_child() == None:
        if not compare_func(tree.get_right_child().get_value(), tree.get_value()):
            return False
        else:
            return is_heap(tree.get_right_child(), compare_func)
    else:
        if not compare_func(tree.get_right_child().get_value(), tree.get_value()) or not compare_func(tree.get_left_child().get_value(), tree.get_value()):
            return False
        else:
            return is_heap(tree.get_right_child(), compare_func) and is_heap(tree.get_left_child(), compare_func)



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    print(find_tree_height(tree1))
    print(find_tree_height(tree2))
    print(find_tree_height(tree3))
    max_heap = Node(21, Node(15, Node(7), Node(11)), Node(3, Node(2), Node(1)))
    min_heap = Node(4, Node(10, Node(18), Node(11)), Node(5, Node(7), Node(8)))
    def compare_min(child: int, parent: int) -> bool:
        return child > parent
    def compare_max(child: int, parent: int) -> bool:
        return child < parent
    print(is_heap(tree1, compare_min))
    print(is_heap(tree1, compare_min))
    print(is_heap(tree2, compare_min))
    print(compare_max(1,2))
    print(compare_min(1,2))
    print(is_heap(max_heap, compare_max))
    print(is_heap(min_heap, compare_min))

    
