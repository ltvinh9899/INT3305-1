class Node:
    def __init__(self, symbol):
        self.left = None
        self.right = None
        self.symbol = symbol


class BinaryTree(Node):
    def __init__(self):
        self.root = Node('root')

    def addNode(self, symbol):
        return Node(symbol)

    def insert(self, codework, symbol):
        self.insertNode(codework, symbol)
        self.Rename(self.root.left)
        self.Rename(self.root.right)

    def insertNode(self, codework, symbol):
        leaves = self.root
        for index in codework:
            if (index == 0):
                if (leaves.left == None):
                    leaves.left = self.addNode(symbol)
                leaves = leaves.left
            else:
                if (leaves.right == None):
                    leaves.right = self.addNode(symbol)
                leaves = leaves.right

    def PreOrder(self, root):
        if root is not None:
            print(root.symbol)
            if root.left is not None:
                self.PreOrder(root.left)
            if root.right is not None:
                self.PreOrder(root.right)

    def Rename(self, root):
        if root is not None:
            if (root.left is not None):
                root.symbol = 'leaves'
                self.Rename(root.left)
            if (root.right is not None):
                root.symbol = 'leaves'
                self.Rename(root.right)

    def decodeNode(self, decodedData):
        message = ""
        self.nodeRoot = self.root
        for index in decodedData:
            if (index == '1'):
                self.nodeRoot = self.nodeRoot.right
            else:
                self.nodeRoot = self.nodeRoot.left
            if (self.nodeRoot.symbol != "leaves" and self.nodeRoot.symbol != "root"):
                message += self.nodeRoot.symbol
                self.nodeRoot = self.root
        return message

    def decode(self, encodedData, datalen):
        bytear = bytearray(encodedData)
        decodedData = ""
        for value in bytear:
            decodedData = decodedData + bin(value)[2:].zfill(8)
        decodedData = decodedData[:datalen]
        message = self.decodeNode(decodedData)
        return message


def main():
    codebook = {
        'x1': [0],
        'x2': [1, 0, 0],
        'x3': [1, 0, 1],
        'x4': [1, 1]
    }
    codeTree = BinaryTree()
    for symbol in codebook:
        codeTree.insert(codebook[symbol], symbol)
    test = codeTree.decode(b'\xd2\x9f\x20', 21)
    print(test)


main()