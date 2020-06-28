from binaryTree import Tree, TreeNode
import numpy as np
if __name__ == "__main__":

    bicycle_tree = Tree(0, 1, '=')
    No = bicycle_tree.add_node(0, False, 1, var_no=1, operator='=')
    bicycle_tree.add_node(No, False, 0)
    bicycle_tree.add_node(No, True, 1)
    No = bicycle_tree.add_node(0, True, 1, var_no=2, operator='=')
    bicycle_tree.add_node(No, True, 0)
    No = bicycle_tree.add_node(No, False, 1, var_no=3, operator='=')
    bicycle_tree.add_node(No, True, 0)
    bicycle_tree.add_node(No, False, 1)



    # eval tree
    #[sonnig, auto is nicht kaputt, kein schnee, muss nicht um 8 anfangen]

    x = np.array([True, False, False, False]).reshape(1,4)

    print(x, " - ", x.shape)
    print("evaluate")
    y = bicycle_tree.eval(x)
    trace = bicycle_tree.trace(x)

    print("Fahre ich mit dem Rad?:", y)
    print("Trace: ", trace)

    print("Programm ENDE")