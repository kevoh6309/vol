# Login Logging and Security Monitoring Guide

This guide explains how to use the enhanced login logging system to monitor user authentication and troubleshoot login issues.

## Overview

The application now includes comprehensive login logging that tracks:
- ✅ Successful login attempts
- ❌ Failed login attempts  
- 🔍 User details and IP addresses
- 🛡️ Suspicious activity detection
- 📊 Login statistics and analytics

## What Gets Logged

### Successful Logins
- User ID and email
- IP address
- User agent (browser/device info)
- Timestamp
- Remember me preference
- User details (premium status, account age, etc.)

### Failed Logins
- Email address attempted
- IP address
- User agent
- Timestamp
- Failure reason (invalid password, user not found, etc.)
- User ID (if user exists)

### Security Events
- Multiple failed attempts from same IP
- Suspicious activity patterns
- Account lockout attempts

## How to View Login Logs

### 1. Web Interface (Admin Dashboard)

**Access:** `/admin/login-logs` (Admin users only)

**Features:**
- Real-time login attempt monitoring
- Filter by success/failure, email, IP, date range
- Suspicious activity alerts
- Pagination for large datasets
- Auto-refresh every 30 seconds

**Steps:**
1. Login as an admin user
2. Go to Admin Dashboard
3. Click "View Login Logs" button
4. Use filters to narrow down results

### 2. Command Line Tool

**Script:** `scripts/view_login_logs.py`

**Usage Examples:**

```bash
# View recent login attempts (last 24 hours)
python scripts/view_login_logs.py

# View only failed attempts
python scripts/view_login_logs.py --failed

# View suspicious activity
python scripts/view_login_logs.py --suspicious

# View statistics
python scripts/view_login_logs.py --stats

# View activity for specific user
python scripts/view_login_logs.py --user user@example.com

# Custom time range (last 48 hours)
python scripts/view_login_logs.py --hours 48

# Limit results
python scripts/view_login_logs.py --limit 20
```

### 3. Application Logs

**Location:** Application logs (stdout/stderr)

**Log Levels:**
- `INFO`: Successful logins and general info
- `WARNING`: Failed login attempts
- `ERROR`: System errors

**Example log entries:**
```
2025-07-31 10:42:46,361 INFO: SUCCESSFUL LOGIN: User 123 (user@example.com) logged in from 192.168.1.100
2025-07-31 10:42:47,352 WARNING: FAILED LOGIN: Invalid password for existing user 123 (user@example.com) from 192.168.1.100
```

## Database Schema

### LoginAttempt Table

```sql
CREATE TABLE login_attempt (
    id INTEGER PRIMARY KEY,
    email VARCHAR(150) NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    user_agent TEXT,
    success BOOLEAN NOT NULL,
    user_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    remember_me BOOLEAN DEFAULT FALSE,
    failure_reason VARCHAR(100)
);
```

**Fields:**
- `email`: Email address used in login attempt
- `ip_address`: IP address of the client (IPv6 compatible)
- `user_agent`: Browser/device information
- `success`: Whether login was successful
- `user_id`: User ID (NULL for failed attempts with non-existent users)
- `timestamp`: When the attempt occurred
- `remember_me`: Whether "remember me" was checked
- `failure_reason`: Reason for failure (invalid_password, user_not_found, etc.)

## Troubleshooting Common Issues

### 1. User Can't Login

**Check these logs:**
```bash
# View recent failed attempts
python scripts/view_login_logs.py --failed --hours 1

# Check specific user activity
python scripts/view_login_logs.py --user user@example.com --hours 24
```

**Common failure reasons:**
- `invalid_password`: Wrong password entered
- `user_not_found`: Email doesn't exist in system
- `account_disabled`: User account is inactive

### 2. Suspicious Activity

**Check for:**
- Multiple failed attempts from same IP
- Failed attempts with non-existent emails
- Unusual user agents

```bash
# View suspicious activity
python scripts/view_login_logs.py --suspicious

# Check specific IP
python scripts/view_login_logs.py --ip 192.168.1.100
```

### 3. Performance Issues

**Monitor:**
- High volume of login attempts
- Database query performance
- Log file size

```bash
# Get statistics
python scripts/view_login_logs.py --stats --hours 24
```

## Security Best Practices

### 1. Regular Monitoring
- Check logs daily for suspicious activity
- Monitor failed login patterns
- Review IP addresses making multiple attempts

### 2. Rate Limiting
The application includes rate limiting:
- 5 login attempts per minute per IP
- Automatic blocking of suspicious IPs
- Progressive delays for repeated failures

### 3. Data Retention
- Login logs are kept indefinitely (consider cleanup for old data)
- Sensitive data is not logged (passwords, etc.)
- IP addresses are logged for security purposes

## Admin Commands

### Database Maintenance

```bash
# Clean old login logs (older than 30 days)
python -c "
from vol.app import app, db, LoginAttempt
from datetime import datetime, timedelta
with app.app_context():
    cutoff = datetime.now() - timedelta(days=30)
    deleted = LoginAttempt.query.filter(LoginAttempt.timestamp < cutoff).delete()
    db.session.commit()
    print(f'Deleted {deleted} old login records')
"
```

### Export Logs

```bash
# Export recent logs to CSV
python -c "
import csv
from vol.app import app, db, LoginAttempt
from datetime import datetime, timedelta

with app.app_context():
    since = datetime.now() - timedelta(hours=24)
    logs = LoginAttempt.query.filter(LoginAttempt.timestamp >= since).all()
    
    with open('login_logs.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Email', 'IP', 'Success', 'Failure_Reason', 'User_Agent'])
        for log in logs:
            writer.writerow([log.timestamp, log.email, log.ip_address, log.success, log.failure_reason, log.user_agent])
    
    print(f'Exported {len(logs)} login records to login_logs.csv')
"
```

## Configuration

### Environment Variables

```bash
# Logging level
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR

# Database logging
LOG_LOGIN_ATTEMPTS=true  # Enable/disable database logging
```

### Customization

You can modify the logging behavior by editing:
- `vol/app.py`: Login route and logging functions
- `vol/templates/admin/login_logs.html`: Admin interface
- `scripts/view_login_logs.py`: Command line tool

## Support

If you encounter issues with the login logging system:

1. Check application logs for errors
2. Verify database connectivity
3. Ensure admin privileges for web interface
4. Check file permissions for command line script

## Privacy and Compliance

- Login logs contain personal data (email addresses, IP addresses)
- Ensure compliance with data protection regulations
- Consider data retention policies
- Implement appropriate access controls for admin users

---

**Last Updated:** July 31, 2025  
**Version:** 1.0