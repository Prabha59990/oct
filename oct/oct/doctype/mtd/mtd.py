# Copyright (c) 2026, prabha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MTD(Document):

    def validate(self):
  	  if self.qty is None or self.qty <= 0:
            frappe.throw("Quantity must be greater than zero")


	# def validate(self):
    #     for row in self.material:
    #         if row.qty <= 0:
    #             frappe.throw(
    #                 "Quantity must be greater than zero for item "
    #             )

# def before_insert(self):
#     if self.qty == 0:
#         frappe.throw(
#             "Quantity must be greater than zero for item "
# 	        )