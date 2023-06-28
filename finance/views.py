from django.shortcuts import redirect, render, get_object_or_404,\
    HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Expense, Wallet, Category
from .forms import CategoryForm, ExpenseForm, WalletForm


@login_required
def expenses_list(request):
    expenses = Expense.objects.filter(wallet__user=request.user).\
        order_by('-date')[:10]
    wallets = Wallet.objects.filter(user=request.user)\
        .order_by('-date', '-hour')[:3]

    return render(request, 'finance/expenses_list.html', locals())


@login_required
def create_expense(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST, request.FILES)

        if expense_form.is_valid():
            expense_form.save()

            return HttpResponseRedirect('/')
    else:
        expense_form = ExpenseForm()

    return render(request, 'finance/create_expense.html', locals())


@login_required
def update_expense(request, id):
    if request.method == 'POST':
        expense = get_object_or_404(Expense, id=id, wallet__user=request.user)
        update_expense_form = ExpenseForm(request.POST, request.FILES,
                                          instance=expense)

        if update_expense_form.is_valid():
            update_expense_form.save()

            return HttpResponseRedirect('/')
    else:
        expense = get_object_or_404(Expense, id=id, wallet__user=request.user)
        update_expense_form = ExpenseForm(instance=expense)

    return render(request, 'finance/update_expense.html', locals())


@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, wallet__user=request.user)

    if request.method == 'POST':
        expense.delete()

        return HttpResponseRedirect('/')

    return render(request, 'finance/delete_expense.html', locals())


@login_required
def wallets_list(request):
    wallets = Wallet.objects.filter(user=request.user).order_by('-date',
                                                                '-hour')

    return render(request, 'finance/wallets_list.html', locals())


@login_required
def create_wallet(request):
    wallet_form = WalletForm(request.POST or None)

    if wallet_form.is_valid():
        f = wallet_form.save(commit=False)
        f.user = request.user
        f.save()

        return HttpResponseRedirect('/')

    return render(request, 'finance/create_wallet.html', locals())


@login_required
def update_wallet(request, id):
    if request.method == 'POST':
        wallet = get_object_or_404(Wallet, id=id, user=request.user)
        update_wallet_form = WalletForm(request.POST or None, instance=wallet)

        if update_wallet_form.is_valid():
            update_wallet_form.save()

            return HttpResponseRedirect('/')
    else:
        wallet = get_object_or_404(Wallet, id=id, user=request.user)
        update_wallet_form = WalletForm(instance=wallet)

    return render(request, 'finance/update_wallet.html', locals())


@login_required
def delete_wallet(request, id):
    wallet = get_object_or_404(Wallet, id=id, user=request.user)

    if request.method == 'POST':
        wallet.delete()

        return HttpResponseRedirect('/')

    return render(request, 'finance/delete_wallet.html', locals())


@login_required
def wallet_detail(request, slug):
    wallet = get_object_or_404(Wallet, slug=slug, user=request.user)
    expenses = Expense.objects.filter(wallet=wallet).order_by('-date')
    expenses_sum = sum(expense.amount for expense in expenses)
    current_ballance = wallet.ballance - expenses_sum

    return render(request, 'finance/wallet_detail.html', locals())


@login_required
def categories_list(request):
    categories = Category.objects.filter(user=request.user).order_by('name')

    return render(request, 'finance/categories_list.html', locals())


@login_required
def create_category(request):
    category_form = CategoryForm(request.POST or None)

    if category_form.is_valid():
        f = category_form.save(commit=False)
        f.user = request.user
        f.save()

        return HttpResponseRedirect('/categories-list/')

    return render(request, 'finance/create_category.html', locals())


@login_required
def update_category(request, id):
    category = get_object_or_404(Category, id=id, user=request.user)
    update_category_form = CategoryForm(request.POST or None,
                                        instance=category)

    if update_category_form.is_valid():
        update_category_form.save()

        return HttpResponseRedirect('/categories-list/')

    return render(request, 'finance/update_category.html', locals())


@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, id=id, user=request.user)

    if request.method == 'POST':
        category.delete()

        return HttpResponseRedirect('/categories-list/')

    return render(request, 'finance/delete_category.html', locals())


@login_required
def duplicate_expense(request, expense_name, expense_wallet, expense_category,
                      expense_amount, expense_date, expense_status):
    wallet = Wallet.objects.get(id=expense_wallet)
    category = Category.objects.get(id=expense_category)

    Expense.objects.create(name=f'{expense_name} copy', wallet=wallet,
                           category=category, amount=expense_amount,
                           date=expense_date, status=expense_status)

    if 'next' in request.GET:
        return redirect(request.GET['next'])
