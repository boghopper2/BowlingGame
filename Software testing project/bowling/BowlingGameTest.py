
# @project: Bowling Game Testing Finn Hawkes

import unittest
from Bowling import BowlingGame


class BowlingGameTests(unittest.TestCase):

    # Test for seeing if when intenonally missing the score remains zero

    def test_all_gutters(self):

        game = BowlingGame()
        game.throw_many(20, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)

    # Test for checking it is plausable to hit the perfect game score of 300

    # def test_perfect_game(self):
       
    #     game = BowlingGame()
    #     game.throw_many(12, 10)
    #     game.calculate_score()
    #     self.assertEqual(game.score, 300)

    # Test for only hitting one pin on every roll

    # def test_all_ones(self):

    #     game = BowlingGame()
    #     number_of_times = 20
    #     pins = 1
    #     game.throw_many(number_of_times, pins)
    #     game.calculate_score()
    #     self.assertEqual(game.score, 20)

    # adding a test method for different types of throws

    # def test_different_throws(self):

    #     game = BowlingGame()
    #     game.throw_one(6)
    #     game.throw_one(0)
    #     game.throw_one(7)
    #     game.throw_one(0)
    #     game.throw_one(2)
    #     for _ in range(15):
    #         game.throw_one(0)
    #     game.calculate_score()
    #     self.assertEqual(game.score, 15)

    # Test for checking what happens when you get a spare

    # def test_for_spare(self):

    #     game = BowlingGame()
    #     game.throw_one(4)
    #     game.throw_one(6)
    #     game.throw_one(7)
    #     game.throw_one(0)
    #     for _ in range(16):
    #         game.throw_one(0)
    #     game.calculate_score()
    #     self.assertEqual(game.score, 24)

    # adding test method to test with one strike

    # def test_for_one_strike(self):

    #     game = BowlingGame()
    #     game.throw_one(10)
    #     game.throw_one(3)
    #     game.throw_one(5)
    #     game.throw_many(19, 0)
    #     game.calculate_score()
    #     self.assertEqual(game.score, 26)

    # adding test method to test 2 strikes

    # def test_for_two_strikes(self):

    #     game = BowlingGame()
    #     game.throw_one(10)
    #     game.throw_one(10)
    #     game.throw_one(4)
    #     game.throw_one(2)
    #     game.throw_many(26, 0)
    #     game.calculate_score()
    #     self.assertEqual(game.score, 46)

# calling all tests in this class to be executed
if __name__ == '__main__':
    unittest.main()
