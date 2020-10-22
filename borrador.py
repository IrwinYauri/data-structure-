class Node:
    def __init__(self,name):
        self.name=name
        self.children=[]

    def addChild(self,name):
        newNode=Node(name)
        self.children.append(newNode)

        return newNode

def dfs(ptr):
    print(ptr.name)
    for p in range(len(ptr.children)):
        dfs(ptr.children[p])

def dfs_iterativo(root):
    stack=[root]
    while len(stack) > 0:
        ptrUlt=stack.pop(len(stack)-1)
        print(ptrUlt.name)
        for p in range(len(ptrUlt.children)-1,-1,-1):
            stack.append(ptrUlt.children[p])

def bfs(root):    
    queue=[root]
    while len(queue) > 0:
        ptr=queue.pop(0)
        print(ptr.name)
        for i in range(len(ptr.children)):            
            queue.append(ptr.children[i])
               

root=Node("A")

b=root.addChild("B")
root.addChild("C")
root.addChild("D")

b.addChild("E")
f=b.addChild("F")

f.addChild("I")
f.addChild("J")

#dfs(root)
#dfs_iterativo(root)
bfs(root)