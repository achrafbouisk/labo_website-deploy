from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import loader
from .models import Accueil, AccueilInfo, equipe, certificat, VisitorCount, informations, actualite, Contact
from django.core.paginator import Paginator


def maintenance(request):
    template = loader.get_template('maintenance.html')
    context = {}
    return HttpResponse(template.render(context, request))


def login_client(request):
    template = loader.get_template('login_client.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/merci') ### just for test
        else:
            messages.error(request, 'Invalid email or password.')
    context = {}
    return HttpResponse(template.render(context, request))



def home(request):
    data = Accueil.objects.all().values()
    latest_blogs = actualite.objects.order_by('-created_at')[:3]
    info = informations.objects.all().values()
    accueilInfo = AccueilInfo.objects.all().values()
    visitor_count = VisitorCount.objects.get(pk=1)
    template = loader.get_template('index.html')
    context = {
        'data': data,
        'visitor_count': visitor_count.count,
        'info': info,
        'latest_blogs': latest_blogs,
        'accueilInfo': accueilInfo

    }
    return HttpResponse(template.render(context, request))


def about(request):
    equipes = equipe.objects.all().values()
    certificats = certificat.objects.all().values()
    info = informations.objects.all().values()
    template = loader.get_template('about.html')
    context = {
        'equipes': equipes,
        'certificats': certificats,
        'info': info,
    }
    return HttpResponse(template.render(context, request))


def blog(request):
    latest_blogs = actualite.objects.order_by('-created_at')[:6]
    blog_list = actualite.objects.order_by('-created_at')
    paginator = Paginator(blog_list, 6)  # paginate into groups of 6
    page_number = request.GET.get('page')  # get the current page number
    page_obj = paginator.get_page(page_number)
    info = informations.objects.all().values()
    template = loader.get_template('blog.html')
    context = {
        'page_obj': page_obj,
        'blogs': blog_list,
        'info': info,
        'latest_blogs': latest_blogs

    }
    return HttpResponse(template.render(context, request))


def blogDetails(request, id):
    latest_blogs = actualite.objects.order_by('-created_at')[:6]
    blog = actualite.objects.get(id=id)
    info = informations.objects.all().values()
    template = loader.get_template('blogDetails.html')
    context = {
        'blog': blog,
        'info': info,
        'latest_blogs': latest_blogs

    }
    return HttpResponse(template.render(context, request))


# def contact(request):
#     template = loader.get_template('contact.html')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         contact = Contact(nom=name, email=email, subject=subject, message=message)
#         contact.save()
#         return HttpResponseRedirect('/merci/')
#     return HttpResponse(template.render(request))


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Create a new ContactMessage object and save it to the database
        contact = Contact(nom=name, email=email,
                          subject=subject, message=message)
        contact.save()

        return HttpResponseRedirect('/merci/')
        # Redirect the user to a thank-you page
        # return HttpResponseRedirect(reverse('contact_thankyou'))

    # If the request method is not POST, render the contact form
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))


def merci(request):
    template = loader.get_template('merci.html')
    return HttpResponse(template.render({}, request))


##############################################

