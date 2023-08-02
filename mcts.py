#modeling after https://github.com/maksimKorzh/tictactoe-mtcs/tree/master/src/tictactoe, https://www.youtube.com/watch?v=LeRCUu5U3kw
import math
import random

class TreeNode():
    def __init__(self, board, gameover, size, turn, parent):
        self.board = board
        self.is_terminal = gameover
        self.is_fully_expanded = self.is_terminal
        self.parent = parent
        self.turn = turn
        self.size = size
        self.visits = 0
        self.score = 0
        self.children = {}

class MCTS():

    #search for best move in the current position
    def search(self, initial_state, size, turn, gameover):
        self.root = TreeNode(initial_state, gameover, turn, size, None)

        for i in range(1000):
            node = self.select(self.root)
            score = self.rollout(node.board)
            self.backpropogate(node, score)

        try:
            return self.get_best_move(self.root, 0)
        except:
            pass

    #select most promising node
    def select(self,node):
        while not node.is_terminal:
            if node.is_fully_expanded:
                node = self.get_best_move(node,2)
            else:
                return self.expand(node)
        return node
    
    def expand(self, node):
        states = []
        for row in node.size:
            for col in node.size:
                if node.board[row][col] == None:
                    state = self.make_new_board(node.size)
                    state[row][col] = node.turn
                    node.turn = self.turn_inverse(node.turn)
                    states.append(state)
        for state in states:
            if str(node.board) not in node.children:
                new_node = TreeNode(state, node.gamover, node.size, node.turn, node)
                node.children[str(node.board)] = new_node

                if len(states) == len(node.children):
                    node.is_fully_expanded = True
                return new_node

    def rollout(self):
        return
    def backpropogate(self):
        return
    def get_best_move(self):
        return 
    def make_new_board(self, size):
        if size == 3:
            return [[None, None, None], [None, None, None], [None, None, None]]
        elif size == 4:
            return [[None, None, None, None], [None, None, None, None], 
                    [None, None, None, None], [None, None, None, None]]
        else:
            return [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], 
                    [None, None, None, None, None], [None, None, None, None, None]]
    
    def turn_inverse(turn):
        if turn == 'X':
            return 'O'
        else:
            return 'X'