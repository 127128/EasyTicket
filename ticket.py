"""@package docstring
Documentation for this module.
More details.
"""
__author__ = "Anto.s"

from EasyTicket.models import *
from generic.serialize import JsonSerializer
from generic.core import CoreMixin
from utils.response import get_resp_error
from core.users import HandleCustomer 

class TicketDetails(CoreMixin):
    """Class Description Goes here...
    """

    _val_fields = {
                    'category': {'name': 'Category', 'type':'alpha', 'pattern': '', 'required': True},
                    'status': {'name': 'Status', 'type':'alpha', 'pattern': '', 'required': True},
                    'raised_by': {'name': 'Raised By', 'type': 'normal', 'pattern': '', 'required': True},
                    'description': {'name': 'Description', 'type':'normal', 'pattern': '', 'required': True},
                    'assigned_to': {'name': 'Assigned To', 'type':'normal', 'pattern': ''},
                    }

    _open_status_list = ['new', 'open', 'assigned']

    def __init__(self):
        """
        init methot initializes the initial variables
        """
        pass

    def get_latest_ticket(self):
        """
        gets the latest ticket of the given contact
        """
        pass

    def get_open_ticket(self):
        """
        gets and returns if any open tickets are available
        """
	filter = {'status__in': self._open_status_list }

    def get_tickets(self, **kwargs):
	"""get the tickets from db with the given filter
	"""
	try:
	    return Ticket.objects.filter(**kwargs)
	except:
	    raise

    def create_ticket(self, request):
        """Creates a new ticket """
        err, req = self._validate_request(request)
        if err:
            resp = get_resp_error(err)
            return resp

        ticket = Ticket(status = req.get('status'))
        ticket.category = req.get('category')
        ticket.status = 'New'
        user_id = req.get('raised_by').get('id') 
        ticket.raised_by = HandleCustomer().get_customer(id= user_id)
        ticket.save()
        return ticket
