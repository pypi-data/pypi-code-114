import unittest

import numpy

import mock_game


class TestMockGame(unittest.TestCase):
    def setUp(self):
        self.game = mock_game.MockGame()
        print(self.game)
        self.board = self.game.get_board_state()

    def test_print_board(self):
        print_board_message = "\n "
        print_board_message += " | ".join(self.board[0])
        print_board_message += "\n---|---|---\n "
        print_board_message += " | ".join(self.board[1])
        print_board_message += "\n---|---|---\n "
        print_board_message += " | ".join(self.board[2])
        print_board_message += "\n"

        self.assertEqual(self.game.print_board(),print_board_message)

    def test_force_team(self):
        self.game.force_team("X")
        self.assertEqual(self.game.get_team(),"X")
        self.game.force_team("O")
        self.assertEqual(self.game.get_team(),"O")
        self.assertEqual(self.game.force_team("FAIL"),"Not a valid parameter value!")
    
    def test_opposite_team(self):
        self.game.force_team("X")
        self.assertEqual(self.game.opposite_team(self.game.get_team()),"O")
        self.game.force_team("O")
        self.assertEqual(self.game.opposite_team(self.game.get_team()),"X")
        self.assertEqual(self.game.opposite_team("FAIL"),"Not a valid parameter value!")

    def test_submit_move(self):
        for x in range(0, 3):
            for y in range(0, 3):
                self.game.submit_move(x, y)

                self.assertNotEqual(self.board[x][y], " ")
        

if __name__ == '__main__':
    unittest.main()
