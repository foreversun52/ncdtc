from django.db import models


# Create your models here.
class NoncoRNA(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    journal = models.CharField(max_length=255)
    pub_time = models.CharField(max_length=10)
    pmid = models.CharField(max_length=20)
    database_id = models.CharField(max_length=20)
    ncrna_id = models.CharField(max_length=50)
    ncrna_name = models.CharField(max_length=50)
    ncrna_type = models.CharField(max_length=30)
    drug_id = models.CharField(max_length=200)
    drug_name = models.CharField(max_length=100)
    cancer_type = models.CharField(max_length=100)
    method_ncrna = models.CharField(max_length=100)
    method_drug = models.TextField()
    tissue = models.CharField(max_length=255)
    ncrna_exp_pattern = models.CharField(max_length=255)
    sensitive_or_resistant = models.CharField(max_length=255)
    major_targets = models.CharField(max_length=255)
    target_gene = models.CharField(max_length=255)
    pathway = models.CharField(max_length=255)
    evidence_code = models.CharField(max_length=255)

    class Meta:
        db_table = 'NoncoRNA'

    def __str__(self):
        return self.ncrna_name


class Submit(models.Model):
    ncRNA_Name = models.CharField(max_length=200, null=False)
    ncRNA_ID = models.CharField(max_length=200, null=False)
    Disease = models.CharField(max_length=200, null=False)
    Drug_Name = models.CharField(max_length=200, null=True)
    Drug_ID = models.CharField(max_length=200, null=True)
    Drug_Response = models.CharField(max_length=200, null=True)
    Expression_pattern = models.CharField(max_length=200, null=False)
    PubMed_ID = models.CharField(max_length=200, null=False)
    Email = models.CharField(max_length=200, null=False)
    Description = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = '提交信息表'

    def __str__(self):
        return self.ncRNA_Name
