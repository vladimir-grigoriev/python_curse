from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView, RedirectView, CreateView, UpdateView, DetailView
from .models import Cart, User, BookInCart, Order
from products.models import Book
from django.urls import reverse_lazy
from .forms import OrderForm
from django.contrib.messages.views import SuccessMessageMixin


class CartView(TemplateView):
    template_name = 'orders/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if not isinstance(user, User):
            user = None
        if cart_id:
            cart = Cart.objects.filter(pk=cart_id).first()
            if not cart:
                cart = Cart.objects.create(customer=user)
                self.request.session['cart_id'] = cart.pk
        else:
            cart = Cart.objects.create(customer=user)
            self.request.session['cart_id'] = cart.pk

        context["cart"] =  cart
        book_id = self.request.GET.get('book')
        if not book_id:
            return context
        book = Book.objects.filter(pk=int(book_id)).first()
        if book:
            book_in_cart, created = BookInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity': 1,
                    'price': book.price
                }
            )
            if not created:
                book_in_cart.quantity += 1
                book_in_cart.price = book_in_cart.construct_price()
                book_in_cart.save()
        else:
            pass

        context["book"] =  book
        return context
    
class DeleteBookInCartView(DeleteView):
    model = BookInCart
    template_name = 'orders/delete-book-in-cart.html'
    success_url = reverse_lazy('orders:cart')

class CartUpdateView(RedirectView):
    def get_redirect_url(self):
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if cart_id:
            cart = Cart.objects.filter(pk=cart_id).first()
        else:
            # redirect to error page
            pass
        button = self.request.POST.get('submit_button')
        print(self.request.POST)
        if button == 'edit':
            obj_list = []
            for book_in_cart_id, quantity in self.request.POST.items():
                if book_in_cart_id not in ['csrfmiddlewaretoken', 'submit_button']:
                    book_in_cart = BookInCart.objects.get(pk=int(book_in_cart_id))
                    if book_in_cart.cart.pk == cart_id:
                        book_in_cart.quantity = int(quantity)
                        obj_list.append(book_in_cart)
            BookInCart.objects.bulk_update(obj_list, ['quantity'])
        else:
            user = self.request.user
            if not isinstance(user, User):
                user = None
            Order.objects.create(
                user=user,
                cart=Cart.objects.get(pk=cart_id)
            )
            self.request.session['order_id'] = str(self.request.session['cart_id'])
            del self.request.session['cart_id']
            return reverse_lazy('orders:create_order')
        return reverse_lazy('orders:cart')


class CreateOrderView(SuccessMessageMixin, UpdateView):
    template_name = 'orders/order.html'
    success_url = reverse_lazy('hello_world:homepage')
    success_message = "Ваш заказ принят!\nНаши менеджеры свяжутся с вами в ближайшее время"
    model = Order
    fields = [
        'fio',
        'phone',
        'email',
        'adress',
        'delivery',
        'comment'
    ]
    def get_object(self, *args, **kwargs):
        obj = Order.objects.get(cart__pk__exact=self.request.session['order_id'])
        return obj
    

class OrderUpdateView(UpdateView):
    model = Order
    template_name = "orders/delete_order.html"
    success_url = reverse_lazy('hello_world:homepage')
    fields = '__all__'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.POST['button'] == 'delete':
            self.object.status = 'var6'
            # order.save()
            
        return super().post(request, *args, **kwargs)