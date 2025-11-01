from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
# Create your views here.
def index(request):
  context = {
    "variable":"this is sent"
  }
  return render(request, "index.html", context)

def about(request):
  return render(request, "about.html")
  # return HttpResponse("this is about page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Basic validation
        if not name or not email or not phone or not desc:
            return render(request, "contact.html", {
                'error': 'All fields are required!',
                'form_data': {'name': name, 'email': email, 'phone': phone, 'desc': desc}
            })

        try:
            new_contact = Contact(
                name=name,
                email=email,
                phone=phone,
                desc=desc,
                date=datetime.today()
            )
            new_contact.save()
            return render(request, "contact.html", {
                'success': 'Your message has been submitted successfully! We will get back to you soon.'
            })
        except Exception as e:
            return render(request, "contact.html", {
                'error': 'An error occurred while submitting your message. Please try again.',
                'form_data': {'name': name, 'email': email, 'phone': phone, 'desc': desc}
            })

    return render(request, "contact.html")  