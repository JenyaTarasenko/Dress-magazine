from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
# from review.forms import ReviewForm  #форма отзыва
from django.db.models import Q


# все продукты выводится в шаблон списком 
def product_list(request, category_slug=None): 
    category = None
    # категории товара вывод на главной странице 
    categories = Category.objects.all()
    # все продукты вывод на главной странице 
    products = Product.objects.filter(available=True)
    # для того чтобы отображалась форма добавления товара в корзину 
    cart_product_form = CartAddProductForm() 
    # добавляем слайдер на главную страницу 
    # slides = Slider.objects.filter(active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category) 
    return render(request,'shop/product/product_list.html', {'category': category, 'categories': categories, 'products': products, 'cart_product_form': cart_product_form})

# вывод одного продукта
def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id, slug=slug, available=True)
    # корзина добавления товара
    cart_product_form = CartAddProductForm()
    #форма отзыва прилетела из myshop.review/forms.py
    # review_form = ReviewForm()
    return render(request, 'shop/product/detail.html',{'product': product, 'cart_product_form': cart_product_form})




