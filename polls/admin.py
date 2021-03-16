from django.contrib import admin

# Register your models here.
# 向管理页面中加入投票应用
from .models import Question


admin.site.register(Question)
