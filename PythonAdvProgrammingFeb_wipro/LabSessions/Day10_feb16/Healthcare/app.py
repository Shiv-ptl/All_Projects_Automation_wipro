from flask import Flask, request, jsonify

app = Flask(__name__)


VALID_TOKEN = "testtoken123"


doctors = {}
patients = {}
appointments = {}

doctor_id_counter = 1
patient_id_counter = 1
appointment_id_counter = 1


@app.before_request
def check_auth():
    if request.endpoint == "health":
        return

    auth = request.headers.get("Authorization")

    if not auth or auth != f"Bearer {VALID_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401



@app.route("/health")
def health():
    return {"status": "ok"}



@app.route("/doctors", methods=["POST"])
def create_doctor():
    global doctor_id_counter

    data = request.json

    if data.get("experience", 0) < 0:
        return {"error": "Invalid experience"}, 400

    doctor = {
        "id": doctor_id_counter,
        "name": data["name"],
        "specialization": data["specialization"],
        "experience": data["experience"]
    }

    doctors[doctor_id_counter] = doctor
    doctor_id_counter += 1

    return {"doctor_id": doctor["id"]}, 201



@app.route("/patients", methods=["POST"])
def create_patient():
    global patient_id_counter

    data = request.json

    if data.get("age", 0) < 0:
        return {"error": "Invalid age"}, 400

    if not data.get("email"):
        return {"error": "Email required"}, 400


    for p in patients.values():
        if p["phone"] == data["phone"]:
            return {"error": "Duplicate phone"}, 409

    patient = {
        "id": patient_id_counter,
        "name": data["name"],
        "age": data["age"],
        "email": data["email"],
        "phone": data["phone"]
    }

    patients[patient_id_counter] = patient
    patient_id_counter += 1

    return {"patient_id": patient["id"]}, 201



@app.route("/appointments", methods=["POST"])
def book_appointment():
    global appointment_id_counter

    data = request.json

    if data["doctor_id"] not in doctors:
        return {"error": "Doctor not found"}, 404

    if data["patient_id"] not in patients:
        return {"error": "Patient not found"}, 404


    for appt in appointments.values():
        if (
            appt["doctor_id"] == data["doctor_id"]
            and appt["date"] == data["date"]
            and appt["time"] == data["time"]
            and appt["status"] == "CONFIRMED"
        ):
            return {"error": "Slot already booked"}, 409

    appt = {
        "id": appointment_id_counter,
        "patient_id": data["patient_id"],
        "doctor_id": data["doctor_id"],
        "date": data["date"],
        "time": data["time"],
        "status": "CONFIRMED"
    }

    appointments[appointment_id_counter] = appt
    appointment_id_counter += 1

    return {"appointment_id": appt["id"]}, 201


@app.route("/appointments/<int:id>", methods=["GET"])
def get_appointment(id):
    appt = appointments.get(id)

    if not appt:
        return {"error": "Not found"}, 404

    return appt, 200



@app.route("/appointments/<int:id>", methods=["PUT"])
def reschedule(id):
    appt = appointments.get(id)

    if not appt:
        return {"error": "Not found"}, 404

    data = request.json


    for other in appointments.values():
        if (
            other["doctor_id"] == appt["doctor_id"]
            and other["date"] == data["date"]
            and other["time"] == data["time"]
            and other["status"] == "CONFIRMED"
        ):
            return {"error": "Slot already booked"}, 409

    appt["date"] = data["date"]
    appt["time"] = data["time"]

    return {"message": "Rescheduled"}, 200



@app.route("/appointments/<int:id>", methods=["DELETE"])
def cancel(id):
    appt = appointments.get(id)

    if not appt:
        return {"error": "Not found"}, 404

    if appt["status"] == "CANCELLED":
        return {"error": "Already cancelled"}, 410

    appt["status"] = "CANCELLED"

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
