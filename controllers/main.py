from odoo import http
from odoo.http import request, Response
import json

class APIBackend(http.Controller):
    @http.route('/api/products', type='http', auth='public', methods=['GET'], csrf=False)
    def get_products(self):
        products = request.env['product.template'].sudo().search([])
        product_list = [{
            'name': product.name,
            'price': product.list_price,
            'quantity_available': product.qty_available
        } for product in products]
        
        return Response(json.dumps(product_list), content_type='application/json', status=200)

    @http.route('/api/customers', type='http', auth='public', methods=['GET'], csrf=False)
    def get_customers(self):
        customers = request.env['res.partner'].sudo().search([('customer_rank', '>', 0)])
        customer_list = [{
            'name': customer.name,
            'email': customer.email or 'N/A',
            'phone': customer.phone or 'N/A'
        } for customer in customers]

        return Response(json.dumps(customer_list), content_type='application/json', status=200)