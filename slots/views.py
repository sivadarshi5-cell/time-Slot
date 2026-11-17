from django.shortcuts import render

def timetable_view(request):
    return render(request, 'slots/timetable.html')