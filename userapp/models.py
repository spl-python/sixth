from django.db import models


class User(models.Model):
    gender_choice = (
        (0, 'male'),
        (1, 'female')
    )
    username = models.CharField(max_length=128)
    re_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    gender = models.SmallIntegerField(choices=gender_choice, default=0)
    status = models.BooleanField(default=True)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Employee(models.Model):
    emp_name = models.CharField(max_length=128)
    img = models.ImageField(upload_to='img',null=True)
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    age = models.IntegerField()

    @property
    def full_img(self):
        return "%s%s%s" % ("http://127.0.0.1:8000/", "media/", self.img)

    class Meta:
        db_table = 'employee'
        verbose_name = '员工'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name