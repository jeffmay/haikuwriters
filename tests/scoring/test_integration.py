from unittest import TestCase
from haikuwriters.scoring.algebra import Multiply
from haikuwriters.scoring.cond import LessThan, Or, IfCond, And, GreaterThan
from haikuwriters.scoring.tree import Score, BlankText


class TestIntegration(TestCase):
    def setUp(self):
        self.program = Multiply(
            IfCond(
                condition=Or(LessThan(Score(0), Score(-1)), And(GreaterThan(Score(1), Score(0)))),
                then=Score(1),
                otherwise=Score(-1)
            ),
            Score(5)
        )

    def test_complex(self):
        self.assertEqual(5, self.program.score(BlankText))

    def test_reproducible(self):
        dump = repr(self.program)
        loaded = eval(dump)
        self.assertEqual(self.program, loaded)
