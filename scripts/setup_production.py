#!/usr/bin/env python3
"""
Production Setup Script
This script helps set up and verify the production environment.
"""

import sys
import os
import secrets
import string
from datetime import datetime

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vol.app import app, db, User, MaintenanceMode
from werkzeug.security import generate_password_hash

def generate_secret_key(length=32):
    """Generate a secure secret key"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def check_environment_variables():
    """Check if critical environment variables are set"""
    print("🔍 Checking Environment Variables...")
    
    critical_vars = [
        'SECRET_KEY',
        'DATABASE_URL',
        'MAIL_SERVER',
        'MAIL_USERNAME',
        'MAIL_PASSWORD',
        'FLASK_ENV',
        'FLASK_DEBUG'
    ]
    
    missing_vars = []
    for var in critical_vars:
        value = os.getenv(var)
        if value:
            # Mask sensitive values
            if 'PASSWORD' in var or 'SECRET' in var or 'KEY' in var:
                print(f"✅ {var}: {'*' * min(len(value), 8)}...")
            else:
                print(f"✅ {var}: {value}")
        else:
            print(f"❌ {var}: NOT SET")
            missing_vars.append(var)
    
    if missing_vars:
        print(f"\n⚠️  Missing {len(missing_vars)} critical environment variables!")
        print("Please set these in your Railway dashboard:")
        for var in missing_vars:
            print(f"   - {var}")
        return False
    else:
        print("\n✅ All critical environment variables are set!")
        return True

def check_database_setup():
    """Check database setup and create admin user if needed"""
    print("\n🔍 Checking Database Setup...")
    
    with app.app_context():
        try:
            # Test database connection
            from sqlalchemy import text
            db.session.execute(text('SELECT 1'))
            print("✅ Database connection: OK")
            
            # Check required tables
            tables = ['user', 'resume', 'login_attempt', 'maintenance_mode']
            for table in tables:
                try:
                    result = db.session.execute(text(f'SELECT COUNT(*) FROM {table}'))
                    count = result.scalar()
                    print(f"✅ Table '{table}': {count} records")
                except Exception as e:
                    print(f"❌ Table '{table}' error: {e}")
                    return False
            
            # Check for admin user
            admin_user = User.query.filter_by(is_admin=True).first()
            if admin_user:
                print(f"✅ Admin user exists: {admin_user.username} ({admin_user.email})")
            else:
                print("⚠️  No admin user found. Creating one...")
                create_admin_user()
            
            return True
            
        except Exception as e:
            print(f"❌ Database setup failed: {e}")
            return False

def create_admin_user():
    """Create an admin user for maintenance mode control"""
    print("\n👤 Creating Admin User...")
    
    with app.app_context():
        try:
            # Check if admin user already exists
            admin_user = User.query.filter_by(is_admin=True).first()
            if admin_user:
                print("✅ Admin user already exists")
                return admin_user
            
            # Create admin user
            admin_username = os.getenv('ADMIN_USERNAME', 'admin')
            admin_email = os.getenv('ADMIN_EMAIL', 'admin@resumebuilderpro.com')
            admin_password = os.getenv('ADMIN_PASSWORD', 'admin123456')
            
            admin_user = User(
                username=admin_username,
                email=admin_email,
                password_hash=generate_password_hash(admin_password),
                is_admin=True,
                is_premium=True
            )
            
            db.session.add(admin_user)
            db.session.commit()
            
            print(f"✅ Admin user created successfully!")
            print(f"   Username: {admin_username}")
            print(f"   Email: {admin_email}")
            print(f"   Password: {admin_password}")
            print(f"   ⚠️  Please change the password after first login!")
            
            return admin_user
            
        except Exception as e:
            print(f"❌ Failed to create admin user: {e}")
            db.session.rollback()
            return None

def check_security_configuration():
    """Check security configuration"""
    print("\n🔒 Checking Security Configuration...")
    
    # Check Flask environment
    flask_env = os.getenv('FLASK_ENV', 'development')
    flask_debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    if flask_env == 'production' and not flask_debug:
        print("✅ Production mode: Enabled")
        print("✅ Debug mode: Disabled")
    else:
        print("⚠️  Not in production mode!")
        print(f"   FLASK_ENV: {flask_env}")
        print(f"   FLASK_DEBUG: {flask_debug}")
    
    # Check secret key strength
    secret_key = os.getenv('SECRET_KEY', '')
    if len(secret_key) >= 32:
        print("✅ Secret key: Strong (32+ characters)")
    else:
        print("⚠️  Secret key: Weak or missing")
        print("   Generate a new one with: python scripts/setup_production.py --generate-key")
    
    # Check HTTPS configuration
    if os.getenv('SESSION_COOKIE_SECURE', 'False').lower() == 'true':
        print("✅ HTTPS cookies: Enabled")
    else:
        print("⚠️  HTTPS cookies: Disabled (set SESSION_COOKIE_SECURE=True)")

def test_maintenance_mode():
    """Test maintenance mode functionality"""
    print("\n🔧 Testing Maintenance Mode...")
    
    with app.app_context():
        try:
            # Test enabling maintenance mode
            maintenance = MaintenanceMode(
                is_active=True,
                message='Production setup test',
                estimated_completion='In 5 minutes',
                status_message='Testing maintenance mode...',
                started_by=1
            )
            db.session.add(maintenance)
            db.session.commit()
            print("✅ Maintenance mode: Enabled successfully")
            
            # Test disabling maintenance mode
            MaintenanceMode.query.update({'is_active': False})
            db.session.commit()
            print("✅ Maintenance mode: Disabled successfully")
            
            return True
            
        except Exception as e:
            print(f"❌ Maintenance mode test failed: {e}")
            db.session.rollback()
            return False

def generate_environment_template():
    """Generate a template .env file for production"""
    print("\n📝 Generating Environment Template...")
    
    template = f"""# Production Environment Variables
# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

# Flask Configuration
SECRET_KEY={generate_secret_key(32)}
FLASK_ENV=production
FLASK_DEBUG=False

# Database Configuration (Railway auto-sets DATABASE_URL)
# DATABASE_URL=postgresql://username:password@host:port/database_name

# Mail Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Security Configuration
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Lax

# Admin User Configuration
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@yourdomain.com
ADMIN_PASSWORD=change-this-password

# Optional: Rate Limiting (Redis)
# REDIS_URL=redis://localhost:6379/0

# Optional: Stripe Configuration
# STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
# STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key

# Optional: AI Services
# GEMINI_API_KEY=your_gemini_api_key_here
# COHERE_API_KEY=your_cohere_api_key_here
# OPENROUTER_API_KEY=your_openrouter_api_key_here
"""
    
    with open('.env.template', 'w') as f:
        f.write(template)
    
    print("✅ Environment template created: .env.template")
    print("   Copy this to Railway dashboard environment variables")

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Production setup and verification')
    parser.add_argument('--generate-key', action='store_true', help='Generate a new secret key')
    parser.add_argument('--create-admin', action='store_true', help='Create admin user')
    parser.add_argument('--generate-env', action='store_true', help='Generate environment template')
    parser.add_argument('--full-check', action='store_true', help='Run full production check')
    
    args = parser.parse_args()
    
    if args.generate_key:
        print(f"🔑 Generated Secret Key: {generate_secret_key(32)}")
        return
    
    if args.generate_env:
        generate_environment_template()
        return
    
    if args.create_admin:
        create_admin_user()
        return
    
    if args.full_check:
        print("🚀 PRODUCTION SETUP CHECK")
        print("=" * 50)
        
        # Check environment variables
        env_ok = check_environment_variables()
        
        # Check database setup
        db_ok = check_database_setup()
        
        # Check security configuration
        check_security_configuration()
        
        # Test maintenance mode
        maintenance_ok = test_maintenance_mode()
        
        print("\n" + "=" * 50)
        print("📋 PRODUCTION SETUP SUMMARY")
        print("=" * 50)
        
        if env_ok and db_ok and maintenance_ok:
            print("✅ PRODUCTION READY!")
            print("\n🎯 Next Steps:")
            print("1. Set environment variables in Railway dashboard")
            print("2. Test the application thoroughly")
            print("3. Monitor logs and performance")
            print("4. Set up monitoring and alerts")
        else:
            print("❌ PRODUCTION NOT READY!")
            print("\n🚨 Issues to fix:")
            if not env_ok:
                print("- Set missing environment variables")
            if not db_ok:
                print("- Fix database configuration")
            if not maintenance_ok:
                print("- Fix maintenance mode functionality")
        
        return
    
    # Default: show help
    print("🔧 Production Setup Script")
    print("\nUsage:")
    print("  python scripts/setup_production.py --full-check     # Run complete check")
    print("  python scripts/setup_production.py --generate-key   # Generate secret key")
    print("  python scripts/setup_production.py --create-admin   # Create admin user")
    print("  python scripts/setup_production.py --generate-env   # Generate env template")

if __name__ == '__main__':
    main()