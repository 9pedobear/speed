from django.urls import path
from .views import *

urlpatterns = [
# --------------------REGISTER------------------------
    path('register/', registerUser, name='register'),

# --------------------LOGIN------------------------
    path('login/', loginUser, name='login'),

# --------------------LOGOUT------------------------
    path('logout/', logoutUser, name='logout'),

# --------------------READ(view)------------------------
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('gallery/', gallery, name='gallery'),
    path('testimonial/', testimonial, name='testimonial'),
    path('search/', search, name='search'),

# --------------------CREATE------------------------
    path('contact/', ContactView.as_view(), name='contact'),
    path('send_message_smtp/', send_message_smtp, name='send_message_smtp'),
]