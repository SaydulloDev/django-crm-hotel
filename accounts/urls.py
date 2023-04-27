from django.urls import path
from .views import login_user, logout_user, register_user, profile_view, profile_edit_view
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('profile/', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='edit')
]