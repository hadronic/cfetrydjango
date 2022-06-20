from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def article_detail_view(request, id=None):
    obj = None
    if id is not None:
        obj = Article.objects.get(id=id)
    context = {'obj': obj}
    
    return render(request, "articles/detail.html", context=context)


def article_search_view(request):
    obj = None
    try:
        q = int(request.GET.get('q'))
    except ValueError:
        q = None
    
    if q is not None:
        obj = Article.objects.get(id=q)
    context = {'obj': obj}
    return render(request, 'articles/search.html', context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save()
        context['form'] = ArticleForm()
        # context['obj'] = obj
        # context['created'] = True

    return render(request, "articles/create.html", context=context)
