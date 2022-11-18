from django.urls import path

from .views import expenses_list, wallet_detail, create_expense, \
    update_expense, delete_expense, create_wallet, update_wallet, \
    delete_wallet, wallets_list, categories_list, create_category, \
    update_category, delete_category

urlpatterns = [
    path('', expenses_list, name='expenses_list'),
    path('wallets-list/', wallets_list, name='wallets_list'),
    path('wallet/<slug:slug>/', wallet_detail, name='wallet_detail'),
    path('create-expense/', create_expense, name='create_expense'),
    path('update-expense/<id>/', update_expense, name='update_expense'),
    path('delete-expense/<id>/', delete_expense, name='delete_expense'),
    path('create-wallet/', create_wallet, name='create_wallet'),
    path('update-wallet/<id>/', update_wallet, name='update_wallet'),
    path('delete/wallet/<id>/', delete_wallet, name='delete_wallet'),
    path('categories-list/', categories_list, name='categories_list'),
    path('create-category/', create_category, name='create_category'),
    path('update-category/<id>/', update_category, name='update_category'),
    path('delete-category/<id>/', delete_category, name='delete_category'),
]
