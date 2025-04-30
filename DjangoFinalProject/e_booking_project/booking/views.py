from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Booking
from django.utils import timezone

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def form_view(request):
    if request.method == 'POST':
        Booking.objects.create(
            name=request.POST['name'],
            room=request.POST['room'],
            attendees=request.POST['attendees'],
            phone=request.POST['phone'],
            start_datetime=request.POST['start_date'] + ' ' + request.POST['start_time'],
            end_datetime=request.POST['end_date'] + ' ' + request.POST['end_time'],
            purpose=request.POST['purpose'],
            equipments=request.POST.get('equipments', ''),
            other=request.POST.get('other', '')
        )
        return redirect('booking_list')
    return render(request, 'form.html')

@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

@login_required
def booking_events(request):
    events = []
    for b in Booking.objects.all():
        events.append({
            'title': f"{b.room} ({b.name})",
            'start': b.start_datetime.isoformat(),
            'end': b.end_datetime.isoformat(),
            'color': '#0d6efd',
        })
    return JsonResponse(events, safe=False)

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('login')
