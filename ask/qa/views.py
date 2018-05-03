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
        'paginator': paginator,
        'page': paginator.page(page_number)
    })


def popular(request):
    qs = Question.objects.popular()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(qs, request.GET.get('limit', 10))
    paginator.base_url = reverse('popular') + '?page='
    return render(request, 'question_list.html', {
        'paginator': paginator,
        'page': paginator.page(page_number),
    })


def question(request, id):
    q = get_object_or_404(Question, id=id)
    return render(request, 'question.html', {
        'question': q,
    })


def create(request):
    for i in range(35, 40):
        title = 'Question' + str(i)
        q = Question.objects.create(title=title, text='Question text')
        q.save()
    return HttpResponse('OK')


def ask(request):
    return HttpResponse('OK')
