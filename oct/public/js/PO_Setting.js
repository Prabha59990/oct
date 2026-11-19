frappe.ui.form.on("Purchase Order", {
supplier: function(frm) {
		frm.set_value('custom_testing', frm.doc.supplier);
	},

});