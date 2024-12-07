from typing import Any, Sequence

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser, Movie


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    """Custom class for UserAdmin

    Args:
        DefaultUserAdmin (_type_): Parent class
    """

    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields: Sequence[str | Sequence[str]] = (
        "title",
        "genre",
        "year",
        "created_date",
        "updated_date",
    )
    list_display: Sequence[str | Any] = (
        "title",
        "genre",
        "year",
        "created_date",
        "updated_date",
    )
    readonly_fields: Sequence[str | Any] = (
        "created_date",
        "updated_date",
    )
