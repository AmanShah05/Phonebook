from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):  
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(first_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'index.html', {'contacts':contacts, 'search_input': search_input})

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            first_name = request.POST['firstname'],
            last_name = request.POST['lastname'],
            location = request.POST['location'],
            international_code = request.POST['internationalcode'],
            phone_number = request.POST['phone-number'],
        )
        new_contact.save()
        return redirect('/')

    return render(request, 'new.html')

def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact':contact})

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.first_name = request.POST['firstname']
        contact.last_name = request.POST['lastname']
        contact.location = request.POST['location']
        contact.international_code = request.POST['internationalcode']
        contact.phone_number = request.POST['phone-number']
        contact.save()

        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})

