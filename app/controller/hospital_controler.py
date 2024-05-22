from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.hospital_model import Hospital
from views import hospital_view
from ultis.decorator import role_required

hospital_bp = Blueprint("hospital", __name__)

@hospital_bp.route("/hospital")
@login_required
def list_hospital():
    hospital = Hospital.get_all()
    return hospital_view.list_hospital(hospital)


@hospital_bp.route("/hospital/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_paciente():
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            birthday = request.form["birtday"]
            paciente = Hospital(name=name,lastname=lastname, ci=int(ci),birthday=birthday)
            paciente.save()
            flash("paciente creado exitosamente", "success")
            return redirect(url_for("hospital.list_hospital"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return hospital_view.create_paciente()


@hospital_bp.route("/hospital/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_paciente(id):
    paciente = Hospital.get_by_id(id)
    if not paciente:
        return "Hospital no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            birthday = request.form["birtday"]
            Hospital.update(name=name, lastname=lastname, ci=ci,birthday=birthday)
            flash("paciente actualizado exitosamente", "success")
            return redirect(url_for("hospital.list_hospital"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return hospital_view.update_paciente(paciente)


@hospital_bp.route("/hospital/<int:id>/delete")
@login_required
@role_required("admin")
def delete_paciente(id):
    paciente = Hospital.get_by_id(id)
    if not paciente:
        return "paciente no encontrado", 404
    if current_user.has_role("admin"):
        paciente.delete()
        flash("paciente eliminado exitosamente", "success")
        return redirect(url_for("hospital.list_hospital"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
