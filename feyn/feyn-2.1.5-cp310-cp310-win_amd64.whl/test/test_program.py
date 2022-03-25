import unittest

from feyn._program import Program


class TestProgram(unittest.TestCase):

    def test_init_invalid_program_only_output(self):
        with self.assertRaises(ValueError):
            Program([10000], qid=1, autopad=True)

    def test_len(self):
        with self.subTest("A single terminal has length 2"):
            program = Program([10000, 10001], qid=1, autopad=True)
            self.assertEqual(len(program), 2)

        with self.subTest("A single unary has length 3"):
            program = Program([10000, 1000, 10001], qid=1, autopad=True)
            self.assertEqual(len(program), 3)

        with self.subTest("A single arity 2 has length 3"):
            program = Program([10000, 2000, 10001, 10002], qid=1, autopad=True)
            self.assertEqual(len(program), 4)

        with self.subTest("A more complex program"):
            program = Program([10000, 2001,2001,1001,10001,10002,10003], qid=1, autopad=True)
            self.assertEqual(len(program), 7)

        with self.subTest("Nonsensical tail gets cut off"):
            # This part creates a completed graph from output to inputs
            valid_program = [10000, 2000, 10001, 10002]

            # The rest here is just remains coming from the QLattice that
            # with proper mutations in the valid program could end up geting
            # connected to the graph later.
            rest = [10002, 10002, 10000]

            program = Program(valid_program + rest, qid=1, autopad=True)
            self.assertEqual(len(program), 4)

    def test_program_parent(self):
        program = Program([10000, 1000, 2000, 1000, 10001, 2000, 10002, 10003], qid=1, autopad=True)
        expected_parent_ixs = [0, 0, 1, 2, 3, 2, 5, 5]
        parent_ixs = [program.find_parent(ix) for ix in range(8)]
        self.assertEqual(expected_parent_ixs, parent_ixs)
