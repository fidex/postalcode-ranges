from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.template import loader
from django.core.cache import cache

from .regex_builder import createIntRegex
import logging
import hashlib
# import re

Logger = logging.getLogger("test")
Logger.setLevel('DEBUG')


def index(request):

    template = loader.get_template('regex_builder/index.html')
    context = {
        'lower': 50672,
        'upper': 52667,
    }
    return HttpResponse(template.render(context, request))


@api_view(['GET'])
def regex_builder(request, lower, upper):
    # Logger.info(lower)
    # Logger.info(dir(request))
    
    hash_base = str(lower) + str(upper)
    hash_key = hashlib.sha224(hash_base.encode()).hexdigest()
    Logger.info(hash_key)

    _cached = cache.get(hash_key)
    if _cached:
        Logger.info('serve from cache')
        return HttpResponse(str(_cached), content_type="text/plain", status=200)
    else:
        try:
            regex = createIntRegex(str(lower), str(upper))
        except Exception as e:
            return HttpResponse(str(repr(e)), content_type="text/plain", status=200)
        cache.set(hash_key, regex, 300)
    # return HttpResponse(f'<test>{lower}-{upper} = {regex}</test>', content_type="text/plain", status=200)
    return HttpResponse(regex, content_type="text/plain", status=200)
