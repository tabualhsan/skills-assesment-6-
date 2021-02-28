"""tests/test_linkedlist.py

Tests for linkedlist.py


Linkedlist.py points: 25
Tree.py points: 25

Discussion Questions (needs manual verificaiton):
Runtime, Stacks & Queues: 50
Total: 100

"""

from io import StringIO

#####################################################################
# Student task: create a function (not a method) that takes in a LinkedList object.
def test_only_vowels(ll_module):
    def linked_list_length(llist):
        count = 0
        current_node = llist.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    # Ensure they did not accidentally subclass anything in either direction
    assert not issubclass(ll_module.LinkedList, ll_module.Node)
    assert not issubclass(ll_module.Node, ll_module.LinkedList)

    test_list = ll_module.LinkedList()
    test_list.add_node("cherry")
    test_list.add_node("berry")
    test_list.add_node("apple")
    test_list.add_node("egg")

    filtered_list = ll_module.only_vowels(test_list)
    # Check that the length is correct
    assert linked_list_length(filtered_list) == 2
    # Check that the head is set correctly
    assert filtered_list.head.data == 'apple'
    # Check that head's next is set correctly
    assert filtered_list.head.next.data == 'egg'
    # Check that last is set correctly
    assert filtered_list.tail.data == 'egg'

if __name__ == "__main__":
    pytest.main()