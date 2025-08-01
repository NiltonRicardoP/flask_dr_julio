#!/usr/bin/env python3
from app import app
import os

if __name__ == '__main__':
    # Ensure upload directory exists
    uploads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
        
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)