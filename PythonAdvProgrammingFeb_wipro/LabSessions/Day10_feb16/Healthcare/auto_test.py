import requests

BASE_URL = "http://127.0.0.1:5000"
TOKEN = "testtoken123"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}



doctor_payload = {
    "name": "Dr. Mehta",
    "specialization": "Cardiologist",
    "experience": 12
}

resp = requests.post(f"{BASE_URL}/doctors", json=doctor_payload, headers=HEADERS)
assert resp.status_code == 201
doctor_id = resp.json()["doctor_id"]
print("Doctor created:", doctor_id)


patient_payload = {
    "name": "Shivanshu",
    "age": 22,
    "email": "shiv@test.com",
    "phone": "9999999999"
}

resp = requests.post(f"{BASE_URL}/patients", json=patient_payload, headers=HEADERS)
assert resp.status_code == 201
patient_id = resp.json()["patient_id"]
print("Patient registered:", patient_id)



appt_payload = {
    "patient_id": patient_id,
    "doctor_id": doctor_id,
    "date": "2026-03-10",
    "time": "10:00"
}

resp = requests.post(f"{BASE_URL}/appointments", json=appt_payload, headers=HEADERS)
assert resp.status_code == 201
appointment_id = resp.json()["appointment_id"]
print("Appointment booked:", appointment_id)



resp = requests.get(f"{BASE_URL}/appointments/{appointment_id}", headers=HEADERS)
assert resp.status_code == 200
print("Appointment details:", resp.json())



update_payload = {
    "date": "2026-03-11",
    "time": "11:00"
}

resp = requests.put(
    f"{BASE_URL}/appointments/{appointment_id}",
    json=update_payload,
    headers=HEADERS
)

assert resp.status_code == 200
print("Appointment rescheduled")



resp = requests.delete(
    f"{BASE_URL}/appointments/{appointment_id}",
    headers=HEADERS
)

assert resp.status_code == 204
print("Appointment cancelled")



resp = requests.delete(
    f"{BASE_URL}/appointments/{appointment_id}",
    headers=HEADERS
)

assert resp.status_code == 410
print("Verified already cancelled")
