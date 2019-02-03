from trytond.model import (
    ModelView, ModelSQL, fields, Unique, sequence_ordered, tree)
from trytond.pyson import Eval, Bool

STATES = {
    'readonly': ~Eval('active', True),
}
DEPENDS = ['active']


class Room(sequence_ordered(), tree(separator='\\'), ModelSQL, ModelView):
    'Room Description'
    __name__ = 'hotel.room'

    name = fields.Char('Name', size=None, required=True, states=STATES)
    code = fields.Char('Code', required=True, select=True,
        states={
            'readonly': Eval('code_readonly', True),
            },
        depends=['code_readonly'],
        help="The unique identifier of the party.")
    code_readonly = fields.Function(fields.Boolean('Code Readonly'),
        'get_code_readonly')
    hotel = fields.Many2One('hotel.hotel', 'Hotel', required=True,
            ondelete="RESTRICT")
    roomtype = fields.Many2One('hotel.roomtype', 'RoomType', required=True,
            ondelete="RESTRICT")
    smoker = fields.Boolean('Smoker Room', states=STATES)

