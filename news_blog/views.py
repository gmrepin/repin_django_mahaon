from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'new_blog/news_list.html', {'articles':articles})
def get_article(request,article_id):
    return render(request,'new_blog/news_article.html',{'articles':articles[article_id -1]})
articles = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]
