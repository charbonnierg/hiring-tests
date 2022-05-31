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

    def test_ask_question(self):
        def provide_the_correct_category(place, category):
            game = Game()
            game.places[0] = place
            self.assertTrue(game._ask_question().startswith(category))

        for place, category in self.expected_place_category_mapping.items():
            provide_the_correct_category(place, category)

