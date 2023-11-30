import frappe


def has_system_access(user_name):
    _iam_settings = frappe.get_single("IAM Settings")
    user_roles = frappe.get_roles(user_name)

    user_specific_condition = bool(frappe.db.exists("Smart System Item", {
        "parent": user_name,
        "smart_system": _iam_settings.system_name_identity
    }))

    group_specific_condition = bool(frappe.db.exists("Smart System Role Item", {
        "parent": ["in", user_roles],
        "smart_system": _iam_settings.system_name_identity
    }))

    return user_specific_condition or group_specific_condition


def has_unit_access(user_name, unit_name):
    _iam_settings = frappe.get_single("IAM Settings")
    user_roles = frappe.get_roles(user_name)

    user_specific_condition = bool(frappe.db.exists("Smart System Item", {
        "parent": user_name,
        "smart_system": _iam_settings.system_name_identity,
        "units": unit_name
    }))

    group_specific_condition = bool(frappe.db.exists("Smart System Role Item", {
        "parent": ["in", user_roles],
        "smart_system": _iam_settings.system_name_identity
    }))

    return user_specific_condition or group_specific_condition


