# from django.urls import reverse
# from django.utils.translation import gettext as _
# import pandas as pd
from django_hookup import core as hookup

# from .atomics import SalesOrderAdminIndexSection


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_simpel_sales_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_DEMO_USERS")
def register_simpel_sales_demo_users():
    from .apps import init_demo_users

    init_demo_users()


# def render_salesorder_section(request):
#     from simpel.simpel_sales.models import SalesOrder

#     qs = SalesOrder.objects.get_stats_by_services()
#     if qs.first() is None:
#         return ""
#     stats_df = pd.DataFrame(qs)
#     service = Departments[stats_df["group"].str]
#     stats_df = stats_df.assign(service=service).set_index("service")
#     summary_df = stats_df
#     services_df = stats_df.transpose().to_dict()
#     section = SalesOrderAdminIndexSection(data=services_df, summary=summary_df)
#     ctx = {"request": request}
#     return section.render(context=ctx)


# @hookup.register("REGISTER_ADMIN_APP_SECTION")
# def register_salesorder_index_summary(request):
#     return "index", render_salesorder_section(request)


# @hookup.register("REGISTER_ADMIN_APP_SECTION")
# def register_salesorder_app_summary(request):
#     return "simpel_sales", render_salesorder_section(request)
