from django.shortcuts import render
from clip.models import Window, Record, Material
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from decimal import Decimal
import parser
from collections import OrderedDict
import math

def index(request):
    context = {
            'windows' : Window.objects.all,
            'materials' : Material.objects.all,
            }
    return render(request, 'clip/index.html', context)

def submit(request):
    material_id = request.POST.get('material_id', 0)
    arr_id = request.POST.getlist('id[]');
    arr_num = request.POST.getlist('num[]');
    arr_x = request.POST.getlist('x[]');
    arr_y = request.POST.getlist('y[]');
    arr_m = request.POST.getlist('m[]');
    arr_z = request.POST.getlist('z[]');

    record = None

    for i in range(len(arr_id)):
        id = int(arr_id[i]);
        num = int(arr_num[i]);
        x = Decimal(arr_x[i]);
        y = Decimal(arr_y[i]);
        m = Decimal(arr_m[i]);
        z = Decimal(arr_z[i]);

        if record == None:
            record = Record()
            record.material = Material.objects.get(pk = material_id)
            record.save()

        window = Window.objects.get(pk = id)
        record.recordwindow_set.create(window = window, x = x, y = y, m = m, z = z, num = num);

        products = window.product_set.all()
        for product in products:
            formula = product.product_name.formula
            a = product.producttrim_set.get(material_id = material_id).trim_length
            code = parser.expr(formula).compile()
            length = eval(code)
            length = math.floor(length * 10) / 10.0
            product_num = num * product.num

            record.recordproduct_set.create(product = product, length = length, num = product_num)

    record.save()

    return HttpResponseRedirect(reverse('clip:record', args=[record.pk]))

def record(request, record_id, is_show_foot = True):
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
            'record_windows' : record.recordwindow_set.all(),
            'results' : results,
            'is_show_foot' : is_show_foot
            }
    return render(request, "clip/record.html", context)

def recent(request):
    record_id = Record.objects.latest('pk').pk
    return record(request, record_id, False)

def history(request):
    records = Record.objects.order_by('id')
    context = {
            'records' : records
            }
    return render(request, "clip/history.html", context)
