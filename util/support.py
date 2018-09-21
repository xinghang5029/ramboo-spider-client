# -*- coding: utf-8 -*-

import re
class Support:

    @classmethod
    def check_url(cls,url):
        if re.match(r'^https?:/{2}\w.+$', url):
            return True
        else:
            return False