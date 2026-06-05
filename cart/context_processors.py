from .models import Cart

def cart_processor(request):
    if not request.session.session_key:
        request.session.create()
    cart, created = Cart.objects.get_or_create(
        session_key = request.session.session_key
    )

    return('cart_total_item': cart.total_items,'cart_sumtotal': cart.sumtotal,)
   