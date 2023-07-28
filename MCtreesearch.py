class Node:
    def __init__(self,name):
        self.state = None
        self.parent = None
        self.childArray = []

class Tree:
    def __init__(self,name):
        self.root = None

class State:
    def __init__(self,name):
        self.board = None
        self.playerNo = 2
        self.visitCount = 0
        self.winScore = 0.0

    def getAllPossibleStates():
        return
    