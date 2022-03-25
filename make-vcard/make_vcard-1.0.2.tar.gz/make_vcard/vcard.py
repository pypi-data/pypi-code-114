# BEGIN:VCARD
# VERSION:3.0
# N;CHARSET=UTF-8:{n}
# FN;CHARSET=UTF-8:{n}
# TEL;TYPE=CELL:{dh}
# NOTE;CHARSET=UTF-8:{c}
# EMAIL:邮箱地址
# END:VCARD

class Item(object):
    def __init__(self, value, type=None) -> None:
        self.type = type
        self.value = self.__escape(value)

    def __escape(self, v):
        if type(v) == str:
            v = v.replace(";", "\;").replace(
                ":", "\:").replace(".", "\.").replace(",", "\,")
            return v
        return str(v)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return "{}".format(self.value)


class VcardData(object):
    def __init__(self, value, type=None) -> None:
        self.__values = [Item(value, type)]

    def get_value(self):
        return self.__values[0].value

    def get_type(self):
        return self.__values[0].type

    def append(self, data, ty):
        self.__values.append(Item(data, ty))
        return self

    @property
    def values(self):
        return self.__values


class VCARD(object):
    def __init__(self) -> None:
        self.__n = ""
        self.__n_flag = ""
        self.__n_flag2 = ""

        self.__vcard = {}

    def _get_values(self):
        return self.__vcard.values()

    def to_string(self):
        return "BEGIN:VCARD\nVERSION:3.0\n"+"{}".format(self.__n)+"".join(self._get_values())+"END:VCARD\n"

    def set_data(self, **kwds):
        if kwds:
            for k in kwds:
                kf = "_set_{}".format(k.lower())
                if hasattr(self, kf):   # 通过反射执行对应的方法
                    getattr(self, kf)(kwds[k].values)
            n = "{}{}{}".format(self.__n_flag, self.__n, self.__n_flag2)
            self.__n = "N;CHARSET=UTF-8:{};;;\n".format(n)
            self.__n += "FN;CHARSET=UTF-8:{}\n".format(n)
        return self

    def _set_n(self, data):
        self.__n = data[0].value

    def _set_n_a(self, data):
        self.__n_flag = data[0].value
        return self

    def _set_n_d(self, data):
        self.__n_flag2 = data[0].value
        return self

    def _set_fn(self, data):
        self.__fn = data[0].value
        self.__vcard["FN"] = "FN;CHARSET=UTF-8:{}\n".format(self.__fn)
        return self

    def _set_nickname(self, data):
        self.__vcard["NICKNAME"] = "NICKNAME:{}\n".format(data[0].value)
        return self

    def _set_note(self, data):
        self.__vcard["NOTE"] = "NOTE:{}\n".format(data[0].value)
        return self

    def _set_bday(self, data):
        self.__vcard["BDAY"] = "BDAY:{}\n".format(data[0].value)
        return self

    def _set_org(self, data):
        self.__vcard["ORG"] = "ORG:{}\n".format(data[0].value)
        return self

    def _set_title(self, data):
        self.__vcard["TITLE"] = "TITLE:{}\n".format(data[0].value)
        return self

    def _set_items(self, data, key):
        s = ""
        for item in data:
            t = ";{}".format(item.type) if item.type is not None else ""
            s += "{k}{t}:{v}\n".format(k=key, t=t, v=item.value)
        self.__vcard[key] = s
        return self

    def _set_tel(self, data):
        return self._set_items(data, "TEL")

    def _set_email(self, data):
        return self._set_items(data, "EMAIL")

    def _set_url(self, data):
        return self._set_items(data, "URL")

    def _set_adr(self, data):
        return self._set_items(data, "ADR")
