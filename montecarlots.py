#modeling after https://github.com/maksimKorzh/tictactoe-mtcs/tree/master/src/tictactoe, https://www.youtube.com/watch?v=LeRCUu5U3kw
import math
import random

# class TreeNode():
#     def __init__(self, board, gameover, size, turn, parent):
#         self.board = board
#         self.is_terminal = gameover
#         self.is_fully_expanded = self.is_terminal
#         self.parent = parent
#         self.turn = turn
#         self.size = size
#         self.visits = 0
#         self.score = 0
#         self.children = {}

# class MCTS():

#     #search for best move in the current position
#     def search(self, initial_state, size, turn, gameover):
#         self.root = TreeNode(initial_state, gameover, turn, size, None)

#         for i in range(1000):
#             node = self.select(self.root)
#             score = self.rollout(node.board)
#             self.backpropogate(node, score)

#         try:
#             return self.get_best_move(self.root, 0)
#         except:
#             pass

#     #select most promising node
#     def select(self,node):
#         while not node.is_terminal:
#             if node.is_fully_expanded:
#                 node = self.get_best_move(node,2)
#             else:
#                 return self.expand(node)
#         return node
    
#     def expand(self, node):
#         states = []
#         for row in node.size:
#             for col in node.size:
#                 if node.board[row][col] == None:
#                     state = self.make_new_board(node.size)
#                     state[row][col] = node.turn
#                     node.turn = self.turn_inverse(node.turn)
#                     states.append(state)
#         for state in states:
#             if str(node.board) not in node.children:
#                 new_node = TreeNode(state, node.gamover, node.size, node.turn, node)
#                 node.children[str(node.board)] = new_node

#                 if len(states) == len(node.children):
#                     node.is_fully_expanded = True
#                 return new_node

#     def rollout(self, board, size, is_terminal, turn):
#         while not is_terminal:
#             try:
#                 states = []
#                 for row in size:
#                     for col in size:
#                         if board[row][col] == None:
#                             state = self.make_new_board(size)
#                             state[row][col] = turn
#                             states.append(state)
#                 board = random.choice(states)
#             except:
#                 return 0
            
#         if turn == 'X':
#         return
#     def backpropogate(self):
#         return
#     def get_best_move(self):
#         return 
#     def make_new_board(self, size):
#         if size == 3:
#             return [[None, None, None], [None, None, None], [None, None, None]]
#         elif size == 4:
#             return [[None, None, None, None], [None, None, None, None], 
#                     [None, None, None, None], [None, None, None, None]]
#         else:
#             return [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], 
#                     [None, None, None, None, None], [None, None, None, None, None]]
    
#     def turn_inverse(turn):
#         if turn == 'X':
#             return 'O'
#         else:
#             return 'X'

class TreeNode():
    def __init__(self, session, parent):
        self.session = session
        self.is_terminal = self.session['gameover']
        self.is_fully_expanded = self.is_terminal
        self.parent = parent
        self.visits = 0
        self.score = 0
        self.children = {}

