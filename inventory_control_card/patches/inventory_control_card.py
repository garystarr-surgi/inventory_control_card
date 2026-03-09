import frappe
from frappe.utils.background_jobs import enqueue

def execute():
    # Check if the card already exists
    card_name = "Inventory Control - Selling Workspace"
    if frappe.db.exists("Workspace Card", card_name):
        return

    # Create the card
    frappe.get_doc({
        "doctype": "Workspace Card",
        "workspace": "Selling",          # The workspace to add the card to
        "title": "Inventory Control",    # Card label
        "card_type": "Custom",           # Custom card
        "icon": "box",                   # Optional icon
        "roles": ["Inventory Control"],  # Only users with this role see it
        "link_type": "Report",           # Can be DocType, Report, Page, or Custom
        "link_to": "#",                  # Replace with your URL / DocType if needed
    }).insert(ignore_permissions=True)
    frappe.db.commit()
