from openerp.osv import osv, fields

class scuola_sezioni(osv.Model):
  _name="scuola.sezioni"
  _columns={
  'name': fields.char('Sezione', size=64),
  #'alunni_id': fields.many2one('scuola.alunni','Alunni'),
  }
class scuola_alunni(osv.Model):
  _name="scuola.alunni"
  _inherits={
    'scuola.sezioni':'sezione_id',
  }
  _columns={
  'name': fields.char('Studente', size=64),
  'birthdate': fields.date('Data di nascita'),
  'sezione_id': fields.many2one('scuola.sezioni','Sezione'),
  }
class scuola_insegnanti(osv.Model):
  _name="scuola.insegnanti"
  _inherits={
    'scuola.materie':'area_id',
  }
  _columns={
  'name': fields.char('Insegnante', size=64),
  #'area': fields.selection([('1', 'italiano'), ('2', 'matematica'), ('3', 'inglese')], string='Materia', required=True,),
  'area_id': fields.many2one('scuola.materie', 'Materia'),
  }
class scuola_materie(osv.Model):
  _name="scuola.materie"
  _columns={
  'name': fields.char('Materia', size=64),
  }
