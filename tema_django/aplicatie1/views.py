from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView
from aplicatie1.models import Companies
from django.urls import reverse


class CreateLocationView(CreateView):
    model = Companies
    fields = ['name', 'website', 'company_type']
    # fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


class UpdateLocationView(UpdateView):
    model = Companies
    fields = ['name', 'website', 'company_type']
    # fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:lista_locatii')


class LocationView(ListView):
    model = Companies
    template_name = 'aplicatie1/location_index.html'


def delete_location(request, pk):
    Companies.objects.filter(id=pk, user_id=request.user.id).delete()
    return redirect('aplicatie1:lista_locatii')



