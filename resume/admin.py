from django.contrib import admin

# Register your models here.
from .models import Skill,Education,Achievement

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Achievement)




