from unittest import TestCase

from game import Game


class TestsGameAskQuestion(TestCase):
    expected_place_category_mapping = {
        0: "Pop",
        1: "Science",
        2: "Sports",
        3: "Rock",
        4: "Pop",
        5: "Science",
        6: "Sports",
        7: "Rock",
        8: "Pop",
        9: "Science",
        10: "Sports",
        11: "Rock",
    }

    def test_ask_question__provide_the_correct_category__pop(self):
        game = Game()
        place = 'Pop'
        game.places[0] = place
        self.assertTrue(game._ask_question().endswith('0'))

    def test_ask_question__provide_the_correct_category__science(self):
        game = Game()
        place = 'Science'
        game.places[0] = place
        self.assertTrue(game._ask_question().endswith('1'))
