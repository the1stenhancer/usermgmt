from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.

class Detail(models.Model):
    MARITAL_STATUS = (
        (_('Yes'), _('Married')),
        (_('No'), _('Not Married')),
    )
    # personal information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(help_text=_("Phone number"), max_length=20, null=False)
    dob = models.DateField(help_text=_("Date of birth"), null=False)
    married = models.CharField(max_length=25, choices=MARITAL_STATUS, help_text=_("Marital status"), null=False)
    kids = models.PositiveIntegerField(default=0, help_text=_("Number of kids"), null=False)
    # work information
    doh = models.DateField(auto_now_add=True, help_text=_("Date of hiring"), null=False)
    title = models.CharField(help_text=_("Job title"), max_length=255, null=False)
    duration = models.PositiveIntegerField(help_text=_("Contract duration"), default=3, null=False)
    # other information
    updated = models.DateTimeField(auto_now=True, help_text=_("Datetime model was last modified"))

    def age(self):
        year = timezone.datetime.date(timezone.datetime.now()).year
        dob_year = self.dob.year
        return year - dob_year
    
    def eoh(self):
        return timezone.datetime.date(self.doh + timezone.timedelta(days=self.duration*365))

    class Meta:
        ordering = ("-doh", "-duration")
        verbose_name = "Detail"
        verbose_name_plural = "Details"
    