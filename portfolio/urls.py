from django.urls import path

from portfolio import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contactme/', views.ContactMeView.as_view(), name='contact'),
    path('contactme/thanks', views.EmailSentView.as_view(), name='thanks'),
]
