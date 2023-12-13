from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'blog/home.html'

class HomeListView(ListView):
     model = Post
     template_name = 'blog/base.html'
     context_object_name = 'posts'
     ordering = ['-created_date']
     paginate_by = 10

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def about_view(request):
    return render(request, 'blog/about.html')

class WorksView(TemplateView):
    template_name = 'blog/works.html'

from .models import Award

def newsroom_view(request):
    awards = Award.objects.all()
    return render(request, 'blog/newsroom.html', {'awards': awards})


from django.shortcuts import render, redirect
from .models import Post

# 새 게시글 추가 기능
def add_project_post(request, project_type):
    if request.method == 'POST':
        new_post = Post(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            project_type=project_type
        )
        new_post.save()
        return redirect('works')
    return redirect('works')  # POST가 아닐 경우 works 페이지로 리다이렉트

# 기존 게시글 보여주기 및 POST 요청 처리 제거
def works_view(request):
    college_posts = Post.objects.filter(project_type='college')
    research_posts = Post.objects.filter(project_type='research')
    return render(request, 'works.html', {
        'college_posts': college_posts,
        'research_posts': research_posts
    })

# 게시글 삭제 기능
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('works')
