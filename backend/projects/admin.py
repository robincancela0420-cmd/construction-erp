from django.contrib import admin
from . models import Project

admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display =(
        "name",
        "client",
        "location",
        "start_date",
        "end_date",
        "budget",
        "status"
    )

    list_filter = ("status")

    search_fields = (
        "name",
        "client",
        "location",
    )