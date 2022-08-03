from multiprocessing import context
from django.shortcuts import HttpResponse
from django.shortcuts import render

from bookmarks.models import Bookmark


def index(request):
    return HttpResponse('<h1>Hello World</h1>')


def bookmark_list(request):
    bookmark_list = Bookmark.objects.all()
    context = {'bookmark_list':bookmark_list}
    return render(request, 'templates/bookmark_list.html', context)



def bookmark_detail(request, pk):
    bookmark = Bookmark.objects.get(id=pk)
    context = {'bookmark':bookmark}
    return render(request, 'templates/bookmark_detail.html',context)