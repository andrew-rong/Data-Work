from django.urls import path

from . import views

from .views import HomeView, Detail_view

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name="Home"),
    path('post/<int:pk>', Detail_view.as_view(), name='Detail'),
    path('about/', views.about, name="About"),
    path('contact', views.contact, name="Contact"),

]
