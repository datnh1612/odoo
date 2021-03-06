# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.multi
    def _post_add_create(self):
        """ Overrides behaviour when the attachment is created through the controller
        """
        super(IrAttachment, self)._post_add_create()
        for record in self:
            record.register_as_main_attachment()

    def register_as_main_attachment(self):
        """ Registers this attachment as the main one of the model it is
        attached to.
        """
        self.ensure_one()
        related_record = self.env[self.res_model].browse(self.res_id)
        # message_main_attachment_id field can be empty, that's why we compare to False;
        # we are just checking that it exists on the model before writing it
        if hasattr(related_record, 'message_main_attachment_id'):
            related_record.message_main_attachment_id = self
