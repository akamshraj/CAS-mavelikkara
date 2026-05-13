from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name


class HOD(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='hods'
    )
    detailss = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='hod_photos/')

    def __str__(self):
        return self.department.name