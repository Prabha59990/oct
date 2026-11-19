
import frappe

@frappe.whitelist()
def get_mtd_records(customer=None, list=None):

    filters = {}

    if customer:
        filters["customer"] = customer.strip()

    if list:
        filters["list"] = list.strip()

    mtd_records = frappe.get_all(
        "MTD",
        filters=filters,
        fields=[
            "name",
            "date",
            "customer",
            "list",
            "qty"
        ],
        order_by="creation desc"
    )

    return {
        "status": "success",
        "applied_filters": filters,
        "data": mtd_records
    }

import frappe

@frappe.whitelist()
def get_mtd_items(mtd=None):

    filters = {
        "parenttype": "MTD",
        "parentfield": "material"
    }

    if mtd:
        filters["parent"] = mtd

    items = frappe.get_all(
        "Material",
        filters=filters,
        fields=[
            "amt",
            "material",
            "qty"
        ],
        order_by="material"
    )

    return {
        "status": "success",
        "data": items
    }


@frappe.whitelist()
def get_mtd_details(docname, material):
    """Helper API to get item details from MTD"""
    try:
        po_doc = frappe.get_doc("MTD", docname)
        
        for item in po_doc.material:
            if item.material == material:
                return {
                    "Item Name": item.material,
                    "Quantity": item.qty,
                    "Amount": item.amt,
                    "Customer Quantity": item.customer
                }

        frappe.throw(_("Item {0} not found in MTD {1}").format(material, docname))
        
    except Exception as e:
        frappe.log_error(f"Error getting item details: {str(e)}")
        frappe.throw(_("Error getting item details: {0}").format(str(e)))