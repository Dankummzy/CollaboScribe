# articles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Collaboration
from .forms import ArticleForm  # Import the ArticleForm
from django.contrib.auth.decorators import login_required

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('view_article', article_id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user == article.author:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('view_article', article_id=article.id)
        else:
            form = ArticleForm(instance=article)
        return render(request, 'articles/article_form.html', {'form': form, 'article': article})
    else:
        # Handle unauthorized access
        return render(request, 'articles/unauthorized_access.html')


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user == article.author:
        if request.method == 'POST':
            article.delete()
            return redirect('home')  # Replace 'home' with your home view name
        return render(request, 'articles/article_confirm_delete.html', {'article': article})  # Create a template for the delete confirmation
    else:
        # Handle unauthorized access
        return render(request, 'articles/unauthorized_access.html')

def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    collaborations = Collaboration.objects.filter(article=article)
    return render(request, 'articles/article_detail.html', {'article': article, 'collaborations': collaborations})
