# Copyright (c) 2026, prabha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MaterialTransfer(Document):
	  
    def before_save(self):
        frappe.msgprint("before save")