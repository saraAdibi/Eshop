from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from eshop_order.forms import UserNewOrderForm
from eshop_order.models import Order
from eshop_products.models import Product


@login_required
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.objects.get_by_id(product_id=product_id)
        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
        # todo: redirect user to user panel
        # return redirect('/user/orders')
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')

    return redirect('/')


@login_required(login_url='/login')
def user_open_order(request):
    context = {
        'order': None,
        'details': None
    }
    # vse moshkhs krdne noe moteghayer =>   open_order: Order
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        # age open order vojod dshte bashe if none nmishe
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
    return render(request, 'order/user_open_order.html', context)
