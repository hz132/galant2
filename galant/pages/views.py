from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'


def LessonPageView(request):
    return render(request, 'lesson.html')

def IndividualPageView(request):
    return render(request, 'individual.html')

def LecturesPageView(request):
    return render(request, 'lectures.html')

def RecordPageView(request):
    return render(request, 'record.html')

def IgorPageView(request):
    return render(request, 'igor.html')

def ZlataPageView(request):
    return render(request, 'zlata.html')

def IrinaPageView(request):
    return render(request, 'irina.html')