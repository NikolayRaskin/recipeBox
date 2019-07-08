from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.country


class PostBase(models.Model):
    class Meta:
        abstract = True
        
    SPAM = 'S'
    NOT_MODERATED = 'N'
    POST_MODERATED = 'P'
    MODERATED = 'M'
    MODERATION_CHOICES = (
        (SPAM, 'SPAM'),
        (NOT_MODERATED, 'Not Moderated'),
        (POST_MODERATED, 'Post Moderated'),
        (MODERATED, 'Moderated')
    )
    LEVEL_CHOICES = (
        ('L1', 'Уровень 1'),
        ('L2', 'Уровень 2'),
        ('L3', 'Уровень 3'),
    )
 
    author = models.ForeignKey(User, verbose_name=_("Автор"),on_delete=models.PROTECT)
    title = models.CharField(_('Заголовок'),max_length=100)
    slug = models.SlugField()
    ingredients = models.TextField(_('Ингредиенты'))
    cookingDescription = models.TextField(_('Рецепт'))
    cookingDifficulty = models.CharField(_('Уровень сложности'),choices=LEVEL_CHOICES,max_length=100)
    preparationTime = models.IntegerField(_('Время изготовления'))
    img = models.ImageField(_('Изображение'),upload_to='recipes/static/recipes/img/')
    country = models.ForeignKey(Country,on_delete=models.PROTECT)
    pub_date = models.DateTimeField(_('Дата публикации'), blank=True, null=True,auto_now=True)
    moderation = models.CharField(
        _('Модерация'),
        max_length=1,
        choices=MODERATION_CHOICES,
        default=NOT_MODERATED
    )

class MeatDish(PostBase):
    class Meta:
        db_table = "MeatDish"
    MEAT_CHOICES = (
        ('CHICKEN','Курица'),
        ('COW','Говядина'),
        ('PIG','Свинина'),
        ('RAM','Баранина'),
        ('VEAL','Телятина'),
        ('TURTLE','Черепаха'),
    )
    kindOfMeat = models.CharField(choices=MEAT_CHOICES,max_length=100)
        
    def __str__(self):
        return self.title

class FishDish(PostBase):
    class Meta:
        db_table = "FishDish"
    
    kindOfFish = models.CharField(max_length=100)
        
    def __str__(self):
        return self.title

class VeganDish(models.Model):
    class Meta:
        db_table = "VeganDish"
    def __str__(self):
        return self.title