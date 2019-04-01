import os
import datetime
from django.http import HttpResponse
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .serializers import *
from .filters import ZxgkFilter
from .models import ZxgkInfo
from django_filters.rest_framework import DjangoFilterBackend
from .zxgk import get_captche_id, zhixing_person_list


class ZxgkViewset(GenericViewSet, ListModelMixin):
    queryset = ZxgkInfo.objects.all()
    filter_class = ZxgkFilter
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        infotype = self.request.query_params.get('type')
        if infotype == 'S':
            return ShiXinSerializer

        elif infotype == 'B':
            return BzxrSerializer

        elif infotype == 'X':
            return XgSerializer

        elif infotype == 'Z':
            return ZbSerializer

        return ZxgkSerializer


def spider(request):
    today = datetime.date.today()
    pname = request.GET.get('pname')
    cardnum = request.GET.get('cardnum')

    if os.path.exists('captcha.jpg'):
        os.remove('captcha.jpg')

    if not pname:
        pname = ''

    if cardnum and pname:
        pname = ''

    if not ZxgkInfo.objects.filter(cardNum=cardnum) or \
            today - ZxgkInfo.objects.filter(cardNum=cardnum)[0].spiderTime > \
            datetime.timedelta(days=3):

        captcheid = get_captche_id()
        zxgk_info = zhixing_person_list(pname, cardnum, captcheid)
        ZxgkInfo.objects.bulk_create(zxgk_info)

    return HttpResponse('1')
