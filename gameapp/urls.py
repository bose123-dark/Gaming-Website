from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('library/', views.library, name='library'),
    path('login/', views.login_view, name='login'), # Points to the new functional view
    path('logout/', views.logout_view, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('article/<slug:slug>/', views.article, name='article'),
]