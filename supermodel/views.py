import json

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


MODELS = {}


@csrf_exempt
def api(request):
    params = {}
    for k, v in request.POST.items():
        params[k] = v
    model = request.META.get('HTTP_X_MODEL', '')
    method = request.META.get('HTTP_X_METHOD', '')
    if model != '':
        model = MODELS.get(model, None)
        if model is not None:
            try:
                results = []
                obj = getattr(model.objects, method)(**params)
                objs = [obj] if not hasattr(obj, '__iter__') else obj
                for o in objs:
                    data = {}
                    for field in model._meta.fields:
                        data[field.name] = getattr(o, field.name)
                    results.append(data)
                return HttpResponse(json.dumps(results))
            except:
                pass
    return HttpResponse('[]')

