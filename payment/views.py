from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import PaymentTitleModel, PaymentModel
from django.shortcuts import get_object_or_404


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


class BuyObjectView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('payment:main_page')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        payment = PaymentModel.objects.create(user=request.user, title_id=pk)
        return HttpResponse(f'zarinpal page - {payment.title.price}')

