# TODO  Maybe unused
def render_address(self, data):
    line1 = []
    if data.get("address", None):
        line1.append(data["address"])
    line2 = []
    if data.get("city", None):
        line2.append(data["city"])
    if data.get("province"):
        line2.append(data["province"])
    if data.get("country", None):
        line2.append(data["country"])
    if data.get("zipcode", None):
        line2.append(data["zipcode"])
    line1 = " ".join(line1)
    line2 = ", ".join(line2)
    return line1, line2


def is_customer(user):
    """
    Check user is valid customer (verified and active)
    """
    customer = getattr(user, "customer", None)
    if not customer:
        return False
    else:
        if not (customer.verified and customer.active):
            return False
        else:
            return True
