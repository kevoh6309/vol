#!/usr/bin/env python3
"""
Resume Download Issue Diagnostic Script
This script helps identify specific issues with resume downloads.
"""

import sys
import os
import requests
from datetime import datetime

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vol.app import app, db, Resume, User

def check_database_health():
    """Check database connectivity and resume data"""
    print("🔍 Checking Database Health...")
    
    with app.app_context():
        try:
            # Test database connection
            from sqlalchemy import text
            db.session.execute(text('SELECT 1'))
            print("✅ Database connection: OK")
            
            # Check resume table
            resume_count = Resume.query.count()
            print(f"✅ Resume table: {resume_count} resumes found")
            
            # Check user table
            user_count = User.query.count()
            print(f"✅ User table: {user_count} users found")
            
            # Show sample resumes
            if resume_count > 0:
                print("\n📋 Sample Resumes:")
                resumes = Resume.query.limit(3).all()
                for resume in resumes:
                    print(f"   - ID: {resume.id}, Name: '{resume.name}', User: {resume.user_id}")
            
            return True
            
        except Exception as e:
            print(f"❌ Database error: {e}")
            return False

def check_pdf_generation():
    """Test PDF generation functionality"""
    print("\n🔍 Checking PDF Generation...")
    
    with app.app_context():
        try:
            from vol.app import get_weasyprint
            
            HTML = get_weasyprint()
            if HTML is None:
                print("❌ WeasyPrint not available")
                return False
            
            # Test basic PDF generation
            test_html = """
            <!DOCTYPE html>
            <html>
            <head><title>Test</title></head>
            <body><h1>Test PDF Generation</h1></body>
            </html>
            """
            
            pdf = HTML(string=test_html).write_pdf()
            print(f"✅ Basic PDF generation: OK ({len(pdf)} bytes)")
            
            # Test resume template
            resume = Resume.query.first()
            if resume:
                from vol.app import render_template
                
                html = render_template('resume_pdf_modern.html',
                    name=resume.name or 'Test Resume',
                    email=resume.email or 'test@example.com',
                    phone=resume.phone or '123-456-7890',
                    address=resume.address or 'Test Address',
                    linkedin=resume.linkedin or 'https://linkedin.com/in/test',
                    summary=resume.summary or 'Test summary',
                    education=resume.education or 'Test education',
                    experience=resume.experience or 'Test experience',
                    skills=resume.skills or 'Test skills',
                    certifications=resume.certifications or 'Test certifications',
                    languages=resume.languages or 'Test languages'
                )
                
                pdf = HTML(string=html).write_pdf()
                print(f"✅ Resume template PDF: OK ({len(pdf)} bytes)")
            else:
                print("⚠️  No resumes found for template testing")
            
            return True
            
        except Exception as e:
            print(f"❌ PDF generation error: {e}")
            return False

def check_download_route():
    """Test download route functionality"""
    print("\n🔍 Checking Download Route...")
    
    with app.app_context():
        try:
            resume = Resume.query.first()
            if not resume:
                print("⚠️  No resumes found for route testing")
                return False
            
            # Test route exists
            from vol.app import download_resume
            print(f"✅ Download route function: OK")
            print(f"✅ Resume ID {resume.id} available for testing")
            
            return True
            
        except Exception as e:
            print(f"❌ Download route error: {e}")
            return False

def check_application_config():
    """Check application configuration"""
    print("\n🔍 Checking Application Configuration...")
    
    try:
        # Check Flask app
        print(f"✅ Flask app: {app.name}")
        print(f"✅ Environment: {app.config.get('FLASK_ENV', 'unknown')}")
        print(f"✅ Debug mode: {app.config.get('DEBUG', 'unknown')}")
        
        # Check WeasyPrint availability
        from vol.app import get_weasyprint
        HTML = get_weasyprint()
        print(f"✅ WeasyPrint: {'Available' if HTML else 'Not available'}")
        
        # Check python-docx availability
        try:
            from docx import Document
            print("✅ python-docx: Available")
        except ImportError:
            print("⚠️  python-docx: Not available (Word downloads disabled)")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def generate_diagnostic_report():
    """Generate a comprehensive diagnostic report"""
    print("=" * 60)
    print("🔧 RESUME DOWNLOAD DIAGNOSTIC REPORT")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Run all checks
    checks = [
        ("Database Health", check_database_health),
        ("PDF Generation", check_pdf_generation),
        ("Download Route", check_download_route),
        ("Application Config", check_application_config)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} check failed: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 DIAGNOSTIC SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {name}")
    
    print(f"\nOverall: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 All systems are working correctly!")
        print("If you're still having download issues, the problem is likely:")
        print("1. User authentication (not logged in)")
        print("2. Browser-specific issues")
        print("3. Network connectivity problems")
        print("4. Resume ownership issues")
    else:
        print(f"\n⚠️  {total - passed} issue(s) detected:")
        for name, result in results:
            if not result:
                print(f"   - {name} needs attention")
        
        print("\n🔧 Recommended actions:")
        print("1. Check application logs for detailed errors")
        print("2. Verify database connectivity")
        print("3. Ensure all dependencies are installed")
        print("4. Contact support with this diagnostic report")

def main():
    """Main function"""
    print("🔧 Resume Download Diagnostic Tool")
    print("This tool will check your system for common download issues.\n")
    
    try:
        generate_diagnostic_report()
    except Exception as e:
        print(f"\n❌ Diagnostic failed: {e}")
        print("Please check your application setup and try again.")

if __name__ == '__main__':
    main()