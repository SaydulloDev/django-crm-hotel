from django.urls import path

from .views import HomeView, Booking, ServicesView, RoomDetail, ServiceDetail, Clients, ClientsDetails, Guests, \
    ClientsCreate, GuestDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('booking/', Booking.as_view(), name='booking'),
    path('booking/<int:pk>', RoomDetail.as_view(), name='room_detail'),
    path('services/<int:pk>', ServiceDetail.as_view(), name='service_detail'),
    # Admin
    path('clients/', Clients.as_view(), name='clients'),
    path('clients/<int:pk>', ClientsDetails.as_view(), name='clients_detail'),
    path('add_clients/', ClientsCreate.as_view(), name='add_client'),
    path('guest/', Guests.as_view(), name='guest'),
    path('guest/<int:pk>/', GuestDetail.as_view(), name='guest_detail'),
]
