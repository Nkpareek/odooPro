from odoo import models, fields, api
import secrets

class MyConnector(models.Model):
    _name = 'my.connector'
    _description = 'My Connector Model'

    name = fields.Char(string='Name', required=True)
    
    api_key = fields.Char(string='API Key', readonly=True)
    db_name = fields.Char(string='Database Name', readonly=True)
    user_name = fields.Char(string='User Name', readonly=True)
    @api.model
    def create(self, vals):
        if 'api_key' not in vals:
            vals['api_key'] =self.env['res.users.apikeys']._generate("","MMCKey")
        if 'db_name' not in vals:
            vals['db_name'] = self.env.cr.dbname
        if 'user_name' not in vals:
            vals['user_name'] = self.env.user.login
        return super(MyConnector, self).create(vals)
    
    def connect_to_mmc_api(self,vals):
        for record in self:
            record.api_key = self.env['res.users.apikeys']._generate("",'MMCKeyX')