from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.index_view, name='index_view'),
    path('myapp/', views.about_view, name='about_view'),
    path('myapp/', views.add_view, name='add_view'),
    path('myapp/', views.edit_view, name='edit_view'),
    path('myapp/', views.delete_view, name='delete_view'),

    # Other URL patterns specific to your app
]