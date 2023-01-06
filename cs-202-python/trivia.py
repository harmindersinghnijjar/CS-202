
import random

class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correctAnswer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correctAnswer = correctAnswer

    # Accessor methods. 
    def set_question(self, question):
        self.__question = question

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_correctAnswer(self, correctAnswer):
        self.__correctAnswer = correctAnswer

    # Mutator methods.
    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correctAnswer(self):
        return self.__correctAnswer

def main():
    # Create the questions.
    question1 = Question("What is the capital of Australia?", "Melbourne", "Sydney", "Canberra", "Perth", 3)
    question2 = Question("What is the capital of Canada?", "Ottawa", "Toronto", "Vancouver", "Montreal", 1)
    question3 = Question("What is the capital of China?", "Beijing", "Shanghai", "Hong Kong", "Nanjing", 1)
    question4 = Question("What is the capital of France?", "Paris", "Bordeaux", "Lyon", "Toulouse", 1)
    question5 = Question("What is the capital of Germany?", "Munich", "Frankfurt", "Berlin", "Dusseldorf", 3)
    question6 = Question("What is the capital of Italy?", "Naples", "Venice", "Milan", "Rome", 4)
    question7 = Question("What is the capital of Japan?", "Tokyo", "Osaka", "Nagoya", "Fukuoka", 1)
    question8 = Question("What is the capital of Mexico?", "Mexico City", "Puebla", "Cuernavaca", "Tijuana", 1)
    question9 = Question("What is the capital of Russia?", "St. Petersburg", "Moscow", "Novosibirsk", "Kazan", 2)
    question10 = Question("What is the capital of the United States of America?", "Washington D.C.", "New York City", "Boston", "Los Angeles", 1)

    # Create the questions list.
    questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]

    # Shuffle the questions.
    random.shuffle(questions)

    #Create the players
    player1 = 0
    player2 = 0

    # Create the counters.
    count1 = 0
    count2 = 0

    # Create the answer variable.
    answer = 0

    # Create the game loop.
    while count1 < 5 and count2 < 5:
        print("Player 1\n")

        # Ask the questions.
        for question in questions:
            print(question.get_question())
            print(f"1.{question.get_answer1()}")
            print(f"2.{question.get_answer2()}")
            print(f"3.{question.get_answer3()}")
            print(f"4.{question.get_answer4()}")

            # Get the answer.
            answer = int(input("Please select an answer: "))
            print("\n")

            #Check the answer
            if answer == question.get_correctAnswer():
                player1 += 1
            count1 += 1

        print("Player 2\n")

        #Ask the questions
        for question in questions:
            print(question.get_question())
            print(f"1.{question.get_answer1()}")
            print(f"2.{question.get_answer2()}")
            print(f"3.{question.get_answer3()}")
            print(f"4.{question.get_answer4()}")

            #Get the answer
            answer = int(input("Please select an answer: "))
            print("\n")

            #Check the answer
            if answer == question.get_correctAnswer():
                player2 += 1
            count2 += 1

    #Output the winner
    if player1 > player2:
        print("Player 1 wins!")
    elif player2 > player1:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

main()