from django.contrib import admin
from equipment_lend.models import User, LendRecord, BelongingsImformation, Company_information
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_password', 'user_name', 'user_class', 'user_email', 'user_phone')
    list_filter = ('user_id', 'user_name')
    search_fields = ('user_id',)
    ordering = ('user_id',) 


class LendRecordAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'equipment_id', 'lend_date', 'borrow_date')
    list_filter = ('user_id', 'equipment_id')
    search_fields = ('user_id',)
    ordering = ('user_id',) 


class BelongingsImformationAdmin(admin.ModelAdmin):
    list_display = ('equipment_id', 'property_number', 'serial_number', 'property_name', 'property_price', 'purchase_date', 'placement', 'property_status', 'company_id')
    list_filter = ('equipment_id', 'property_number')
    search_fields = ('equipment_id',)
    ordering = ('equipment_id',) 


class Company_informationAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'company_editor', 'company_name', 'company_contact_name', 'company_contact_email', 'company_phone')
    list_filter = ('company_id', 'company_name')
    search_fields = ('company_id', 'company_name',)
    ordering = ('company_id',) 


admin.site.register(User, UserAdmin)
admin.site.register(LendRecord, LendRecordAdmin)
admin.site.register(BelongingsImformation, BelongingsImformationAdmin)
admin.site.register(Company_information, Company_informationAdmin)

