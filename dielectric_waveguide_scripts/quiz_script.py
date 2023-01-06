import yaml

from IPython.display import display, HTML

class Quiz:
    def __init__(self,
                 quiz_path='dielectric_waveguide_scripts/quiz.yml'):
        
        with open(quiz_path, 'r') as file:
            quiz_info = yaml.safe_load(file)
 
        self.questions = quiz_info['questions']
        self.answers = quiz_info['answers']
        self.correct = quiz_info['correct']
        
        self.quiz_answers = []
        
    def run_quiz(self):
        button_template = '<button class="btn btn-primary mr-2" onclick="display_result({}, \'{}\')">{}) {}</button>'
        
        for i in range(len(self.questions)):
            display(HTML('<b>Question {}:</b>'.format(i+1)))
            display(HTML(self.questions[i]))
            
            for j in range(len(self.answers[i])):
                button = button_template.format(i+1, chr(65+j), chr(65+j), self.answers[i][j])
                display(HTML(button))
                
            while True:
                answer = input(f'Enter the answer for question {i+1}: ')
                if answer in [chr(65+k) for k in range(len(self.answers[i]))]:
                    self.quiz_answers.append(answer)
                    break
                else:
                    print(f'Invalid answer. Please enter a valid answer ({[chr(65+k) for k in range(len(self.answers[i]))]}).')
                    
    def check_quiz_answers(self):
        correct_answers = 0
        incorrect_answers = 0
        
        for i in range(len(self.questions)):
            if self.quiz_answers[i] == self.correct[i]:
                correct_answers += 1
            else:
                incorrect_answers += 1
        print('-----')
        print(f'Your answers:    {self.quiz_answers}')
        print(f'Correct answers: {self.correct}')
        print('-----')
        print(f'Number of correct answers:   {correct_answers}')
        print(f'Number of incorrect answers: {incorrect_answers}')
       