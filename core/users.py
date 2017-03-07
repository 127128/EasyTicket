__author__ = "Anto.s"
import json
import datetime
from django.contrib.auth.models import User
from django.db import IntegrityError
from EasyTicket.models import AgentUser, UserData
from utils.response import * 
from utils.validator import DataValidator
from generic.serialize import JsonSerializer
from generic.core import CoreMixin

class HandleUser(CoreMixin):
    
    def __init__(self):
        pass
    
    _val_fields = {'username': {'name': 'User Name', 'type':'alphanumeric', 'pattern': '', 'required': True},
                    'password': {'name': 'Password', 'type':'normal', 'pattern': '', 'required': True },
                    'first_name': {'name': 'First Name', 'type':'alpha', 'pattern': '', 'required': True},
                    'last_name': {'name': 'Last Name', 'type':'alpha', 'pattern': '', 'required': True},
                    'contact': {'name': 'Contact Number', 'type': 'numeric', 'pattern': '', },
                    'address': {'name': 'Address', 'type':'normal', 'pattern': '' },
                    'email': {'name': 'Email', 'type':'normal', 'pattern': '' },
                    'comment': {'name': 'Comments', 'type':'normal', 'pattern': '', },
                    'remarks': {'name': 'Remarks', 'type':'normal', 'pattern': '', },
                    'plan': {'name': 'Plan', 'type':'normal', 'pattern': '', },
                    'dob': {'name': 'Date Of Birth', 'type':'datetime', 'pattern': '', },
                    }

    def _add_authuser(self, request):
        try:
            user = User.objects.create_user(request.get('username'), request.get('email'), request.get('password'))
            user.first_name = request.get('first_name')
            user.last_name = request.get('last_name')
            user.save()
        except IntegrityError as e:
            return get_resp_exception(str(e.__cause__))
        return user

    def _add_agent(self, request, user):
        agent = AgentUser(agent_id= request.get('email'),
                          user= user)
        try:
            agent.save()
        except IntegrityError as e:
            return get_resp_exception(str(e.__cause__))
        return agent

    def create_user(self, request):
        """Creates a user with given details in the request"""
        err, req = self._validate_request(request)
        if err:
            resp = get_resp_error(err)
            return resp

        user = self._add_authuser(req)
        if type(user) == User:
            agent = self._add_agent(req, user)
            return agent
        return user


class HandleCustomer(HandleUser):

    _val_fields = {
                    'first_name': {'name': 'First Name', 'type':'alpha', 'pattern': '', 'required': True},
                    'last_name': {'name': 'Last Name', 'type':'alpha', 'pattern': '', 'required': True},
                    'contact': {'name': 'Contact Number', 'type': 'numeric', 'pattern': '', 'required': True},
                    'address': {'name': 'Address', 'type':'normal', 'pattern': '', 'required': True},
                    'email': {'name': 'Email', 'type':'normal', 'pattern': '',  'required': True},
                    'comment': {'name': 'Comments', 'type':'normal', 'pattern': '', },
                    'remarks': {'name': 'Remarks', 'type':'normal', 'pattern': '', },
                    'plan': {'name': 'Plan', 'type':'normal', 'pattern': '', },
                    'dob': {'name': 'Date Of Birth', 'type':'datetime', 'pattern': '', 'required': True},
                    } 

    def add_customer(self, request):
        """Creates a customer account with the system"""
        err, req = self._validate_request(request)
        if err:
            resp = get_resp_error(err)
            return resp

        cust_data = UserData(first_name = req.get('first_name'))
        cust_data.last_name = req.get('last_name')
        cust_data.contact = req.get('contact')
        cust_data.contact = req.get('address')
        cust_data.contact = req.get('email')
        cust_data.contact = req.get('remarks')
        cust_data.contact = req.get('plan')
        cust_data.contact = req.get('dob')
        cust_data.created_datetime = datetime.datetime.now()
        try:
            cust_data.save()
        except IntegrityError as e:
            raise
            return get_resp_exception(str(e.__cause__))
        return cust_data


    def get_customer(self, **kwargs):
        """get a customer from DB"""
        return UserData.getOrNone(**kwargs)


    def get_all_customers(self, **kwargs):
        """get all customers from DB matching the filters"""
        return UserData.objects.filter(**kwargs)

    def get_user_data(self, contact, **kwargs):
        """
        gets and returns the basic user data if presents
        """
        user_data = UserData.getOrNone(contact= contact)
        if not user_data:
            return ""
        if kwargs.has_key('Json'):
            return JsonSerializer().serialize([user_data])
        elif kwargs.has_key('dict_res'):
            return DataSerializer().serialize([user_data])
        return user_data
