from django.shortcuts import render
from clip.models import Window, Record
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from decimal import Decimal
import parser
from collections import OrderedDict

def index(request):
    context = {
            'windows' : Window.objects.all
            }
    return render(request, 'clip/index.html', context)

def submit(request):
    windows = Window.objects.all()

    record = None

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

        if record == None:
            record = Record()
            record.save()

        record.recordwindow_set.create(window = window, x = x, y = y, m = m, z = z, num = num)

        products = window.product_set.all()
        for product in products:
            formula = product.product_name.formula
            a = product.producttrim_set.get(material_id=1).trim_length
            code = parser.expr(formula).compile()
            length = eval(code)
            product_num = num * product.num

            record.recordproduct_set.create(product = product, length = length, num = product_num)

    record.save()

    return HttpResponseRedirect(reverse('clip:record', args=[record.pk]))

def record(request, record_id):
    record = Record.objects.get(pk=record_id)
    results = {}
    record_products = record.recordproduct_set.all()
    for record_product in record_products:
        name = record_product.product.product_name.name
        order = record_product.product.product_name.order
        length = record_product.length
        num = record_product.num
        try:
            results[order][name][length] += num
        except:
            results.setdefault(order,{}).setdefault(name,{}).setdefault(length,num)


    results = OrderedDict(sorted(results.items(), key=lambda t: t[0]))
    context = {
            'record' : record,
            'record_windows' : record.recordwindow_set,
            'results' : results,
            }
    return render(request, "clip/record.html", context)
