from django.shortcuts import get_object_or_404,redirect
from django.views.generic import View
from django.http import JsonResponse,HttpResponse
from django.template.response import TemplateResponse
from django.contrib import messages
from django.db import transaction
from main.models import Product,ProductSize
from .models import Cart,CartItem
from .forms import AddToCartForm,UpdateCartItemForm
import json

class CartMixin:
    def get_cart(self,request):
        if hasattr(request,'cart'):
            return request
        if not request.session.session_key:
            request.session.create()
        cart,created = Cart.objects.get_or_create(
            session_key=request.session.session_key
        )
        request.session['cart_id'] = cart.id
        request.session.modifiend = True
        return cart