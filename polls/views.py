from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


def index(request):
    try:
        questions = Question.objects.order_by('-pub_date')[:8]
    except Question.DoesNotExist:
        raise Http404('No polls are exist')

    context = {'questions': questions}
    
    return render(request, 'polls/index_.html', context)

def list_polls(request):
    try:
        questions = Question.objects.order_by('-pub_date')
    except Question.DoesNotExist:
        raise Http404('No polls are exist')

    context = {'questions': questions}

    return render(request, 'polls/list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    
    return render(request, 'polls/detail.html', context)
    

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['choice']
        choice = get_object_or_404(question.choice_set, pk=choice_id)
        choice.votes += 1
        choice.save()
        question.popularity += 1
        question.save()
        return HttpResponseRedirect('/polls/'+str(question_id)+'/results/')
    except KeyError:
        context = {'error_message': 'please select a choice', 'question': question}
        return render(request, 'polls/detail.html', context)
