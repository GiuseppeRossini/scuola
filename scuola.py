from openerp import models, fields, api

class ScuolaSezioni(models.Model):
  
    _name="scuola.sezioni"

    name = fields.Char("Sezione", size=64)
    alunni_id = fields.One2many('scuola.alunni', 'sezione_id', string="Alunni")
    numero_alunni = fields.Integer(compute='get_count_alunni')

    def get_count_alunni(self):
	for sez in self:
	    sez.numero_alunni = len(sez.alunni_id)

  
class ScuolaAlunni(models.Model):
    
    _name="scuola.alunni"
  
    name = fields.Char("Studente", size=64)
    birthdate = fields.Date("Data di nascita")
    sezione_id = fields.Many2one('scuola.sezioni', string="Sezione") 
  

class ScuolaInsegnanti(models.Model):
    
    _name="scuola.insegnanti"
  
    name = fields.Char("Insegnante", size=64)
    materia_ids = fields.Many2many('scuola.materie')


class ScuolaMaterie(models.Model):
  
    _name="scuola.materie"
  
    name = fields.Char("Materia", size=64)
    docente_ids = fields.Many2many('scuola.insegnanti')
