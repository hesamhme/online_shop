from django.urls import path
from .views import HomePage, AboutUsPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about-us/', AboutUsPage.as_view(), name='about'),

]

