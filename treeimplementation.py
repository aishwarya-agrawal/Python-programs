class node:
    def __init__(self,initdata):
        self.data = initdata
        self.left = None
        self.right= None
    def setLeft(self,left):
        self.left = left
    def setRight(self,right):
        self.right = right
    def getData(self):
        return self.data
    def setData(self,newData):
        self.initdata= newData
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def __repr__(self):
        return str(self.data)
class tree:
    def __init__(self,root):
        self.root = root
        self.size = 0
    def __len__(self):
        return self.size
    def length(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def insertnode(self,root1,node1):
        if node1.data < root1.data :
            if root1.left != None :
                self.insertnode(root.left,node1)
            else :
                root1.left = node1
                return
        else:
            if node1.data > root1.data :
                if root1.right != None :
                    self.insertnode(root.right,node1)
                else :
                    root1.right = node1
                    return
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    def postorder(self,node):
         if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
    def preorder(self,node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def bfs(self,node,item):
        stck = stack()
        if node :
            stck.push(node)
            if(int(stck.items[stck.top].data) == item):
                return "found"
            else:
                stck.pop()
                if node.left :
                    stck.push(node.left)
                if node.right:
                    stck.push(node.right)
                self.bfs(stck.items[stck.top],item)
        

class stack:
    def __init__(self):
        self.items=[]
        self.top = -1
    def push(self,item):
        self.items.append(item)
        self.top = self.top + 1
    def pop(self):
        self.top = self.top - 1
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

root = node(53)
tree1 = tree(root)
newnode = node(54)
newnode1 = node(51)
tree1.insertnode(root,newnode)
tree1.insertnode(root,newnode1)
newnode2 = node(41)
newnode3 = node(56)
tree1.insertnode(root,newnode2)
tree1.insertnode(root,newnode3)
'''
print("postorder:")
tree1.postorder(root)
print("preorder:")
tree1.preorder(root)
print("inorder :")
tree1.inorder(root)
'''
print(tree1.bfs(root,56))
'''
print(tree1.root)
print(tree1.root.left)
print(tree1.root.right)
print(tree1.root.left.left)
print(tree1.root.right.right)
newel = node(52)
stack1 = stack()
newel1 = node(54)
stack1.push(newel)
stack1.push(newel1)
print(stack1.pop())
print(stack1.pop())
'''
