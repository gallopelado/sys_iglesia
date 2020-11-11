from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, json, session,abort
from app.Models.gestionar_cursos.planificacion_examen.PlanificacionExamen_dao import PlanificacionExamen_dao
from app.rutas.gestionar_cursos.planificacion_examen.Formulario import Formulario

ple = Blueprint('planificacion_examen', __name__, template_folder='templates')

@ple.before_request
def before_request():
    if 'username' not in session:
        return redirect(url_for('login.login'))
    elif 'grupo' not in session:
        return redirect(url_for('login.login'))
    elif 'username' in session and 'grupo' in session and session['grupo'] not in ('ADMIN', 'PASTOR'):
        abort(403, description="Acceso prohibido")

@ple.route('/')
def index():
    jusa_dao = PlanificacionExamen_dao()
    data = jusa_dao.getLista()
    return render_template('planificacion_examen/index.html', titulo='Registrar Planificación de exámenes', items = data)

@ple.route('/formulario_planifica_examen/<int:malla_id>/<int:cur_id>/<int:asi_id>/<int:num_id>/<turno>/<int:per_id>')
def formularioPlanificaExamen(malla_id, cur_id, asi_id, num_id, turno, per_id):
    form = Formulario()
    form.malla_id.data = malla_id
    form.cur_id.data = cur_id
    form.asi_id.data = asi_id
    form.num_id.data = num_id
    form.turno.data = turno
    form.turno_h.data = turno
    form.idmaestro.data = per_id
    jusa_dao = PlanificacionExamen_dao()
    data = jusa_dao.getLista()
    examenes = jusa_dao.getListaExamenes(asi_id, num_id)
    examenes.insert(0, { 'exa_id':'', 'exa_nombre':'...' })
    form.examenes.choices = [ (str(item['exa_id']), item['exa_nombre']) for item in examenes ]
    lista_examenes_planificados = jusa_dao.getListaExamenesPlanificados(malla_id, cur_id, asi_id, num_id, turno, per_id)

    # Cargar datos de la cabecera
    for item in data:
        if item['malla_id'] == malla_id and item['cur_id'] == cur_id and item['asi_id'] == asi_id and item['num_id'] == num_id and item['turno'] == turno and item['per_id'] == per_id:
            form.maestro.data = item['docente']
            form.curso.data = item['cur_des']
            form.asignatura.data = f"{item['asi_des']} {item['num_des']}"
            form.turno.data = item['turno']

    return render_template('planificacion_examen/formulario_planifica_examen.html', titulo='Formulario Planificar Examen', form=form, items=lista_examenes_planificados)

@ple.route('/guardar', methods=['POST'])
def guardar():
    form = Formulario()
    jusa_dao = PlanificacionExamen_dao()
    res = jusa_dao.guardar(form.malla_id.data, form.cur_id.data, form.asi_id.data, form.num_id.data, form.turno_h.data, form.idmaestro.data, form.examenes.data, form.fecha.data, form.hora.data, int(session['usu_id']))
    if res==True:
        flash('Se guardó correctemente', 'success')
    else:
        flash(res['mensaje'], 'warning')
    return redirect(url_for('planificacion_examen.formularioPlanificaExamen', malla_id=form.malla_id.data, cur_id=form.cur_id.data, asi_id=form.asi_id.data, num_id=form.num_id.data, turno=form.turno_h.data, per_id=form.idmaestro.data))

@ple.route('/anular_planificacion_examen/<int:planex_id>/<int:malla_id>/<int:cur_id>/<int:asi_id>/<int:num_id>/<turno>/<int:per_id>')
def anularPlanificacionExamen(planex_id, malla_id, cur_id, asi_id, num_id, turno, per_id):
    jusa_dao = PlanificacionExamen_dao()
    res = jusa_dao.anularExamen(planex_id, session['usu_id'])
    if res:
        flash('Se anulo un examen correctemente', 'success')
    else:
        flash('Hubo problemas al procesar', 'warning')
    return redirect(url_for('planificacion_examen.formularioPlanificaExamen', malla_id=malla_id, cur_id=cur_id, asi_id=asi_id, num_id=num_id, turno=turno, per_id=per_id))
