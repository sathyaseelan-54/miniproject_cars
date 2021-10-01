from django.urls import path
from .views import Index
from .views import About,Contact,Servies



urlpatterns = [
    path('',Index,name = 'home'),
    path('about/',About.as_view(),name = 'about'),
    path('servies/',Servies.as_view(),name = 'servies'),
    path('contact/',Contact,name = 'contact'),

]