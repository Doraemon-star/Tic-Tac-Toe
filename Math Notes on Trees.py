# A rooted tree is a hierarchical data structure.

# A rooted tree is a collection of nodes and edges that can e organized recursiely as follows.
  # The tree has a root node with an associated value and a list of references to a collection of sutrees. 
  # The root nodes of these sutrees are the childeren of the root node for the orginal tree while the root node is the parent of the children.
  # Each node in the tree should have exactly one parent with the exception of the root which has no parent.
  # The tree is hierarchical since each subtree of the root is then guaranteed to be disjoint from the other subtrees.

# The nodes of a tree are typically classified based on their number of children. 
  # A node with no children is a leaf node.
  # Nodes with one or more children are internal(or interior) nodes.
  
# The distinction b/w leaf nodes and internal nodes allows us to specifu simple recursive definitions for several important structural quantities associated with trees.
  # The number of nodes in a tree satisfies: 
    # if the root node of the tree is a leaf: 
      # return 1
    # else:
      # return 1 + the sum of the number of nodes for each subtree
  
  # The number of leaves in a tree satisfies:
    # if the root nodes of the tree is a leaf:
      # return 1
    # else:
      # return the sum of the number of leaves for each subtree
  
  # The height of a tree is the length of the longest sequence of edges from the root to a leaf. 
  # The height can be computed recursively via: 
    # if the root node of the tree is a leaf:
      # return 0
    # else:
      # return 1 + the maximum of the heights of the subtrees

# One particularly important class of trees are binary trees in which all nodes have two or fewer children. 
  # Binary trees in which all internal nodes have exactly two nodes are called full binary trees. 
  # Full bianry trees often arise in applications involving searching and sorting.
  
"""
Python definition of basic Tree class

IMPORTANT:  Some class methods assume that instances of the Tree class
always have a single parent (or no parent for the root). See problem #8
on homework #3 for more details.
"""


class Tree:
    """
    Recursive definition for trees plus various tree methods
    """
    
    def __init__(self, value, children):
        """
        Create a tree whose root has specific value (a string)
        Children is a list of references to the roots of the subtrees.  
        """
        
        self._value = value
        self._children = children
        
        
    def __str__(self):
        """
        Generate a string representation of the tree
        Use an pre-order traversal of the tree
        """
        
        ans = "["
        ans += str(self._value)
                   
        for child in self._children:
             ans += ", "
             ans += str(child)
        return ans + "]"

    def get_value(self):
        """
        Getter for node's value
        """
        return self._value

    def children(self):
        """
        Generator to return children
        """
        for child in self._children:
            yield child
                    
    def num_nodes(self):
        """
        Compute number of nodes in the tree
        """
        ans = 1
        for child in self._children:
            ans += child.num_nodes()
        return ans
    
    def num_leaves(self):
        """
        Count number of leaves in tree
        """
        if len(self._children) == 0:
            return 1
        
        ans = 0
        for child in self._children:
            ans += child.num_leaves()
        return ans

    def height(self):
        """
        Compute height of a tree rooted by self
        """
        height = 0
        for child in self._children:
            height = max(height, child.height() + 1)
        return height

    
def run_examples():
    """
    Create some trees and apply various methods to these trees
    """
    tree_a = Tree("a", [])
    tree_b = Tree("b", [])
    print "Tree consisting of single leaf node labelled 'a'", tree_a
    print "Tree consisting of single leaf node labelled 'b'", tree_b
    
    tree_cab = Tree("c", [tree_a, tree_b])
    print "Tree consisting of three node", tree_cab
    
    tree_dcabe = Tree("d", [tree_cab, Tree("e", [])])
    print "Tree consisting of five nodes", tree_dcabe
    print 
    
    my_tree = Tree("a", [Tree("b", [Tree("c", []), Tree("d", [])]), 
                         Tree("e", [Tree("f", [Tree("g", [])]), Tree("h", []), Tree("i", [])])])
    print "Tree with nine nodes", my_tree
    
    print "The tree has", my_tree.num_nodes(), "nodes,", 
    print my_tree.num_leaves(), "leaves and height",
    print my_tree.height()

    #import poc_draw_tree
    #poc_draw_tree.TreeDisplay(my_tree)
    
             
#run_examples()

