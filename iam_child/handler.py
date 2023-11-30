import frappe


@frappe.whitelist(allow_guest=True)
def logout_mod():
    frappe.local.login_manager.logout()
    frappe.db.commit()


@frappe.whitelist(allow_guest=True)
def web_logout_mod():
    redirect_to = frappe.local.request.args.get("redirect-to")

    frappe.local.login_manager.logout()
    frappe.db.commit()

    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = redirect_to
