from django.contrib import admin
from .models import User, RedesSociales, RepresentanteLegal, Aspirante, Reclutador_empresa, FormacionAspirante, IdiomaAspirante, ExperienciaLaboral

# Register your models here.


admin.site.register(User)
admin.site.register(RedesSociales)
admin.site.register(RepresentanteLegal)
admin.site.register(Aspirante)
admin.site.register(Reclutador_empresa)
admin.site.register(FormacionAspirante)
admin.site.register(IdiomaAspirante)
admin.site.register(ExperienciaLaboral)



