import hashlib

import six
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def wechat_main(request):
    timestamp = request.GET.get("timestamp", "")
    nonce = request.GET.get("nonce", "")
    signature = request.GET.get("signature", "")

    token = "yxuoffernet307943baf3"

    if not check_signature(
            token=token, timestamp=timestamp, nonce=nonce, signature=signature
    ):
        return HttpResponse("hello")
    if request.method == "GET":
        return HttpResponse(request.GET.get("echostr", ""))


def check_signature(token, timestamp, nonce, signature):
    if not (token and timestamp and nonce and signature):
        return False
    sign = get_signature(token, timestamp, nonce)
    return sign == signature


def get_signature(token, timestamp, nonce, *args):
    sign = [token, timestamp, nonce] + list(args)
    sign.sort()
    sign = to_binary(''.join(sign))
    return hashlib.sha1(sign).hexdigest()


def to_binary(value, encoding="utf-8"):
    if isinstance(value, six.binary_type):
        return value
    if isinstance(value, six.text_type):
        return value.encode(encoding)
    return six.binary_type(value)


from werobot.contrib.django import make_view
