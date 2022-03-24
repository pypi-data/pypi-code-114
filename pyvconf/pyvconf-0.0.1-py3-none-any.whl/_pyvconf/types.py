"""Types for the pyvconf package."""

# from configparser import SectionProxy

ItemName = str
ItemValue = object
# If we define Items in types.py as SectionProxy, then
# a dict(ConfigParser().items()) will match a Sections type. Once the
# .mypy_cache is updated, we can revert Items to a dict, and the aforementioned
# type check will still pass. Or, we could just ignore the error for now.
# Items = SectionProxy
Items = dict[ItemName, ItemValue]
SectionName = str
Sections = dict[SectionName, Items]

