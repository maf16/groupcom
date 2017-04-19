from django.core.management.base import BaseCommand
import os
import sys
from ask.models import Question
from pprint import pprint
ROOT = os.path.dirname(__file__)
QUESTION_FOLDER = '/cleaned_questions/'


class Command(BaseCommand):
    def handle(self, **options):
        gen = QuestionGenerator()
        for question in gen:
            question.save()
        for n,question in enumerate(Question.objects.all()):
            print(n,question)


def list_files():
    for i in os.walk(ROOT + QUESTION_FOLDER):
        return i[2]


class QuestionGenerator(object):
    def __iter__(self):
        question_files = list_files()
        for file in question_files:
            file_handle = open(ROOT + QUESTION_FOLDER + file)
            for line in file_handle:
                # assume there's one document per line, tokens separated by whitespace
                line = line.replace("\n", "")
                obj, created = Question.objects.get_or_create(question_text = line)
                yield obj


