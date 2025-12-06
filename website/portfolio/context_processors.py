from .models import BackgroundImage,About

def background_image(request):
    bg_image = BackgroundImage.objects.first()
    return {'bg_image': bg_image}

def global_about(request):
    return {
        'about_detail':About.objects.first()
    }
