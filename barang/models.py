from django.db import models


class CategoryBrg(models.Model):
    id_cat =models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class TblBarang(models.Model):
    id_barang = models.AutoField(primary_key=True)
    nama_barang = models.CharField(max_length=100,blank=True, null=True)
    harga_barang = models.CharField(max_length=30, blank=True, null=True)
    category = models.ForeignKey(CategoryBrg, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    code_brg = models.CharField(max_length=20)
    updated_at = models.DateField(auto_now=True)
    status = models.IntegerField(default=1) 
    
    def __str__(self): 
        return self.nama_barang + '' + self.harga_barang