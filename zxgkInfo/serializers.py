from rest_framework.serializers import ModelSerializer
from .models import ZxgkInfo


class ShiXinSerializer(ModelSerializer):

    class Meta:
        model = ZxgkInfo
        exclude = ('spiderTime','execMoney', 'finalDate', 'unperformMoney')


class XgSerializer(ModelSerializer):

    class Meta:
        model = ZxgkInfo
        fields = ('zxgk_type', 'iname', 'cardNum', 'sexy', 'courtName', 'areaName', 'caseCode', 'regDate')


class BzxrSerializer(ModelSerializer):

    class Meta:
        model = ZxgkInfo
        fields = ('zxgk_type', 'iname', 'cardNum', 'sexy', 'courtName', 'regDate', 'caseCode', 'execMoney')


class ZbSerializer(ModelSerializer):

    class Meta:
        model = ZxgkInfo
        fields = ('zxgk_type', 'iname', 'cardNum', 'caseCode', 'sexy', 'courtName', 'regDate', 'finalDate', 'execMoney', 'unperformMoney')


class ZxgkSerializer(ModelSerializer):

    class Meta:
        model = ZxgkInfo
        exclude = ('spiderTime', 'id')
