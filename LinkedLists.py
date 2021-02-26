# The current python file presents the creation of linked lists and its usage.
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("Error: The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode


list = SLinkedList()
list.AtBegining('Mon')
list.Inbetween(list.headval, "Tue")
k = list.headval
# for day in range(100) :
#     k = k.nextval
#     list.Inbetween(k, day)
# # Put something before 50
# k = list.headval
# while k.nextval != None:
#     if k.dataval == 50:
#         list.Inbetween(k,'khondeuhcbiifncqiuchhcjkfjn  croiju od jhf u owfoouioxnkiepx i xoioq xoj  oii dodhjoxn jqwd jq ')
#     k = k.nextval

print(list.headval.dataval, 'yes')
list.AtEnd('Sun')
list.listprint()