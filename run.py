#!/usr/bin/env python3
"""
CarWash Pro - Simple run script
This script helps you get started quickly with the CarWash Pro application.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def run_app():
    """Run the Flask application"""
    print("Starting CarWash Pro application...")
    try:
        # Set environment variables
        os.environ['FLASK_APP'] = 'app.py'
        os.environ['FLASK_ENV'] = 'development'
        
        # Import and run the app
        from app import app
        print("🚀 CarWash Pro is running!")
        print("📱 Open your browser and go to: http://localhost:5000")
        print("⏹️  Press Ctrl+C to stop the server")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError:
        print("❌ Flask not found. Please install requirements first.")
        return False
    except KeyboardInterrupt:
        print("\n👋 CarWash Pro stopped. Thanks for using our service!")
        return True
    except Exception as e:
        print(f"❌ Error running application: {e}")
        return False

def main():
    """Main function"""
    print("=" * 50)
    print("🚗 CarWash Pro - Premium Car Care Services")
    print("=" * 50)
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found!")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    print("\n" + "=" * 50)
    
    # Run the application
    run_app()

if __name__ == "__main__":
    main()
