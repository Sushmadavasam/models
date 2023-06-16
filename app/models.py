from django.db import models

# Create your models here.
class Department(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)

    DEPTNAME=models.CharField(max_length=100)
    
    LOC=models.CharField(max_length=100)

    def __str__(self):
        return self.DEPTNAME

class EMP(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HIREDATE=models.DateField()
    SAl=models.IntegerField()
    COMM=models.IntegerField(null=True)
    DEPTNO=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.ENAME