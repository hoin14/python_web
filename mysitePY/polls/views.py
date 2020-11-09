from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'elections/index.html', context)

def areas(request, area) : #어떤 지역인지를 매개변수 area로 받습니다.
   return HttpResponse(area)