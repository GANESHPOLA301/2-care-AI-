from fastapi import APIRouter

router = APIRouter()

appointments = []

@router.post("/book")
def book_appointment(data: dict):
    appointments.append(data)
    return {
        "message": "Appointment booked",
        "data": data
    }

@router.get("/appointments")
def get_appointments():
    return appointments
