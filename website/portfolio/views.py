from django.shortcuts import render,get_object_or_404
from .models import About,Skill,Blog,ContactForm,SocialLink,Resume,Project,BackgroundImage
# Create your views here.

def home(request):
    about_detail = About.objects.first()
    project_detail = Project.objects.all()
    
    return render(request, 'portfolio/home.html', {
        'about_detail': about_detail,
        'project_detail': project_detail
    })




def eachProjectDetail(request,id):
    each_detail = get_object_or_404(Project,id=id)
    
    return render(request,'portfolio/project_detail.html',{'each_detail':each_detail})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
        ContactForm.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )


    return render(request,'portfolio/home.html')
