from django.contrib import admin
from Receipt.models import Receipts
class ReceiptAdmin(admin.ModelAdmin):
    list_display=['receipt_number','Name','date','email','mobile_number','amount','years']

admin.site.register(Receipts,ReceiptAdmin)
# Register your models here.
