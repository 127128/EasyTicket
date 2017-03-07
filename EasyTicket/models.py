
from django.db import models
from generic.models import GModel #generic Model
from django.contrib.auth.models import User

class BaseData(GModel):
    id = models.CharField(max_length=20, primary_key=True)
    plan = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    email = models.TextField(max_length=20)
    comment = models.TextField(max_length=20) 
    category = models.CharField(max_length=20)
    status = models.CharField(max_length=20)


class AgentUser(GModel):
    """
    Extended User model for Agents
    """
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    agent_id = models.CharField(max_length=20)

    def natural_key(self):
        return self.agent_id

class UserData(GModel):
    """It contains the data for the user who connected with 
       the system
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    plan = models.CharField(max_length=20) #can be changed later to plan table
    contact = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_datetime = models.DateTimeField()
    remarks = models.CharField(max_length=20)

    def __unicode__(self):
        return self.first_name

class Ticket(GModel):
    """
    The Tickets that are raised will be schedulded here
    """
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    raised_by  = models.ForeignKey(UserData)
    description = models.TextField()
    assigned_to = models.ForeignKey(AgentUser, blank= True, null= True)

    def __unicode__(self):
        return self.description

class Comments(GModel):
    """
    Any comments can be entered here and
    linked to it's place
    """
    id = models.AutoField(primary_key=True)
    comments = models.TextField()
    created_datetime =  models.DateTimeField()
    last_updated = models.DateTimeField()
    author = models.ForeignKey(UserData)
    related_article= models.ForeignKey(Ticket)

    def __unicode__(self):
        return self.comments
