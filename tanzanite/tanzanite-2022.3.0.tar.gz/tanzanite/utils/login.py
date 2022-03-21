"""
Based in part on https://github.com/gautamkrishnar/socli

Copyright (c) 2017, Gautam krishna.R
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of socli nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


"""
import os

from datetime import datetime
from functools import wraps
from http.cookiejar import LWPCookieJar


def login_required(func, cookies_file_path=None):
    """
    :desc: decorator method to check user's login status
    """
    if cookies_file_path is None:
        raise RuntimeError('[-] cookies_file_path must not be None')

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        :desc: Wrapper to check if user is logged in, if the
               stored cookies contain cookie named `acct`
               and is not expired.
        """

        is_login = False
        resp = {'success': False, 'message': 'You are not logged in!'}
        if os.path.exists(cookies_file_path):
            cookiejar = LWPCookieJar(filename=cookies_file_path)
            cookiejar.load()
            for cookie in cookiejar:
                if cookie.name == 'acct':
                    expiry_time_obj = datetime.utcfromtimestamp(cookie.expires)
                    if datetime.now() > expiry_time_obj:
                        is_login = True
            if not is_login:
                os.remove(cookies_file_path)
            else:
                return func(*args, **kwargs)
        return resp
    return wrapper


# vim: set ts=4 sw=4 tw=0 et :
