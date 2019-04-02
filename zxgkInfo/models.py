from django.db import models
from datetime import date


class ZxgkInfo(models.Model):
    ZXGK_TYPE = (
        ('S', '失信'),
        ('B', '仅被执行人'),
        ('Z', '终本结案信息'),
        ('X', '限制高消费')
    )
    type = models.CharField(max_length=1, choices=ZXGK_TYPE)
    areaName = models.CharField(max_length=32)
    cardNum = models.CharField(max_length=20)
    caseCode = models.CharField(max_length=64)
    courtName = models.CharField(max_length=32)
    disruptTypeName = models.CharField(max_length=64)
    duty = models.TextField()
    gistId = models.CharField(max_length=32)
    gistUnit = models.CharField(max_length=32)
    iname = models.CharField(max_length=8)
    performance = models.CharField(max_length=32)
    publishDate = models.CharField(max_length=32)
    regDate = models.CharField(max_length=32)
    sexy = models.CharField(max_length=8)
    execMoney = models.CharField(max_length=16)
    finalDate = models.CharField(max_length=32)
    unperformMoney = models.CharField(max_length=16)
    spiderTime = models.DateField(default=date.today)
