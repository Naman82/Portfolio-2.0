from django.shortcuts import render
from .models import FormInfo, Resume
# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        query=FormInfo(name=name,email=email,subject=subject,message=message)
        query.save()

    resume=Resume.objects.all().first()
    # print(resume)
    return render(request,'index.html',{'resume':resume})