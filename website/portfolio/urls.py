from django.urls import path
from .views import home,eachProjectDetail,contact


urlpatterns = [
    path('home',home,name='home'),
    path('project_detail/<int:id>/',eachProjectDetail,name='each_project_detail'),
    path('contact/', contact, name='contact'),
]
