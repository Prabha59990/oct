// Copyright (c) 2026, prabha and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Material Transfer", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Material Transfer", {
	item: function(frm) {
		frm.set_value('description', frm.doc.item);
	},

    refresh(frm) {
        frm.add_custom_button("Do Something", function() {
            alert("Hello from client script");
        });
    }

});
