from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

from .models import Page
from .settings import pages_settings

# This view is called from SimpelPageFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
# However, we can't just wrap this view; if no matching simpelpage exists,
# or a redirect is required for authentication, the 404 needs to be returned
# without any CSRF checks. Therefore, we only
# CSRF protect the internal implementation.


def simpelpage(request, url=None):
    """
    Public interface to the flat page view.

    Models: `simpel_pages.simpel_pages`
    Templates: Uses the template defined by the ``template_name`` field,
        or :template:`simpel_pages/default.html` if template_name is not defined.
    Context:
        simpelpage
            `simpel_pages.simpel_pages` object
    """

    if url is None:
        url = "/"

    if not url.startswith("/"):
        url = "/" + url

    site_id = get_current_site(request).id
    # f = get_object_or_404(SimpelPage, url=url, sites=site_id)
    try:
        f = get_object_or_404(Page, url=url, sites=site_id)
    except Http404:
        if not url.endswith("/") and settings.APPEND_SLASH:
            url += "/"
            f = get_object_or_404(Page, url=url, sites=site_id)
            return HttpResponsePermanentRedirect("%s/" % request.path)
        else:
            raise
    return render_simpelpage(request, f)


@csrf_protect
def render_simpelpage(request, f):
    """
    Internal interface to the flat page view.
    """
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if f.registration_required and not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login

        return redirect_to_login(request.path)
    if not f.template:
        template = loader.get_template(pages_settings.DEFAULT_TEMPLATE)
    else:
        template = f.template.specific

    # To avoid having to always use the "|safe" filter in simpelpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    f.title = mark_safe(f.title)

    return HttpResponse(
        template.render(
            {
                "object": f,
                "page_title": f.seo_title or f.title,
                "page_description": f.seo_title or f.title,
            },
            request,
        )
    )
