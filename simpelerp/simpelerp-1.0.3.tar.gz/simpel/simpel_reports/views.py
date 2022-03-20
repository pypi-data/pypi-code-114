from django.http.response import HttpResponse

from .forms import EXPORT_WIZARD_TEMPLATES

# def pay_by_credit_card(wizard):
#     """Return true if user opts to pay by credit card"""
#     # Get cleaned data from payment step
#     cleaned_data = wizard.get_cleaned_data_for_step("paytype") or {"method": "none"}
#     # Return true if the user selected credit card
#     return cleaned_data["method"] == "cc"
