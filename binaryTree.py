import numpy as np

class TreeNode:
    """
    Every tree node knows his own number and his parent id (child_of), as if its successor will be following a True or False branch
    If the TreeNode is a LeafNode ( last node of the Tree), then it has stored the value, which marks the output value
    """
    def __init__(self, number, value, child_of=None, operator='<', var_no=0):
        self.number = number
        self.child_of = child_of            # index pointing to a number in the self.nodes list from the Tree class
        self.left_true = None
        self.right_false = None
        self.value = value
        self.var_no = var_no
        self.operator = operator

    def __call__(self):
        # returns the value of the treenode if it is printed in the cmd
        return self.value

    def leaf_node(self):
        """
        Tests if the TreeNode is a leaf node. If a branch is None, it can attach a new node return True, if not return False
        :return: True/False
        """
        if self.left_true is not None and self.right_false is not None:
            return False
        else:
            return True

    def eval_condition(self, x):
        """

        :param x: feature vector?
        :return: True/False
        """

        print("- call eval_condition: \n- x: ",x)

        if self.operator == '=':
            cond = x[:, self.var_no] == self.value
        elif self.operator == '<':
            cond = x[:, self.var_no] == self.value
        else: # case >
            cond = x[:, self.var_no] > self.value

        return cond

    def trace(self, x, index=None, trace_route=None):
        """

        :param x:       feature vector
        :param index:
        :param trace_route:
        :return:
        """

        if index is None:
            index = np.arange(len(x))                       # to trace the feature vector in the batch of feature vectors e.g x[4,:]
        if trace_route is None:
            trace_route = [[] for x in range(len(x))]       # initialize empty

        for k in index:
            trace_route[k].append(self.number)

        if self.leaf_node():                                # if we are in a leaf node exit recursion
            return trace_route, index

        cond = self.eval_condition(x[index])                #
        true_index = index[cond]                            # contains all stapleindizes of the featurevectors if they where positive
        print("- true index: ", true_index)

        false_index = index[~cond]
        print("- false index: ", false_index)

        # depending of the route will the stack be handed to the one or other branch

        if self.left_true is not None and true_index.size != 0:
            trace_route = self.left_true.trace(x, true_index, trace_route)[0]
        if self.right_false is not None and false_index.size != 0:
            trace_route = self.right_false.trace(x, false_index, trace_route)[0]
        return trace_route


class Tree:
    def __init__(self, var_no, value, operator):
        self.root_node = TreeNode(0, value,  operator=operator, var_no=var_no)
        self.nodes = []
        self.leaf_nodes = []

        self.nodes.append(self.root_node)
        self.leaf_nodes.append(0)

    def add_node(self, child_of, branch, value, operator='<', var_no=0):
        """

        :param child_of:    who is de predecessor / parent node
        :param branch:      True/False
        :param value:
        :param operator:
        :param var_no:
        :return:            node number that was attached to the tree
        """

        # create a new node attach it to the node list, every node has to be a "TreeNode" first
        node = TreeNode(len(self.nodes), value, child_of=child_of, operator=operator, var_no=var_no)
        self.leaf_nodes.append(node.number)
        self.nodes.append(node)

        # node will be attached to its parent node
        parent = self.nodes[child_of]
        if branch is True:
            parent.left_true = node
        else:
            parent.right_false = node
        # if the parent node has no open True or False branch (== None) the node is no leafnode anymore and will be deleted
        if parent.left_true is not None and parent.right_false is not None:     # ????

            to_delete = self.leaf_nodes.index(parent.number)
            del self.leaf_nodes[to_delete]
        # we hand his number so we can work further on this node
        return node.number

    def trace(self, x):
        """
        gives back a route which nodes a feature vector has passed
        :param x:
        :return: list of passed nodes
        """
        trace_route = self.root_node.trace(x)[0]
        return trace_route

    def eval(self, x):
        """
        creates the route of nodes that is returned back - it uses trace method.
        takes allways the last element of the trace route and attaches it to a vector to create the real
        trace of nodes the freature vector has taken
        :param x:
        :return: numpy vector with trace of nodes the feature vector has taken
        """
        trace_route = self.trace(x)
        y = np.zeros(len(trace_route))

        for i in range(len(y)):
            y[i] = self.nodes[trace_route[i][-1]]()
        return y

