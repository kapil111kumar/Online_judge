from django import template
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Problems
from .models import Testcase
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    question_list = Problems.objects.all()
    template = loader.get_template('webapp/index.html')
    context = {
        'question_list': question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, problem_id):
    problem = Problems.objects.get(pk=problem_id)
    testcases = problem.testcase_set.all()
    return render(request, 'webapp/detail.html', {'problem': problem, 'testcases': testcases} )

def finalpage(request, problem_id, form_id):
    folder = 'media/'
    myfile = request.FILES['file']
    fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
    filename = fs.save(myfile.name, myfile)
    verdict = fs
    return render(request, 'webapp/finalpage.html', {'verdict':verdict} )