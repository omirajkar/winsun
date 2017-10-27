import frappe
from pprint import pprint

def actualizarPreciosBom(doc, method):
    try:
        for item in doc.items:
            bom_list = frappe.db.sql("""SELECT name from tabBOM where item=%s AND is_default = 1""", item.item_code)
            for bomName in bom_list:
               frappe.get_doc("BOM",bomName[0]).update_cost_and_exploded_items()
               frappe.get_doc("BOM",bomName[0]).update_cost()
		


    except Exception, e:
        frappe.throw(e)
		
		
def actualizarPreciosDesdeFacturas():
	try:
		item_list = frappe.db.sql("""SELECT DISTINCT item_code FROM `tabSales Invoice Item` """)
		
		for item in item_list:
			bom_list = frappe.db.sql("""SELECT name from tabBOM where item=%s AND is_default = 1""", item[0])
			
			boms = []
			
			for bomName in bom_list:
				if bomName[0] not in boms:
					boms.append(bomName[0]) 
					#frappe.get_doc("BOM",bomName[0]).update_cost_and_exploded_items()
					frappe.get_doc("BOM",bomName[0]).update_cost()
					pprint (bomName[0])
	
	except Exception, e:
		frappe.throw(e)
		
def actualizarPrecioBom():
	try:
		bom_list = frappe.db.sql("""SELECT name from tabBOM where is_default= 1 """)
		
		boms = []
		
		for bomName in bom_list:
			if bomName[0] not in boms:
				boms.append(bomName[0]) 
				#frappe.get_doc("BOM",bomName[0]).update_cost_and_exploded_items()
				try:
					frappe.get_doc("BOM",bomName[0]).update_cost()
				except Exception, e:
					pprint (bomName[0])
					continue
				#pprint (bomName[0])
	
	except Exception, e:
		frappe.throw(e)