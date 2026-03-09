app_name = "inventory_control_card"
app_title = "Inventory Control Card"
app_publisher = "SurgiShop"
app_description = "Create and control Inventory Control Card"
app_email = "gary.starr@surgishop.com"
app_license = "MIT"
required_apps = ["frappe/erpnext"]
required_frappe_version = ">=16.0.0"

# Add patch to execute after app installation
patches = [
    "inventory_control_card.patches.inventory_control_card.execute"
]
