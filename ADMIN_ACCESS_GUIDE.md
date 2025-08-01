# 🔐 Admin Access Guide

## 🎯 **Admin Login Information**

### **Admin Credentials:**
- **Username:** `admin`
- **Password:** `admin123456`

## 🔗 **Admin Links**

### **Main Admin Dashboard:**
```
https://your-railway-app.railway.app/admin
```

### **Admin Features Available:**

#### **1. Main Admin Dashboard**
- **URL:** `/admin`
- **Features:**
  - View all users
  - Toggle premium status for users
  - Delete users
  - View maintenance mode status
  - Access to all admin controls

#### **2. Login Logs & Security Monitoring**
- **URL:** `/admin/login-logs`
- **Features:**
  - View all login attempts
  - Monitor suspicious activity
  - Filter by success/failure
  - Filter by email, IP address, date
  - Security analytics and statistics

#### **3. Maintenance Mode Controls**
- **Enable Maintenance:** `/admin/enable-maintenance` (POST)
- **Disable Maintenance:** `/admin/disable-maintenance`
- **Features:**
  - Enable/disable maintenance mode
  - Customize maintenance message
  - Set estimated completion time
  - Monitor maintenance status

#### **4. User Management**
- **Toggle Premium:** `/admin/toggle-premium/<user_id>` (POST)
- **Delete User:** `/admin/delete-user/<user_id>` (POST)
- **Features:**
  - Grant/revoke premium access
  - Delete user accounts
  - Manage user permissions

## 🚀 **How to Access Admin Panel**

### **Step 1: Get Your Railway URL**
1. Go to your Railway dashboard
2. Find your project
3. Go to "Settings" tab
4. Copy your "Domain" URL

### **Step 2: Access Admin Panel**
1. Visit: `https://your-railway-app.railway.app/admin`
2. Log in with:
   - **Username:** `admin`
   - **Password:** `admin123456`

### **Step 3: Navigate Admin Features**
1. **Main Dashboard:** View all users and system status
2. **Login Logs:** Monitor security and login attempts
3. **Maintenance Mode:** Control maintenance page
4. **User Management:** Manage user accounts and premium status

## 🛡️ **Admin Security Features**

### **Access Control:**
- ✅ Admin-only access to sensitive routes
- ✅ Session-based authentication
- ✅ CSRF protection on all forms
- ✅ Login attempt logging
- ✅ IP address tracking

### **Security Monitoring:**
- ✅ Real-time login attempt monitoring
- ✅ Suspicious activity detection
- ✅ Failed login tracking
- ✅ User agent logging
- ✅ IP address logging

## 🔧 **Admin Functions**

### **User Management:**
- **View all users** and their details
- **Toggle premium status** for any user
- **Delete user accounts** if needed
- **Monitor user activity** and login patterns

### **System Management:**
- **Enable/disable maintenance mode**
- **Customize maintenance messages**
- **Monitor system health**
- **View security logs**

### **Security Monitoring:**
- **View login attempts** (successful and failed)
- **Monitor suspicious IP addresses**
- **Track user authentication patterns**
- **Analyze security trends**

## 🎯 **Quick Admin Actions**

### **Enable Maintenance Mode:**
1. Go to `/admin`
2. Click "Maintenance Mode" button
3. Fill in maintenance details
4. Click "Enable Maintenance Mode"

### **View Security Logs:**
1. Go to `/admin/login-logs`
2. View recent login attempts
3. Filter by various criteria
4. Monitor for suspicious activity

### **Manage Users:**
1. Go to `/admin`
2. View user list
3. Toggle premium status or delete users
4. Monitor user activity

## 🚨 **Important Security Notes:**

### **Change Default Password:**
- **Immediately change** the admin password after first login
- **Use a strong password** with letters, numbers, and symbols
- **Keep credentials secure** and don't share them

### **Monitor Access:**
- **Regularly check** login logs for suspicious activity
- **Monitor admin access** patterns
- **Review user management** actions

### **Backup Data:**
- **Regular backups** of your database
- **Export user data** if needed
- **Keep configuration** secure

## 📊 **Admin Dashboard Features:**

### **User Overview:**
- Total number of users
- Premium vs free users
- Recent registrations
- User activity status

### **System Status:**
- Maintenance mode status
- Database connection
- Email system status
- Payment system status

### **Security Overview:**
- Recent login attempts
- Failed login patterns
- Suspicious IP addresses
- Security alerts

## 🎉 **Admin Access Ready!**

Your admin panel is fully functional with:
- ✅ **Complete user management**
- ✅ **Security monitoring**
- ✅ **Maintenance mode controls**
- ✅ **System health monitoring**
- ✅ **Payment system management**

**Access your admin panel at:** `https://your-railway-app.railway.app/admin`

**Login with:** `admin` / `admin123456`

---

**Remember to change the default admin password for security!**