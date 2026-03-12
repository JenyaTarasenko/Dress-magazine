# from django.contrib import admin


# from django.contrib import admin
# from .models import Order, OrderItem


# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product']


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'email',
#                     'nova_poshta_branch', 'city', 'paid',
#                     'created', 'updated']
#     list_filter = ['paid', 'created', 'updated']
#     inlines = [OrderItemInline]


from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    readonly_fields = ['price', 'quantity', 'get_cost']
    extra = 0

    def get_cost(self, obj):
        return obj.get_cost()
    get_cost.short_description = 'Стоимость'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'city', 'paid', 'created', 'get_total_cost', 'nova_poshta_branch']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['first_name', 'last_name', 'email', 'nova_poshta_branch']
    inlines = [OrderItemInline]

    def get_total_cost(self, obj):
        return obj.get_total_cost()
    get_total_cost.short_description = 'Общая сумма заказа'