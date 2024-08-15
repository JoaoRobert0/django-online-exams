from django.contrib import admin
from .models import *

admin.site.register(Theme)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Choices)