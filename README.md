# CarWash Pro - Premium Car Wash & Detailing Services

A modern, responsive web application for a car wash and detailing business built with Python Flask.

## Features

- **Landing Page**: Beautiful hero section with services overview and customer testimonials
- **Online Booking**: Complete booking system with service selection and scheduling
- **Payment System**: Under construction page with placeholder for future payment integration
- **Responsive Design**: Mobile-first design that works on all devices
- **Modern UI**: Clean, professional interface with Bootstrap 5 and custom CSS

## Services Offered

1. **Basic Car Wash** - $25.00 (30 minutes)
   - Exterior wash, tire cleaning, and basic interior vacuum

2. **Premium Car Wash** - $45.00 (60 minutes)
   - Full exterior wash, wax, tire shine, and interior detailing

3. **Full Detailing** - $120.00 (120 minutes)
   - Complete interior and exterior detailing with premium products

4. **Interior Detailing** - $80.00 (90 minutes)
   - Deep interior cleaning, leather conditioning, and odor removal

## Installation & Setup

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Project Structure

```
Carwash/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation and footer
│   ├── index.html        # Landing page
│   ├── booking.html      # Online booking form
│   ├── payment.html      # Payment page (under construction)
│   ├── about.html        # About us page
│   └── contact.html      # Contact page
└── static/               # Static assets
    ├── css/
    │   └── style.css     # Custom CSS styling
    ├── js/
    │   └── main.js       # JavaScript functionality
    └── images/           # Image assets (placeholder)
```

## Key Features

### Landing Page
- Hero section with call-to-action buttons
- Services overview with pricing
- Customer testimonials
- Why choose us section
- Contact information

### Booking System
- Service selection with detailed descriptions
- Date and time scheduling
- Vehicle information collection
- Real-time booking summary
- Form validation

### Payment Integration
- Currently shows "Under Construction" page
- Placeholder for future payment gateway integration
- Alternative contact methods for payment

### Responsive Design
- Mobile-first approach
- Bootstrap 5 framework
- Custom CSS for enhanced styling
- Smooth animations and transitions

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)

## Future Enhancements

- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] User authentication and accounts
- [ ] Booking management system
- [ ] Email notifications
- [ ] Admin dashboard
- [ ] Mobile app
- [ ] Real-time booking availability
- [ ] Customer reviews and ratings

## Development Notes

- The application is currently set up for development with debug mode enabled
- For production deployment, ensure to:
  - Set a secure secret key
  - Use a production WSGI server (e.g., Gunicorn)
  - Configure proper database integration
  - Set up SSL/HTTPS
  - Implement proper error handling and logging

## Contact

For questions about this project or to request features, please contact the development team.

---

**CarWash Pro** - Professional car care services with modern technology.
