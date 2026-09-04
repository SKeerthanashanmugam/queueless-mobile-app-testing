import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

doctors = [
    {
        "id": "DOC-001",
        "name": "Dr. Meena Raman",
        "specialty": "Cardiology",
        "hospital": "QueueLess Medical Centre"
    },
    {
        "id": "DOC-002",
        "name": "Dr. Arjun Kumar",
        "specialty": "Dermatology",
        "hospital": "City Care Hospital"
    },
    {
        "id": "DOC-003",
        "name": "Dr. Priya Nair",
        "specialty": "Pediatrics",
        "hospital": "Rainbow Hospital"
    }
]

appointments = {}


class QueueLessHandler(BaseHTTPRequestHandler):

    def send_json(self, status_code, data):
        response = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}

        try:
            return json.loads(self.rfile.read(length).decode("utf-8"))
        except json.JSONDecodeError:
            return {}

    def authorized(self):
        return self.headers.get("Authorization", "").startswith("Bearer ")

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/api/health":
            self.send_json(200, {
                "status": "ok",
                "service": "QueueLess API"
            })
            return

        if path == "/api/doctors":
            specialty = query.get("specialty", [""])[0]

            results = [
                doctor for doctor in doctors
                if not specialty
                or doctor["specialty"].lower() == specialty.lower()
            ]

            self.send_json(200, {
                "count": len(results),
                "doctors": results
            })
            return

        if path.startswith("/api/doctors/") and path.endswith("/slots"):
            doctor_id = path.split("/")[3]

            self.send_json(200, {
                "doctor_id": doctor_id,
                "date": "2026-09-05",
                "slots": ["09:00 AM", "10:30 AM", "02:00 PM"]
            })
            return

        if path.startswith("/api/appointments/") and path.endswith("/prescription"):
            if not self.authorized():
                self.send_json(401, {
                    "error": "Unauthorized",
                    "message": "A valid bearer token is required"
                })
                return

            self.send_json(200, {
                "prescription": "No prescription available"
            })
            return

        if path.startswith("/api/appointments/"):
            appointment_id = path.split("/")[3]
            appointment = appointments.get(appointment_id)

            if appointment is None:
                appointment = {
                    "appointment_id": appointment_id,
                    "doctor_id": "DOC-001",
                    "patient_name": "Keerthana S",
                    "slot": "09:00 AM",
                    "status": "confirmed"
                }

            self.send_json(200, appointment)
            return

        self.send_json(404, {
            "error": "Endpoint not found"
        })

    def do_POST(self):
        path = urlparse(self.path).path
        body = self.read_json()

        if path == "/api/auth/otp/request":
            mobile = body.get("mobile", "9629499073")

            self.send_json(200, {
                "message": "OTP sent successfully",
                "mobile": mobile,
                "token": "queueless-test-token"
            })
            return

        if path == "/api/appointments":
            appointment_id = f"APT-{len(appointments) + 1:03d}"

            appointment = {
                "appointment_id": appointment_id,
                "doctor_id": body.get("doctor_id", "DOC-001"),
                "patient_name": body.get("patient_name", "Keerthana S"),
                "slot": body.get("slot", "09:00 AM"),
                "status": "confirmed"
            }

            appointments[appointment_id] = appointment
            self.send_json(201, appointment)
            return

        self.send_json(404, {
            "error": "Endpoint not found"
        })

    def log_message(self, format, *args):
        print(f"API: {format % args}")


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), QueueLessHandler)
    print("QueueLess API running at http://127.0.0.1:8000")
    print("Press Ctrl+C to stop")
    server.serve_forever()