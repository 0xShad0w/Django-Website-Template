from django.shortcuts import render
from .models import Topic, Question


def index(request):
    
    topic_questions = {}
    
    topics = Topic.objects.all()
    
    for t in topics:
        questions = Question.objects.filter(question_topic_id=t)
        topic_questions[t] = questions
    
    context = {'topic_questions': topic_questions}
    return render(request, 'FAQ/index.html', context)