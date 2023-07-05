from django.http import HttpResponse
from django.shortcuts import render
from contact.models import Contact
from subscribe.models import Subscribe
from django.contrib import messages
from django.shortcuts import redirect


def homePage(request):
    return render(request,"index.html")

def privatefunds(request):
    return render(request,"private-funds.html")

def businessLoans(request):
    return render(request,"business-loans.html")

def commercialLoans(request):
    return render(request,"commercial.html")

def constructionLoans(request):
    return render(request,"construction.html")

def contact(request):
    return render(request,"contact.html")

def privacypolicy(request):
    return render(request,"privacy-policy.html")

def termsofuse(request):
    return render(request,"terms-of-use.html")

def disclaimer(request):
    return render(request,"disclaimer.html")

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        location=request.POST.get('location')
        en= Contact(name=name,phone=phone,email=email,location=location)
        en.save()
        messages.success(request, 'Form submitted successfully.')
        # return redirect('homePage')
    return render(request,"index.html")

def subscribe(request):
    if request.method=="POST":
        email=request.POST.get('email')
        sb= Subscribe(email=email)
        sb.save()
        messages.success(request, 'Form submitted successfully.')
        # return redirect('homePage')
    return render(request,"index.html")
     









# news letter app to be done 
# make more content info for this 
# needs more work as too the footer, the links needs to be donw 