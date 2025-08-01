# Maintenance Mode System Guide

## 🛠️ **Overview**

Your application now includes a **comprehensive maintenance mode system** that allows administrators to temporarily put the application into maintenance mode, showing users a professional maintenance page while you perform updates or fixes.

## ✅ **Features**

### **1. Professional Maintenance Page**
- **Beautiful, responsive design** with animations
- **Customizable messages** and estimated completion times
- **Progress indicators** and status updates
- **Auto-refresh** to check when maintenance is complete
- **Social media links** and contact information

### **2. Admin Controls**
- **Easy enable/disable** through admin dashboard
- **Customizable messages** and timing
- **Admin bypass** - administrators can still access the app
- **Audit trail** - tracks who enabled maintenance and when

### **3. Smart User Experience**
- **Automatic detection** of maintenance mode
- **Graceful handling** of all routes
- **Admin bypass** for continued access
- **Real-time status** updates

## 🎯 **How It Works**

### **For Users:**
1. **Normal access** - Users can use the application normally
2. **Maintenance triggered** - Admin enables maintenance mode
3. **Maintenance page** - Users see a professional maintenance page
4. **Auto-refresh** - Page automatically checks if maintenance is complete
5. **Normal access restored** - Users can access the app again

### **For Administrators:**
1. **Access admin dashboard** - Go to `/admin`
2. **Enable maintenance** - Click "Maintenance Mode" button
3. **Customize message** - Set custom message and timing
4. **Perform updates** - Make your changes while users see maintenance page
5. **Disable maintenance** - Click "Disable Maintenance Mode" when done

## 🛠️ **How to Use**

### **1. Enable Maintenance Mode**

**Via Admin Dashboard:**
1. Log in as an administrator
2. Go to `/admin`
3. Click the "Maintenance Mode" button
4. Fill in the form:
   - **Message**: What to tell users (e.g., "We're updating our systems")
   - **Estimated Completion**: When you expect to be done (e.g., "In 30 minutes")
   - **Status Message**: Current status (e.g., "Updating database...")
5. Click "Enable Maintenance Mode"

**Via Command Line:**
```bash
# Check current status
python scripts/test_maintenance_mode.py --status

# Enable maintenance mode (programmatically)
python -c "
from vol.app import app, db, MaintenanceMode
with app.app_context():
    maintenance = MaintenanceMode(
        is_active=True,
        message='Scheduled maintenance in progress',
        estimated_completion='In 1 hour',
        status_message='Updating systems...',
        started_by=1
    )
    db.session.add(maintenance)
    db.session.commit()
    print('Maintenance mode enabled')
"
```

### **2. Disable Maintenance Mode**

**Via Admin Dashboard:**
1. Go to `/admin`
2. Click "Maintenance Mode" button
3. Click "Disable Maintenance Mode"

**Via Command Line:**
```bash
python -c "
from vol.app import app, db, MaintenanceMode
with app.app_context():
    MaintenanceMode.query.update({'is_active': False})
    db.session.commit()
    print('Maintenance mode disabled')
"
```

### **3. Check Maintenance Status**

```bash
# Show current status
python scripts/test_maintenance_mode.py --status

# Run full test
python scripts/test_maintenance_mode.py --test
```

## 📋 **Admin Dashboard Features**

### **Maintenance Mode Button**
- **Location**: Admin dashboard (`/admin`)
- **Function**: Opens maintenance mode control modal
- **Access**: Admin users only

### **Status Display**
- **Current Status**: Shows if maintenance mode is active or inactive
- **Visual Indicators**: Color-coded badges (🟢 Inactive, 🟡 Active)
- **Real-time Updates**: Status updates automatically

### **Control Modal**
- **Enable Mode**: Form to configure and enable maintenance
- **Disable Mode**: Quick button to disable maintenance
- **Customization**: Set message, timing, and status

## 🔧 **Technical Details**

### **Database Schema**
```sql
CREATE TABLE maintenance_mode (
    id INTEGER PRIMARY KEY,
    is_active BOOLEAN DEFAULT FALSE,
    message TEXT,
    estimated_completion VARCHAR(200),
    status_message VARCHAR(500),
    started_at DATETIME,
    started_by INTEGER,
    created_at DATETIME
);
```

### **Configuration**
```python
# Environment variables (optional)
MAINTENANCE_MODE=False
MAINTENANCE_MESSAGE="We are currently performing scheduled maintenance..."
MAINTENANCE_ESTIMATED_COMPLETION="Shortly"
```

