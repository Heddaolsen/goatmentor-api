from django.contrib import admin

from training.models import Drill_types, Drills, Training_sessions

# Register your models here.

admin.site.register(Drill_types)
admin.site.register(Drills)
admin.site.register(Training_sessions)
