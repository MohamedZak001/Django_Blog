from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
from .forms import create_post
# Create your views here.

class list_posts(generic.ListView):
    model = Post
    template_name = 'app/home.html'
    context_object_name = 'posts'
    paginate_by = 5

class user_list_posts(generic.ListView):
    model = Post
    template_name = 'app/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')
class detail_post(generic.DetailView):
    model = Post
    template_name = 'app/deatil-post.html'



class post(LoginRequiredMixin,generic.CreateView):
    model = Post
    fields=[
        'title','content',
    ]
    template_name = 'app/create_post.html'
    context_object_name = 'form'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class updata(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Post
    fields=[
        'title','content',
    ]
    template_name = 'app/create_post.html'
    context_object_name = 'form'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class delete(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Post
    template_name = 'app/delete-post.html'
    context_object_name = 'form'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False     




def About(request):
    return render(request, 'app/about.html')
