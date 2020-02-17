#! python3
# Random Quiz Generator from Automate the Boring Stuff with python3
# Creates quizzes with questions in random order, along with answer key
# 14 Feb 20

import random

# Quiz data: keys are states, values are capitals
capitals = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
'Hawaii': 'Honolulu',
'Idaho': 'Boise',
'Illinois': 'Springfield',
'Indiana': 'Indianapolis',
'Iowa': 'Des Moines',
'Kansas': 'Topeka',
'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge',
'Maine': 'Augusta',
'Maryland': 'Annapolis',
'Massachusetts': 'Boston',
'Michigan': 'Lansing',
'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson',
'Missouri': 'Jefferson City',
'Montana': 'Helena',
'Nebraska': 'Lincoln',
'Nevada': 'Carson City',
'New Hampshire': 'Concord',
'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe',
'New York': 'Albany',
'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck',
'Ohio': 'Columbus',
'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg',
'Rhode Island': 'Providence',
'South Carolina': 'Columbia',
'South Dakota': 'Pierre',
'Tennessee': 'Nashville',
'Texas': 'Austin',
'Utah': 'Salt Lake City',
'Vermont': 'Montpelier',
'Virginia': 'Richmond',
'Washington': 'Olympia',
'West Virginia': 'Charleston',
'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'
}

# we run the full loop 10 times to generate 10 quizzes
for quizNum in range(10):

    # open a file with the placeholder %s replaced by quizNum + 1
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    # opens an answer file in the same way
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # writes the title to the quiz file
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    # writes the title, again with a placeholder replaced by the number
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # creates a real list of the states; they are the keys in the dictionary
    states = list(capitals.keys())
    # this acts on the list, shuffling them into a random order
    random.shuffle(states)

# We now have all the states only shuffled into a random order.
# The next section will generate the 50 questions.

    # we need 50 iterations
    for questionNum in range(50):

        # the dictionary is unordered, so we're using a list in this next term
        # that we set up in line 77
        # states[questionNum] gives one of the states from the list (which has been shuffled)
        # this state is used as a key in the capitals dict
        # to pull the correct answer
        correctAnswer = capitals[states[questionNum]]
        # the wrong answers are the remaining values in the dictionary
        # we sort them into a list
        wrongAnswers = list(capitals.values())
        # the index method searches a list for the argument,
        # and returns the index.  We then delete that index,
        # removing the right answer from the list
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # now we resate the wrongAnswers variable as a random sample of 3 from itself
        wrongAnswers = random.sample(wrongAnswers, 3)
        # we create another list, with the wrong answers and the correct one
        answerOptions = wrongAnswers + [correctAnswer]
        # we ransomise the order of the answers
        random.shuffle(answerOptions)

        # for writing, we have 2 placeholders; one is the question number
        # (the +1 is needed because it starts at 0), the second is
        # the state name pulled from the list we made at 77 and shuffled at 79
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

        # this next loop works 4 times, once for each potential answer
        for i in range(4):
            # this is a new feature; the first placeholder treats 'ABCD' as an
            # array, and picks the value equivalent to i.
            # it then prints one of the options from our answerOptions
            # list, which was shuffled in line 105
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        # this writes the answer key.  The first placeholder is the question number,
        # the second one again treats ABCD as an array, and then looks at the answerOptions list
        # it checks which index is occupied by the right answer, and then pulls the appropriate
        # letter
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
