from flask import render_template
from flask_login import current_user


def list_hospital(hospital):
    return render_template(
        "hospital.html",
        hospital=hospital,
        title="Lista de pacientes",
        current_user=current_user,
    )


def create_paciente():
    return render_template(
        "create_paciente.html", 
        title="Crear paciente",
        current_user=current_user
    )

def update_paciente(paciente):
    return render_template(
        "update_paciente.html",
        title="Editar paciente",
        paciente=paciente,
        current_user=current_user,
    )
