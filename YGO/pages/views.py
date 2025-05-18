from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Card
from .forms import CardForm
from django.http import HttpRequest, HttpResponse
from typing import Any

class CardListView(ListView):
    """
    Displays a list of all Card objects.
    Inherits from Django's generic ListView.
    """
    model = Card
    template_name = 'home.html'
    context_object_name = 'card_list'

class CardDetailView(DetailView):
    """
    Displays the details of a single Card object.
    Inherits from Django's generic DetailView.
    """
    model = Card
    template_name = 'details.html'
    context_object_name = 'card'
    # def get_object(self, queryset: Any | None = None) -> Card:
    #     """Retrieve the card object based on the URL."""
    #     return super().get_object(queryset)

class CardCreateView(CreateView):
    """
    Handles the form for creating a new Card object.
    Inherits from Django's generic CreateView.
    """
    model = Card
    form_class = CardForm
    template_name = 'card_form.html'
    success_url = reverse_lazy('home')
    # def form_valid(self, form: CardForm) -> HttpResponse:
    #     """If the form is valid, save the object."""
    #     return super().form_valid(form)

class CardUpdateView(UpdateView):
    """
    Handles the form for updating an existing Card object.
    Inherits from Django's generic UpdateView.
    """
    model = Card
    form_class = CardForm
    template_name = 'card_form.html'
    context_object_name = 'card'
    success_url = reverse_lazy('home')

class CardDeleteView(DeleteView):
    """
    Handles the confirmation and deletion of a Card object.
    Inherits from Django's generic DeleteView.
    """
    model = Card
    template_name = 'card_confirm_delete.html'
    context_object_name = 'card'
    success_url = reverse_lazy('home')
