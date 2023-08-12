#modeling after https://github.com/maksimKorzh/tictactoe-mtcs/tree/master/src/tictactoe, https://www.youtube.com/watch?v=LeRCUu5U3kw
import math
import random
import copy

class TreeNode():
    def __init__(self, session, parent):
        self.session = session
        self.turn = session['turn']
        if self.is_win(session) or self.is_draw(session):
            self.is_terminal = True
        else:
            self.is_terminal = False
        self.is_fully_expanded = self.is_terminal
        self.parent = parent
        self.visits = 0
        self.score = 0
        self.children = {}
    def is_win(self, session):
        if session['board_size'] == 3:
            if session['board'][0] == ['X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][1] == 'X' and session['board'][2][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X'):
                session['xWin'] = True
                session['gameover'] = True
                return True
            elif session['board'][0] == ['O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][1] == 'O' and session['board'][2][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
                return True
        if session['board_size'] == 4:
            if session['board'][0] == ['X', 'X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X', 'X'] or session['board'][3] == ['X', 'X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X' and session['board'][3][3] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][2] == 'X' and session['board'][2][1] == 'X' and session['board'][3][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X' and session['board'][3][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X' and session['board'][3][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X' and session['board'][3][2] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][3] == 'X' and session['board'][2][3] == 'X' and session['board'][3][3] == 'X'):
                session['xWin'] = True
                session['gameover'] = True
                return True
            elif session['board'][0] == ['O', 'O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O', 'O'] or session['board'][3] == ['O', 'O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O' and session['board'][3][3] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][2] == 'O' and session['board'][2][1] == 'O' and session['board'][3][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O' and session['board'][3][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O' and session['board'][3][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O' and session['board'][3][2] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][3] == 'O' and session['board'][2][3] == 'O' and session['board'][3][3] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
                return True
        if session['board_size'] == 5:
            if session['board'][0] == ['X', 'X', 'X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X', 'X', 'X'] or session['board'][3] == ['X', 'X', 'X', 'X', 'X'] or session['board'][4] == ['X', 'X', 'X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X' and session['board'][3][3] == 'X' and session['board'][4][4] == 'X') or (session['board'][0][4] == 'X' and session['board'][1][3] == 'X' and session['board'][2][2] == 'X' and session['board'][3][1] == 'X' and session['board'][4][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X' and session['board'][3][0] == 'X' and session['board'][4][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X' and session['board'][3][1] == 'X' and session['board'][4][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X' and session['board'][3][2] == 'X' and session['board'][4][2] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][3] == 'X' and session['board'][2][3] == 'X' and session['board'][3][3] == 'X' and session['board'][4][3] == 'X') or (session['board'][0][4] == 'X' and session['board'][1][4] == 'X' and session['board'][2][4] == 'X' and session['board'][3][4] == 'X' and session['board'][4][4] == 'X'):
                session['xWin'] = True
                session['gameover'] = True
                return True
            elif session['board'][0] == ['O', 'O', 'O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O', 'O', 'O'] or session['board'][3] == ['O', 'O', 'O', 'O', 'O'] or session['board'][4] == ['O', 'O', 'O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O' and session['board'][3][3] == 'O' and session['board'][4][4] == 'O') or (session['board'][0][4] == 'O' and session['board'][1][3] == 'O' and session['board'][2][2] == 'O' and session['board'][3][1] == 'O' and session['board'][4][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O' and session['board'][3][0] == 'O' and session['board'][4][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O' and session['board'][3][1] == 'O' and session['board'][4][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O' and session['board'][3][2] == 'O' and session['board'][4][2] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][3] == 'O' and session['board'][2][3] == 'O' and session['board'][3][3] == 'O' and session['board'][4][3] == 'O') or (session['board'][0][4] == 'O' and session['board'][1][4] == 'O' and session['board'][2][4] == 'O' and session['board'][3][4] == 'O' and session['board'][4][4] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
                return True
    def is_draw(self, session):
        for row in range(session['board_size']):
            for col in range(session['board_size']):
                if session['board'][row][col] == None:
                    return False
        return True

class MCTS():

    #search for best move in the current position
    def search(self, session):
        self.root = TreeNode(copy.deepcopy(dict(session)), None)
        print(self.root)
        for i in range(1000):
            print("iteration: ")
            print(i)
            node = self.select(self.root)
          
            score = self.rollout(node.session)
            print(score)
            self.backpropogate(node, score)

        try:
            print('search')
            return self.get_best_move(self.root, 0)
            
        except:
            pass

    # select most promising node
    def select(self, node):
        print("select")
        while not node.is_terminal:
            if node.is_fully_expanded:
                node = self.get_best_move(node, 2)
            else:
                
                return self.expand(node)

        return node
    
    #expand node
    def expand(self, node):
        print('expand')
        states = self.generate_states(node.session)
        for state in states: #state same as session
            if str(state['board']) not in node.children:
                print('true:')
                print(state['board'])
                new_node = TreeNode(state, node)
                node.children[str(state['board'])] = new_node

                if len(states) == len(node.children):
                    node.is_fully_expanded = True
                return new_node
        print('debug: should not get here')

    #simulate the game until reach end of the game
    def rollout(self, session):
        print('rollout')
        while not self.is_win(session): # may have to use a copy of session here
            try:
                session = random.choice(self.generate_states(session))
            except:
                return 0

        print(session['oWin'])
        print(session['xWin'])    
        if session['oWin']:
            return 10
        
        else:
            return -10

    #update the number of visits and score up to the root node 
    def backpropogate(self, node, score):
        while node is not None:
            node.visits += 1
            node.score += score
            node = node.parent
        print('backpropogate')

    #select the best node using UCB formula
    def get_best_move(self, node, exploration_constant):
        best_score = float('-inf')
        best_moves = []

        for child_node in node.children.values():
            if child_node.turn == 'X': 
                curr_player = 1
            else: 
                curr_player = -1
            print(child_node.session['board'])

            move_score = curr_player * child_node.score / child_node.visits + exploration_constant * math.sqrt(math.log(node.visits / child_node.visits))

            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            elif move_score == best_score:
                best_moves.append(child_node)
        print("best moves:")
        for c in best_moves:
            print(c.session['board'])
        print(random.choice(best_moves).session['board'])
        return random.choice(best_moves)

    def generate_states(self, session):
        states = []
        for row in range(session['board_size']):
            for col in range(session['board_size']):
                if session['board'][row][col] == None:
                    state = copy.deepcopy(dict(session))
                    state['board'][row][col] = state['turn']
                    state['turn'] = self.turn_inverse(state['turn'])
                    states.append(state)
                    print(state['board'])
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
                return True
            elif session['board'][0] == ['O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][1] == 'O' and session['board'][2][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
                return True
        if session['board_size'] == 4:
            if session['board'][0] == ['X', 'X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X', 'X'] or session['board'][3] == ['X', 'X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X' and session['board'][3][3] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][2] == 'X' and session['board'][2][1] == 'X' and session['board'][3][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X' and session['board'][3][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X' and session['board'][3][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X' and session['board'][3][2] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][3] == 'X' and session['board'][2][3] == 'X' and session['board'][3][3] == 'X'):
                session['xWin'] = True
                session['gameover'] = True
                return True
            elif session['board'][0] == ['O', 'O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O', 'O'] or session['board'][3] == ['O', 'O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O' and session['board'][3][3] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][2] == 'O' and session['board'][2][1] == 'O' and session['board'][3][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O' and session['board'][3][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O' and session['board'][3][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O' and session['board'][3][2] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][3] == 'O' and session['board'][2][3] == 'O' and session['board'][3][3] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
                return True
        if session['board_size'] == 5:
            if session['board'][0] == ['X', 'X', 'X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X', 'X', 'X'] or session['board'][3] == ['X', 'X', 'X', 'X', 'X'] or session['board'][4] == ['X', 'X', 'X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X' and session['board'][3][3] == 'X' and session['board'][4][4] == 'X') or (session['board'][0][4] == 'X' and session['board'][1][3] == 'X' and session['board'][2][2] == 'X' and session['board'][3][1] == 'X' and session['board'][4][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X' and session['board'][3][0] == 'X' and session['board'][4][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X' and session['board'][3][1] == 'X' and session['board'][4][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X' and session['board'][3][2] == 'X' and session['board'][4][2] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][3] == 'X' and session['board'][2][3] == 'X' and session['board'][3][3] == 'X' and session['board'][4][3] == 'X') or (session['board'][0][4] == 'X' and session['board'][1][4] == 'X' and session['board'][2][4] == 'X' and session['board'][3][4] == 'X' and session['board'][4][4] == 'X'):
                session['xWin'] = True
                session['gameover'] = True
                return True
            elif session['board'][0] == ['O', 'O', 'O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O', 'O', 'O'] or session['board'][3] == ['O', 'O', 'O', 'O', 'O'] or session['board'][4] == ['O', 'O', 'O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O' and session['board'][3][3] == 'O' and session['board'][4][4] == 'O') or (session['board'][0][4] == 'O' and session['board'][1][3] == 'O' and session['board'][2][2] == 'O' and session['board'][3][1] == 'O' and session['board'][4][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O' and session['board'][3][0] == 'O' and session['board'][4][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O' and session['board'][3][1] == 'O' and session['board'][4][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O' and session['board'][3][2] == 'O' and session['board'][4][2] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][3] == 'O' and session['board'][2][3] == 'O' and session['board'][3][3] == 'O' and session['board'][4][3] == 'O') or (session['board'][0][4] == 'O' and session['board'][1][4] == 'O' and session['board'][2][4] == 'O' and session['board'][3][4] == 'O' and session['board'][4][4] == 'O'):
                session['oWin'] = True
                session['gameover'] = True
                return True
    def is_draw(self, session):
        for row in range(session['board_size']):
            for col in range(session['board_size']):
                if session['board'][row][col] == None:
                    return False
        return True