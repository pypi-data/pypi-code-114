from . import UOError
from ._uoerror import _ERROR_MESSAGES, ErrorCodes

_EIO_MSG_DICT = {
    1: "A bad partitioning algorithm exists for this file",
    2: "No such part file",
    3: "Record ID contains unmappable NLS characters",
    4: "Record data contains unmappable NLS characters",
    5: "An IO Error has occured"
}
    
class UOFileError(UOError):
    '''
    This class extends the UOError class.
    This class can provide each error information for each key read while invoking the uopy.File.read_named_fields method.
    
    Attributes:
    response_errors: a list of dictionaries.
    Each item in the list indicates the error information for each key read from the file.
    An example of the content in response_errors is [{0: 'No Error'}, {30001: 'This Record was not found'}].

    id_list: a list of the file keys.
    An example of the content in id_list is ['0111', 'bad_id']
    '''

    def __init__(self, code=..., message=None, obj=None, response_codes=[], status_codes=[], id_list=[]):
        '''
        Initializes a UOFileError class.
        Args:
            code (int): error code
            message (string, optinal): error message
            response_codes (list, optional): a list of response codes returned from the server.
            status_codes (list, optional): a list of status codes returned from the server.
            id_list (list, optional): a list of file fields.
        '''
        self._set_response_codes(response_codes)
        self._set_status_codes(status_codes)
        self._set_id_list(id_list)
        if code == ErrorCodes.UOE_EIO:
            if len(self._status_codes_list) > 0:
                statusCode = self._status_codes_list[0] if self._status_codes_list[0] in _EIO_MSG_DICT else 5
                message = _EIO_MSG_DICT[statusCode]
        super().__init__(code, message, obj)

    def _set_response_codes(self, codes):
        if not codes:
            codes = []
        if type(codes) != list:
            codes = [codes]
        self._response_code_list = codes

    @property
    def response_errors(self):
        ''' A list of errors for each field. Each error contains a code and a message.'''
        '''
        self._response_errors = []
        for idx, response_code in enumerate(self._response_code_list):
            if response_code == ErrorCodes.UOE_EIO:
                status = self._status_codes_list[idx] if self._status_codes_list[idx] in _EIO_MSG_DICT else 5
                err = {response_code: _EIO_MSG_DICT[status]} 
                self._response_errors.append(err)
            else:
                err = {response_code: _ERROR_MESSAGES.get(response_code, 'Unknown Error Code')}
                self._response_errors.append(err)
        '''
        self._response_errors = [{code: _EIO_MSG_DICT[self._status_codes_list[idx] if self._status_codes_list[idx] in _EIO_MSG_DICT else 5]}\
             if code == ErrorCodes.UOE_EIO else {code: _ERROR_MESSAGES.get(code, 'Unknown Error Code')} for idx,code in enumerate(self._response_code_list)]
        return self._response_errors

    def _set_status_codes(self, codes):
        if not codes:
            codes = []
        if type(codes) != list:
            codes = [codes]
        self._status_codes_list = codes

    def _set_id_list(self, ids):
        if not ids:
            self._id_list = []
            return
        if type(ids) != list:
            ids = [ids]
        self._id_list = ids

    @property
    def id_list(self):
        ''' A list of fields. '''
        return self._id_list
