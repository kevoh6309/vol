#!/usr/bin/env python3
"""
Real-time Login Monitoring Script
This script continuously monitors login attempts and alerts on suspicious activity.
"""

import sys
import os
import time
from datetime import datetime, timedelta

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vol.app import app, db, LoginAttempt

def monitor_logs(check_interval=10):
    """Monitor login logs in real-time"""
    print("🔍 Real-time Login Monitor Started")
    print("Press Ctrl+C to stop monitoring\n")
    
    with app.app_context():
        # Get initial count
        last_count = LoginAttempt.query.count()
        print(f"Initial login attempts: {last_count}")
        
        try:
            while True:
                time.sleep(check_interval)
                
                # Get current count
                current_count = LoginAttempt.query.count()
                
                if current_count > last_count:
                    # New login attempts detected
                    new_attempts = current_count - last_count
                    print(f"\n🚨 {new_attempts} new login attempt(s) detected!")
                    
                    # Get recent attempts
                    recent_attempts = LoginAttempt.query.order_by(
                        LoginAttempt.timestamp.desc()
                    ).limit(new_attempts).all()
                    
                    for attempt in reversed(recent_attempts):  # Show oldest first
                        status = "✅ SUCCESS" if attempt.success else "❌ FAILED"
                        timestamp = attempt.timestamp.strftime('%H:%M:%S')
                        print(f"[{timestamp}] {status} - {attempt.email} from {attempt.ip_address}")
                        
                        if not attempt.success and attempt.failure_reason:
                            print(f"    Reason: {attempt.failure_reason}")
                        
                        # Check for suspicious activity
                        if not attempt.success:
                            # Count failed attempts from this IP in last hour
                            hour_ago = datetime.now() - timedelta(hours=1)
                            failed_count = LoginAttempt.query.filter(
                                LoginAttempt.ip_address == attempt.ip_address,
                                LoginAttempt.success == False,
                                LoginAttempt.timestamp >= hour_ago
                            ).count()
                            
                            if failed_count >= 3:
                                print(f"    ⚠️  WARNING: {failed_count} failed attempts from {attempt.ip_address} in last hour")
                    
                    print()
                    
                    # Update count
                    last_count = current_count
                
                # Show periodic status
                if int(time.time()) % 60 == 0:  # Every minute
                    successful = LoginAttempt.query.filter_by(success=True).count()
                    failed = LoginAttempt.query.filter_by(success=False).count()
                    print(f"📊 Status: {successful} successful, {failed} failed attempts total")
                
        except KeyboardInterrupt:
            print("\n\n🛑 Monitoring stopped by user")
            print("Final statistics:")
            
            total = LoginAttempt.query.count()
            successful = LoginAttempt.query.filter_by(success=True).count()
            failed = LoginAttempt.query.filter_by(success=False).count()
            
            print(f"Total attempts: {total}")
            print(f"Successful: {successful}")
            print(f"Failed: {failed}")
            if total > 0:
                success_rate = (successful / total) * 100
                print(f"Success rate: {success_rate:.1f}%")

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Monitor login logs in real-time')
    parser.add_argument('--interval', type=int, default=10, 
                       help='Check interval in seconds (default: 10)')
    
    args = parser.parse_args()
    
    print("=== Real-time Login Monitor ===")
    print(f"Check interval: {args.interval} seconds")
    print("Monitoring for new login attempts...\n")
    
    monitor_logs(args.interval)

if __name__ == '__main__':
    main()