from django.shortcuts import render, get_object_or_404, redirect

from .forms import ThreadForm, PostForm
from .models import Thread, Post

# Create your views here.
def board_view(request):
    thread_list = Thread.objects.all()
    op_posts = []

    for t in thread_list:
        op_post = Post.objects.filter(thread_id=t.id).earliest('post_time')
        op_posts.append(op_post)

    t_form = ThreadForm(request.POST or None)
    p_form = PostForm(request.POST or None)

    if t_form.is_valid() and p_form.is_valid():
        new_thread = Thread(subject=request.POST['subject'])
        new_thread.save()

        if request.POST['name'] == '':
            name = 'Anonymous'
        else:
            name = request.POST['name']

        new_post = Post(name=name, content=request.POST['content'], thread=new_thread)
        new_post.save()

        return redirect('/{}/'.format(new_thread.id))

    context = {
        "thread_list": thread_list,
        "op_posts": op_posts,
        "t_form": t_form,
        "p_form": p_form
    }
    return render(request, "board.html", context)

def thread_view(request, id):
    queryset = Post.objects.filter(thread_id=id)
    thread = get_object_or_404(Thread, id=id)

    form = PostForm(request.POST or None)

    if form.is_valid():
        if request.POST['name'] == '':
            name = 'Anonymous'
        else:
            name = request.POST['name']

        new_post = Post(name=name, content=request.POST['content'], thread=thread)
        new_post.save()

        form = PostForm()

    context = {
        "thread": thread,
        "object_list": queryset,
        "form": form
    }
    return render(request, "thread.html", context)
