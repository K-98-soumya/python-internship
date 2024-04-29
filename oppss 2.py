class node:
    def __init__(self, d):
        self.data= d 
        self.next= None 
        
class LL:
    def __init__(self):
        self.head = None 
        
        
    def add_node(self , val):
        new_node = node(val)
        if(self.head == None):
            self.head = new_node 
            
        else:
            traveller = self.head 
            while(traveller.next != None):
                traveller = traveller.next
            traveller.next =new_node
            
    def traverse(self):
        traveller = self.head 
        while(traveller.next != None):
            print(traveller.data)
            traveller = traveller.next
        print(traveller.data)
        
LL1 = LL()
LL1.add_node(3)
LL1.add_node(8)
LL1.add_node(7)
LL1.add_node(1)
LL1.traverse()












