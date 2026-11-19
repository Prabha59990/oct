
# Copyright (c) 2026, prabha and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters or {})
    return columns, data


def get_columns():
    return [
        {
            "label": _("Date"),
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 150,
        },
        {
            "label": _("Customer"),
            "fieldname": "customer",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 180,
        },
        {
            "label": _("List"),
            "fieldname": "list",
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "label": _("Qty"),
            "fieldname": "qty",
            "fieldtype": "Float",
            "width": 100,
        },
    ]


def get_data(filters=None):
    filters = filters or {}
    conditions = get_conditions(filters)

    data = frappe.db.sql(
        """
        SELECT
            d.date AS date,
            d.customer AS customer,
            d.`list` AS `list`,
            d.qty AS qty
        FROM `tabMTD` d
        WHERE
            {conditions}
        ORDER BY d.creation DESC
        """.format(conditions=conditions),
        filters,
        as_dict=True,
    )

    return data


def get_conditions(filters):
    conditions = ["1=1"]

    if filters.get("customer"):
        conditions.append("d.customer = %(customer)s")

    return " AND ".join(conditions)


def execute_snapshot_report(filters: dict | None = None):
    """Return columns and data for the snapshot report."""

    from frappe.database.duckdb.database import get_latest_sync

    filters = filters or {}

    latest_sync = get_latest_sync("MTD Report", filters)

    if latest_sync:
        columns, data = latest_sync
    else:
        columns, data = get_columns(), get_data(filters)

    return columns, data
