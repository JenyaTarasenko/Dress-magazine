from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Slide
from cart.forms import CartAddProductForm
# from review.forms import ReviewForm  #форма отзыва
from django.db.models import Q


def product_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()

    # создаём queryset
    products = Product.objects.all()
    # для того чтобы отображалась форма добавления товара в корзину 
    cart_product_form = CartAddProductForm()
    # добавляем слайдер на главную страницу 
    slider = Slide.objects.filter(active=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        template = 'shop/product/category_list.html'  # главная страница
    else:
        products = products.order_by('-created')[:3]
        template = 'shop/product/product_list.html'  # главная страница

    return render(
        request,
        template,
        # 'shop/product/product_list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
            'cart_product_form': cart_product_form,
            'slider': slider
        }
    )
# вывод одного продукта
def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id, slug=slug, available=True)
      # Случайные 4 товара, кроме текущего
    also_bought = Product.objects.exclude(id=product.id).order_by('?')[:3]
    # корзина добавления товара
    cart_product_form = CartAddProductForm()
    #форма отзыва прилетела из myshop.review/forms.py
    # review_form = ReviewForm()
    return render(request, 'shop/product/detail.html',{'product': product, 'cart_product_form': cart_product_form, 'also_bought': also_bought})




