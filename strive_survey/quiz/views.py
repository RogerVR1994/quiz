from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question


def quiz(request):
    latest_question_list = Question.objects.order_by('question_id')
    output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'quiz/index.html', context)

def questions(request, question_id):
    print(request.body)
    try:
        question = Question.objects.get(pk = question_id)
        total_questions = Question.objects.count()
    except Question.DoesNotExist:
        return render(request, 'quiz/error.html')
    return render(request, 'quiz/questions.html', {
                                                    'question': question.question_text, 
                                                    'question_id': "quiz/questions/" + str(question_id + 1),
                                                    'current_question': question_id,
                                                    'total_questions': total_questions,
                                                    'progress': (question_id/total_questions)*100
                                                    }
                )

def thanks(request):
    return render(request, 'quiz/thanks.html')
