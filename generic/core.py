__author__ = "Anto.s"

import json
from utils.response import get_resp_invalid
from utils.validator import DataValidator

class CoreMixin(object):
    
    def _validate_request(self, request):
        """validates the request format"""
        try:
            req = json.loads(request)
        except:
            return get_resp_invalid(), ''
        err = ''
        for field in self._val_fields:
	    import pdb; pdb.set_trace()
            err+= DataValidator(self._val_fields[field]).validate(req.get(field))
        return err, req
