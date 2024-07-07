import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *

def home(request):
    content = {'categories':Types.objects.all()}

    if request.GET.get('gfg'):
        return redirect(f"/quiz/?gfg={request.GET.get('gfg')}")
    return render(request, 'home.html', content)

def quiz(request):
    context = {'gfg': request.GET.get('gfg')}
    return render(request, 'quiz.html', context)

def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        if request.GET.get('gfg'):
            question_objs = Question.objects.filter(gfg__type_name__icontains =request.GET.get('gfg'))
        question_objs = list(question_objs)
        data=[]
        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                "uid" : question_obj.uid,
                "gfg" : question_obj.gfg.type_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()
            })
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
            print(e)
            return HttpResponse("Something went wrong")


# Create your views here.
