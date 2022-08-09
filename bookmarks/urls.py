from django.urls import path
from bookmarks import views

app_name = 'bookmarks'

urlpatterns = [
    path('', views.bookmark_list, name='list'),
    path('<int:pk>/',views.bookmark_detail ,name = 'detail'),
    path('create/',views.bookmark_create, name='cr'),
    path('update/<int:pk>/',views.bookmark_update, name='update'),
    path('delete/<int:pk>/', views.bookmark_delete, name='delete')
]