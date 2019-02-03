from trytond.model import (
    ModelView, ModelSQL, fields, Unique, sequence_ordered, tree)
from trytond.pyson import Eval, Bool

STATES = {
    'readonly': ~Eval('active', True),
}
DEPENDS = ['active']


class RoomType(sequence_ordered(), tree(separator='\\'), ModelSQL, ModelView):
    'Room Type Description'
    __name__ = 'hotel.roomtype'

    name = fields.Char('Name', size=None, required=True, states= STATES)
    code = fields.Char('Code', required=True, select=True,
        states={
            'readonly': Eval('code_readonly', True),
            },
        depends=['code_readonly'],
        help="The unique identifier of the party.")
    code_readonly = fields.Function(fields.Boolean('Code Readonly'),
        'get_code_readonly')