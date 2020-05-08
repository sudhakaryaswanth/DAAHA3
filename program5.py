class HuffmanNode:
    def __init__(self, weight, char):
        self.weight = weight
        self.char = char
        self.left = None
        self.right = None


class minHeap:
    # For getting the index of the parent Node.
    def parent(self, idx): return (idx // 2)

    # For getting the index of the leftChild Node.
    def leftChild(self, idx): return (idx * 2)

    # For getting the index of the rightChild Node.
    def rightChild(self, idx): return (idx * 2 + 1)
    
    # Initializing a empty heap.
    def __init__(self):
        self.heapSize = 0
        self.heapArr = [0]

    # Max_Heapify function for placing parent node in its proper position.
    def heapify(self, idx):
        l = self.leftChild(idx)
        r = self.rightChild(idx)
        # Comparing with the left child.
        if l <= self.heapSize and self.heapArr[l].weight < self.heapArr[idx].weight:
            smallest = l
        else:
            smallest = idx
        # Comparing with the right child.
        if r <= self.heapSize and self.heapArr[r].weight < self.heapArr[smallest].weight:
            smallest = r
        # If the parent Node is less than the leftchild or rightchild.
        if smallest != idx:
            # Swap the largest of the three nodes with the parent.
            self.heapArr[idx], self.heapArr[smallest] = self.heapArr[smallest], self.heapArr[idx]
            self.heapify(smallest)

    # Extracting the root of the heap.
    def extractMin(self):
        if self.heapSize > 0:
            res = self.heapArr[1]
            self.heapArr[1], self.heapArr[self.heapSize] = self.heapArr[self.heapSize], self.heapArr[1]
            self.heapSize -= 1
            if self.heapSize != 0:
                self.heapify(1)
            self.heapArr.pop()
            return res

    # Building maxHeap of a given array.
    def buildHeap(self, A):
        self.heapSize = len(A)
        self.heapArr = [0] + A
        idx = self.parent(self.heapSize)
        for i in range(idx, 0, -1):
            self.heapify(i)

    # Inserting node.
    def insert(self, ele):
        self.heapArr.append(ele)
        self.heapSize = len(self.heapArr) - 1
        idx = self.heapSize
        while self.parent(idx) != 0 and ele.weight < self.heapArr[self.parent(idx)].weight:
            self.heapArr[self.parent(idx)], self.heapArr[idx] = self.heapArr[idx], self.heapArr[self.parent(idx)]
            idx = self.parent(idx)

    # Displaying current status.
    def displayHuffman(self):
        print(len(h.heapArr) - 1)
        for i in range(1, h.heapSize + 1):
            print(self.heapArr[i].weight, end = "")
            print(self.heapArr[i].char, end= " ")
        print()


# Getting input.
data = input()

# Creating a hash map.
freqCount = {}
for x in data:
    if x not in freqCount:
        freqCount[x] = 0
    freqCount[x] += 1

# Creating a min heap of frequencies.
A = []
h = minHeap()
for x in freqCount:
    weight = freqCount[x]
    ht = HuffmanNode(weight, x)
    A.append(ht)

h.buildHeap(A)

def encode():
    while h.heapSize > 1:
        low1 = h.extractMin()
        low2 = h.extractMin()
        weight = low1.weight + low2.weight
        char = "^^"
        newNode = HuffmanNode(weight, char)
        newNode.left = low1
        newNode.right = low2
        h.insert(newNode)
    return h.extractMin()

new = encode()

def findPath(new, s, char):
    if new == None:
        return None
    if new.char == char:
        return s
    left = findPath(new.left, s + "0", char)
    right = findPath(new.right, s + "1", char)
    if left != None:
        return left
    elif right != None:
        return right

keys = {}
def decoding():
    for x in freqCount:
        keys[x] = findPath(new, "", x)

    print("For the given input::", data)
    
    for x in data:
        if keys[x] == None:
            print(x, end= "")
        print(keys[x], end = "")
decoding()
print()
