from django.core.management.base import BaseCommand
from pprint import pprint
BASEPATH = '/Users/maf/Documents/Django/groupcom/ask/management/commands/'


class Command(BaseCommand):
    def handle(self, **options):
        questions = []
        full_doc = open(BASEPATH + 'full_doc.txt')
        target_doc = open(BASEPATH + '75_questions.txt','w')
        for line in full_doc:
            if line[0].isdigit():
                questions.append(line)
                target_doc.write(line)
        pprint(questions)
        print('list length: %s' %len(questions))


