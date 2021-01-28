from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from .models import Post
from django.contrib.admin.views.decorators import staff_member_required

def posts(request):  # -------------------------------------
    response = []
    d = {'response': response}
    posts = Post.objects.filter().order_by('-datetime')

    for post in posts:
        response.append(
            {
                'datetime': post.datetime,
                'content': post.content,
                'author': f'{post.user}'
            }
        )

    return JsonResponse(d)

#----------------


# -------------------------------------- home page progetto
def home(response):
    return render(response, 'api/home.html', {})


# -------------------------------------- 1 registration e login

# Gestito in cartella 'socialDex/register'


# --------------------------------- punto 2
from .forms import PostForm

def post_list(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            posts = Post.objects.all()
            w_post = PostForm(request.POST)
            if w_post.is_valid():
                post = w_post.save(commit=False)
              #  post.author = request.user
              #  post.published_date = timezone.now()
                post.save()
            return render(request, 'api/post_list.html', {'w_post': w_post, 'posts': posts})
        else:
            w_post = PostForm()
            posts = Post.objects.all()
            return render(request, 'api/post_list.html', {'w_post': w_post, 'posts': posts})
    else:
        return render(request, 'api/login_link_page.html', {})


# --------------------------- solo admin, numero di post pubblicati da ciascun utente, punto 3

from django.contrib.auth.models import User

@staff_member_required
def n_post_user(request):
    lista = []
    d = {'lista':lista}
    all_users = User.objects.all()
    for u in all_users:
        post_user = Post.objects.filter(user=u)
        n_post = len(post_user)
        lista.append(
            {f'{u}':n_post}
        )
    return JsonResponse(d)


# ------- Una pagina, accessibile dall’url /utente/[id],
# dove [id] è un parametro che rappresenta l’id dell’utente (HINT), punto 4

def id_page(response, id):
    user_id = User.objects.get(id=id)
    return render(response, 'api/id_page.html', {'user_id': user_id})

# id di prova: http://127.0.0.1:8000/utente/1/


# --------------------------- tutti post ultima ora, punto 5
def posts_last_h(request):
    l_last_h = []
    d = {'l_last_h':l_last_h}
    posts = Post.objects.all()
    now = timezone.now()
    last_hour = now - timedelta(hours=1)
    for post in posts:
        if post.datetime > last_hour:
            l_last_h.append(
                {
                    'datetime': post.datetime,
                    'user': f'{post.user}',
                    'content': post.content
                }
            )
    return JsonResponse(d)

# -------------------------- FINE