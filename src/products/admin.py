from django.contrib import admin

# Register your models here.


from .models import Product, Hardness, Height, Material1, Material2, Material3, Material4, Material5, Material6, Material7, Material8, Material9, Material10, Weight, Sofa, Child, Filler, Spring, Variation, ProductImage, Category, CategoryImage, ProductFeatured, Collection, CollectionImage, Brand, BrandImage

class CollectionImageInline(admin.TabularInline):
	model = CollectionImage
	extra = 0
	max_num = 1

class CategoryImageInline(admin.TabularInline):
	model = CategoryImage
	extra = 0
	max_num = 1

class BrandImageInline(admin.TabularInline):
	model = BrandImage
	extra = 0
	max_num = 1


class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0
	max_num = 10

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0
	max_num = 10


class ProductAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'price']
	inlines = [
		ProductImageInline,
		VariationInline,
	]
	class Meta:
		model = Product

class CollectionAdmin(admin.ModelAdmin):
	list_display = ['__str__']
	inlines = [
		CollectionImageInline,		
	]
	class Meta:
		model = Collection

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['__str__']
	inlines = [
		CategoryImageInline,		
	]
	class Meta:
		model = Category

class BrandAdmin(admin.ModelAdmin):
	list_display = ['__str__']
	inlines = [
		BrandImageInline,		
	]
	class Meta:
		model = Brand

admin.site.register(Product, ProductAdmin)

#admin.site.register(Variation)

#admin.site.register(ProductImage)

#admin.site.register(CollectionImage)

#admin.site.register(CategoryImage)

#admin.site.register(BrandImage)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Brand, BrandAdmin)

admin.site.register(Hardness)

admin.site.register(Material1)

admin.site.register(Material2)

admin.site.register(Material3)

admin.site.register(Material4)

admin.site.register(Material5)

admin.site.register(Material6)

admin.site.register(Material7)

admin.site.register(Material8)

admin.site.register(Material9)

admin.site.register(Material10)

admin.site.register(Height)

admin.site.register(Weight)

admin.site.register(Sofa)

admin.site.register(Child)

admin.site.register(Filler)

admin.site.register(Spring)

admin.site.register(Collection, CollectionAdmin)

admin.site.register(ProductFeatured)