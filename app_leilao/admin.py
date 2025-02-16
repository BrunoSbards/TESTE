from django.contrib import admin
from .models import estado, matricula, leiloeiro, anexo

admin.site.register(estado)
class estadoAdmin(admin.ModelAdmin):
    list_display = ('sigla_estado',)

admin.site.register(matricula)
class matriculaAdmin(admin.ModelAdmin):
    list_display = ('numero_matricula')

admin.site.register(leiloeiro)
class leiloeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'telefone', 'site')

admin.site.register(anexo)
class anexoAdmin(admin.ModelAdmin):
    list_display = ('leioeiro', 'matricula', 'arquivo')