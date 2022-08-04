from multiprocessing import context
from django.shortcuts import HttpResponse, redirect
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


def bookmark_create(request):
    # if request.method == 'POST':
    #     context = {'text':'POST METHOD!!!'}
    #     return render(request, 'templates/bookmark_create.html', context)
    # context = {'text':'GET METHOD!!!'}
    # return render(request, 'templates/bookmark_create.html', context)
    bookmark = Bookmark()
    if request.method == 'POST':
        bookmark.title = request.POST['title']
        bookmark.url = request.POST['url']
        bookmark.memo = request.POST['memo']

        bookmark.save()

        return redirect(f'/bookmark/{bookmark.id}')

    return render(request, 'templates/bookmark_create.html')




def bookmark_update(request, pk):
    bookmark = Bookmark.objects.get(id=pk)
    context = {'bookmark':bookmark}
    if request.method == 'POST':
        bookmark.title = request.POST['title']
        bookmark.url = request.POST['url']
        bookmark.memo = request.POST['memo']

        bookmark.save()

        return redirect(f'/bookmark/{bookmark.id}')

    return render(request, 'templates/bookmark_update.html', context)
    
def bookmark_delete(request, pk):
    bookmark = Bookmark.objects.get(id=pk)

    if request.method == 'POST':
        bookmark.delete()
        return redirect('/bookmark/')

    return render(request, 'templates/bookmark_delete.html')