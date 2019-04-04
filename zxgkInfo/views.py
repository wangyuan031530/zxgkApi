import os
import datetime
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .serializers import *
from .filters import *
from .models import Person
from django_filters.rest_framework import DjangoFilterBackend
from .zxgk import get_captche_id, zhixing_person_list


class PersonViewSet(GenericViewSet, ListModelMixin):
    serializer_class = PersonSerializer
    filter_class = PersonFilter
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        sign = self.spider()
        print(sign)
        if sign == '1':
            return Person.objects.all()

    def spider(self):
        today = datetime.date.today()
        pname = self.request.query_params.get('pname')
        cardnum = self.request.query_params.get('cardnum')

        if os.path.exists('captcha.jpg'):
            os.remove('captcha.jpg')

        if not pname:
            pname = ''

        if cardnum and pname:
            pname = ''

        if Person.objects.filter(cardNum=cardnum) and \
                today - Person.objects.filter(cardNum=cardnum)[0].addTime < \
                datetime.timedelta(days=7):

            return '1'
        else:
            captcheid = get_captche_id()
            zhixing_person_list(pname, cardnum, captcheid)

            return '1'
