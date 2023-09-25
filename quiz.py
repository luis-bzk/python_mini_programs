quiz = {
    'question_one': {
        'question': 'What is the capital of France?',
        'answer': 'Paris',
    },
    'question_two': {
        'question': 'What is the capital of Germany?',
        'answer': 'Berlin',
    },
    'question_three': {
        'question': 'What is the capital of Italy?',
        'answer': 'Rome',
    },
    'question_four': {
        'question': 'What is the capital of Spain?',
        'answer': 'Madrid',
    },
    'question_five': {
        'question': 'What is the capital of Portugal?',
        'answer': 'Lisboa',
    },
    'question_six': {
        'question': 'What is the capital of Switzerland?',
        'answer': 'Bern',
    },
    'question_seven': {
        'question': 'What is the capital of Austria?',
        'answer': 'Vienna',
    }
}
score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer: ')

    if answer.lower() == value['answer'].lower():
        print('Correct 😎')
        score = score + 1
        print(f'Your score: {score}/{len(quiz)}')
    else:
        print('Incorrect ☠️')
        print(f'The answer is {value["answer"]} 😵‍💫')
        print(f'Your score: {score}/{len(quiz)}')
