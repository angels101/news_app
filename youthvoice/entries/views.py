from django.shortcuts import render

#from django.http import HttpResponse,Http404
from  django.views.generic import ListView
from  .models import Entry




# Create your views here.

class HomeView(ListView):
     model = Entry
     template_name = 'entries/index.html'
     context_object_name ="youthvoice_entries"
 
     class EntryView(DetailView):
          model = Entry
          template_name = 'entries/entry_detail.html'