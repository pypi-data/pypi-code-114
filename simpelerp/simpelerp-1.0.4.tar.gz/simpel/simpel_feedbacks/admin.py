from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_comments_xtd.admin import XtdCommentsAdmin

from .models import UserComment, UserFeedback, UserFlag, UserRating


class UserFlagAdmin(admin.ModelAdmin):
    pass


class UserRatingAdmin(admin.ModelAdmin):
    pass


class UserFeedbackAdmin(admin.ModelAdmin):
    pass


class UserCommentAdmin(XtdCommentsAdmin):
    list_display = (
        "submit_date",
        # "title",
        # "cid",
        "name",
        # "content_type",
        # "object_pk",
        "followup",
        "is_public",
        "is_removed",
    )
    list_display_links = (
        "submit_date",
        # "title",
    )
    list_filter = ("is_public", "is_removed", "followup")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "content_type",
                    "object_pk",
                    "site",
                ),
            },
        ),
        (
            _("Content"),
            {
                "fields": (
                    # "title",
                    "user",
                    "user_name",
                    "user_email",
                    "user_url",
                    "comment",
                    "followup",
                ),
            },
        ),
        (
            _("Metadata"),
            {
                "fields": (
                    "submit_date",
                    "ip_address",
                    "is_public",
                    "is_removed",
                ),
            },
        ),
    )


admin.site.register(UserFlag, UserFlagAdmin)
admin.site.register(UserRating, UserRatingAdmin)
admin.site.register(UserFeedback, UserFeedbackAdmin)
admin.site.register(UserComment, UserCommentAdmin)
