from django.urls import path
from .views import *

urlpatterns = [
# --------------------READ(view)------------------------
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('testimonial/', testimonial, name='testimonial'),
    # path('search/', search, name='search'),

# --------------------CREATE------------------------
    path('contact/', contact, name='contact'),
]