class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def traverseAndPrint(head):
    currentNode = head
    while currentNode != None:
        print(currentNode.data, end="->")
        currentNode = currentNode.next
    print("null")
def insertNodeAtPoint(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    currentNode = head
    for i in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

#main program

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
traverseAndPrint(node1)
insertNodeAtPoint(node1, Node(13), 2)
traverseAndPrint(node1)
deleteNode(node4)
traverseAndPrint(node1)
