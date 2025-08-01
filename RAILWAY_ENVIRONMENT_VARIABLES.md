# Railway Environment Variables for Production

## 🚀 **Copy These Variables to Your Railway Dashboard**

Go to your Railway project → Variables tab and add these environment variables:

### **Required Variables:**

```bash
SECRET_KEY=L-]L2T}d7UDRM'UR4p-=W}as5R6-Algr
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=kevohmutwiri35@gmail.com
MAIL_PASSWORD=jhkf nzos cykp bxaj
FLASK_ENV=production
FLASK_DEBUG=False
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Lax
```

### **Optional Variables (Recommended):**

```bash
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@resumebuilderpro.com
ADMIN_PASSWORD=admin123456
LOG_LEVEL=INFO
```

### **PayPal Configuration (Optional):**

```bash
PAYPAL_CLIENT_ID=your_paypal_client_id_here
PAYPAL_CLIENT_SECRET=your_paypal_client_secret_here
PAYPAL_MODE=live
PAYPAL_RECEIVER_EMAIL=kevohmutwiri35@gmail.com
```

### **Note:**
- `DATABASE_URL` will be automatically set by Railway
- All other variables need to be manually added

## 🔧 **How to Add Variables in Railway:**

1. Go to your Railway project dashboard
2. Click on your project
3. Go to the **"Variables"** tab
4. Click **"New Variable"** for each variable above
5. Enter the **Name** and **Value**
6. Click **"Add"**
7. Repeat for all variables
8. Railway will automatically redeploy your app

## ✅ **After Setting Variables:**

1. **Wait for Railway to redeploy** (usually 1-2 minutes)
2. **Test your application** at your Railway URL
3. **Log in as admin** with:
   - Username: `admin`
   - Password: `admin123456`
4. **Test maintenance mode** from the admin dashboard
5. **Test PayPal payments** (if configured)

## 🎯 **Expected Results:**

After setting these variables, your application will be:
- ✅ **Production-ready** with proper security
- ✅ **Email notifications** working
- ✅ **Maintenance mode** fully functional
- ✅ **Admin controls** accessible
- ✅ **HTTPS cookies** enabled
- ✅ **Debug mode** disabled
- ✅ **PayPal payments** ready (if configured)

---

**Status:** Ready for production deployment! 🚀