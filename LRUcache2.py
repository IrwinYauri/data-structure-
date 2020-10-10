class Node:
    def __init__(self, k=None, v=None):
        self.key=k
        self.value=v
        self.next=None
        self.prev=None

class List:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.count=0
    
    def insert_between(self,prev,new_node,curr):
        prev.next=new_node
        curr.prev=new_node
        new_node.next=curr
        new_node.prev=prev
        self.count += 1

    def remove(self,node):
        node.next.prev=node.prev
        node.prev.next=node.next
        self.count -= 1

        return node

    def push_front(self,node):
        self.insert_between(self.head,node,self.head.next)

    def remove_last(self):
        return self.remove(self.tail.prev)

    def first(self):
        return self.head.next

    def last(self):
        return self.tail.prev

    def to_string(self):
        output=""
        curr=self.head.next
        while curr != self.tail:
            output+="("+str(curr.key)+" -> "+str(curr.value)+"),"
            curr=curr.next

        return output

class LRUcache:
    def __init__(self,s):
        self.size=s
        self.dicc={} #<key,(list<pair<key,value>>)>
        self.heap=List()

    def insertKeyValuePair(self,k,v):
        if len(self.dicc) < self.size:
            currente_node=Node(k,v)
            self.heap.push_front(currente_node)
            self.dicc[k]=currente_node
        else:
            #len(self.dicc)==self.size
            currente_node=Node(k,v)
            self.heap.push_front(currente_node)
            self.dicc[k]=currente_node

            old_node=self.heap.remove_last() #O(1) 
            self.dicc.pop(old_node.key) # delete specific key in the diccionary

    def getMostRecentKey(self):
        if self.heap.first():
            return self.heap.first().key
        return None

    def getValueFromKey(self,k):
        if k in self.dicc:
            #Update heap order
            node_to_remove=self.dicc[k] #O(1)
            self.heap.remove(node_to_remove) #O(1)
            node=Node(node_to_remove.key,node_to_remove.value)
            self.heap.push_front(node) #O(1)
            return node.value

#runtime O(1)
#space O(3) -> O(1)

cache=LRUcache(3) # Instantiate LRUcache of size 3
cache.insertKeyValuePair("b",2)
cache.insertKeyValuePair("a",1)
cache.insertKeyValuePair("c",3)

print(cache.getMostRecentKey()) # "c" // c was the most recently insetted
print(cache.getValueFromKey("a")) # 1
print(cache.getMostRecentKey()) # "a" // a 

cache.insertKeyValuePair("d",4) #the each had 3 entries, the least
print(cache.getValueFromKey("b")) # None// b was evicted in the previus operation
cache.insertKeyValuePair("a",5) # "a" already exists in the cache so its value
print(cache.getValueFromKey("a")) # 5



    

    



