from django.contrib import admin

from .models import PoliticalParty, Income, Amount

class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']

admin.register(PoliticalParty, PoliticalPartyAdmin)

class IncomeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

admin.register(Income, IncomeAdmin)

class AmountAdmin(admin.ModelAdmin):
    list_display = ['party__short_name', 'income', 'amount']
    ordering = ['year']

admin.register(Amount, AmountAdmin)