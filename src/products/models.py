from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from random import choice
from string import ascii_letters

# Create your models here.

class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)


class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self, *args, **kwargs):
		return self.get_queryset().active()

	def get_related(self, instance):
		#products_one = self.get_queryset().filter(categories__in=instance.categories.all())
		products_three = self.get_queryset().filter(collection__in=instance.collection.all())
		products_two = self.get_queryset().filter(default=instance.default)
		qs = ( products_two | products_three ).exclude(id=instance.id).distinct()
		return qs



class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=0, max_digits=20)
	active = models.BooleanField(default=True)
	category = models.ForeignKey('Category', null=True, blank=True)
	collection = models.ManyToManyField('Collection', blank=True)
	hardness = models.ForeignKey('Hardness', null=True, blank=True)
	height = models.DecimalField(decimal_places=1, max_digits=20)
	weight = models.DecimalField(decimal_places=0, max_digits=20)
	spring = models.ForeignKey('Spring', null=True, blank=True)
	sofa = models.ForeignKey('Sofa', null=True, blank=True)
	child = models.ForeignKey('Child', null=True, blank=True)
	filler = models.ForeignKey('Filler', null=True, blank=True)
	brand = models.ForeignKey('Brand', null=True, blank=True)
	material = models.ForeignKey('Material1', null=True, blank=True)
	material2 = models.ForeignKey('Material2', null=True, blank=True)
	material3 = models.ForeignKey('Material3', null=True, blank=True)
	material4 = models.ForeignKey('Material4', null=True, blank=True)
	material5 = models.ForeignKey('Material5', null=True, blank=True)
	material6 = models.ForeignKey('Material6', null=True, blank=True)
	material7 = models.ForeignKey('Material7', null=True, blank=True)
	material8 = models.ForeignKey('Material8', null=True, blank=True)
	material9 = models.ForeignKey('Material9', null=True, blank=True)
	material10 = models.ForeignKey('Material10', null=True, blank=True)
	default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)

	objects = ProductManager()

	class Meta:
		ordering = ["-title"]

	def __str__(self): #def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse("product_detail", kwargs={"pk": self.pk})

	def get_image_url(self):
		img = self.productimage_set.first()
		if img:
			return img.image.url
		return img #None


class Variation(models.Model):
	product = models.ForeignKey(Product)
	title = models.CharField(max_length=120)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
	active = models.BooleanField(default=True)
	inventory = models.IntegerField(null=True, blank=True) #refer none == unlimited amount

	def __str__(self):
		return self.title

	def get_price(self):
		if self.sale_price is not None:
			return self.sale_price
		else:
			return self.price

	def get_html_price(self):
		if self.sale_price is not None:
			html_text = "<span class='sale-price'>%s <i class='fa fa-rub fa-1x'></i></span><br><span class='og-price'>%s</span>" %(self.sale_price, self.price)
		else:
			html_text = "<span class='price'>%s <i class='fa fa-rub fa-1x'></i></span>" %(self.price)
		return mark_safe(html_text)

	def get_absolute_url(self):
		return self.product.get_absolute_url()

	def add_to_cart(self):
		return "%s?item=%s&qty=1" %(reverse("cart"), self.id)

	def remove_from_cart(self):
		return "%s?item=%s&qty=1&delete=True" %(reverse("cart"), self.id)

	def get_title(self):
		return "%s - %s" %(self.product.title, self.title)



def product_post_saved_receiver(sender, instance, created, *args, **kwargs):
	product = instance
	variations = product.variation_set.all()
	if variations.count() == 0:
		new_var = Variation()
		new_var.product = product
		new_var.title = "Default"
		new_var.price = product.price
		new_var.save()


post_save.connect(product_post_saved_receiver, sender=Product)


def image_upload_to(instance, filename):
	new_filename = ''.join(choice(ascii_letters) for i in range(20))
	basename, file_extension = filename.split(".")
	new_filename = "%s.%s" %(new_filename, file_extension)
	return "products/%s" %(new_filename)


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to=image_upload_to)

	def __str__(self):
		return self.product.title

# Product Category


class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	brand = models.ManyToManyField('Brand', blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("category_detail", kwargs={"slug": self.slug })

	def get_image_url(self):
		img = self.categoryimage_set.first()
		if img:
			return img.image.url
		return img #None


def image_upload_to_category(instance, filename):
	new_filename = ''.join(choice(ascii_letters) for i in range(20))
	basename, file_extension = filename.split(".")
	new_filename = "%s.%s" %(new_filename, file_extension)
	return "categories/%s" %(new_filename)

class CategoryImage(models.Model):
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to=image_upload_to_category)

	def __str__(self):
		return self.category.title

class Brand(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("brand_detail", kwargs={"slug": self.slug })

	def get_image_url(self):
		img = self.brandimage_set.first()
		if img:
			return img.image.url
		return img #None

def image_upload_to_brand(instance, filename):
	new_filename = ''.join(choice(ascii_letters) for i in range(20))
	basename, file_extension = filename.split(".")
	new_filename = "%s.%s" %(new_filename, file_extension)
	return "brands/%s" %(new_filename)

class BrandImage(models.Model):
	brand = models.ForeignKey(Brand)
	image = models.ImageField(upload_to=image_upload_to_brand)

	def __str__(self):
		return self.brand.title

class Collection(models.Model):
	title = models.CharField(max_length=120, unique=True)
	description = models.TextField(blank=True, null=True)
	category = models.ManyToManyField('Category', blank=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("collection_detail", kwargs={"slug": self.slug })

	def get_image_url(self):
		img = self.collectionimage_set.first()
		if img:
			return img.image.url
		return img #None

def image_upload_to_collection(instance, filename):
	new_filename = ''.join(choice(ascii_letters) for i in range(20))
	basename, file_extension = filename.split(".")
	new_filename = "%s.%s" %(new_filename, file_extension)
	return "collections/%s" %(new_filename)

class CollectionImage(models.Model):
	collection = models.ForeignKey(Collection)
	image = models.ImageField(upload_to=image_upload_to_collection)

	def __str__(self):
		return self.collection.title


def image_upload_to_featured(instance, filename):
	new_filename = ''.join(choice(ascii_letters) for i in range(20))
	basename, file_extension = filename.split(".")
	new_filename = "%s.%s" %(new_filename, file_extension)
	return "products/featured/%s" %(new_filename)

class Hardness(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material1(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material2(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material3(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material4(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material5(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material6(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material7(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title


class Material8(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material9(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Material10(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Height(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Weight(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Spring(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Sofa(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Child(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class Filler(models.Model):
	title = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.title

class ProductFeatured(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to=image_upload_to_featured)
	title = models.CharField(max_length=120, null=True, blank=True)
	text = models.CharField(max_length=220, null=True, blank=True)
	text_right = models.BooleanField(default=False)
	text_css_color = models.CharField(max_length=6, null=True, blank=True)
	show_price = models.BooleanField(default=False)
	make_image_background = models.BooleanField(default=False)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.product.title