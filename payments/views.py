import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import Item


class SuccessView(TemplateView):
    template_name = 'success.html'


class FailView(TemplateView):
    template_name = 'fail.html'


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    context = {
        'item': item,
    }
    return render(request, 'item.html', context)


@csrf_exempt
def create_session(request, id):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item = get_object_or_404(Item, pk=id)
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'fail/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': item.name,
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': item.price * 100,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
