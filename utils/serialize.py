__author__ = "Anto.s"

class DataSerializer(object):

    _type_list = ['json', 'xml', 'python']

    def __init__(self, obj, **kwargs):
        self.obj = obj

    def serialize(self, type):
        _check_type
        


