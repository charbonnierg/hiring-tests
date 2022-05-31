class Game:
    players = []
    places = [None] * 6
    purses = [None] * 6
    in_penalty_box = [None] * 6

    pop_questions = []
    science_questions = []
    sports_questions = []
    rock_questions = []

    current_player = 0
    is_getting_out_of_penalty_box = False

    def create_rock_question(self, index):
        return "Rock Question " + str(index)

    def __init__(self):
        for i in range(50):
            self.pop_questions.append("Pop Question " + str(i))
            self.science_questions.append("Science Question " + str(i))
            self.sports_questions.append("Sports Question " + str(i))
            self.rock_questions.append(self.create_rock_question(i))

    def did_the_player_win(self):
        return not (self.purses[self.current_player] == 6)

    def current_category(self):
        if self.places[self.current_player] == 0:
            return 'Pop'
        if self.places[self.current_player] == 4:
            return 'Pop'
        if self.places[self.current_player] == 8:
            return 'Pop'
        if self.places[self.current_player] == 1:
            return 'Science'
        if self.places[self.current_player] == 5:
            return 'Science'
        if self.places[self.current_player] == 9:
            return 'Science'
        if self.places[self.current_player] == 2:
            return 'Sports'
        if self.places[self.current_player] == 6:
            return 'Sports'
        if self.places[self.current_player] == 10:
            return 'Sports'
        return 'Rock'

    places = places

    def is_playable(self, how_many_players):
        return how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players() - 1] = 0
        self.purses[self.how_many_players() - 1] = 0
        self.in_penalty_box[self.how_many_players() - 1] = False

        print(player_name + " was added")
        print("They are player number " + str(len(self.players)))

        return True

    def how_many_players(self):
        return len(self.players)

    def _ask_question(self):
        if self.current_category() == 'Pop':
            return self.pop_questions.pop(0)
        if self.current_category() == 'Science':
            return self.science_questions.pop(0)
        if self.current_category() == 'Sports':
            return self.sports_questions.pop(0)
        if self.current_category() == 'Rock':
            return self.rock_questions.pop(0)

    def ask_question(self):
        print(self._ask_question())

    def roll(self, roll):
        print(self.players[self.current_player] + " is the current player")
        print("They have rolled a " + str(roll))

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print(self.players[self.currentPlayer] + " is getting out of the penalty box")
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(self.players[self.current_player] + "'s new location is " + str(self.places[self.current_player]))
                print("The category is " + self.current_category())
                self.ask_question()
            else:
                print(self.players[self.current_player] + " is not getting out of the penalty box")
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(self.players[self.current_player] + "'s new location is " + str(self.places[self.current_player]))
            print("The category is " + self.current_category())
            self.ask_question()

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + " now has " +
                      str(self.purses[self.current_player]) + " Gold Coins.")

                winner = self.did_the_player_win()
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players):
                    self.current_player = 0
                return True
        else:
            print('Answer was correct!!!!')
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + " now has " +
                  str(self.purses[self.current_player]) + " Gold Coins.")

            winner = self.did_the_player_win()

            self.current_player += 1
            if self.current_player == len(self.players):
                self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.places):
            self.current_player = 0
        return True
