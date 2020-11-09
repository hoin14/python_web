from django.contrib import admin

from .models import Candidate, Poll, Partner
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Poll)
admin.site.register(Partner)