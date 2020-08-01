from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
import datetime
# Create your views here.
def index(request):
    blog = Blog.objects
    return render(request, 'index.html', {'blogs':blog})

def create(request):
    return render(request, 'create.html')
    
def new(request):
    blog = Blog() #빈 blog오브젝트가 만들어죔
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    if(request.GET.get('category') == 'Django'):
        blog.category = 'Django'
    elif(request.GET.get('category') == 'Python'):
        blog.category = 'Python'
    elif(request.GET.get('category') == 'html/css'):
        blog.category = 'html/css'
    elif(request.GET.get('category') == 'Js/Jquery'):
        blog.category = 'Js/Jquery'
    blog.save() #값저장
    return redirect('/') #redirect는 처리는 안하고 이동만시킴, 변수값같은거 못보냄

def detail(request, blog_id): #urls에서 지정한 blog_id받아오기
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'blog':blog})

def updat(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.date = datetime.datetime.now()
    if(request.GET.get('category') == 'Django'):
        blog.category = 'Django'
    elif(request.GET.get('category') == 'Python'):
        blog.category = 'Python'
    elif(request.GET.get('category') == 'html/css'):
        blog.category = 'html/css'
    elif(request.GET.get('category') == 'Js/Jquery'):
        blog.category = 'Js/Jquery'
    blog.save()
    return redirect('/detail/'+str(blog_id))

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')