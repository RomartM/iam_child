from frappe.frappeclient import FrappeClient


def before_request():
    print('Check if currently login to iam')


def after_request(response, request):
    print('Check if currently login to iam [AFTER]')
