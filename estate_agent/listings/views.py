from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Avg, F
from .models import Listings


class AgentDashboardView(LoginRequiredMixin, ListView):
    model = Listings
    template_name = 'users/profile.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Listings.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listings = self.get_queryset()

        # Статистика
        context['total_listings'] = listings.count()
        context['active_listings'] = listings.filter(status='active').count()
        context['sold_listings'] = listings.filter(status='sold').count()

        # Топ-3 города по количеству объявлений
        context['top_cities'] = listings.values('city').annotate(
            total=Count('id')
        ).order_by('-total')[:3]

        # Средняя цена по типам недвижимости
        context['avg_prices'] = listings.values('property_type').annotate(
            avg_price=Avg('price')
        )

        return context


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listings
    fields = [
        'title', 'description', 'price', 'area', 'rooms',
        'transaction_type', 'property_type', 'status',
        'address', 'city'
    ]
    template_name = 'listings/listing_form.html'
    success_url = reverse_lazy('listings:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListingUpdateView(LoginRequiredMixin, UpdateView):
    model = Listings
    fields = [
        'title', 'description', 'price', 'area', 'rooms',
        'transaction_type', 'property_type', 'status',
        'address', 'city'
    ]
    template_name = 'listings/listing_form.html'
    success_url = reverse_lazy('listings:dashboard')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ListingDeleteView(LoginRequiredMixin, DeleteView):
    model = Listings
    template_name = 'listings/listing_confirm_delete.html'
    success_url = reverse_lazy('listings:dashboard')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)