from dataclasses import dataclass

@dataclass
class Testpaper:
    theme: str
    answers_scheme: list
    correct_answer: str

class Student:
    def __init__(self, testpaper: Testpaper=None, answers: list=[]):
        self.testpaper = testpaper
        self.answers = answers
        self._tests_taken = {}
        if testpaper:
            self._tests_taken[testpaper.theme] = check_answers(testpaper, answers)

    def take_test(self, testpaper: Testpaper, answers: list):
        if testpaper:
            self._tests_taken[testpaper.theme] = check_answers(testpaper, answers)

    @property
    def tests_taken(self):
        if self._tests_taken:
            return self._tests_taken
        return 'No tests taken'


def check_answers(testpaper: Testpaper, answers: list):
    truly_answers = 0
    for st_answer, corr_answer in zip(answers, testpaper.answers_scheme):
        if st_answer == corr_answer:
            truly_answers += 1
    answers_percs = int(round(truly_answers / len(testpaper.answers_scheme) * 100, 0))
    if answers_percs >= int(testpaper.correct_answer[:-1]):
        return f'Passed! ({answers_percs}%)'
    return f'Failed! ({answers_percs}%)'
      