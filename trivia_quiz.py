"""
@uthor: Himaghna Bhattacharjee, 6th January 2019
Description: An interactive quiz !
"""

import numpy as np

def ask_question(question_number, questions):
    """

    :param question_number:(int) Question number to ask
    :param questions:(string) List of questions
    :return: (string) Question to ask
    """
    #consecutive lines in list(questions) is question(line1) and option(line2)
    #hence line number for kth questions is 2*k and line number for options
    #is 2*k+1
    question_line = questions[2*question_number]
    options_line = questions[2*question_number + 1]
    return '\n' + question_line +'\n'+options_line

def check_correctness(response, question_number, answers):
    """

    :param response: response that was entered to the question
    :param question_number: question number for the question asked
    :param answers: list of all answers indexed by question number
    :return: True (if correct) False otherwise
    """
    correct_answer = answers[question_number].strip('\n').lower()
    if response == correct_answer:
        return True  # correct
    return False  # incorrect

def __main__():
    question_file = './questions.txt'
    answer_file = './answers.txt'
    with open(question_file, "r") as fp:
        questions = fp.readlines()
    with open(answer_file, "r") as fp:
        answers = fp.readlines()
    quiz_size = len(answers)
    questions_asked = list()
    correct_answered = 0
    print("--- Welcome to Trivia! ---")
    to_continue = input("Press any key to continue")
    to_continue = True
    while to_continue:
        question_number = np.random.randint(low=0, high=quiz_size)
        if question_number in questions_asked:
            # question has already been asked!
            continue
        else:
            print(ask_question(question_number, questions))
            response = input("Enter an option: ")
            response = response.lower()  #convert response to lowercase
            if response not in ['a', 'b', 'c', 'd']:
                print("Invalid response. Game will continue\n")
                continue
            else:
                correct = check_correctness(response=response,
                                            question_number=question_number,
                                            answers=answers)
                if not correct:
                    # incorrect answer
                    print("Incorrect answer :(\n")
                else:
                    #correct answer
                    correct_answered += 1
                    print("Five points to Gryffindor!\n")
                continue_response = input("Do you want to continue? (Y/N)")
                continue_response = continue_response.lower()
                if continue_response == 'y':
                    pass
                else:
                    to_continue = False  # don't continue
            questions_asked.append(question_number)
            if len(questions_asked) == quiz_size and to_continue:
                print("Questions exhausted. Exiting")
                to_continue = False
    # print summary
    print("Your score is {}/{}".format(correct_answered, len(questions_asked)))


if __name__ == __main__():
    __main__()



