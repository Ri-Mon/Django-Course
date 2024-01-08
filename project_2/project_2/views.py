from django.shortcuts import render 
# F:\PHITRON\DJango\project_2\global_templates
def index(request):
    return render(request, 'index.html')