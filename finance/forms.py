from dataclasses import fields
from django import forms
from .models import Expense, Wallet, Category

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            'name',
            'wallet',
            'category',
            'description',
            'amount',
            'proof',
            'date_and_hour',
            'status',
        ]


class WalletForm(forms.ModelForm):
    class Meta: 
        model = Wallet
        fields = [
            'name',
            'date',
            'ballance',
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
