class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    def Insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.Insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.Insert(data)
        else:
            self.data = data


    def Print(self):
        if self.left:
            self.left.Print()
        print(self.data),
        if self.right:
            self.right.Print()

    def InOrder(self, root):
        temp = []
        if root:
            temp = self.InOrder(root.left)
            temp.append(root.data)
            temp = temp + self.InOrder(root.right)
        return temp

    def PreOrder(self, root):
        temp = []
        if root:
            temp.append(root.data)
            temp = temp + self.PreOrder(root.left)
            temp = temp + self.PreOrder(root.right)
        return temp

    def PostOrder(self, root):
        temp = []
        if root:
            temp = self.PostOrder(root.left)
            temp = temp + self.PostOrder(root.right)
            temp.append(root.data)
        return temp

def main():
    temp=int(raw_input("How many inputs do you want?"))
    root=Node(int(raw_input()))
    for i in range(0,temp-1):
        root.Insert(int(raw_input()))
    print("There are your inputs ")
    root.Print()
    print("\n")
    print "These is InOrder Traverse", root.InOrder(root)
    print "These is PreOrder Traverse", root.PreOrder(root)
    print "These si PostOrder Traverse" , root.PostOrder(root)

main()