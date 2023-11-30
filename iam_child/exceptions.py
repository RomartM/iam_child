import frappe


class SystemAccessError(Exception):
    width = 350
    custom = True
    indicator_color = "red"
    http_status_code = 403
    primary_label = 'Manage IAM Account'
    primary_action = 'https://iam.buksu.edu.ph'

    @property
    def title(self):
        _iam_settings = frappe.get_single("IAM Settings")
        return 'Access Denied: %s' % _iam_settings.system_name_identity

    @property
    def message(self):
        return 'Your account lacks the necessary authorization to access this system. <p>If you think this is an error, please get in touch with the Data Center at local hotline 131.</p>'
