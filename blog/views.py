from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm



# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'home.html', context)


def druga_strana(request):
    context = {

    }
    return render(request, 'druga-strana.html', context)


def lista(request):

    queryset = Article.objects.all().order_by('-datetime')
    # article = Article.objects.get(id=id)

    context = {
        'obj': queryset,
        # 'art': article
    }
    return render(request, 'lista.html', context)


def detail(request, id):

    obj = Article.objects.get(id=id)

    context = {
        'obj': obj
    }
    return render(request, 'detail.html', context)


@login_required
def article_create(request):

    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article_obj = form.save()

        return redirect('../')


    context = {
        'form': form
    }
    return render(request, 'create.html', context)



def article_delete(request, id):
    obj = Article.objects.get(id=id)



    if request.method == 'POST':
        obj.delete()
        return redirect('../../../')

    context = {
        'obj': obj
    }


    return render(request, 'delete.html', context)





















