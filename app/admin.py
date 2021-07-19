from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from .models import *

@admin.register(Tamaño)
class TamañoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "precio",)

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("__str__", "codigo", "precio",)

@admin.register(Sandwich)
class SandwichAdmin(admin.ModelAdmin):
    list_display = ("__str__", "tamaño","precio")

@admin.register(IngredientesSandwich)
class IngredientesSandwichAdmin(admin.ModelAdmin):
    list_display = ("__str__", "precio")

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ("__str__", "cliente", "fecha", "total",)

@admin.register(OrdenSandwich)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ("__str__",)

##################################33


# class InLineImage(nested_admin.NestedTabularInline):
#     model=Image
#     extra=2

# class InLineSize(nested_admin.NestedTabularInline):
#     model=ItemColorwaySize
#     extra=1

# class InLineIC(nested_admin.NestedTabularInline):
#     model=ItemColorway
#     inlines = [InLineImage, InLineSize]

# @admin.register(Item)
# class ItemAdmin(nested_admin.NestedModelAdmin):
#     inlines = [InLineIC]

#     list_display = ("__str__","price",)
#     list_editable = ("price",)
#     search_fields = ("name",)

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ("__str__","name","itemColorwayId","order")
#     list_editable = ("name","order",)
#     search_fields = ("itemColorwayId__itemId__name",)

# @admin.register(ItemColorway)
# class ItemColorwayAdmin(nested_admin.NestedModelAdmin):
#     inlines = [InLineImage, InLineSize]

#     list_display = ("__str__", "itemId", "colorwayId",)
#     search_fields = ("itemId__name", "colorwayId__name")

# @admin.register(ItemColorwaySize)
# class ItemColorwaySizeAdmin(admin.ModelAdmin):
#     list_display = ("__str__","itemColorwayId","sizeId","stock",)
#     list_editable =("stock",)
#     search_fields = ("itemColorwayId__itemId__name","sizeId__name","itemColorwayId__colorwayId__name")

# @admin.register(Type)
# class TypeAdmin(admin.ModelAdmin):
#     pass
