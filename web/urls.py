from django.urls import path

from . import views
from .views import my_form_view
from .views import success_view
from .views import show_records
from .views import delete_record
urlpatterns = [
    path("", views.index, name="index"),
    path('myform/', my_form_view, name='myform'),
    path('success/', success_view, name='success'), 
    path('show_records/', show_records, name='show_records'),
    path('delete_record/<int:record_id>/', delete_record, name='delete_record'),

 
]