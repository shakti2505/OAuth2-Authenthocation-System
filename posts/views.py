from django.shortcuts import render
from  .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

@login_required
def post_create(request):
    if request.method =='POST':
        print(request.POST)
        form = PostCreateForm(request.POST or None, request.FILES or None )
        if form.is_valid():
            obj = form.save(commit=False)
            print('object',obj)
            obj.user = request.user
            obj.save()
            form = PostCreateForm
    else:   
        form = PostCreateForm(data=request.GET)
    return render(request, 'posts/create.html', {'form':form})


@login_required    
def index(request):
    current_user = request.user
    posts=Post.objects.filter(user=current_user)
    return render(request, 'posts/index.html', {'posts': posts})