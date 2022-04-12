class TreeNode():
    '''the definition of tree node'''
    def __init__(self, elem, left = None, right = None):
        '''data is the value of the current node, left and right are left tree and right tree of current node'''
        self.ele = elem
        self.left = left
        self.right = right

class BinaryTree(object):
    '''initial function'''
    def __init__(self, root = None):
        self.root = root                                                    # initial the root as None
        self.stack = []

    '''for str() implementation for printing'''
    def __str__(self):
        return " : ".join(map(str, self.to_list()))

    '''iter'''
    def __iter__(self):
        self.stack = self.to_list()
        self.it = 0
        return self.it

    '''next'''
    def __next__(self):
        if self.it >= len(self.stack):
            raise StopIteration
        else:
            self.it += 1
            return self.it

    '''find the node which its elem equal to the item '''
    def findElem(self, item):
        parentNode = None
        currNode = None
        if self.root == None:
            print("the set is empty")
            res = False
        else:
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                if currNode.ele == item:
                    print("the item is in the set") 
                    res = True
                    break                                                   # if item is equal to the root.ele, return node
                elif currNode.ele > item:
                    if currNode.left != None:
                        parentNode = currNode
                        queue.append(currNode.left)                         # search the left child tree
                    else:                                                   # the item is not in the set
                        print("the item is not int the set")
                        currNode = None
                        parentNode = None
                        res = False
                        break                      
                else:
                    if currNode.right != None:  
                        parentNode = currNode
                        queue.append(currNode.right)                        # search the right child tree
                    else:
                        print("the item is not in the set")
                        parentNode = None
                        currNode = None
                        res = False
                        break
        return res, parentNode, currNode

    def add(self, item):
        '''add node to tree'''
        node = TreeNode(item)           # instance of the node
        if(self.root == None):          # if the set is empty
            self.root = node
            return
        else:
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                if currNode.ele == item:                                # if the item is already in the set
                    print("the item is already in the set")
                    return
                elif currNode.ele > item:
                    if currNode.left:   queue.append(currNode.left)     # if the item is smaller than the currNode.ele
                    else:
                        currNode.left = node
                        return
                else:                                                   # if the item is larger than the currNode.ele
                    if currNode.right:  queue.append(currNode.right)
                    else:   
                        currNode.right = node
                        return

    '''delete the item'''
    def delete(self, item):
        res, parentNode, currNode = self.findElem(item)                 # search the item wheather in the set
        if res == False:    return                                      # if item does not in the set, return false
        else:                                                           # else
            if currNode.left:                                           # find the instead node of the delete node
                parentOfInsteadNode = currNode
                insteadNode = currNode.left
            while insteadNode.right:
                parentOfInsteadNode = insteadNode
                insteadNode = insteadNode.right
            parentOfInsteadNode.right = insteadNode.left
            insteadNode.left = currNode.left
            if parentNode:                                              # replace the delete node by find node
                if parentNode.left == currNode:
                    parentNode.left = insteadNode
                else:   parentNode.right = insteadNode
            else:
                self.root = insteadNode
            return 

    '''size'''
    def getSize(self):
        if self.root == None:    return 0                               # if the set is empty, return 0
        else:                                                           # count the size
            size = 0
            queue = [self.root]                                         # queue for count
            while queue:
                currNode = queue.pop(0)
                size += 1
                if currNode.left:   queue.append(currNode.left)
                if currNode.right:  queue.append(currNode.right)
            return size

    '''to list'''
    def to_list(self):
        res = []
        queue = [self.root]
        while queue:
            currNode = queue.pop(0)
            res.append(currNode.ele)
            if currNode.left:   queue.append(currNode.left)
            if currNode.right:  queue.append(currNode.right)
        return res

    '''from list'''
    def from_list(self, tlist):
        for i in tlist:
            self.add(i)
        return 

    '''filter, the rule is defined by func'''
    def filter(self, func):
        if self.root is None:   return
        else:
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                if currNode.left:   queue.append(currNode.left)
                if currNode.right:  queue.append(currNode.right)
                if not func(currNode.ele):  self.delete(currNode.ele)

    '''map, the rule is defined by func'''
    def map(self, func):
        if self.root is None:   return 
        else:
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                currNode.ele = func(currNode.ele)
                if currNode.left:   queue.append(currNode.left)
                if currNode.right:  queue.append(currNode.right)
            return 


    '''reduce'''
    def reduce(self, func):
        it = self.__iter__()
        value = 0
        while it:
            value += func(it)
            self.delete(it)
            it = self.__next__(it)
        self.add(value)
        return 

    '''mempty'''
    def mempty(self):
        return None
        
    '''mconcat'''
    def mconcat(self, tree1, tree2):
        if tree1.root and tree.root:
            list1 = tree1.to_list()
            list2 = tree2.to_list()
            bt = BinaryTree()
            for i in list1:
                bt.add(i)
            for j in list2:
                bt.add(j)
            return bt
        elif not tree1.root:    return tree1
        elif not tree2.root:    return tree2
        else:
            bt = BinaryTree()
            return bt

if __name__ == '__main__':
    tree = BinaryTree()
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree.from_list(list1)
    iterator = tree.__iter__()
    while(iterator < len(tree.stack)):
        print(tree.stack[iterator])
        iterator = tree.__next__()
    tree.findElem(1)
    tree.findElem(11)