from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import User, Journal, Entry

def index(request):
    return HttpResponse("This will be the login page")

def home(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    template = loader.get_template('journals/home.html')
    context = {
        'user': user
    }
    return render(request, 'journals/home.html', context)

def journal_view(request, user_id, journal_id):
    journal = Journal.objects.get(pk=journal_id)
    return HttpResponse("Logged in as %s. Viewing journal %s." % (user_id, journal.journal_name))

def entry_view(request, journal_id, user_id, entry_id):
    return HttpResponse("You can read the entry here. You are reading entry id %s from journal %s logged in as user %s." % (entry_id, journal_id, user_id))

def new_entry(request, user_id, journal_id):
    return HttpResponse("You input your entry here. You are inputting into journal id %s logged in as user id %s." % (journal_id, user_id))