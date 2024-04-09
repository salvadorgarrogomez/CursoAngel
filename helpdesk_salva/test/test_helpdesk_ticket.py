from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase

class TestHelpdeskTicket(TransactionCase):
    def setUp(self):
        super (TestHelpdeskTicket, self).setUp()
        self.ticket = self.env['helpdesk.ticket'].create({
            'name': 'test ticket',
        })

    def test_time_can_not_be_negative(self):
        self.ticket.time = 3
        self.assertEqual(self.ticket.time,3)
        with self.assertRaises(ValidationError):
            self.ticket.time = -1
