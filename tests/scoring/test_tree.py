from unittest import TestCase
from haikuwriters.scoring import *


class TestScoreTree(TestCase):
    def test_str_empty(self):
        self.assertEqual("Empty", str(Empty))

    def test_repr_empty(self):
        self.assertEqual("Empty", repr(Empty))

    def test_str_empty_equals_str_none_tree(self):
        self.assertEqual(str(Empty), str(ScoreTree(None)))

    def test_repr_empty_equals_repr_none_tree(self):
        self.assertEqual(repr(Empty), repr(ScoreTree(None)))

    def test_equal_empty_and_none_tree(self):
        self.assertEqual(Empty, ScoreTree(None))

    def test_score_empty(self):
        self.assertEqual(NotImplemented, Empty.score(BlankText))


class TestScore(TestCase):

    def setUp(self):
        self.one = Score(1)
        self.zero = Score(0)

    def test_str_score(self):
        self.assertEqual("1", str(self.one))

    def test_repr_score(self):
        self.assertEqual("Score(1)", repr(self.one))

    def test_equal_scores(self):
        self.assertEqual(self.one, self.one)

    def test_not_equal_scores(self):
        self.assertNotEqual(self.one, self.zero)

    def test_score_one(self):
        self.assertEqual(1, self.one.score(BlankText))


class TestScoreTerm(TestCase):

    def setUp(self):
        self.a_one = ScoreTerm("a", Score(1))
        self.x_empty = ScoreTerm("x", Empty)
        self.y_empty = ScoreTerm("y", Empty)
        self.nest_x = ScoreTerm("nest_x", self.x_empty)
        self.nest_y = ScoreTerm("nest_y", self.y_empty)

    def test_str_empty(self):
        self.assertEqual("x@Empty", str(self.x_empty))

    def test_str_score(self):
       self.assertEqual("a@1", str(self.a_one))

    def test_repr_empty(self):
        self.assertEqual("ScoreTerm('x', Empty)", repr(self.x_empty))

    def test_repr_score(self):
        self.assertEqual("ScoreTerm('a', Score(1))", repr(self.a_one))

    def test_equal_scoreterm(self):
        self.assertEqual(self.x_empty, self.x_empty)

    def test_not_equal_scoreterm(self):
        self.assertNotEqual(self.x_empty, self.y_empty)

    def test_equal_nested_scoreterm(self):
        self.assertEqual(self.nest_x, self.nest_x)

    def test_not_equal_nested_scoreterm(self):
        self.assertNotEqual(self.nest_x, self.nest_y)

    def test_score_one_not_equal_scoreterm_one(self):
        self.assertNotEqual(Score(1), self.a_one)

    def test_score_empty_not_equal_scoreterm_empty(self):
        self.assertNotEqual(Empty, self.x_empty)

    def test_score_one_not_equal_scoreterm_empty(self):
        self.assertNotEqual(Score(1), self.x_empty)

    def test_scoreterm_one_score(self):
        self.assertEqual(1, self.a_one.score(BlankText))

    def test_scoreterm_empty_score(self):
        self.assertEqual(Empty.score(BlankText), self.x_empty.score(BlankText))
