# -*- coding: utf-8 -*-

import re
class Support:

    @classmethod
    def check_url(cls,url):
        if re.match(r'^https?:/{2}\w.+$', url):
            return True
        else:
            return False


    @classmethod
    def reg_validate_python(cls,content,reg):
        try:
            index = int(reg[reg.rindex("[")+1:-1])
            matchObj = re.search(reg[:reg.rindex(")")].replace("reg(",""), content, re.S)
            if matchObj:
                return matchObj.group(index)
            else:
                return None
        except Exception as a:
            return None