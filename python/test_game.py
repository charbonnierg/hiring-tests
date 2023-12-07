from unittest import TestCase

from game import Game


class TestsGameAskQuestion(TestCase):
    expected_place_category_mapping = {
        1: "Science",
        2: "Sports",
        3: "Rock",
        4: "Culture",
        5: "History",
        6: "Pop",
        7: "Science",
        8: "Sports",
        9: "Rock",
        10: "Culture",
        11: "History",
        12: "Pop",
        13: "Science",
        14: "Sports",
        15: "Rock",
        16: "Culture",
        17: "History",

    }

    def test_ask_question(self):
        def provide_the_correct_category(place, category):
            game = Game()
            game.places[0] = place
            self.assertTrue(game._ask_question().startswith(category))

        for place, category in self.expected_place_category_mapping.items():
            provide_the_correct_category(place, category)

