from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .utils import n2w as n2w_util, w2n as w2n_util


def index(request):
    return render(request, 'index.html')


def n2w(request):
    num = request.POST.get('number', None)
    if num:
        if len(str(num)) > 12:
            return HttpResponse({"Please enter less than billion!"}, content_type='application/json', status=406)
        num = num.replace('.', '').replace(',', '')
        res = n2w_util.get_number_as_words(int(num))
        return JsonResponse({'res': res})
    else:
        return HttpResponseBadRequest()


def w2n(request):
    words = request.POST.get('text', None)
    if words:
        words = words.replace(' and ', ' ').replace('-', ' ').lower()
        try:
            res = w2n_util.get_words_as_number(words)
            return JsonResponse({'res': res})
        except Exception as e:
            print(e)
            return HttpResponse(e, content_type='application/json', status=406)
    else:
        return HttpResponseBadRequest()