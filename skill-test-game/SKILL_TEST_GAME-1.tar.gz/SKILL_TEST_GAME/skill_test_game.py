"""
This class contains code for the game "Skill Test Game".
Author: DigitalCreativeApkDev

This game is inspired by LinkedIn Skill Assessments (https://www.linkedin.com/skill-assessments/hub/quizzes/).
"""

# Game version: pre-release


# Importing necessary libraries


import sys
import uuid
import pickle
import copy
import random
from datetime import datetime, timedelta
import os

from mpmath import mp, mpf

mp.pretty = True


# Creating static functions to be used in this game.


def load_player_data(file_name):
    # type: (str) -> Player
    return pickle.load(open(file_name, "rb"))


def save_player_data(player_data, file_name):
    # type: (Player, str) -> None
    pickle.dump(player_data, open(file_name, "wb"))


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating necessary classes to be used in the game.


class Player:
    """
    This class contains attributes of the player in this game.
    """

    def __init__(self, name, available_skill_tests):
        # type: (str, list) -> None
        self.player_id: str = str(uuid.uuid1())  # Generating random player ID
        self.name: str = name
        self.__badges_earned: list = []  # initial value
        self.__available_skill_tests: list = available_skill_tests
        self.__locked_skill_tests: list = []  # initial value

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += "Player ID: " + str(self.player_id) + "\n"
        res += "Name: " + str(self.name) + "\n"
        res += "You have earned " + str(len(self.__badges_earned)) + " skill badges!\n\n"
        for skill_badge in self.__badges_earned:
            res += str(skill_badge) + "\n"

        return res

    def add_skill_badge(self, skill_badge):
        # type: (SkillBadge) -> None
        self.__badges_earned.append(skill_badge)

    def lock_skill_test(self, skill_test):
        # type: (SkillTest) -> bool
        if skill_test in self.__available_skill_tests:
            if skill_test.lock():
                self.__available_skill_tests.remove(skill_test)
                self.__locked_skill_tests.append(skill_test)
                return True
            return False
        return False

    def unlock_skill_test(self, skill_test):
        # type: (SkillTest) -> bool
        if skill_test in self.__locked_skill_tests:
            if skill_test.unlock():
                self.__locked_skill_tests.remove(skill_test)
                self.__available_skill_tests.append(skill_test)
                return True
            return False
        return False

    def get_available_skill_tests(self):
        # type: () -> list
        return self.__available_skill_tests

    def get_locked_skill_tests(self):
        # type: () -> list
        return self.__locked_skill_tests

    def get_badges_earned(self):
        # type: () -> list
        return self.__badges_earned

    def clone(self):
        # type: () -> Player
        return copy.deepcopy(self)


class SkillTest:
    """
    This class contains attributes of a skill test in this game.
    """

    def __init__(self, name, potential_questions):
        # type: (str, list) -> None
        self.name: str = name
        self.__potential_questions: list = potential_questions
        self.is_unlocked: bool = True
        self.unlock_time: datetime or None = None
        self.remaining_attempts: int = 2
        self.skill_badge_earned: bool = False

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += str(self.name).upper() + "\n"
        res += "Remaining attempts: " + str(self.remaining_attempts) + "\n"
        return res

    def lock(self):
        # type: () -> bool
        if self.remaining_attempts == 0:
            self.is_unlocked = False
            now: datetime = datetime.now()
            self.unlock_time = now + timedelta(days=182)
            return True
        elif self.skill_badge_earned:
            self.is_unlocked = False
            self.unlock_time = None
            return True
        return False

    def unlock(self):
        # type: () -> bool
        if not self.is_unlocked and not self.skill_badge_earned:
            if isinstance(self.unlock_time, datetime):
                now: datetime = datetime.now()
                if now >= self.unlock_time:
                    self.is_unlocked = True
                    self.unlock_time = None
                    self.remaining_attempts = 2
                    return True
                return False
            return False
        return False

    def get_potential_questions(self):
        # type: () -> list
        return self.__potential_questions

    def clone(self):
        # type: () -> SkillTest
        return copy.deepcopy(self)


