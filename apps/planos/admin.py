from django.contrib import admin
from .models import TblCidade, TblFidelidade, TblPlano, TblItens, TblItensCombo, TblAbrangenciaPlano, TblAcordos

class TblCidadeAdmin(admin.ModelAdmin):
    list_display = ['cdd_id', 'cdd_nome', 'cdd_uf', 'cdd_ativo']

admin.site.register(TblCidade, TblCidadeAdmin)

class TblFidelidadeAdmin(admin.ModelAdmin):
    list_display = ['fid_id', 'fid_qtdemeses', 'fid_tipocliente', 'fid_ativo']

admin.site.register(TblFidelidade, TblFidelidadeAdmin)

class TblPlanoAdmin(admin.ModelAdmin):
    list_display = ['plan_id', 'plan_nome', 'plan_valor', 'plan_ordem', 'plan_taxaup', 'plan_taxadown',
                    'plan_destacarplano', 'plan_textdestaque', 'plan_tipocliente', 'plan_tipolink', 'plan_combo',
                    'plan_icon', 'plan_ativo']

admin.site.register(TblPlano, TblPlanoAdmin)

class TblItensAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'item_nome', 'item_scm', 'item_ordem', 'item_icone', 'item_detalhe',
                    'item_linkexterno', 'item_ativo']

admin.site.register(TblItens, TblItensAdmin)

class TblItensComboAdmin(admin.ModelAdmin):
    list_display = ['icomb_id', 'icomb_plan', 'icomb_item']

admin.site.register(TblItensCombo, TblItensComboAdmin)

class TblAbrangenciaPlanoAdmin(admin.ModelAdmin):
    list_display = ['abrang_id', 'abrang_cdd', 'abrang_plan']

admin.site.register(TblAbrangenciaPlano, TblAbrangenciaPlanoAdmin)

class TblAcordosAdmin(admin.ModelAdmin):
    list_display = ['acor_id', 'acor_plan', 'acor_fid', 'acor_valor', 'acor_sla', 'acor_padrao', 'acor_ativo']

admin.site.register(TblAcordos, TblAcordosAdmin)
