from django import template
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Problems
from .models import Testcase

# Create your views here.
def index(request):
    question_list = Problems.objects.all()
    template = loader.get_template('webapp/index.html')
    context = {
        'question_list': question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, problem_id):
    try:
        problem = Problems.objects.get(pk=problem_id)
    except Problems.DoesNotExist:
        raise Http404("Problem does not exist")
    return render(request, 'webapp/detail.html', {'problem': problem.Statement})
