from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def register(self):
        self.save()

    @staticmethod
    def get_login_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def email_exist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
