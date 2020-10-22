#Breadth First-search

class Node:
    def __init__(self,name):
        self.name=name
        self.children=[]
    
    def addChild(self,name):
        new_node=Node(name)
        self.children.append(new_node)
        return new_node

def bfs_iter(root):
    queue=[(root,0)]
    d={}
    while len(queue)>0:
        ptr,level=queue.pop(0)
        if level not in d:
            d[level]=[]
        d[level].append(ptr.name)
        for i in range(len(ptr.children)):
            queue.append((ptr.children[i],level+1))
    print(d)

root=Node("A")
b=root.addChild("B")
c=root.addChild("C")
d=root.addChild("D")

e=b.addChild("E")
f=b.addChild("F")

f.addChild("I")
f.addChild("J")

bfs_iter(root)

