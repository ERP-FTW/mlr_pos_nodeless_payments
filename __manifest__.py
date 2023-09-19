# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS Crypto Payments Nodeless',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 7,
    'summary': 'Integrate your POS with Bitcoin on-chain and lightning payments',
    'description': '',
    'data': [
        'views/pos_payment_method.xml',
    ],
    'depends': ['point_of_sale','mlr_pos_cryptopayments'],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'mlr_pos_nodeless_payments/static/**/*',
            'mlr_pos_nodeless_payments/static/**/**/*',
        ],
    },
    'license': 'LGPL-3',
}
