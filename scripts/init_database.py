#!/usr/bin/env python3
"""
Database Initialization Script
This script creates the database tables including the new LoginAttempt table.
"""

import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vol.app import app, db

def init_database():
    """Initialize the database and create all tables"""
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Check if LoginAttempt table exists
        try:
            from vol.app import LoginAttempt
            count = LoginAttempt.query.count()
            print(f"✅ LoginAttempt table exists with {count} records")
        except Exception as e:
            print(f"❌ Error checking LoginAttempt table: {e}")

if __name__ == '__main__':
    init_database()