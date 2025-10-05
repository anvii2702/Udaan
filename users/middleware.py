from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class AdminSessionCookieMiddleware(MiddlewareMixin):
    def proocess_request (self ,request):
        if request.path.startswith("/admin/"):
            settings.session_cookie_name=getattr(settings,"ADMIN_SESSION_COOKIE_NAME","admin_sessionid")
        else:
            settings.SESSION_COOKIE_NAME = getattr(settings, "SESSION_COOKIE_NAME", "project_sessionid")

