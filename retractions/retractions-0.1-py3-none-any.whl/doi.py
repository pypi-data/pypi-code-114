from typing import NamedTuple


class DOI(NamedTuple):
    prefix: str
    suffix: str

    def __str__(self):
        return self.to_str()

    def to_str(self):
        return "doi:" + self.to_minimal()

    def to_minimal(self):
        return f"{self.prefix}/{self.suffix}"

    def to_url(self):
        return "https://doi.org/" + self.to_minimal()

    def to_handle(self):
        return "info:doi/" + self.to_minimal()

    @classmethod
    def parse(cls, s: str):
        s = s.strip()
        skip = 0
        if s.startswith("doi:"):
            skip = len("doi:")
        elif s.startswith("http"):
            skip = len("http://doi.org/")
            if s[4] == "s":
                skip += 1
        elif s.startswith("info:doi/"):
            skip = len("info:doi/")
        pref_suf = s[skip:].split("/")
        if len(pref_suf) != 2:
            raise ValueError(f"Could not parse DOI from {pref_suf}")
        return cls(*pref_suf)
