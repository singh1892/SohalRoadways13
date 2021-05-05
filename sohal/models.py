from django.db import models
from datetime import datetime ,date


# Create your models here.
class Task(models.Model):
    taskcollectionDt = models.DateField(blank=True, null=True,)
    taskDispatchDt = models.DateField(blank=True, null=True,auto_now=False,auto_now_add=False)
    taskShipNo = models.IntegerField()
    taskSDMNo = models.IntegerField()
    taskModelNo = models.CharField(max_length=300)
    taskChassisNo = models.CharField(max_length=300)
    taskFrom = models.CharField(max_length=300)
    taskTo = models.CharField(max_length=300)
    taskDealerName = models.CharField(max_length=300)
    taskDelDate = models.DateField(blank=True, null=True,auto_now=False,auto_now_add=False)
    taskStatus = models.CharField(max_length=300)
    taskDrivername =models.CharField(max_length=300)
    taskcontact = models.IntegerField()
    taskDistance = models.FloatField() 
    taskAverage = models.FloatField()
    taskHSDpump =models.FloatField()
    taskCashOnHand = models.FloatField()
    taskDeiselDRate = models.FloatField()
    taskTotalDeisel = models.FloatField()
    taskDriverPayment = models.FloatField()
    taskTax = models.FloatField()
    taskOtherExpenses = models.FloatField()
    taskTotalBillAmnt = models.FloatField()
    taskTaxableamnt = models.FloatField()
    taskIgst = models.FloatField()
    taskTotalBillingAmount = models.FloatField()
    taskPoddt = models.DateField(blank=True, null=True,auto_now=False,auto_now_add=False)
    taskBillNo =models.CharField(max_length=300)
    taskBillDt = models.DateField(blank=True, null=True,auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.taskChassisNo
    