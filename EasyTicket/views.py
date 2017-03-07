from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from generic.views import ViewMixin
from core.ticket import TicketDetails
from utils.response import *
def home(request):
    return HttpResponse(django.VERSION)


def get_data(request):
    html = """
    <form method="POST" action="/post_data">
    <input type="text" name="chumma"></input>
    <input type="submit">generate post</input>
    </form>
    """
    return HttpResponse(html)

@csrf_exempt
def post_data(request):
    if request.POST:
        return HttpResponse(json.dumps(request.POST))
    else:
        return HttpResponse("POST data not found")

class BaseData(ViewMixin):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BaseData, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        html = """
        <form method="POST" action="">
        <input type="text" name="contact"></input>
        <input type="submit" value="generate post"></input>
        </form>
        """
        return HttpResponse(html)

    def post(self, request, *args, **kwargs):
        contact = request.POST.get('contact','')
        if contact:
            response = TicketDetails(contact=contact).get_user_data(Json=True)
        else:
            response = get_resp_invalid()
        if not response:
            response = get_resp_notfound()
        return HttpResponse(response)


class CreateUser(ViewMixin):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BaseData, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        html = """
        <form method="POST" action="">
        <input type="text" name="contact"></input>
        <input type="submit" value="generate post"></input>
        </form>
        """
        return HttpResponse(html)

    def post(self, request, *args, **kwargs)

        req = request.POST.get('request','')
        if not req:
            response = get_resp_invalid()
            return HttpResponse(response)
        response = HandleAgent.create_user(req)
        return HttpResponse(response)
