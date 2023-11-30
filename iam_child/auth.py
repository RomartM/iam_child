import frappe
from iam_child.conditions import has_system_access
from iam_child.exceptions import SystemAccessError


def validate():
    user = frappe.session.user
    exempted_roles = ['System Manager']
    user_roles = frappe.get_roles(user)

    exempted_found = any(role in user_roles for role in exempted_roles)

    query_string = str(frappe.request.query_string)
    path = str(frappe.request.path)

    if user == 'Guest':
        return

    if '/login' in path:
        return

    if '/api/method/' in path:
        return

    if 'cmd=web_logout' in query_string:
        return

    if 'cmd=logout' in query_string:
        return

    if not exempted_found and not has_system_access(user):
        raise SystemAccessError
