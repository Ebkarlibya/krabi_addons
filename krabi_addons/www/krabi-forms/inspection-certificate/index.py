import frappe


def get_context(ctx):
    ctx.no_cache = 1

    is_name = frappe.request.args['name']
    is_orm = frappe.get_doc("Inspection Certificate", is_name)
    ctx['is_orm'] = is_orm
