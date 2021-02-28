"""tests/test_tree.py

Tests for tree.py


Tree.py points: 25
Linkedlist.py points: 25

Discussion Questions (needs manual verificaiton):
Runtime, Stacks & Queues: 50
Total: 100
"""

from io import StringIO
import pytest_check as check
import logging

# Set up logging so we can log passing tests as well as failing tests
# TODO: Colorize the logs and set up a custom format somehow for the
# HTML report.
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()

#####################################################################

def test_get_nodes(tree_module):
    # Ensure they did not accidentally subclass anything in either direction
    assert not issubclass(tree_module.Tree, tree_module.Node)
    assert not issubclass(tree_module.Node, tree_module.Tree)

    b1 = tree_module.Node('B')
    b2 = tree_module.Node('B')
    e = tree_module.Node('E')
    c = tree_module.Node('C', [b1, e])
    a = tree_module.Node('A', [b2, c])
    tree = tree_module.Tree(a)

    # Ensure that the nodes are returned in hierarchical order; this checks
    # to see if they're reversed, and spits out a log message if they are.
    if not check.equal(tree.get_nodes('B'), [b2, b1]):
        mylogger.error('Nodes returned were correct, but in wrong order! They need to be returned in hierarchical order!')

    # Check that the nodes get returned correctly, and in the right order
    assert tree.get_nodes("B") == [b2, b1]
    # Ensure it correctly returns an empty list when no nodes are found
    assert tree.get_nodes("L") == []


if __name__ == "__main__":
    pytest.main()