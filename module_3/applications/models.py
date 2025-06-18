from django.db import models
from accounts.models import User


SERVICE_CHOICES = [
    ("main", "Общий клининг"),
    ("general", "Генеральная уборка"),
    ("build", "Послестроительная уборка"),
    ("chemical", "Химчистка ковров и мебели"),
    ("other", "Иная услуга"),
]

PAYMENT_CHOICES = [
    ("cash", "Наличными"),
    ("card", "Картой"),
]

STATUS_CHOICES = [
    ("new", "Новая заявка"),
    ("completed", "Услуга оказана"),
    ("canceled", "Услуга отменена"),
]

class ApplicationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Заявитель")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    date_time = models.DateTimeField(verbose_name="Дата и время услуги")
    service_type = models.CharField(choices=SERVICE_CHOICES, max_length=9, verbose_name="Вид услуги")
    other_service_description = models.TextField(blank=True, null=True, verbose_name="Описание услуги")
    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=5)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="new", verbose_name="Статус заявки")
    cancel_reason = models.TextField(null=True, blank=True, verbose_name="Причина отмены")
    
    class Meta:
        verbose_name="Услуга"
        verbose_name_plural="Услуги"
    
    def __str__(self):
        return f"Заявка №{self.id} от {self.user.full_name}"