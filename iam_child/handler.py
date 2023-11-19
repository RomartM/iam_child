import frappe
from iam.callbacks.user import on_logout


@frappe.whitelist(allow_guest=True)
def logout():
    frappe.local.login_manager.logout()
    frappe.db.commit()
    on_logout()


@frappe.whitelist(allow_guest=True)
def web_logout():
    frappe.local.login_manager.logout()
    frappe.db.commit()
    on_logout()
