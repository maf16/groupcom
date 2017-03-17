from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_occurrence = models.IntegerField(default=0, verbose_name=1)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)
    #creation_date =
    #edit_date =

    def __str__(self):
        return self.answer_text
