from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def About(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
# def gallery(request):
#     return render(request,'gallery.html')
# def gallery2(request):
#     return render(request,'gallery-single.html')
def services(request):
    return render(request,'services.html')
# def sample(request):
#     return render(request,'sample-inner-page.html')