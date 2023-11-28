from django.contrib import admin
from .models import TblAcordos, TblCidade, TblCiddplan, TblFidelidade, TblItens, TblPlaniten, TblPlano

class TblAcordosAdmin(admin.ModelAdmin):
    list_display = ('acor_id', 'acor_plan', 'acor_fid', 'acor_valor', 'acor_sla', 'acor_padrao', 'acor_ativo')

admin.site.register(TblAcordos, TblAcordosAdmin)

class TblCidadeAdmin(admin.ModelAdmin):
    list_display = ('cdd_id', 'cdd_nome', 'cdd_uf', 'cdd_ativo')

admin.site.register(TblCidade, TblCidadeAdmin)

class TblCiddplanAdmin(admin.ModelAdmin):
    list_display = ('cdd', 'plan')

admin.site.register(TblCiddplan, TblCiddplanAdmin)

class TblFidelidadeAdmin(admin.ModelAdmin):
    list_display = ('fid_id', 'fid_qtdemeses', 'fid_ativo')

admin.site.register(TblFidelidade, TblFidelidadeAdmin)

class TblItensAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_nome','item_detalhe', 'item_linkexterno'  , 'item_ativo')

admin.site.register(TblItens, TblItensAdmin)

class TblPlanitenAdmin(admin.ModelAdmin):
    list_display = ('item', 'plan')

admin.site.register(TblPlaniten, TblPlanitenAdmin)

class TblPlanoAdmin(admin.ModelAdmin):
    list_display = ('plan_id', 'plan_nome', 'plan_valor', 'plan_taxaup', 'plan_taxadown', 'plan_destacarplano', 'plan_textdestaque', 'plan_tipocliente', 'plan_tipolink', 'plan_ativo')

admin.site.register(TblPlano, TblPlanoAdmin)


