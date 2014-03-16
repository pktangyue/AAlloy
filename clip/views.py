from django.shortcuts import render
from clip.models import Window
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from decimal import Decimal
import parser

def index(request):
    context = {
            'windows' : Window.objects.all
            }
    return render(request, 'clip/index.html', context)

def submit(request):
    windows = Window.objects.all()
    results = []
    for window in windows:
        id = window.pk
        has_num = request.POST.get('id_%d' % id, False);
        if not has_num:
            continue
        num = int(request.POST.get('num_%d' % id, 0))
        if num == 0:
            continue
        x = Decimal(request.POST.get('x_%d' % id, 0))
        y = Decimal(request.POST.get('y_%d' % id, 0))
        m = Decimal(request.POST.get('m_%d' % id, 0))
        z = Decimal(request.POST.get('z_%d' % id, 0))
        products = window.product_set.all()
        for product in products:
            formula = product.product_name.formula
            a = product.producttrim_set.get(material_id=1).trim_length
            code = parser.expr(formula).compile()
            length = eval(code)
            result = {
                    'name' : product.product_name,
                    'length' : length,
                    'num' : num * product.num
                    }
            results.append(result)

    return HttpResponseRedirect(reverse('clip:result'))

def result(request):
    context = {
            }
    return render(request, "clip/result.html", context)
