from frappe import _

app_name = "iam_child"
app_title = "Iam Child"
app_publisher = "Kid Mediante"
app_description = "IAM integration for child sites"
app_email = "krmediante27@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/iam_child/css/iam_child.css"
# app_include_js = "/assets/iam_child/js/iam_child.js"

# include js, css files in header of web template
# web_include_css = "/assets/iam_child/css/iam_child.css"
# web_include_js = "/assets/iam_child/js/iam_child.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "iam_child/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "iam_child/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "iam_child.utils.jinja_methods",
#	"filters": "iam_child.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "iam_child.install.before_install"
# after_install = "iam_child.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "iam_child.uninstall.before_uninstall"
# after_uninstall = "iam_child.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "iam_child.utils.before_app_install"
# after_app_install = "iam_child.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "iam_child.utils.before_app_uninstall"
# after_app_uninstall = "iam_child.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "iam_child.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"iam_child.tasks.all"
#	],
#	"daily": [
#		"iam_child.tasks.daily"
#	],
#	"hourly": [
#		"iam_child.tasks.hourly"
#	],
#	"weekly": [
#		"iam_child.tasks.weekly"
#	],
#	"monthly": [
#		"iam_child.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "iam_child.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "frappe.handler.logout": "iam_child.handler.logout",
    "frappe.handler.web_logout": "iam_child.handler.web_logout"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "iam_child.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
before_request = ["iam_child.utils.before_request"]
after_request = ["iam_child.utils.after_request"]

# Job Events
# ----------
# before_job = ["iam_child.utils.before_job"]
# after_job = ["iam_child.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

auth_hooks = [
	"iam_child.auth.validate"
]

website_context = {
    "post_login": [
        {"label": _("My Account"), "url": "https://iam.buksu.edu.ph/dashboard"},
        {"label": _("Log out"), "url": "/?cmd=web_logout"},
    ],
}

fixtures = ["Custom Field"]

on_logout = "iam_child.callbacks.user.on_logout"
