import os
from datetime import timedelta
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from utils.custom_json_response import JsonResponse
from django.db.models import Q
from .serializers import *
from .filters import *
from .models import Person
from django_filters.rest_framework import DjangoFilterBackend
from .zxgk import get_captche_id, zxgk_list


class PersonViewSet(GenericViewSet, ListModelMixin):
    serializer_class = PersonSerializer
    filter_class = PersonFilter
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        sign = self.spider()
        c = self.request.query_params.get("category")
        cardnum = self.request.query_params.get("cardnum")
        pname = self.request.query_params.get("pname")
        if sign == '1':
            if c == 'S':
                return ShiXin.objects.filter(person=Person.objects.filter(Q(cardNum=cardnum) & Q(iname=pname))[0].id)
            elif c == 'B':
                return Bzxr.objects.filter(person=Person.objects.filter(Q(cardNum=cardnum) & Q(iname=pname))[0].id)
            elif c == 'X':
                return Xgl.objects.filter(person=Person.objects.filter(Q(cardNum=cardnum) & Q(iname=pname))[0].id)
            elif c == 'Z':
                return ZhongBen.objects.filter(person=Person.objects.filter(Q(cardNum=cardnum) & Q(iname=pname))[0].id)
            else:
                return Person.objects.all()

    def spider(self):
        today = date.today()
        pname = self.request.query_params.get('pname')
        cardnum = self.request.query_params.get('cardnum')

        if os.path.exists('captcha.jpg'):
            os.remove('captcha.jpg')

        if not pname:
            pname = '无'

        if Person.objects.filter(Q(cardNum=cardnum) & Q(iname=pname)) and \
                today - Person.objects.filter(cardNum=cardnum)[0].updateTime < \
                timedelta(days=7):
            return '1'
        else:
            Person.objects.update_or_create(cardNum=cardnum, iname=pname, defaults={"updateTime":today})
            captcheid = get_captche_id()
            zxgk_list(cardnum, captcheid)

            return '1'

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(data=serializer.data, message="success", code=200)
