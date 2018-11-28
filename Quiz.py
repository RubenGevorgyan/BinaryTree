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

    def min_val(self,node):
        current = node

        while (current.left is not None):
            current = current.left

        return current


    def remove(self,root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.remove(root.left, data)

        elif (data > root.data):
            root.right = self.remove(root.right, data)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_val(root.right)
            root.data = temp.data
            root.right = self.remove(root.right, temp.data)

        return root

    def get_height(self,root):
        if root is None:
            return 0;
        else:
            left_Depth = self.get_height(root.left)
            right_Depth = self.get_height(root.right)

            if (left_Depth > right_Depth):
                return left_Depth + 1
            else:
                return right_Depth + 1
    def is_empty(self,root):
        if root is None:
            return False;
        return True

    def get_number_of_nodes(self,root):
        if root is None:
            return 0

        return 1 + self.size(root.left) + self.size(root.right)

def main():
    temp=int(raw_input("How many inputs do you want?"))
    root=Node(int(raw_input()))
    for i in range(0,temp-1):
        root.Insert(int(raw_input()))
    print("There are your inputs ")
    root.Print()
    print("\n")
    deletion=int(raw_input("Which node do you want to delete?"))
    root.remove(root,deletion)
    root.Print()
    print("\n")
    print("Is tree empty??")
    print("\n")
    if(root.is_empty(root)):
        print("The height of the tree is:::"+root.get_height(root))
    else:
        print("It's empty")
    print("\n")
    print("The number of nodes of tree is :::"+ root.get_number_of_nodes(root))

main()
