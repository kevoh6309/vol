#!/usr/bin/env python3
"""
Login Logs Viewer Script
This script helps you view and analyze login attempts from the command line.
"""

import sys
import os
from datetime import datetime, timedelta
import argparse

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vol.app import app, db, LoginAttempt, User

def view_recent_logs(hours=24, limit=50):
    """View recent login logs"""
    since = datetime.now() - timedelta(hours=hours)
    
    with app.app_context():
        logs = LoginAttempt.query.filter(
            LoginAttempt.timestamp >= since
        ).order_by(LoginAttempt.timestamp.desc()).limit(limit).all()
        
        print(f"\n=== Login Logs (Last {hours} hours) ===\n")
        
        if not logs:
            print("No login attempts found in the specified time period.")
            return
        
        for log in logs:
            status = "✅ SUCCESS" if log.success else "❌ FAILED"
            timestamp = log.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] {status} - {log.email} from {log.ip_address}")
            if not log.success and log.failure_reason:
                print(f"    Failure reason: {log.failure_reason}")
            if log.user_agent:
                print(f"    User-Agent: {log.user_agent[:80]}...")
            print()

def view_failed_attempts(hours=24, limit=20):
    """View failed login attempts"""
    since = datetime.now() - timedelta(hours=hours)
    
    with app.app_context():
        failed_logs = LoginAttempt.query.filter(
            LoginAttempt.success == False,
            LoginAttempt.timestamp >= since
        ).order_by(LoginAttempt.timestamp.desc()).limit(limit).all()
        
        print(f"\n=== Failed Login Attempts (Last {hours} hours) ===\n")
        
        if not failed_logs:
            print("No failed login attempts found in the specified time period.")
            return
        
        for log in failed_logs:
            timestamp = log.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] ❌ FAILED - {log.email} from {log.ip_address}")
            if log.failure_reason:
                print(f"    Reason: {log.failure_reason}")
            print()

def view_suspicious_activity(hours=24):
    """View suspicious activity (multiple failed attempts from same IP)"""
    since = datetime.now() - timedelta(hours=hours)
    
    with app.app_context():
        # Get IPs with multiple failed attempts
        suspicious = db.session.query(
            LoginAttempt.ip_address,
            db.func.count(LoginAttempt.id).label('attempt_count')
        ).filter(
            LoginAttempt.success == False,
            LoginAttempt.timestamp >= since
        ).group_by(LoginAttempt.ip_address).having(
            db.func.count(LoginAttempt.id) >= 3
        ).order_by(db.func.count(LoginAttempt.id).desc()).all()
        
        print(f"\n=== Suspicious Activity (Last {hours} hours) ===\n")
        
        if not suspicious:
            print("No suspicious activity detected.")
            return
        
        for ip, count in suspicious:
            print(f"🚨 IP {ip}: {count} failed attempts")
            
            # Show recent attempts from this IP
            recent_attempts = LoginAttempt.query.filter(
                LoginAttempt.ip_address == ip,
                LoginAttempt.success == False,
                LoginAttempt.timestamp >= since
            ).order_by(LoginAttempt.timestamp.desc()).limit(5).all()
            
            for attempt in recent_attempts:
                timestamp = attempt.timestamp.strftime('%H:%M:%S')
                print(f"    [{timestamp}] {attempt.email} - {attempt.failure_reason}")
            print()

def view_user_activity(email, hours=24):
    """View login activity for a specific user"""
    since = datetime.now() - timedelta(hours=hours)
    
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if not user:
            print(f"User with email {email} not found.")
            return
        
        logs = LoginAttempt.query.filter(
            LoginAttempt.email == email,
            LoginAttempt.timestamp >= since
        ).order_by(LoginAttempt.timestamp.desc()).all()
        
        print(f"\n=== Login Activity for {email} (Last {hours} hours) ===\n")
        print(f"User ID: {user.id}")
        print(f"Username: {user.username}")
        print(f"Premium: {'Yes' if user.is_premium else 'No'}")
        print(f"Active: {'Yes' if user.is_active else 'No'}")
        print()
        
        if not logs:
            print("No login attempts found for this user in the specified time period.")
            return
        
        for log in logs:
            status = "✅ SUCCESS" if log.success else "❌ FAILED"
            timestamp = log.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] {status} from {log.ip_address}")
            if not log.success and log.failure_reason:
                print(f"    Failure reason: {log.failure_reason}")
            print()

def get_statistics(hours=24):
    """Get login statistics"""
    since = datetime.now() - timedelta(hours=hours)
    
    with app.app_context():
        total = LoginAttempt.query.filter(LoginAttempt.timestamp >= since).count()
        successful = LoginAttempt.query.filter(
            LoginAttempt.success == True,
            LoginAttempt.timestamp >= since
        ).count()
        failed = LoginAttempt.query.filter(
            LoginAttempt.success == False,
            LoginAttempt.timestamp >= since
        ).count()
        
        success_rate = (successful / total * 100) if total > 0 else 0
        
        print(f"\n=== Login Statistics (Last {hours} hours) ===\n")
        print(f"Total attempts: {total}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Success rate: {success_rate:.1f}%")
        print()

def main():
    parser = argparse.ArgumentParser(description='View login logs from command line')
    parser.add_argument('--hours', type=int, default=24, help='Hours to look back (default: 24)')
    parser.add_argument('--limit', type=int, default=50, help='Limit number of results (default: 50)')
    parser.add_argument('--failed', action='store_true', help='Show only failed attempts')
    parser.add_argument('--suspicious', action='store_true', help='Show suspicious activity')
    parser.add_argument('--user', type=str, help='Show activity for specific email')
    parser.add_argument('--stats', action='store_true', help='Show statistics')
    
    args = parser.parse_args()
    
    if args.stats:
        get_statistics(args.hours)
    elif args.failed:
        view_failed_attempts(args.hours, args.limit)
    elif args.suspicious:
        view_suspicious_activity(args.hours)
    elif args.user:
        view_user_activity(args.user, args.hours)
    else:
        view_recent_logs(args.hours, args.limit)

if __name__ == '__main__':
    main()