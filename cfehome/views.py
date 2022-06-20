from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    article_obj = Article.objects.get(id=3)
    obj_list = Article.objects.all()
    context = {
        'obj_list': obj_list,
        'title': article_obj.title,
        'content': article_obj.content,
        'id': article_obj.id
    }
    
    return HttpResponse(render_to_string('home-view.html', context=context))
