from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class ProductsView(View):
    template_name = 'products.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)


class StoreView(View):
    template_name = 'store.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)
