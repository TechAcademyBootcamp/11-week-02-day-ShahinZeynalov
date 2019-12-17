from django.db import models

# Create your models here.
SUBJECT = ((1,'Dram'),
               (2,'Comedy'),
               (3,'Detective'))
class Book(models.Model):
    #relations

    #informations
    title = models.CharField('Basligi',max_length=50)
    author = models.CharField('Muellifi',max_length=50)
    page_count = models.PositiveIntegerField('Sehife')
    price = models.DecimalField('Qiymeti',max_digits = 10, decimal_places = 2,null = True,blank=True)
    cover = models.ImageField('Uz Qabigi',upload_to='books_cover/',null=True,blank=True)
    description = models.TextField('Aciqlama',default='Yaxshi kitabdir.')
    subject = models.IntegerField(choices=SUBJECT,default=1)
    pdf = models.FileField('Uz Qabigi',upload_to='books_pdfs/',null=True,blank=True)

    #moderators
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'my_books'

        verbose_name = 'Kitab'
        verbose_name_plural = 'Kitablar'
        ordering = ('price',)

GOODS = ((0,'Convenience Goods'),
         (1,'Shopping Goods'),
         (2,'Specialty Goods')

)
class Product(models.Model):
    name = models.CharField('Product adi',max_length=125,unique=True)
    description = models.TextField('Aciqlama',max_length=500)
    category = models.IntegerField(choices = GOODS,default = 1)
    picture = models.ImageField('Sekil',upload_to = 'products/images/',null=True,blank=True)
    amount = models.IntegerField('Miqdari',default = 0,null=True,blank=True)
    price = models.DecimalField('Qiymeti',max_digits=5,decimal_places=2,null=True,blank=True,default=0.00)
    production_date=models.DateTimeField('Istehsal_tarixi',auto_now_add=True)
    is_new = models.BooleanField("Veziyyeti",default = False,null=True,blank=True)
    certificate = models.FileField('Sertifikat',upload_to='products/files/',null=True,blank=True)
    rating = models.DecimalField('Rating',max_digits=1,decimal_places=1,null=True,blank=True)
    detailed_view_link = models.URLField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'company_products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering =('name',)






    






