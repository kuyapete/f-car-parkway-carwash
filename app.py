from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# Sample services data
SERVICES = {
    'basic_wash': {
        'name': 'Premium Car Wash',
        'description': 'Exterior wash, tire cleaning, gas cap cleaning,and basic interior vacuum',
        'price': 200.00,
        'duration': 45
    },
    'premium_wash': {
        'name': 'Premium Car Wash with Wax',
        'description': 'Full exterior wash, wax, tire shine, gas cap cleaning, exterior waxing,and interior detailing',
        'price': 500.00,
        'duration': 60
    },
    'full_detailing': {
        'name': 'Full Detailing',
        'description': 'Complete interior and exterior detailing with premium products',
        'price': 7000.00,
        'duration': 2,
        'duration_unit': 'days'
    },
    'interior_only': {
        'name': 'Interior Detailing',
        'description': 'Deep interior cleaning, leather conditioning, and odor removal',
        'price': 3500.00,
        'duration': 1,
        'duration_unit': 'days'
    }
}

# Sample time slots
def generate_time_slots():
    slots = []
    start_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    end_time = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
    
    current = start_time
    while current < end_time:
        slots.append(current.strftime('%H:%M'))
        current += timedelta(minutes=30)
    
    return slots

@app.route('/')
def index():
    """Landing page with hero section and services overview"""
    return render_template('index.html', services=SERVICES)

@app.route('/booking')
def booking():
    """Online booking page"""
    time_slots = generate_time_slots()
    return render_template('booking.html', services=SERVICES, time_slots=time_slots)

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    """Handle booking form submission"""
    try:
        booking_data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'service': request.form['service'],
            'date': request.form['date'],
            'time': request.form['time'],
            'vehicle_type': request.form['vehicle_type'],
            'license_plate': request.form['license_plate'],
            'special_requests': request.form.get('special_requests', ''),
            'timestamp': datetime.now().isoformat()
        }
        
        # In a real application, you would save this to a database
        # For now, we'll just flash a success message and redirect to payment
        
        flash('Booking submitted successfully!', 'success')
        return redirect(url_for('payment', booking_id='temp_booking_id'))
        
    except Exception as e:
        flash('Error submitting booking. Please try again.', 'error')
        return redirect(url_for('booking'))

@app.route('/payment/<booking_id>')
def payment(booking_id):
    """Payment page (under construction)"""
    return render_template('payment.html', booking_id=booking_id)

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
