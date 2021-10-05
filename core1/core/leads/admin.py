from django.contrib import admin

# Register your models here.

from leads.models import *

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)