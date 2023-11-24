

from django.db import models

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ContactInfo(models.Model):
    UserInfo = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    def __str__(self):
        return f"Contact Info for {self.personal_info.first_name} {self.personal_info.last_name}"