class MCTS():

    #search for best move in the current position
    def search(self, session):
        self.root = TreeNode(session, None)

        for i in range(1000):
            node = self.select(self.root)
            score = self.rollout(session['board'])
            self.backpropogate(node, score)

        try:
            return self.get_best_move(self.root, 0)
        except:
            pass

    def select(self, node):
        while not node.is_terminal:
            if node.is_fully_expanded:
                node = self.get_best_move(node, 2)
            else:
                return self.expand(node)
        return node
    
    def expand(self, node):
        states = self.generate_states(node.session)
        for state in states:
            if str(state['board']) not in node.children:
                new_node = TreeNode(state, node)
                node.children[str(state['board'])] = new_node

                if len(states) == len(node.children):
                    node.is_fully_expanded = True
                return new_node
        print('debug: should not get here')

    def rollout(self, session):
        while not session['gameover']:
            try:
                session = random.choice(self.generate_states(session))
            except:
                return 0
            
        if session['turn'] == 'X':
            return 1
        else:
            return -1
        
    def backpropogate(self, node, score):
        while node is not None:
            node.visits += 1
            node.score += score
            node = node.parent

    def get_best_move(self, node, exploration_constant):
        best_score = float('-inf')
        best_moves = []

        for child_node in node.children.values():
            if child_node.session['turn'] == 'X': curr_player = 1
            elif child_node.session['turn'] == 'O': curr_player = -1

            move_score = curr_player * child_node.score / child_node.visits + exploration_constant * math.sqrt(math.log(node.visits / child_node.visits))

            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            elif move_score == best_score:
                best_moves.append(child_node)

        return random.choice(best_moves)

    def generate_states(self, session):
        states = []
        for row in session['board_size']:
            for col in session['board_size']:
                if session['board'][row][col] == None:
                    state = session
                    state['board'][row][col] = state['turn']
                    state['turn'] = self.turn_inverse(state['turn'])
                    states.append(state)
        return states





    def make_new_board(self, size):
        if size == 3:
            return [[None, None, None], [None, None, None], [None, None, None]]
        elif size == 4:
            return [[None, None, None, None], [None, None, None, None], 
                    [None, None, None, None], [None, None, None, None]]
        else:
            return [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], 
                    [None, None, None, None, None], [None, None, None, None, None]]
    
    def turn_inverse(self, turn):
        if turn == 'X':
            return 'O'
        else:
            return 'X'
    def is_win(self, session):
        if session['board_size'] == 3:
            if session['board'][0] == ['X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][1] == 'X' and session['board'][2][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X'):
                session['xWin'] = True
                session['gameover'] = True
            elif session['board'][0] == ['O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][1] == 'O' and session['board'][2][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
        if session['board_size'] == 4:
            if session['board'][0] == ['X', 'X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X', 'X'] or session['board'][3] == ['X', 'X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X' and session['board'][3][3] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][2] == 'X' and session['board'][2][1] == 'X' and session['board'][3][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X' and session['board'][3][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X' and session['board'][3][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X' and session['board'][3][2] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][3] == 'X' and session['board'][2][3] == 'X' and session['board'][3][3] == 'X'):
                session['xWin'] = True
                session['gameover'] = True
            elif session['board'][0] == ['O', 'O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O', 'O'] or session['board'][3] == ['O', 'O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O' and session['board'][3][3] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][2] == 'O' and session['board'][2][1] == 'O' and session['board'][3][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O' and session['board'][3][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O' and session['board'][3][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O' and session['board'][3][2] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][3] == 'O' and session['board'][2][3] == 'O' and session['board'][3][3] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
        if session['board_size'] == 5:
            if session['board'][0] == ['X', 'X', 'X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X', 'X', 'X'] or session['board'][3] == ['X', 'X', 'X', 'X', 'X'] or session['board'][4] == ['X', 'X', 'X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X' and session['board'][3][3] == 'X' and session['board'][4][4] == 'X') or (session['board'][0][4] == 'X' and session['board'][1][3] == 'X' and session['board'][2][2] == 'X' and session['board'][3][1] == 'X' and session['board'][4][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X' and session['board'][3][0] == 'X' and session['board'][4][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X' and session['board'][3][1] == 'X' and session['board'][4][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X' and session['board'][3][2] == 'X' and session['board'][4][2] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][3] == 'X' and session['board'][2][3] == 'X' and session['board'][3][3] == 'X' and session['board'][4][3] == 'X') or (session['board'][0][4] == 'X' and session['board'][1][4] == 'X' and session['board'][2][4] == 'X' and session['board'][3][4] == 'X' and session['board'][4][4] == 'X'):
                session['xWin'] = True
                session['gameover'] = True
            elif session['board'][0] == ['O', 'O', 'O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O', 'O', 'O'] or session['board'][3] == ['O', 'O', 'O', 'O', 'O'] or session['board'][4] == ['O', 'O', 'O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O' and session['board'][3][3] == 'O' and session['board'][4][4] == 'O') or (session['board'][0][4] == 'O' and session['board'][1][3] == 'O' and session['board'][2][2] == 'O' and session['board'][3][1] == 'O' and session['board'][4][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O' and session['board'][3][0] == 'O' and session['board'][4][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O' and session['board'][3][1] == 'O' and session['board'][4][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O' and session['board'][3][2] == 'O' and session['board'][4][2] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][3] == 'O' and session['board'][2][3] == 'O' and session['board'][3][3] == 'O' and session['board'][4][3] == 'O') or (session['board'][0][4] == 'O' and session['board'][1][4] == 'O' and session['board'][2][4] == 'O' and session['board'][3][4] == 'O' and session['board'][4][4] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
