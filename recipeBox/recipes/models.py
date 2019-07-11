from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


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
 
    author = models.ForeignKey(User, verbose_name=_("Автор"),on_delete=models.PROTECT,null=True)
    title = models.CharField(_('Заголовок'),max_length=100,default=None)
    kindOfDish = models.CharField(_('Категория блюда'),max_length=100,default=None)
    ingredients = models.TextField(_('Ингредиенты'),default='default',null=True)
    instruction = models.TextField(_('Инструкция'),default='default',null=True)
    description = models.TextField(_('Примечание'),default='default',null=True)
    level = models.CharField(_('Уровень сложности'),max_length=100,default=None)
    oursForCooking = models.IntegerField(_('Час(ов)'),default=None)
    minutsForCooking = models.IntegerField(_('Минут(ы)'),default=None)
    #img = models.ImageField(_('Изображение'),upload_to='recipes/static/recipes/img/')
    country = models.CharField(_('Происхождение'),max_length=100,default=None)
    pub_date = models.DateTimeField(_('Дата публикации'), blank=True,null=True,auto_now=True)
    moderation = models.CharField(
        _('Модерация'),
        max_length=1,
        choices=MODERATION_CHOICES,
        default=NOT_MODERATED
    )

class MeatDish(PostBase):
    kindOfMeat = models.CharField(max_length=100,default=None,null=True)
        
    def __str__(self):
        return self.title

class FishDish(PostBase): 
    kindOfFish = models.CharField(max_length=100,default=None,null=True)
        
    def __str__(self):
        return self.title

class VeganDish(PostBase):
    def __str__(self):
        return self.title