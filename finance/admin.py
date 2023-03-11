from django.contrib import admin
from .models import  Wallet, Category, Expense

# Register your models here.
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'ballance',)
    prepopulated_fields = {'slug': ('name', 'date',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'amount',
        'date',
    )

    list_filter = ('date', 'category',)

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wallet, WalletAdmin)
