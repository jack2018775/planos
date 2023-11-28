from django.db import models

class TblAcordos(models.Model):
    acor_id = models.AutoField(primary_key=True)
    acor_plan = models.ForeignKey('TblPlano', models.CASCADE, default='1')
    acor_fid = models.ForeignKey('TblFidelidade', models.CASCADE, default='1')
    acor_valor = models.FloatField()
    acor_sla = models.CharField(max_length=30, blank=True, null=True)
    acor_padrao = models.IntegerField()
    acor_ativo = models.IntegerField()

    def __str__(self):
        return f'TblAcordos: {self.acor_id}'

class TblCidade(models.Model):
    cdd_id = models.AutoField(primary_key=True)
    cdd_nome = models.CharField(max_length=100)
    cdd_uf = models.CharField(max_length=45)
    cdd_ativo = models.IntegerField()

    def __str__(self):
        return f'TblCidade: {self.cdd_nome}'

class TblCiddplan(models.Model):
    cdd = models.ForeignKey('TblCidade', models.CASCADE, default='1')
    plan = models.ForeignKey('TblPlano', models.CASCADE, default='1')

    def __str__(self):
        return f'TblCiddplan: {self.cdd.cdd_nome} - {self.plan.plan_nome}'

class TblFidelidade(models.Model):
    fid_id = models.AutoField(primary_key=True)
    fid_qtdemeses = models.IntegerField(unique=True)
    fid_ativo = models.IntegerField()

    def __str__(self):
        return f'TblFidelidade: {self.fid_qtdemeses} meses'

class TblItens(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_nome = models.CharField(max_length=25)
    item_ordem = models.IntegerField(unique=True, blank=True, null=True, db_comment='Cadastre os itens que agregam maior valor no topo da lista')
    item_icone = models.CharField(max_length=45, blank=True, null=True)
    item_detalhe = models.TextField(blank=True, null=True)
    item_linkexterno = models.CharField(max_length=45, blank=True, null=True)
    item_ativo = models.IntegerField()

    def __str__(self):
        return f'TblItens: {self.item_nome}'

class TblPlaniten(models.Model):
    item = models.ForeignKey('TblItens', models.CASCADE, default='1')
    plan = models.ForeignKey('TblPlano', models.CASCADE, default='1')

    def __str__(self):
        return f'TblPlaniten: {self.item.item_nome} - {self.plan.plan_nome}'

class TblPlano(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_nome = models.CharField(max_length=100, blank=True, null=True)
    plan_valor = models.FloatField(blank=True, null=True)
    plan_ordem = models.IntegerField(unique=True, blank=True, null=True)
    plan_taxaup = models.FloatField(blank=True, null=True)
    plan_taxadown = models.FloatField(blank=True, null=True)
    plan_destacarplano = models.IntegerField()
    plan_textdestaque = models.CharField(max_length=20, blank=True, null=True)
    plan_tipocliente = models.CharField(max_length=20)
    plan_tipolink = models.CharField(max_length=13)
    plan_combo = models.IntegerField()
    plan_icon = models.CharField(max_length=255, blank=True, null=True)
    plan_ativo = models.IntegerField()

    def __str__(self):
        return f'TblPlano: {self.plan_nome}'
