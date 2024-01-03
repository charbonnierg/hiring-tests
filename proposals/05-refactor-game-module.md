# Refactor game module


1. State initialization is a mess:
    - Some state is initialized at class definition (line 2 to 15)
    - Some state is initialized at init (line 21 to 27)
    - Some state is initialized using factories but not others (line 17/18)


2. No separation of concern:
    - The game is responsible for generating the card deck in the current implemetation.
        It would make sense for the game to "accept" a card deck as an argument.

3. No data structures:
    - Players are represented using primary types which makes the code more complex
    - Player position and player purse are stored in primary data stuctures (lists)

4. No random generation:
    - There is a roll method, but there is no way to generate a random data. It makes it more difficult to write the game_runner.py
