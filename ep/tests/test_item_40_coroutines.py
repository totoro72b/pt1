import unittest
from item_40_coroutines import (Board,
                                ALIVE,
                                EMPTY,
                                game_logic,
                                count_neighbors,
                                Query,
                                step_cell,
                                live_a_generation
                               )


# test coroutines
class TestCoroutines(unittest.TestCase):

    def test_board_class(self):
        b = Board(2, 3)
        b.assign(0, 0, ALIVE)
        b.assign(1, 1, ALIVE)
        alive_cells = [(0, 0), (1, 1)]
        for i in range(2):
            for j in range(3):
                state = ALIVE if (i, j) in alive_cells else EMPTY
                self.assertEqual(b.query(i, j), state)

        expected_str = '*--\n-*-'
        self.assertEqual(expected_str, str(b))

    def test_game_logic(self):
        self.assertEqual(game_logic(ALIVE, 4), EMPTY)
        self.assertEqual(game_logic(ALIVE, 1), EMPTY)
        self.assertEqual(game_logic(ALIVE, 2), ALIVE)
        self.assertEqual(game_logic(ALIVE, 3), ALIVE)

        self.assertEqual(game_logic(EMPTY, 3), ALIVE)
        self.assertEqual(game_logic(EMPTY, 5), EMPTY)
        self.assertEqual(game_logic(EMPTY, 2), EMPTY)

    def test_count_neighbors(self):
        it = count_neighbors(1, 1)
        query = next(it)
        for i in range(8):
            state = ALIVE if i % 2 == 0 else EMPTY
            try:
                it.send(state)
            except StopIteration as e:
                self.assertEqual(e.value, 4)

    def test_step_cell(self):
        """just get rid of syntax errorrs for my own sanity"""
        b = Board(2, 3)
        b.assign(0, 0, ALIVE)
        b.assign(1, 1, ALIVE)

        it = step_cell(b)
        q = next(it)
        self.assertEqual(q, Query(0, 0))

    def test_live_a_generation(self):
        """Test fetching simulating the next gen ok"""
        b = Board(2, 3)
        b.assign(0, 0, ALIVE)
        b.assign(1, 1, ALIVE)
        b2 = live_a_generation(b)
        self.assertEqual(str(b2), '***\n***')  # full population due to wrap around

        b3 = live_a_generation(b2)
        self.assertEqual(str(b3), '---\n---')  # all empty


