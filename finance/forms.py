# from dataclasses import fields
from django import forms
from .models import Expense, Wallet, Category
from users.models import User


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'wallet', 'category', 'description', 'amount',
                  'proof', 'date', 'status', ]


class WalletForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Wallet
        fields = ['name', 'user', 'date', 'ballance', ]


class CategoryForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Category
        fields = ['name', 'user', ]
