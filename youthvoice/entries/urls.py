from django.urls import include, path

from .views import HomeView, EntryView,CreateEntryView
from django.contrib.messages.api import success



urlpatterns = [
path('', EntryView.as_view(), name= 'entry-detail'),
path('', HomeView.as_view(), name = 'youthvoice-home'),
path('<int:pk>/', EntryView.as_view(), name = 'entry-detail' ),
path('create_entry/', CreateEntryView.as_view(), name='create-entry')
#path('', include(('home.urls', 'home'), namespace='home')

] 