from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

import django_filters
from django import forms

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import CharFilter, NumberFilter, ModelChoiceFilter

# Create your views here.

from .forms import VariationInventoryFormSet
from .mixins import StaffRequiredMixin
from .models import Product, Variation, Category, Collection, Brand, Material1, Material2, Material3, Material4, Material5, Material6, Material7, Material8, Material9, Material10, Hardness, Height, Weight, Sofa, Child, Filler, Spring
from .serializers import ProductSerializer

class BrandListView(ListView):
	model = Brand
	queryset = Brand.objects.all()
	template_name = "products/brand_list.html"


class BrandDetailView(DetailView):
	model = Brand

	def get_context_data(self, *args, **kwargs):
		context = super(BrandDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		category_set = obj.category_set.all()
		#default_products = obj.default_category.all()
		#collections = ( collection_set | default_products ).distinct()
		categories = category_set
		context["categories"] = categories
		return context

class CategoryListView(ListView):
	model = Category
	queryset = Category.objects.all()
	template_name = "products/category_list.html"


class CategoryDetailView(DetailView):
	model = Category

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		collection_set = obj.collection_set.all()
		#default_products = obj.default_category.all()
		#collections = ( collection_set | default_products ).distinct()
		collections = collection_set
		context["collections"] = collections
		return context

class CollectionListView(ListView):
	model = Collection
	queryset = Collection.objects.all()
	template_name = "products/collection_list.html"


class CollectionDetailView(DetailView):
	model = Collection

	def get_context_data(self, *args, **kwargs):
		context = super(CollectionDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		product_set = obj.product_set.all()
		#default_products = obj.default_category.all()
		#products = ( product_set | default_products ).distinct()
		products = product_set
		context["products"] = products
		return context

class VariationListView(StaffRequiredMixin, ListView):
	model = Variation
	queryset = Variation.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(VariationListView, self).get_context_data(*args, **kwargs)
		context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset())
		return context

	def get_queryset(self, *args, **kwargs):
		product_pk = self.kwargs.get("pk")
		if product_pk:
			product = get_object_or_404(Product, pk=product_pk)
			queryset = Variation.objects.filter(product=product)
		return queryset

	def post(self, request, *args, **kwargs):
		formset = VariationInventoryFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				new_item = form.save(commit=False)
				#if new_item.title:
				product_pk = self.kwargs.get("pk")
				product = get_object_or_404(Product, pk=product_pk)
				new_item.product = product
				new_item.save()
				
			messages.success(request, "Your inventory and pricing has been updated.")
			return redirect("products")
		raise Http404


class ProductFilter(django_filters.FilterSet):    
    min_price = django_filters.NumberFilter(name='variation__price', label='От', lookup_expr='gte', distinct=True)
    max_price = django_filters.NumberFilter(name='variation__price', label='До', lookup_expr='lte', distinct=True)    
    category = django_filters.ModelMultipleChoiceFilter(
        name='category', label='Категория', widget=forms.CheckboxSelectMultiple,
        queryset=Category.objects.all(),
    )
    brand = django_filters.ModelMultipleChoiceFilter(
        name='brand', label='Бренд', widget=forms.CheckboxSelectMultiple,
        queryset=Brand.objects.all(),
    )
    hardness = django_filters.ModelMultipleChoiceFilter(
        name='hardness', label='Жёсткость', widget=forms.CheckboxSelectMultiple(attrs={'class': 'special'}),
        queryset=Hardness.objects.all(),
    )
    height = django_filters.NumberFilter(
        name='height', label='Высота матраса, см', lookup_expr='gte', distinct=True
    )
    weight = django_filters.NumberFilter(
        name='weight', label='Вес на спальное место, кг', lookup_expr='gte', distinct=True
    )
    spring = django_filters.ModelMultipleChoiceFilter(
        name='spring', label='Пружинный блок', widget=forms.CheckboxSelectMultiple,
        queryset=Spring.objects.all(),
    )
    sofa = django_filters.ModelMultipleChoiceFilter(
        name='sofa', label='Для дивана', widget=forms.CheckboxSelectMultiple,
        queryset=Sofa.objects.all(),
    )
    child = django_filters.ModelMultipleChoiceFilter(
        name='child', label='Детский', widget=forms.CheckboxSelectMultiple,
        queryset=Child.objects.all(),
    )
    filler = django_filters.ModelMultipleChoiceFilter(
        name='filler', label='Наполнитель', widget=forms.CheckboxSelectMultiple,
        queryset=Filler.objects.all(),
    )


    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'category_id', 'brand', 'hardness', 'height', 'weight', 'filler', 'child', 'sofa', 'spring']


#def product_list(request):
	#qs = Product.objects.all()
	#ordering = request.GET.get("ordering")
	#if ordering:
		#qs = Product.objects.all().order_by(ordering)
	#f = ProductFilter(request.GET, queryset=qs)
	#return render(request, "products/product_list.html", {"object_list": f })

def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'products/product_list.html', {'filter': f})


class FilterMixin(object):
	filter_class = None
	search_ordering_param = "ordering"

	def get_queryset(self, *args, **kwargs):
		try:
			qs = super(FilterMixin, self).get_queryset(*args, **kwargs)
			return qs
		except:
			raise ImproperlyConfigured("You must have a queryset in order to use the FilterMixin")

	def get_context_data(self, *args, **kwargs):
		context = super(FilterMixin, self).get_context_data(*args, **kwargs)
		qs = self.get_queryset()
		#ordering = self.request.GET.get(self.search_ordering_param)
		#if ordering:
			#qs = qs.order_by(ordering)
		filter_class = self.filter_class
		if filter_class:
			f = filter_class(self.request.GET, queryset=qs)
			context["object_list"] = f
		return context


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ProductFilter


import random
class ProductDetailView(DetailView):
	model = Product
	#template_name = "product.html"
	#template_name = "<appname>/<modelname>_detail.html"
	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		instance = self.get_object()
		#order_by("-title")
		context["related"] = sorted(Product.objects.get_related(instance)[:6], key= lambda x: random.random())
		return context


def product_detail_view_func(request, id):
	#product_instance = Product.objects.get(id=id)
	product_instance = get_object_or_404(Product, id=id)
	try:
		product_instance = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise Http404
	except:
		raise Http404

	template = "products/product_detail.html"
	context = {	
		"object": product_instance
	}
	return render(request, template, context)