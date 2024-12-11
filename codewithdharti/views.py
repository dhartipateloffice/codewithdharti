import random
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Langdb, Topicdb, Subtopicdb,Nanotopicdb,Codeideadb

def home(request):
    languages = Langdb.objects.all()
    return render(request, 'home.html', {'languages': languages})

def lang_detail(request, slug):
    lang = get_object_or_404(Langdb, slug=slug)
    topics = Topicdb.objects.filter(langname=lang)
    print(topics)
    return render(request, 'lang_detail.html', {'lang': lang, 'topics': topics})

def subtopic_detail(request, slug):
    # subtopic = get_object_or_404(Subtopicdb, slug=slug)
    # topics = Topicdb.objects.filter(langname=subtopic.topic.langname)
    subtopic = Subtopicdb.objects.get(slug=slug)
    # Group code sections by nanotopic
    code_sections_by_nanotopic = {}
    for nanotopic in subtopic.nanotopics.all():
        code_sections_by_nanotopic[nanotopic] = nanotopic.code_blocks.all()

        print(code_sections_by_nanotopic)

    return render(request, 'subtopic_detail.html', {
        'subtopic': subtopic,
        'topics': subtopic.topic.langname.topics.all(),
        'code_sections_by_nanotopic': code_sections_by_nanotopic
    })
def tutorial(request):
    return render(request, 'tutorial.html')  

def notes(request):
    return render(request, 'notes.html')  

def blog(request):
    return render(request, 'blog.html')  

def contact(request):
    return render(request, 'contact.html')  

def python_tutorial(request,slug):
    lang = get_object_or_404(Langdb, slug=slug)
    topics = Topicdb.objects.filter(langname=lang)
    # print(topics)
    return render(request, 'tutorial.html', {'lang': lang, 'topics': topics}) 

def codegallary(request):
    codeideas = list(Codeideadb.objects.all())
    # print(codeideas)
    random.shuffle(codeideas)  
    return render(request, 'codegallary.html', {'codeideas': codeideas})



