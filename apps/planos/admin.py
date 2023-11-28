from django.contrib import admin
from .models import TblAcordos, TblCidade, TblCiddplan, TblFidelidade, TblItens, TblPlaniten, TblPlano

def get_model_fields(model):
    return [field.name for field in model._meta.fields]

class DynamicListDisplayAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.list_display = get_model_fields(model)

admin.site.register(TblAcordos, DynamicListDisplayAdmin)
admin.site.register(TblCidade, DynamicListDisplayAdmin)
admin.site.register(TblCiddplan, DynamicListDisplayAdmin)
admin.site.register(TblFidelidade, DynamicListDisplayAdmin)
admin.site.register(TblItens, DynamicListDisplayAdmin)
admin.site.register(TblPlaniten, DynamicListDisplayAdmin)
admin.site.register(TblPlano, DynamicListDisplayAdmin)
