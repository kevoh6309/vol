#!/usr/bin/env python3
"""
Database initialization script
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, Resume, CoverLetter, JobApplication, PracticeSession, Reminder, TeamCV, TeamMember, AffiliateLink

def init_database():
    """Initialize the database with all tables"""
    print("🗄️ Initializing database...")
    
    with app.app_context():
        # Drop all tables to ensure clean slate
        print("🗑️ Dropping existing tables...")
        db.drop_all()
        
        # Create all tables with new schema
        print("🏗️ Creating new tables...")
        db.create_all()
        
        # Verify tables were created
        print("✅ Database initialized successfully!")
        print("📋 Tables created:")
        print("   - User")
        print("   - Resume") 
        print("   - CoverLetter")
        print("   - JobApplication")
        print("   - PracticeSession")
        print("   - Reminder")
        print("   - TeamCV")
        print("   - TeamMember")
        print("   - AffiliateLink")
        
        # Test creating a user with is_admin column
        try:
            test_user = User(
                username='testuser',
                email='test@example.com',
                password_hash='test_hash',
                is_admin=False
            )
            db.session.add(test_user)
            db.session.commit()
            print("✅ Test user created successfully!")
            
            # Verify is_admin column exists
            user = User.query.first()
            if hasattr(user, 'is_admin'):
                print("✅ is_admin column exists and works!")
            else:
                print("❌ is_admin column missing!")
                return False
            
            # Clean up test user
            db.session.delete(test_user)
            db.session.commit()
            print("🧹 Test user cleaned up")
            
        except Exception as e:
            print(f"❌ Error creating test user: {e}")
            return False
    
    print("🎉 Database initialization complete!")
    return True

if __name__ == "__main__":
    success = init_database()
    sys.exit(0 if success else 1) 