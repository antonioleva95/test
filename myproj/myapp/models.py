from django.db import models



class content(models.Model):
    name=models.CharField(max_length=25, verbose_name='наименование')
    description=models.CharField(max_length=300,verbose_name='описание')
    country=models.CharField(default="ru",max_length=20,verbose_name='страна')
    cost=models.IntegerField( default=0 ,verbose_name='цена')
    count=models.IntegerField(verbose_name='количество')
    dod=models.DateField(auto_now=True, verbose_name='дфта создания')
    img=models.ImageField(upload_to="myapp/static/img", blank=True)


    def __str__(self):
        return self.name
    
    def sum(self):
        summ=0
        res = content.objects.all()
        for i in res:
            summ = summ + i.count
        
        

        return summ

#hello world



    







# Create your models here.
