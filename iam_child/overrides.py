import frappe
from frappe import _
from frappe import app
from frappe.utils import escape_html
from frappe.utils.error import log_error_snapshot
from frappe.website.serve import get_response

def handle_exception_mod(e):
    response = None
    custom = getattr(e, "custom", False)
    title = getattr(e, "title", False)
    message = getattr(e, "message", False)
    indicator_color = getattr(e, "indicator_color", "red")
    width = getattr(e, "width", 640)
    primary_label = getattr(e, "primary_label", '')
    primary_action = getattr(e, "primary_action", '')

    http_status_code = getattr(e, "http_status_code", 500)
    return_as_message = False
    accept_header = frappe.get_request_header("Accept") or ""
    respond_as_json = (
            frappe.get_request_header("Accept")
            and (frappe.local.is_ajax or "application/json" in accept_header)
            or (frappe.local.request.path.startswith("/api/") and not accept_header.startswith("text"))
    )

    allow_traceback = frappe.get_system_settings("allow_error_traceback") if frappe.db else False

    if not frappe.session.user:
        # If session creation fails then user won't be unset. This causes a lot of code that
        # assumes presence of this to fail. Session creation fails => guest or expired login
        # usually.
        frappe.session.user = "Guest"

    if respond_as_json:
        # handle ajax responses first
        # if the request is ajax, send back the trace or error message
        response = frappe.utils.response.report_error(http_status_code)

    elif isinstance(e, frappe.SessionStopped):
        response = frappe.utils.response.handle_session_stopped()

    elif (
            http_status_code == 500
            and (frappe.db and isinstance(e, frappe.db.InternalError))
            and (frappe.db and (frappe.db.is_deadlocked(e) or frappe.db.is_timedout(e)))
    ):
        http_status_code = 508

    elif http_status_code == 401:
        frappe.respond_as_web_page(
            _("Session Expired"),
            _("Your session has expired, please login again to continue."),
            http_status_code=http_status_code,
            indicator_color="red",
        )
        return_as_message = True

    elif http_status_code == 403:
        frappe.respond_as_web_page(
            _("Not Permitted"),
            _("You do not have enough permissions to complete the action"),
            http_status_code=http_status_code,
            indicator_color="red",
        )
        return_as_message = True

    elif http_status_code == 404:
        frappe.respond_as_web_page(
            _("Not Found"),
            _("The resource you are looking for is not available"),
            http_status_code=http_status_code,
            indicator_color="red",
        )
        return_as_message = True

    elif http_status_code == 429:
        response = frappe.rate_limiter.respond()

    else:
        traceback = "<pre>" + escape_html(frappe.get_traceback()) + "</pre>"
        # disable traceback in production if flag is set
        if frappe.local.flags.disable_traceback or not allow_traceback and not frappe.local.dev_server:
            traceback = ""

        frappe.respond_as_web_page(
            "Server Error", traceback, http_status_code=http_status_code, indicator_color="red", width=640
        )
        return_as_message = True

    if custom:

        frappe.respond_as_web_page(
            title=title,
            html=message,
            http_status_code=http_status_code,
            indicator_color=indicator_color,
            width=width,
            primary_label=primary_label,
            primary_action=primary_action
        )
        return_as_message = True

    if e.__class__ == frappe.AuthenticationError:
        if hasattr(frappe.local, "login_manager"):
            frappe.local.login_manager.clear_cookies()

    if http_status_code >= 500:
        log_error_snapshot(e)

    if return_as_message:
        response = get_response("message", http_status_code=http_status_code)

    if frappe.conf.get("developer_mode") and not respond_as_json:
        # don't fail silently for non-json response errors
        print(frappe.get_traceback())

    return response


app.handle_exception = handle_exception_mod
