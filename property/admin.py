from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owners__fio")
    readonly_fields = ("created_at",)
    list_display = (
        "address",
        "price",
        "new_building",
        "construction_year",
        "town",
    )
    list_editable = ("new_building",)
    list_filter = ("new_building",)
    raw_id_fields = ("liked_by", "owners")


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("creator", "target_flat")


class FlatsOwnInline(admin.TabularInline):
    model = Owner.flats_own.through
    raw_id_fields = ("flat",)


class OwnerAdmin(admin.ModelAdmin):
    inlines = [
        FlatsOwnInline,
    ]
    list_display = (
        "fio",
        "owners_phonenumber",
        "owner_pure_phone",
    )
    raw_id_fields = ("flats_own",)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
