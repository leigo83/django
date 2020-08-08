from django.urls import path

from . import views

urlpatterns = [
    #path('', views.HelloDjango.as_view())
    path('', views.PostListView.as_view(), name = "home"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = "post"),
    path('post/new/', views.PostCreateView.as_view(), name = "make_post"),
    path('post/edit/<int:pk>', views.PostUpdataView.as_view(), name = "edit"),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name = "delete")
]
