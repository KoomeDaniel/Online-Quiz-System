import uuid
import random
from django.db import models

class Quiz(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Set editable to False
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Types(Quiz):
    type_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.type_name
    
class Question(Quiz):
    gfg = models.ForeignKey(Types, related_name='gfg', on_delete=models.CASCADE)  # Improved related_name
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        data = []
        random.shuffle(answer_objs)
        for answer_obj in answer_objs:
            data.append({
                'answer': answer_obj.answer,
                'is_correct': answer_obj.is_correct
            })
        return data  # Dedented this line

class Answer(Quiz):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)  # Improved related_name
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer

