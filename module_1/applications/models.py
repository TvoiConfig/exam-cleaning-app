from django.db import models
from accounts.models import User


SERVICE_CHOICES = [
    ("main", "Общий клининг"),
    ("general", "Генералньая уборка"),
    ("building", "Послестроительная уборка"),
    ("chemical", "химчистка ковров и мебели"),
]

PAYMENT_CHOICES = [
    ("cash", "Наличными"),
    ("card", "Картой"),
]

class ApplicationModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, verbose_name="Адрес")
    contacts = models.CharField(max_length=100, verbose_name="Контактные данные")
    service_type = models.CharField(
        max_length=8,
        choices=SERVICE_CHOICES,
        default="main",
        verbose_name="Вид услуги"
    )
    payment_type = models.CharField(
        max_length=5,
        choices=PAYMENT_CHOICES,
        default='card',
        verbose_name="Тип оплаты"
    )
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        
    def __str__(self):
        return f"{self.author} {self.address}"