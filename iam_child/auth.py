import frappe


def validate():
    user = frappe.session
    print(user)
