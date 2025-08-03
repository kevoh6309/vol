# Railway Environment Variables for Production

## 🚀 **Copy These Variables to Your Railway Dashboard**

Go to your Railway project → Variables tab and add these environment variables:

### **Required Variables:**

```bash
SECRET_KEY=your-strong-secret-key-here
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-gmail-app-password
FLASK_ENV=production
FLASK_DEBUG=False
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Lax
```

### **PayPal Configuration (Required for Payments):**

```bash
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_CLIENT_SECRET=your_paypal_client_secret
PAYPAL_MODE=sandbox
PAYPAL_RECEIVER_EMAIL=your_paypal_business_email@example.com
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
PAYPAL_MODE=sandbox
PAYPAL_RECEIVER_EMAIL=your-paypal-email@gmail.com
```

### **Note:**
- `DATABASE_URL` will be automatically set by Railway
- All other variables need to be manually added
- **PayPal keys are required for the upgrade functionality to work**

## 🔧 **How to Add Variables in Railway:**

1. Go to your Railway project dashboard
2. Click on your project
3. Go to the **"Variables"** tab
4. Click **"New Variable"** for each variable above
5. Enter the **Name** and **Value**
6. Click **"Add"**
7. Repeat for all variables
8. Railway will automatically redeploy your app

## 🎯 **PayPal Setup Instructions:**

### **1. Create PayPal Business Account:**
- Go to [paypal.com](https://paypal.com) and create a business account
- Complete your business verification

### **2. Get Your API Credentials:**
- Go to PayPal Developer Dashboard → My Apps & Credentials
- Create a new app or use an existing one
- Copy your **Client ID** and **Client Secret**
- Use **sandbox** credentials for testing, **live** credentials for production

### **3. Configure PayPal Mode:**
- Set `PAYPAL_MODE=sandbox` for testing
- Set `PAYPAL_MODE=live` for production

### **4. Set Receiver Email:**
- Use your PayPal business email address
- This is where payments will be received

### **5. Add to Railway:**
- Add all PayPal variables to your Railway environment
- Wait for redeployment

## ✅ **After Setting Variables:**

1. **Wait for Railway to redeploy** (usually 1-2 minutes)
2. **Test your application** at your Railway URL
3. **Log in as admin** with:
   - Username: `admin`
   - Password: `admin123456`
4. **Test maintenance mode** from the admin dashboard
5. **Test PayPal payments** using sandbox accounts:
   - **Success**: Use PayPal sandbox buyer account
   - **Decline**: Use invalid payment method

## 🎯 **Expected Results:**

After setting these variables, your application will be:
- ✅ **Production-ready** with proper security
- ✅ **Email notifications** working
- ✅ **Maintenance mode** fully functional
- ✅ **Admin controls** accessible
- ✅ **HTTPS cookies** enabled
- ✅ **Debug mode** disabled
- ✅ **PayPal payments** working
- ✅ **Upgrade functionality** fully operational

## 🚨 **Troubleshooting:**

### **If Upgrade Doesn't Work:**
1. **Check PayPal Keys**: Ensure all PayPal variables are set
2. **Verify PayPal Mode**: Make sure mode is set to 'sandbox' or 'live'
3. **Test Mode**: Use sandbox credentials for development
4. **Receiver Email**: Ensure PayPal receiver email is correct
5. **Check Logs**: Monitor Railway logs for errors

### **Common Issues:**
- **"Error creating payment"**: Missing or invalid PayPal keys
- **"PayPal authentication failed"**: Incorrect client ID or secret
- **"Payment not found"**: PayPal API connection issues

---

**Status:** Ready for production deployment! 🚀