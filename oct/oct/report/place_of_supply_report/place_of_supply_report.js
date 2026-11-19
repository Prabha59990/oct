// Copyright (c) 2026, prabha and contributors
// For license information, please see license.txt

frappe.query_reports["Place_Of_Supply_Report"] = {
    filters: [
        {
            fieldname: "customer",
            label: __("Customer"),
            fieldtype: "Link",
            options: "Customer"
        }
    ]
};
