from requests.packages.urllib3.fields import RequestField
from requests.packages.urllib3.filepost import encode_multipart_formdata


def encode_multipart(params: dict):
    new_fields = []

    for key, value in params.items():
        if value is None:
            continue

        if hasattr(value, "read"):
            filename = "data"
            if hasattr(value, "name"):
                filename = str(value.name)

            fdata = value.read()
            rf = RequestField(name=key, data=fdata, filename=filename)
            rf.make_multipart(content_type="application/octet-stream")
            new_fields.append(rf)
        else:
            if not isinstance(value, bytes):
                value = str(value)

            key = key.decode("utf-8") if isinstance(key, bytes) else key
            value = value.encode("utf-8") if isinstance(value, str) else value

            new_fields.append((key, value))

    return encode_multipart_formdata(new_fields)
