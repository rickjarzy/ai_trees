from binaryTree import Tree, TreeNode
import numpy as np


if __name__ == "__main__":

    # Abbildung 6.3 - S 122 - Maschinelles lernen - Jörg Forchte - 2. Auflage 2019
    bicycle_tree = Tree(0, 1, '=')                                      # root node
    No = bicycle_tree.add_node(0, False, 1, var_no=1, operator='=')     # attach a descission node on the False Branch
    bicycle_tree.add_node(No, False, 0)                                 # add a leaf to the False Branch
    bicycle_tree.add_node(No, True, 1)                                  # add a leaf to the False Branch
    No = bicycle_tree.add_node(0, True, 1, var_no=2, operator='=')      # add decission node to the True branch
    bicycle_tree.add_node(No, True, 0)                                  # add a leaf to the True decission branch
    No = bicycle_tree.add_node(No, False, 1, var_no=3, operator='=')    # add a decission node to the False branch
    bicycle_tree.add_node(No, True, 0)                                  # add a leaf to the decission True branch
    bicycle_tree.add_node(No, False, 1)                                 # add a leaf to the decission False branch

    # eval tree
    #[sonnig, auto is nicht kaputt, kein schnee, muss nicht um 8 anfangen]

    x = np.array([True, False, False, False]).reshape(1,4)
    #x = np.random.randint(2, size=(10,4))

    print(x, " - ", x.shape)
    print("evaluate")
    y = bicycle_tree.eval(x)
    print("y: ", y)
    print("Fahre ich mit dem Rad?:", y)
    print("Programm ENDE")