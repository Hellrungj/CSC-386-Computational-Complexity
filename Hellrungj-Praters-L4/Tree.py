#John Hellrung & Shadia Prater
# A8/L4
# CSC 386

# simple binary tree
# in this implementation, a node is inserted between an existing node and the root
# http://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree-in-python

def add(node, v):
    new = [v, [], []]
    if node:
        left, right = node[1:]
        if not left:
            left.extend(new)
        elif not right:
            right.extend(new)
        else:
            add(left, v)
    else:
       node.extend(new)

def binary_tree(s):
    root = []
    for e in s:
        add(root, e)
    return root

def traverse(n, order):
    if n:
        v = n[0]
        if order == 'pre':
            yield v
        for left in traverse(n[1], order):
            yield left
        if order == 'in':
            yield v
        for right in traverse(n[2], order):
            yield right
        if order == 'post':
            yield v       


