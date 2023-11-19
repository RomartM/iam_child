import frappe


def on_logout():
    print('test=s')
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = "/desk"
    return 'sds'