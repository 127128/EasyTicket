__author__ = "Anto.s"

from django.db.models import Model

class GModel(Model):
    @classmethod
    def getOrNone(cls, **kwargs):
        """
        A generic method to get object, If not returns None
        cls: class object that is given by @classmethod decorator
        """
        try:
            return cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None


    class Meta:
        abstract = True

