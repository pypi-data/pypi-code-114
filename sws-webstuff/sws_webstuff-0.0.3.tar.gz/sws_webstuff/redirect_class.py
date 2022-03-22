class Redirect:
    def __init__(self, url: str = ""):
        self.redirect_url = url

    def to_dict(self):
        tmp_dict = {
            "redirect_url": self.redirect_url,
        }
        return tmp_dict