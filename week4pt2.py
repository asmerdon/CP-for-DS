class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return str(self.cargo)
    
node1 = Node("data1")
node2 = Node("data2")
node3 = Node("data3")
node1.next = node2
node2.next = node3
#print(node1.next)
type(node1)

def getDepth(node):
    count = 0
    while node:
        count += 1
        node = node.next
        return(count)
    
def getPosition(node, int):
    count = 0
    while count < int:
       count += 1
       node = node.next
       return(node, node.next)   

def returnLL(node, depth):
        count = getDepth(node)
        print(node)
        if (count < depth) and (node.next != None):
            print(node1)
            returnLL(node.next, depth)

def addNode(node, string, int):
    addNode, nextNode = getPosition(node, int)
    print(addNode)
    print(nextNode)
         

addNode(node1, "test", 2)



