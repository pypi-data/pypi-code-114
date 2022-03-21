from kabaret import flow
from libreflow.baseflow.site import WorkingSite as BaseWorkingSite


class WorkingSite(BaseWorkingSite):

    package_source_dir = flow.Param()
    package_target_dir = flow.Param()
    package_layout_dir = flow.Param()
    package_clean_dir  = flow.Param()
    target_sites       = flow.OrderedStringSetParam()
