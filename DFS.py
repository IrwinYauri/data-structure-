class Node:
    def __init__(self,name):
        self.name=name
        self.children=[]
    
    def addChild(self,name):
        new_node=Node(name)
        self.children.append(new_node)
        return new_node

#dfs: n-orden,pre-orden,post-order
#pre-order(tree):[tree.name+pre-order(tree.child[0])+n-order(tree.child[1]...)]
#T(V,E) = O(|V| + |E|)

#runtime:T(n)=O(n + O(1))=O(n)
#space complexity:O(height(tree))

def dfs(ptr):
    print(ptr.name)
    for c in ptr.children:
        dfs(c)

#runtime: T(n)=O(n)
#space Complexity: O(hegiht(tree))

def dfs_iterativo(root):
    stack=[root]
    while len(stack) > 0:
        ptrUlt=stack.pop(len(stack)-1)
        print(ptrUlt.name)
        for p in range(len(ptrUlt.children)-1,-1,-1):
            stack.append(ptrUlt.children[p])
            

root=Node("A")
b=root.addChild("B")
c=root.addChild("C")
d=root.addChild("D")

e=b.addChild("E")
f=b.addChild("F")

f.addChild("I")
f.addChild("J")

#dfs(root)

dfs_iterativo(root)