class Question:
    """
    This class contains attributes of a question in a skill test.
    """

    def __init__(self, question, choices, correct_answer):
        # type: (str, list, str) -> None
        self.question: str = question
        self.__choices: list = choices
        self.correct_answer: str = correct_answer

    def __str__(self):
        # type: () -> str
        res: str = str(self.question) + "\n"  # initial value
        for choice in self.__choices:
            res += str(choice) + "\n"

        return res

    def get_choices(self):
        # type: () -> list
        return self.__choices

    def clone(self):
        # type: () -> Question
        return copy.deepcopy(self)


class SkillBadge:
    """
    This class contains attributes of a skill badge.
    """

    def __init__(self, skill_test_name, score):
        # type: (str, mpf) -> None
        self.skill_test_name: str = skill_test_name
        self.score: mpf = score

    def __str__(self):
        # type: () -> str
        res: str = ""  # initial value
        res += "Skill test name: " + str(self.skill_test_name) + "\n"
        res += "Score: " + str(self.score) + "%\n"
        return res

    def clone(self):
        # type: () -> SkillBadge
        return copy.deepcopy(self)


# Creating main function used to run the game.


def main():
    """
    This main function is used to run the game.
    :return: None
    """

    print("Welcome to 'Skill Test Game' by 'DigitalCreativeApkDev'.")
    print("In this game, you will answer questions from skill tests to earn skill badges ")
    print("like in LinkedIn Skill Assessments (https://www.linkedin.com/skill-assessments/hub/quizzes/).")
    print("To earn a skill badge, you will need to answer at least 80% of the questions in the skill test correctly.")

    # Initialising function level variables to be used in the game.
    # 1. Available skill tests.
    available_skill_tests: list = [
        SkillTest("Python",
                  [
                    Question("Which built-in list method is used to add an element to a list? ",
                             [
                                 "A. .add()",
                                 "B. .append()",
                                 "C. add_elem(my_list, elem)",
                                 "D. insert_elem(my_list, elem)"
                             ], "B"),
                    Question("What is the correct syntax used to initialise a new object of type Car? ",
                      [
                          "A. car = new Car()",
                          "B. Car car = new Car()",
                          "C. Car car = Car()",
                          "D. car = Car()"
                      ], "D"),
                    Question("What happens if you do not explicitly return the value of a function? ",
                             [
                                 "A. A RuntimeError.",
                                 "B. True is returned by default.",
                                 "C. None is returned by default.",
                                 "D. 0 is returned by default."
                             ], "C"),
                    Question("How many arguments does the following function have?\ndef sum(a: int, b: int) -> int",
                             [
                                 "A. 0",
                                 "B. 1",
                                 "C. 2",
                                 "D. 3"
                             ], "C"),
                    Question("When does a while loop stop iterating? ",
                             [
                                 "A. When the condition is False.",
                                 "B. It will never stop iterating.",
                                 "C. When the condition is True.",
                                 "D. When either the condition is False or the break keyword is encountered."
                             ], "D"),
                    Question("Which collection type is associated with unique keys? ",
                             [
                                 "A. list",
                                 "B. dictionary",
                                 "C. linked list",
                                 "D. set"
                             ], "B"),
                    Question("How many times will the following loop be executed?\n"
                             "for i in range(1, 5, 2):\n    print(i)",
                             [
                                 "A. 1",
                                 "B. 2",
                                 "C. 3",
                                 "D. 4"
                             ], "B"),
                    Question("Is it possible to annotate types of each variable defined in a program in Python 3.x? ",
                             [
                                 "A. Yes. 'a: int = 5' is an example of doing so.",
                                 "B. Yes. 'int a = 5' is an example of doing so.",
                                 "C. No. Because Python is not a static-typed language.",
                                 "D. Yes. 'let a: int = 5' is an example of doing so,"
                             ], "A"),
                    Question("What would this expression return?\na = [1, 2, 3, 4, 5]\na[0] = 6\nprint(sum(a))",
                             [
                                 "A. 15",
                                 "B. 20",
                                 "C. 25",
                                 "D. 30"
                             ], "B"),
                    Question("Which of the following types in Python can be used as function arguments? ",
                             [
                                 "A. function",
                                 "B. int",
                                 "C. bool",
                                 "D. All of the above"
                             ], "D"),
                    Question("What happens if the 'and' keyword is used between conditions a and b? ",
                             [
                                 "A. True will be returned if both conditions a and b are False.",
                                 "B. True will be returned if both conditions a and b are True.",
                                 "C. True will be returned if either one of the conditions a and b is True.",
                                 "D. True will be returned if a is True but b is False."
                             ], "B"),
                    Question("What symbol do you use to assess equality between two elements? ",
                             [
                                 "A. ==",
                                 "B. !=",
                                 "C. ||",
                                 "D. &&"
                             ], "A"),
                    Question("What would be the output of the following expression?\na = 5\nb = 6\nprint(a and b)",
                             [
                                 "A. error",
                                 "B. True",
                                 "C. 5",
                                 "D. 6"
                             ], "D"),
                    Question("Review the code below. What is the correct syntax to change the currHP to 0?\n"
                             "player = {'name' : 'random', 'currHP' : 500, 'maxHP' : 1000, 'attack' : 275}",
                             [
                                 "A. 0 = player['currHP']",
                                 "B. player['currHP'] == 0",
                                 "C. player['currHP'] = 0",
                                 "D. player.currHP = 0"
                             ], "C"),
                    Question("Which of the following is the correct code to get the sum of the first 5 "
                             "positive integers using a for loop?",
                             [
                                 "A. sum = 0\nfor i in range(1, 5):\n    sum += i\nprint(sum)",
                                 "B. sum = 0\nfor i in range(1, 6):\n    sum += i\nprint(sum)",
                                 "C. sum = 0\nfor i in range(0, 5):\n    sum += i\nprint(sum)",
                                 "D. sum = 1\nfor i in range(0, 6):\n    sum += i\nprint(sum)",
                             ], "B"),
                    Question("Where can a return statement be used?",
                             [
                                 "A. Inside a static function.",
                                 "B. Inside a class method.",
                                 "C. Inside a lambda.",
                                 "D. Both A and B but not C."
                             ], "D"),
                    Question("Which of the following is the correct syntax to define a lambda in Python?",
                             [
                                 "A. mult = lambda a, b: a * b",
                                 "B. mult = lambda a, b: return a * b",
                                 "C. lambda a, b: a * b = mult",
                                 "D. lambda a, b: return a * b = mult"
                             ], "A"),
                    Question("Which of the following data types in Python can be unpacked?",
                             [
                                 "A. list",
                                 "B. tuple",
                                 "C. No data types",
                                 "D. Both A and B"
                             ], "D"),
                    Question("Which of the following is not a valid example of list unpacking?",
                             [
                                 "A. f  = [1, 2, 3]\na, b, c = f",
                                 "B. f  = [1, 2, 3]\na, b, *c = f",
                                 "C. f  = [1, 2, 3, 4]\na, b, c = f",
                                 "D. f  = [1, 2, 3, 4]\na, b, *c = f",
                             ], "C"),
                    Question("What is the output of the following code?\nf = [1, 2, 3, 4, 5]\na, *b, c = f\nprint(b)",
                             [
                                 "A. 1",
                                 "B. 2"
                                 "C. [2, 3, 4]"
                                 "D. 5"
                             ], "C"),
                    Question("When unpacking a list or tuple, what is the maximum number of variables we can "
                             "add asterisk (*) to?",
                             [
                                 "A. 0",
                                 "B. 1",
                                 "C. 2",
                                 "D. No limit"
                             ], "B"),
                    Question("What is the output of the following code?\nf = (1, 2, 3)\na, b, *c = f\nprint(type(c))",
                             [
                                 "A. int",
                                 "B. list",
                                 "C. tuple",
                                 "D. None"
                             ], "B"),
                    Question("What is the output of the following code?\nf = (1, 2, 3)\na, b, c, *d = f\nprint(f)",
                             [
                                 "A. None",
                                 "B. []",
                                 "C. 0",
                                 "D. error"
                             ], "B"),
                    Question("Which of the following is the correct code to remove the second element from a list "
                             "'a_list'?",
                             [
                                 "A. a_list.pop()",
                                 "B. a_list.pop(1)",
                                 "C. delete a_list[1]",
                                 "D. Both B and C"
                             ], "D"),
                    Question("What is the correct syntax used to define class 'Car', if it inherits "
                             "from a parent class called 'Vehicle'?",
                             [
                                 "A. class Car(Vehicle): pass",
                                 "B. class Vehicle.Car(): pass",
                                 "C. def Car(Vehicle): pass",
                                 "D. def Vehicle.Car(): pass"
                             ], "A"),
                    Question("What is the algorithm paradigm of quick sort?",
                             [
                                 "A. dynamic programming",
                                 "B. divide and conquer",
                                 "C. backtracking",
                                 "D. depth first search"
                             ], "B"),
                    Question("What is the difference between a set and a dictionary in terms of syntax?",
                             [
                                 "A. No difference",
                                 "B. A dictionary uses colons to separate keys and values, a set only includes values.",
                                 "C. A set uses colons to separate keys and values, a dictionary only includes values.",
                                 "D. A set must use the keyword 'set', a dictionary can be defined using curly braces "
                                 "(i.e., '{' and '}')."
                             ], "B"),
                    Question("Which type of loop does not exist in Python?",
                             [
                                 "A. for",
                                 "B. while",
                                 "C. do-while",
                                 "D. All of the above exist"
                             ], "C"),
                    Question("Which statement correctly describes how items are added and removed from a stack?",
                             [
                                 "A. A stack add items to the top and removes item from the bottom.",
                                 "B. A stack add items to the bottom and removes item from the top.",
                                 "C. A stack add items to the top and removes item from the top.",
                                 "D. A stack add items on one side and removes items on the other side."
                             ], "C"),
                    Question("Which symbol is used to start line comments in Python?",
                             [
                                 "A. --",
                                 "B. //",
                                 "C. %",
                                 "D. #"
                             ], "D")
                  ])
    ]

    """
            SkillTest("Java",
                      [

                      ]),
            SkillTest("JavaScript",
                      [

                      ]),
            SkillTest("HTML",
                      [

                      ]),
            SkillTest("CSS",
                      [

                      ]),
            SkillTest("Microsoft Word",
                      [

                      ]),
            SkillTest("C++",
                      [

                      ]),
            SkillTest("C#",
                      [

                      ]),
            SkillTest("PHP",
                      [

                      ]),
            SkillTest("Microsoft Excel",
                      [

                      ])
    """

    # 2. Name of file containing saved game data
    file_name: str = "SAVED SKILL TEST GAME DATA - "

    # 3. Saved player data
    player_data: Player
    name: str = input("Please enter your name: ")
    try:
        player_data = load_player_data(file_name + str(name).upper())

        # Clearing up the command line window
        clear()

        print("Your current stats:\n" + str(player_data))
    except FileNotFoundError:
        # Clearing up the command line window
        clear()

        player_data = Player(name, available_skill_tests)

    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_playing: str = input("Do you want to continue playing 'Skill Test Game'? ")
    while continue_playing == "Y":
        # Clearing up the command line window
        clear()

        # Unlock all possible skill tests
        for skill_test in player_data.get_locked_skill_tests():
            player_data.unlock_skill_test(skill_test)

        if len(player_data.get_available_skill_tests()) > 0:
            print("Below is a list of skill tests you can take.\n")
            index: int = 1
            for skill_test in player_data.get_available_skill_tests():
                print(str(index) + "." + str(skill_test) + "\n")
                index += 1

            selected_index: int = int(input("Please enter the index of the skill test you want to take (1 - " +
                                            str(len(player_data.get_available_skill_tests())) + "): "))
            while selected_index < 1 or selected_index > len(player_data.get_available_skill_tests()):
                selected_index: int = int(input("Sorry, invalid input! Please enter the index of the skill test you "
                                                "want to take (1 - " +
                                                str(len(player_data.get_available_skill_tests())) + "): "))

            selected_skill_test: SkillTest = player_data.get_available_skill_tests()[selected_index - 1]

            # Proceed to asking 15 random questions from the selected skill test.
            selected_questions: list = []  # initial value
            score: int = 0
            for i in range(15):
                # Clearing up the command line window
                clear()

                curr_question: Question = selected_skill_test.get_potential_questions() \
                    [random.randint(0, len(selected_skill_test.get_potential_questions()) - 1)]
                while curr_question in selected_questions:
                    curr_question = selected_skill_test.get_potential_questions() \
                        [random.randint(0, len(selected_skill_test.get_potential_questions()) - 1)]

                max_time: datetime = datetime.now() + timedelta(seconds=90)
                answered: bool = False
                answer: str = ""
                while datetime.now() <= max_time and not answered:
                    selected_questions.append(curr_question)
                    print("Please answer the following question before " + str(max_time))
                    print(str(curr_question) + "\n")
                    answer = input("Your answer: ")
                    if answer == curr_question.correct_answer:
                        score += 1
                    else:
                        pass  # do nothing

                    answered = True

                if datetime.now() > max_time:
                    answer = ""

            final_score: mpf = mpf(score) / mpf("15") * mpf("100")

            # Clearing up the command line window
            clear()

            if final_score >= mpf("80"):
                print("Congratulations! You score " + str(final_score) + "% in " + str(selected_skill_test.name) +
                      " Skill Test!\nYou earn a skill badge!")
                skill_badge: SkillBadge = SkillBadge(str(selected_skill_test.name).upper() + " SKILL TEST", final_score)
                player_data.add_skill_badge(skill_badge)

                selected_skill_test.skill_badge_earned = True
                player_data.lock_skill_test(selected_skill_test)

                print("Enter 'Y' for yes.")
                print("Enter anything else for no.")
                add_to_linkedin_profile: str = input("Do you want to add your skill badge for " +
                                                     str(selected_skill_test.name).upper() + " SKILL TEST to your "
                                                                                        "LinkedIn profile? ")
                if add_to_linkedin_profile == "Y":
                    # Clearing up the command line window
                    clear()

                    print("Please press the '+' button in 'Test scores' section of your LinkedIn profile then "
                          "enter the following details.\n")
                    print("Title: " + str(skill_badge.skill_test_name) + " SKILL TEST (SKILL TEST GAME)")
                    print("Score: " + str(skill_badge.score) + "%\n\n")
            else:
                print("Better luck next time! You score " + str(final_score) + "% in " + str(selected_skill_test) +
                      " Skill Test!")
                selected_skill_test.remaining_attempts -= 1
                if selected_skill_test.remaining_attempts == 0:
                    player_data.lock_skill_test(selected_skill_test)
                    print("You can take " + str(selected_skill_test.name) + " Skill Test again at " +
                          str(selected_skill_test.unlock_time) + "!")
        else:
            print("Sorry! You have no skill tests you can currently take! Please wait!")

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_playing = input("Do you want to continue playing 'Skill Test Game'? ")

    # Saving game data and quitting the game.
    save_player_data(player_data, file_name + str(name).upper())
    return 0


if __name__ == '__main__':
    main()
