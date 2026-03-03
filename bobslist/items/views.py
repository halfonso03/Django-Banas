from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Item
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "item_list.html"
    login_url = "login"
        
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item_detail.html"
    login_url = "login"
    
    
class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ('title', 'description', 'price')
    template_name = "item_edit.html"
    login_url = "login"
    
    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user
    
    
class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = "item_delete.html"
    success_url = reverse_lazy('item_list')
    login_url = "login"
    
    def test_func(self, form):
        obj = self.get_object()
        return obj.seller == self.request.user
    
    
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "item_new.html"
    fields = ('title', 'description', 'seller', 'price', 'photos')
    success_url = reverse_lazy('item_create')
    login_url = "login"
    
    def form_valid(self, form):
        form.instance.seller = self.request.seller
        return super().form_valid(form)
    

    
