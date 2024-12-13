from django.contrib import admin
from .models import Filme, Episodio, Usuario, Serie
from django.contrib.auth.admin import UserAdmin

# só existe porque a gente quer que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos', 'series_vistas')})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
admin.site.register(Serie)

