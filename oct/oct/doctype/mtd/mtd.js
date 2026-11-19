// Copyright (c) 2026, prabha and contributors
// For license information, please see license.txt
frappe.ui.form.on("MTD", {
    //Button Practice
    refresh(frm) {
        frm.add_custom_button("TEST BUTTON", function() {

            // Set parent fields
            frm.set_value("date", frappe.datetime.get_today());
            frm.set_value("mtd", "from button");
            frm.set_value("customer", "JDM1");

            // Set fields in the first child row
            let row = (frm.doc.material || [])[0];

            if (row) {
                frappe.model.set_value(
                    row.doctype,
                    row.name,
                    "customer",
                    "JDM1"
                );

                frappe.model.set_value(
                    row.doctype,
                    row.name,
                    "material",
                    "test"
                );
            }

            frm.refresh_field("material");
        });
    },

    //Callout Practice
customer: function(frm) {
		frm.set_value('mtd', frm.doc.customer);
	},

});