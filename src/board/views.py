import socket
import re
from .modules import hex
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ThreadForm, PostForm
from .models import Thread, Post

def get_ip_address(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        socket.inet_aton(ip)
        return ip
    except socket.error:
        return False

def greentext(match):
    return "<span class='quote'>{}</span>".format(match.group())

def spoiler(match):
    string = match.group()
    string = string.replace("[spoiler]", '')
    string = string.replace("[/spoiler]", '')
    return "<span class='spoiler'>{}</span>".format(string)

def parse_text(content):
    # Quotes
    p = re.compile("(?<!>)(>[a-zA-Z0-9]).+")
    parsed_content = p.sub(greentext, content)

    # Post links
    p = re.compile("(>>)[0-9]+")
    iter = p.finditer(parsed_content)
    for i in iter:
        try:
            linked_post = Post.objects.get(id=int(i.group()[2:]))
            replace = "<a class='post-link' href='/{}/#{}'>{}</a>".format(linked_post.thread_id, i.group()[2:], i.group())
            print(replace)
        except:
            print("Could not find post #{}".format(i.group()[2:]))
            continue

        parsed_content = parsed_content.replace(i.group(), replace)

    parsed_content = parsed_content.replace("[spoiler]", "<span class='spoiler'>")
    parsed_content = parsed_content.replace("[/spoiler]", "</span>")

    return parsed_content

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

        parsed_content = parse_text(request.POST['content'])

        ipaddr = get_ip_address(request)
        hex_code = hex.get_hex_id(ipaddr)

        new_post = Post(name=name, content=parsed_content, thread=new_thread, ip=ipaddr, hex_id=hex_code)
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
    parsed_content = ''

    if form.is_valid():
        if request.POST['name'] == '':
            name = 'Anonymous'
        else:
            name = request.POST['name']

        parsed_content = parse_text(request.POST['content'])

        ipaddr = get_ip_address(request)
        hex_code = hex.get_hex_id(ipaddr)

        new_post = Post(name=name, content=parsed_content, thread=thread, ip=ipaddr, hex_id=hex_code)
        new_post.save()

        form = PostForm()

    context = {
        "thread": thread,
        "object_list": queryset,
        "form": form
    }
    return render(request, "thread.html", context)
