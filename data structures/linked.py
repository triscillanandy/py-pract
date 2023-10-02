#A linked list is represented by a pointer to the first node of the linked list.
#The first node is called the head. 
#If the linked list is empty, then the value of the head is NULL. 
#Each node in a list consists of at least two parts:
#Data
#Pointer (Or Reference) to the next node

# class node
class Node:
    def __init__(self,data):
        self.data = data#assign data
        self.next = None#initailize the next as null 


class LinkedList:
        
    def __init__(self):
        self.head=None

if __name__ == '__main__':
        #start with empty linked list

        list=LinkedList()
        list.head=Node(1)
        second=Node(2)
        third= Node(3)

        list.head.next=second;#link first node with seconf

        second.next=third; # link second node with the third node 
        #Now next of second Node refers to third. So all three
    #nodes are linked.
 
        
     