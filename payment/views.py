from django.shortcuts import render, redirect
from django.views import View
from .models import PaymentTitleModel, PaymentModel
from django.shortcuts import get_object_or_404
from django.conf import settings
import requests
import json
from django.http import JsonResponse


class MainPageView(View):
    def get(self, request):
        selected_object_id = request.GET.get('selected_object_id')
        if selected_object_id:
            selected_object = get_object_or_404(PaymentTitleModel, id=selected_object_id)
        else:
            selected_object = PaymentTitleModel.objects.order_by('created').first()
        context = {
            'buy_objects': PaymentTitleModel.objects.all(),
            'selected_object': selected_object
        }
        return render(request, 'main_page.html', context)


if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"


class BuyObjectView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('payment:main_page')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        payment = PaymentModel.objects.create(user=request.user, title_id=pk)
        request.session['payment'] = {'payment_id': payment.id}
        data = {
            'MerchantID': settings.MERCHANT,
            'Amount': payment.title.price,
            'Description': payment.title.title,
            'CallbackURL': 'http://127.0.0.1:8000/verify/'
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        try:
            response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    url = ZP_API_STARTPAY + str(response['Authority'])
                    return redirect(url)
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response
        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}


class VerifyPayView(View):
    def get(self, request, authority):
        id = request.session['payment']['payment_id']
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": PaymentModel.objects.get(id=id).title.price,
            "Authority": authority,
        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'RefID': response['RefID']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response


class TestView(View):
    def get(self, request):
        url = 'https://payment.zarinpal.com/pg/v4/payment/request.json'
        data = {
            'merchant_id': settings.MERCHANT,
            'amount': 100000,
            'description': 'test',
            'callback_url': 'http://127.0.0.1:8000/verify/'
        }
        data = json.dumps(data)
        headers = {'accept': 'application/json', 'content-type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        print(response)
        return JsonResponse(response.json())
