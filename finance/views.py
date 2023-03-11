from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .models import Expense, Wallet, Category
from .forms import CategoryForm, ExpenseForm, WalletForm

# Create your views here.
def expenses_list(request):
    expenses = Expense.objects.all().order_by('-date')[:10]
    wallets = Wallet.objects.all().order_by('-date', '-hour')[:4]

    return render(request, 'finance/expenses_list.html', locals())


def create_expense(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST, request.FILES)

        if expense_form.is_valid():
            expense_form.save()

            return HttpResponseRedirect('/')
    else:
        expense_form = ExpenseForm()


    return render(request, 'finance/create_expense.html', locals())


def update_expense(request, id):
    if request.method == 'POST':
        expense = get_object_or_404(Expense, id=id)
        update_expense_form = ExpenseForm(request.POST, request.FILES,
                                          instance=expense)
        
        if update_expense_form.is_valid():
            update_expense_form.save()

            return HttpResponseRedirect('/')
    else:
        expense = get_object_or_404(Expense, id=id)
        update_expense_form = ExpenseForm(instance=expense)

    return render(request, 'finance/update_expense.html', locals())


def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    
    if request.method == 'POST':
        expense.delete()

        return HttpResponseRedirect('/')

    return render(request, 'finance/delete_expense.html', locals())


def wallets_list(request):
    wallets = Wallet.objects.all().order_by('-date', '-hour')

    return render(request, 'finance/wallets_list.html', locals())
    

def create_wallet(request):
    wallet_form = WalletForm(request.POST or None)

    if wallet_form.is_valid():
        wallet_form.save()

        return HttpResponseRedirect('/')

    return render(request, 'finance/create_wallet.html', locals())


def update_wallet(request, id):
    wallet = get_object_or_404(Wallet, id=id)
    update_wallet_form = WalletForm(request.POST or None, instance=wallet)

    if update_wallet_form.is_valid():
        update_wallet_form.save()

        return HttpResponseRedirect('/')

    return render(request, 'finance/update_wallet.html', locals())


def delete_wallet(request, id):
    wallet = get_object_or_404(Wallet, id=id)

    if request.method == 'POST':
        wallet.delete()

        return HttpResponseRedirect('/')

    return render(request, 'finance/delete_wallet.html', locals())


def wallet_detail(request, slug):
    wallet = Wallet.objects.get(slug=slug)
    expenses = Expense.objects.filter(wallet=wallet).order_by('-date')
    expenses_sum = 0

    for expense in expenses:
        expenses_sum += expense.amount

    current_ballance = wallet.ballance - expenses_sum

    return render(request, 'finance/wallet_detail.html', locals())


def categories_list(request):
    categories = Category.objects.all().order_by('name')

    return render(request, 'finance/categories_list.html', locals())


def create_category(request):
    category_form = CategoryForm(request.POST or None)

    if category_form.is_valid():
        category_form.save()

        return HttpResponseRedirect('/categories-list/')

    return render(request, 'finance/create_category.html', locals())


def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    update_category_form = CategoryForm(request.POST or None,
                                        instance=category)

    if update_category_form.is_valid():
        update_category_form.save()

        return HttpResponseRedirect('/categories-list/')

    return render(request, 'finance/update_category.html', locals())


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        category.delete()

        return HttpResponseRedirect('/categories-list/')

    return render(request, 'finance/delete_category.html', locals())
