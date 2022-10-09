from django.shortcuts import render
from .models import FormInfo, Resume
from django.http import FileResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        query=FormInfo(name=name,email=email,subject=subject,message=message)
        query.save()

    # print(resume)
    return render(request,'index.html')

def download(request):
    obj = Resume.objects.all()
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response