from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.core.paginator import Paginator
from django.urls import reverse

from qa.models import Question


def question(request):
    return HttpResponse('OK')


def main(request):
    qs = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(qs, limit)
    paginator.base_url = reverse('main') + '?page='
    return render(request, 'question_list.html', {
        'questions': paginator.object_list,
        'paginator': paginator,
        'page': paginator.page(page_number)
    })


def popular(request):
    qs = Question.objects.popular()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(qs, request.GET.get('limit', 10))
    paginator.base_url = reverse('popular') + '?page='
    return render(request, 'question_list.html', {
        'questions': paginator.object_list,
        'paginator': paginator,
        'page': page_number
    })


def question(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'question.html', {
        'question': question,
    })


def ask(request):
    return HttpResponse('OK')
