booked_slots = {}

def check_availability(doctor, slot):
    if slot in booked_slots.get(doctor, []):
        return False
    return True

def book_slot(doctor, slot):
    if doctor not in booked_slots:
        booked_slots[doctor] = []

    booked_slots[doctor].append(slot)
    return True
