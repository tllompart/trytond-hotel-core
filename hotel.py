from trytond.model import (
    ModelView, ModelSQL, fields, Unique, sequence_ordered, tree)
from trytond.pyson import Eval, Bool

STATES = {
    'readonly': ~Eval('active', True),
}
DEPENDS = ['active']


class Hotel(sequence_ordered(), tree(separator='\\'), ModelSQL, ModelView):
    'Hotel Description'
    __name__ = 'hotel.hotel'

    name = fields.Char('Name', size=None, required=True, states=STATES)
    code = fields.Char('Code', required=True, select=True,
                       states={'readonly': Eval('code_readonly', True), },
                       depends=['code_readonly'],
                       help="The unique identifier of the party.")
    code_readonly = fields.Function(fields.Boolean('Code Readonly'),
                                    'get_code_readonly')
    company = fields.Many2One('company.company', 'Company',
                              required=True, ondelete="RESTRICT")
