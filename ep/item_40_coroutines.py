from collections import namedtuple

ALIVE = '*'
EMPTY = '-'

Query = namedtuple('Query', ['i', 'j'])
Transition = namedtuple('Transition', ['i', 'j', 'state'])
TICK = object()


def count_neighbors(i, j):
    """count the number of alive neighbors of cell(i, j)"""
    q0 = yield Query(i - 1, j - 1)
    q1 = yield Query(i - 1, j)
    q2 = yield Query(i - 1, j + 1)
    q3 = yield Query(i, j - 1)
    q4 = yield Query(i, j + 1)
    q5 = yield Query(i + 1, j - 1)
    q6 = yield Query(i + 1, j)
    q7 = yield Query(i + 1, j + 1)

    states = [q0, q1, q2, q3, q4, q5, q6, q7]
    # count the number of neighbors
    #TODO? or return
    return states.count(ALIVE)


def step_cell(board):
    """step through each cell and count its neighbors
    and figuring out its next state."""

    for i in range(board.num_rows):
        for j in range(board.num_cols):
            # calls count_neighbors and returns Transition
            cur_state = yield Query(i, j)
            #TODO HOW did this work???
            num_neighbors = yield from count_neighbors(i, j)
            new_state = game_logic(cur_state, num_neighbors)
            yield Transition(i, j, new_state)

    yield TICK


def game_logic(state, num_neighbors):
    """
    given the current state and its number of alive neighbors,
    return its next state
    """
    if state == ALIVE:
        if num_neighbors > 3:
            return EMPTY
        if num_neighbors < 2:
            return EMPTY
    else:  # empty state
        if num_neighbors == 3:
            return ALIVE

    return state


def live_a_generation(board):
    """return the next generation of the game board"""

    next_gen = Board(board.num_rows, board.num_cols)
    it = step_cell(board)
    res = next(it)
    while res is not TICK:
        if type(res) is Query:
            # fetch the state for this position
            s = board.query(res.i, res.j)
            print('query {}, {} = {}'.format(res.i, res.j, s))
            res = it.send(s)
        else: # type is Transition??
            next_gen.assign(res.i, res.j, res.state)
            res = next(it)
    return next_gen


class Board(object):
    """depicts the game board"""

    def __init__(self, num_rows, num_cols):
        if num_rows < 1 or num_cols < 1:
            raise ValueError('both num_rows and num_cols must be positive integers.')
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = []
        for i in range(num_rows):
            row = [EMPTY] * num_cols
            self.board.append(row)

    def query(self, i, j):
        num_row = i % self.num_rows
        num_col = j % self.num_cols
        return self.board[num_row][num_col]

    def assign(self, i, j, state):
        if not state in [ALIVE, EMPTY]:
            raise ValueError('state must be alive or empty')

        num_row = i % self.num_rows
        num_col = j % self.num_cols
        self.board[num_row][num_col] = state

    def __str__(self):
        lst = []
        for row in self.board:
            lst.append(''.join(row))
        return '\n'.join(lst)


def similator():
    num_rows = 10
    num_cols = 10
    b = Board(num_rows, num_cols)
    #TODO initialize it
    for i in range(5):
        print(b)
        b = live_a_generation(b)


def foo():
    x = yield 1
    y = yield 2
    return x + y

def bar():
    r = yield from foo()
    print('got r {}'.format(r))
    return r
