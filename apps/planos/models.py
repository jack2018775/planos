from django.db import models

class TblCidade(models.Model):
    cdd_id = models.AutoField(primary_key=True)
    cdd_nome = models.CharField(max_length=100)
    cdd_uf = models.CharField(max_length=2)
    cdd_ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_Cidade'

    def __str__(self):
        return f'Cidade: {self.cdd_nome} ({self.cdd_uf})'

class TblFidelidade(models.Model):
    fid_id = models.AutoField(primary_key=True)
    fid_qtdemeses = models.IntegerField()
    fid_tipocliente = models.CharField(max_length=11)
    fid_ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_Fidelidade'

    def __str__(self):
        return f'Fidelidade: {self.fid_qtdemeses} meses'

class TblPlano(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_nome = models.CharField(max_length=100, blank=True, null=True)
    plan_valor = models.FloatField(blank=True, null=True)
    plan_ordem = models.IntegerField(unique=True, blank=True, null=True)
    plan_taxaup = models.FloatField()
    plan_taxadown = models.FloatField()
    plan_destacarplano = models.IntegerField()
    plan_textdestaque = models.CharField(max_length=20, blank=True, null=True)
    plan_tipocliente = models.CharField(max_length=11)
    plan_tipolink = models.CharField(max_length=13)
    plan_combo = models.IntegerField()
    plan_icon = models.CharField(max_length=255, blank=True, null=True)
    plan_ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_Plano'

    def __str__(self):
        return f'Plano: {self.plan_nome}'

class TblItens(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_nome = models.CharField(max_length=25)
    item_scm = models.IntegerField(blank=True, null=True)
    item_ordem = models.IntegerField(unique=True, blank=True, null=True)
    item_icone = models.CharField(max_length=255, blank=True, null=True)
    item_detalhe = models.TextField(blank=True, null=True)
    item_linkexterno = models.CharField(max_length=255, blank=True, null=True)
    item_ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_Itens'

    def __str__(self):
        return f'Item: {self.item_nome}'

class TblItensCombo(models.Model):
    icomb_id = models.AutoField(primary_key=True)
    icomb_plan = models.ForeignKey(TblPlano, models.DO_NOTHING, db_column='icomb_plan_ID')
    icomb_item = models.ForeignKey(TblItens, models.DO_NOTHING, db_column='icomb_item_ID')

    class Meta:
        managed = False
        db_table = 'tbl_ItensCombo'

    def __str__(self):
        return f'Combo: {self.icomb_id}'

class TblAbrangenciaPlano(models.Model):
    abrang_id = models.AutoField(primary_key=True)
    abrang_cdd = models.ForeignKey(TblCidade, models.DO_NOTHING, db_column='abrang_cdd_ID')
    abrang_plan = models.ForeignKey(TblPlano, models.DO_NOTHING, db_column='abrang_plan_ID')

    class Meta:
        managed = False
        db_table = 'tbl_AbrangenciaPlano'

    def __str__(self):
        return f'Abrangência do Plano ({self.abrang_id})'

class TblAcordos(models.Model):
    acor_id = models.AutoField(primary_key=True)
    acor_plan = models.ForeignKey(TblPlano, models.DO_NOTHING, db_column='acor_plan_ID')
    acor_fid = models.ForeignKey(TblFidelidade, models.DO_NOTHING, db_column='acor_fid_ID')
    acor_valor = models.FloatField(db_column='acor_Valor')
    acor_sla = models.CharField(max_length=30, blank=True, null=True)
    acor_padrao = models.IntegerField()
    acor_ativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_Acordos'

    def __str__(self):
        return f'Acordo ({self.acor_id}) para {self.acor_plan.plan_nome} com Fidelidade de {self.acor_fid.fid_qtdemeses} meses'
