from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.topic_name


class Question(models.Model):
    question_topic = \
        models.ForeignKey(
            Topic,
            on_delete=models.CASCADE
        )
    question_question = models.CharField(max_length=200)
    question_answer = models.TextField()
    
    def __str__(self):
        return f"{self.question_topic} - {self.question_question}"
    