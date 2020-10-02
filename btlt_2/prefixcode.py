class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


class BinaryTree:
    def __init__(self):
        self.root = Node(None)
        self.current = None

    def add(self, codeword, symbol):
        self.current = self.root
        for i in range(0, len(codeword) - 1):
            if (codeword[i] == 0):
                if (self.current.left == None):
                    self.current.left = Node(None)
                self.current = self.current.left
            else:
                if (self.current.right == None):
                    self.current.right = Node(None)
                self.current = self.current.right
        end = len(codeword) - 1
        if (codeword[end] == 0):
            self.current.left = Node(symbol)
        else:
            self.current.right = Node(symbol)

    def find(self, sbin):
        message = ""
        self.current = self.root
        for c in sbin:
            if (c == '1'):
                self.current = self.current.right
            else:
                self.current = self.current.left
            if (self.current.data != None):
                message += self.current.data
                self.current = self.root

        return message


class PrefixCodeTree:
    def __init__(self):
        self.tree = BinaryTree()

    def insert(self, codeword, symbol):
        self.tree.add(codeword, symbol)

    def decode(self, encodedData, datalen):
        sbin = ""
        l = list(encodedData)
        for i in l:
            ssbin = bin(i)[2:].zfill(8)
            sbin += ssbin
        sbin = sbin[:datalen]
        message = self.tree.find(sbin)
        return message