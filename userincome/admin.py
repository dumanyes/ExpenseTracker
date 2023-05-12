from django.contrib import admin
from .models import UserIncome, Source


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'owner', 'source', 'date',)
    search_fields = ('description', 'source', 'date', 'owner')

    list_per_page = 20

admin.site.register(UserIncome, IncomeAdmin),
admin.site.register(Source)
