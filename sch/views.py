from django.shortcuts import render
from django.http import HttpResponse
from .models import Slide, Update, HAbout, Hadmission, Whyu, Teacher, Logo




#def about(request):
 #   return render(request, 'about.html')  # New view function for the "About" page

def home(request):
    slides = Slide.objects.filter(is_active=True) 
    update =  Update.objects.first()
    about = HAbout.objects.first()
    hd = Hadmission.objects.first()
    whyu = Whyu.objects.all()
    teacher = Teacher.objects.all()
    logo = Logo.objects.first() 
    
    context = {
        'slides': slides,
        'update': update,
        'about' : about,
        'hd' : hd,
        'whyu' : whyu,
        'teacher' : teacher,
        'logo' : logo,
        

    }

    return render(request, 'home.html', context)
