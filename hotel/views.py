from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Room, Service, Client, Guest


# Create your views here.
class HomeView(ListView):
    queryset = Room.objects.all()
    template_name = 'home.html'
    context_object_name = 'rooms'


class ServicesView(ListView):
    queryset = Service.objects.all()
    template_name = 'hotel/services.html'
    context_object_name = 'services'


class Booking(ListView):
    queryset = Room.objects.all()
    template_name = 'hotel/booking.html'
    context_object_name = 'rooms'


class RoomDetail(DetailView):
    model = Room
    template_name = 'hotel/room_detail.html'

    def get_queryset(self):
        return Room.objects.filter(id=self.kwargs['pk'])


class ServiceDetail(DetailView):
    model = Service
    template_name = 'hotel/service_detail.html'

    def get_queryset(self):
        return Service.objects.filter(id=self.kwargs['pk'])


class Clients(ListView):
    queryset = Client.objects.all()
    template_name = 'hotel/clients.html'


class ClientsDetails(DetailView):
    model = Client
    template_name = 'hotel/clients_detail.html'

    def get_queryset(self):
        return Client.objects.filter(id=self.kwargs['pk'])


class ClientsCreate(CreateView):
    model = Client
    fields = ['first_name', 'last_name', 'dob', 'age', 'passport_serial', 'image', 'country', 'region', 'address']
    template_name = 'hotel/client_create.html'
    success_url = reverse_lazy('clients')


class Guests(ListView):
    template_name = 'hotel/guest.html'
    model = Guest
    context_object_name = 'guests'


class GuestDetail(DetailView):
    model = Guest
    template_name = 'hotel/guest_detail.html'

    def get_queryset(self):
        return Client.objects.filter(id=self.kwargs['pk'])
