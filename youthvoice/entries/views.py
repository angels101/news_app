from django.shortcuts import render


from  django.views.generic import ListView, DetailView, CreateView
from  .models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin
#from entries.models import Entry
#from django.http import HttpResponse,Http404
# Create your views here.

class HomeView(LoginRequiredMixin, ListView):
     model = Entry
     template_name = 'entries/index.html'
     context_object_name ='youthvoice_entries'
     ordering = ['-entry_date']
     paginate_by = 3
 
class EntryView(LoginRequiredMixin, DetailView):
     model = Entry
     template_name = 'entries/entry_detail.html'

class CreateEntryView(LoginRequiredMixin, CreateView):
     model = Entry
     template_name = 'entries/create_entry.html'
     fields = ['entry_title', 'entry_text']
#class SubmitView(ComplainView):
    # model = Entry
     #template_name = 'all-news/animations_entry.html'
     #fields = [ 'entry_title', 'entry_text']

     def form_valid(self, form):
          form.instance.entry_author = self.request.user 
          return super().form_valid(form)
          