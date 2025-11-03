from flask import Flask, render_template, abort
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

# Demo in-memory patient data
PATIENTS = [
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'gender': 'Male',
        'created': '2025-01-12',
        'assessments': [
            {
                'id': 'A-1001',
                'date': '2025-02-01',
                'glucose': 92,
                'bmi': 24.7,
                'smoking_status': 'never',
                'stroke_status': 'negative',
            },
            {
                'id': 'A-1014',
                'date': '2025-06-18',
                'glucose': 110,
                'bmi': 25.1,
                'smoking_status': 'former',
                'stroke_status': 'negative',
            },
        ],
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com',
        'gender': 'Female',
        'created': '2025-02-03',
        'assessments': [
            {
                'id': 'B-2003',
                'date': '2025-03-10',
                'glucose': 135,
                'bmi': 29.3,
                'smoking_status': 'never',
                'stroke_status': 'positive',
            },
            {
                'id': 'B-2030',
                'date': '2025-08-22',
                'glucose': 99,
                'bmi': 28.4,
                'smoking_status': 'never',
                'stroke_status': 'negative',
            },
        ],
    },
    {
        'id': 3,
        'name': 'Michael Brown',
        'email': 'michael.brown@example.com',
        'gender': 'Male',
        'created': '2025-03-21',
        'assessments': [
            {
                'id': 'C-3008',
                'date': '2025-04-02',
                'glucose': 120,
                'bmi': 27.0,
                'smoking_status': 'current',
                'stroke_status': 'negative',
            },
        ],
    },
    {
        'id': 4,
        'name': 'Emily Johnson',
        'email': 'emily.johnson@example.com',
        'gender': 'Female',
        'created': '2025-05-07',
        'assessments': [
            {
                'id': 'D-4011',
                'date': '2025-05-30',
                'glucose': 88,
                'bmi': 21.9,
                'smoking_status': 'never',
                'stroke_status': 'negative',
            },
        ],
    },
    {
        'id': 5,
        'name': 'Sam Taylor',
        'email': 'sam.taylor@example.com',
        'gender': 'Non-binary',
        'created': '2025-07-29',
        'assessments': [
            {
                'id': 'E-5005',
                'date': '2025-09-12',
                'glucose': 145,
                'bmi': 31.2,
                'smoking_status': 'former',
                'stroke_status': 'positive',
            },
            {
                'id': 'E-5010',
                'date': '2025-10-20',
                'glucose': 118,
                'bmi': 30.5,
                'smoking_status': 'former',
                'stroke_status': 'negative',
            },
        ],
    },
]

USERS_OVERVIEW=[
    
     {
        "label": "Total users",
        "value": "1,234",
        "description": "Total registered users in the system"
    },
    {
        "label": "Confirmed Users",
        "value": "56",
        "description": "Total users confirmed their accounts"
    },
    {
        "label": "Unconfirmed Users",
        "value": "3,421",
        "description": "Total users pending confirmation"
    }
]

PATIENTS_OVERVIEW=[
    
    {
        "label": "Total Patients",
        "value": "1,234",
        "description": "Registered patients in the system"
    },
    {
        "label": "Total Users",
        "value": "56",
        "description": "Active users managing data"
    },
    {
        "label": "Total Predictions",
        "value": "3,421",
        "description": "Stroke predictions made"
    }
]

@app.route("/")
def login():
    return render_template('pages/auth/login.html')

@app.route("/forgot-password")
def forgot_password():
    return render_template('pages/auth/forgot_password.html')

@app.route("/verify-mfa", methods=['GET', 'POST'])
def verify_mfa():
    return render_template('pages/auth/verify.html')

@app.route("/set_password")
def set_password():
    return render_template('pages/auth/set_password.html')

@app.route("/dashboard")
def dashboard():
    return render_template('pages/dashboard.html')

@app.route("/patient-management")
def patient_management():
    # In a real app, fetch from DB. For now, use demo list.
    return render_template('pages/patient_management.html', patients=PATIENTS, patients_overview=PATIENTS_OVERVIEW)

@app.route("/patient-management/<int:patient_id>")
def patient_info(patient_id: int):
    patient = next((p for p in PATIENTS if p['id'] == patient_id), None)
    if not patient:
        abort(404)
    return render_template('modules/patients/patient_info.html', patient=patient)

@app.route("/patients/new")
def new_patient():
    # Placeholder create form page
    return render_template('pages/patient_new.html', )

@app.route("/users-management")
def users_management():
    return render_template('pages/users_management.html', users_overview=USERS_OVERVIEW)

@app.route("/activity-log")
def activity_log():
    return render_template('pages/activity_log.html')


@app.route("/settings")
def settings():
    return render_template('pages/settings.html')


if __name__=='__main__':
    app.run(debug=True)