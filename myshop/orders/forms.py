from django import forms
from .models import Order


# 1) предоставитьпользователюформузаказа,чтобытотзаполнилеесвои- ми данными;
# 2) создать новый экземпляр Order с введенными данными и создать свя- занный экземпляр OrderItem для каждого товара в корзине;
# 3) очистить все содержимое корзины и перенаправить пользователя на страницу успеха.

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email','nova_poshta_branch', 'city']