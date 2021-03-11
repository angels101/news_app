from django.urls import path

from .views import HomeView, EntryView,CreateEntryView
from django.contrib.messages.api import success



urlpatterns = [


path('', HomeView.as_view(), name = "youthvoice-home"),
path('entry/<int:pk>/', EntryView.as_view(), name = "entry-detail" ),
path('create_entry/', CreateEntryView.as_view(success), name="create-entry")


]