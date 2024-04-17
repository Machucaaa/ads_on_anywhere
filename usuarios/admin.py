from django.contrib import admin
from .models import Propietario
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Propietario
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Informacion de Cuenta',
            {
                'fields': (
                    'url',
                    'plan',
                    'fin_de_plan',
                    'esta_activo',
                )
            }
        )
    )

admin.site.register(Propietario, CustomUserAdmin)
