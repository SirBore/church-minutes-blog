from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from rest_framework import viewsets          
from .serializers import PostSerializer
from .models import Post
from django.views.generic import ListView, DetailView
#home view for posts. Posts are displayed in a list
class IndexView(ListView):
 template_name='Church/index.html'
 context_object_name = 'post_list'
 def get_queryset(self):
  return Post.objects.all()
#Detail view (view post detail)
class PostDetailView(DetailView):
 model=Post
 template_name = 'Church/post-detail.html'
#New post view (Create new post)
class PostView(viewsets.ModelViewSet):       
  serializer_class = PostSerializer          
  queryset = Post.objects.all()
def postview(request):
 if request.method == 'POST':
  form = PostForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = PostForm()
 return render(request,'Church/post.html',{'form': form})
#Edit a post
def edit(request, pk, template_name='Church/edit.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})
#Delete post
def delete(request, pk, template_name='Church/confirm_delete.html'):
    post= get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})
              