### **Routes Protected**
- **All routes** are protected by maintenance mode
- **Admin bypass** - Admin users can still access all routes
- **Static files** - Still accessible during maintenance
- **API endpoints** - Protected (except admin functions)

## 🎨 **Customization**

### **Maintenance Page Styling**
The maintenance page (`vol/templates/maintenance.html`) can be customized:

- **Colors**: Modify CSS variables for branding
- **Messages**: Update default text and features list
- **Animations**: Adjust timing and effects
- **Social links**: Update contact information

### **Admin Interface**
The admin modal (`vol/templates/admin.html`) can be customized:

- **Form fields**: Add more customization options
- **Validation**: Add custom validation rules
- **Styling**: Match your admin theme

## 🔒 **Security Features**

### **Admin-Only Access**
- **Role-based access**: Only admin users can control maintenance mode
- **Session validation**: Checks user authentication and admin status
- **Audit logging**: Tracks who enabled/disabled maintenance

### **Bypass Protection**
- **Admin bypass**: Administrators can still access the app during maintenance
- **Session validation**: Ensures only authenticated admins can bypass
- **Secure routes**: All admin routes are protected

## 📊 **Monitoring and Logging**

### **Activity Logging**
```python
# Maintenance mode events are logged
logger.info(f"Maintenance mode enabled by admin {user.id} ({user.email})")
logger.info(f"Maintenance mode disabled by admin {user.id} ({user.email})")
```

### **Database Tracking**
- **Start time**: When maintenance was enabled
- **Duration**: How long maintenance was active
- **User tracking**: Who enabled/disabled maintenance
- **Message history**: What messages were shown

## 🚀 **Deployment Considerations**

### **Railway Deployment**
- **Auto-deployment**: Changes are automatically deployed
- **Database migration**: MaintenanceMode table is created automatically
- **Environment variables**: Can be set in Railway dashboard

### **Production Setup**
1. **Database**: Ensure MaintenanceMode table exists
2. **Admin users**: Create admin accounts for maintenance control
3. **Testing**: Test maintenance mode before going live
4. **Monitoring**: Set up alerts for maintenance mode activation

## 🛠️ **Troubleshooting**

### **Common Issues**

**Maintenance mode won't enable:**
```bash
# Check database table exists
python scripts/test_maintenance_mode.py --status

# Check admin permissions
python -c "
from vol.app import app, db, User
with app.app_context():
    user = User.query.filter_by(is_admin=True).first()
    print(f'Admin user: {user.username if user else None}')
"
```

**Users can still access the app:**
- Check if user is an admin (admins can bypass)
- Verify maintenance mode is actually enabled
- Check browser cache (try hard refresh)

**Maintenance page not showing:**
- Check if maintenance.html template exists
- Verify before_request handler is working
- Check application logs for errors

### **Debug Commands**
```bash
# Test maintenance mode functionality
python scripts/test_maintenance_mode.py --test

# Check current status
python scripts/test_maintenance_mode.py --status

# Check database tables
python scripts/check_deployment_status.py
```

## 📚 **Best Practices**

### **Before Enabling Maintenance Mode**
1. **Plan your maintenance** - Know what you're going to do
2. **Set realistic timing** - Don't underestimate completion time
3. **Prepare your message** - Be clear about what's happening
4. **Test the system** - Ensure maintenance mode works
5. **Notify your team** - Let other admins know

### **During Maintenance**
1. **Monitor progress** - Keep track of your updates
2. **Update status** - Change status message as needed
3. **Test functionality** - Ensure your changes work
4. **Keep users informed** - Update estimated completion if needed

### **After Maintenance**
1. **Test thoroughly** - Ensure everything works
2. **Disable maintenance mode** - Restore normal access
3. **Monitor for issues** - Watch for any problems
4. **Document changes** - Record what was updated

## 🎉 **Summary**

Your application now has a **professional maintenance mode system** that:

✅ **Protects users** from accessing incomplete features  
✅ **Provides clear communication** about maintenance status  
✅ **Allows admin access** during maintenance  
✅ **Tracks maintenance history** for auditing  
✅ **Integrates seamlessly** with your existing admin system  
✅ **Auto-deploys** with Railway  

**The system is ready to use!** Administrators can now easily put the application into maintenance mode whenever updates are needed, providing a professional experience for users while ensuring smooth operations.

---

*Last Updated: August 1, 2025*