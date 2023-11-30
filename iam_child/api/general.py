import frappe


@frappe.whitelist(allow_guest=True)
def common():
    _iam_settings = frappe.get_single("IAM Settings")
    return {
        'system_name': _iam_settings.system_name_identity,
    }
