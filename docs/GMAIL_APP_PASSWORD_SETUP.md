# Gmail App Password Setup Guide

## 🚨 **Issue Found: App Password Required**

Your email test failed because Gmail requires an **App Password** instead of your regular password for SMTP authentication.

## 🔧 **How to Fix This:**

### **Step 1: Enable 2-Factor Authentication (2FA)**

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Click on **"Security"** in the left sidebar
3. Find **"2-Step Verification"** and click **"Get started"**
4. Follow the setup process to enable 2FA on your account

### **Step 2: Generate App Password**

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Click on **"Security"** in the left sidebar
3. Find **"App passwords"** (under "2-Step Verification")
4. Click **"App passwords"**
5. Select **"Mail"** as the app
6. Select **"Other (Custom name)"** as device
7. Enter a name like **"ResumeBuilder Pro"**
8. Click **"Generate"**
9. **Copy the 16-character password** (it will look like: `abcd efgh ijkl mnop`)

### **Step 3: Update Environment Variables**

Replace your current `MAIL_PASSWORD` with the generated App Password:

```bash
# Old (won't work):
MAIL_PASSWORD=kevoh2071M@

# New (use the generated App Password):
MAIL_PASSWORD=abcd efgh ijkl mnop
```

### **Step 4: Test Again**

After updating the password, test the email configuration:

```bash
python scripts/test_email_config.py
```

## 📧 **Alternative Email Providers**

If you prefer not to use Gmail, here are other options:

### **SendGrid (Recommended for Production)**
```bash
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=apikey
MAIL_PASSWORD=your_sendgrid_api_key
```

### **Outlook/Hotmail**
```bash
MAIL_SERVER=smtp-mail.outlook.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@outlook.com
MAIL_PASSWORD=your-password
```

### **Yahoo**
```bash
MAIL_SERVER=smtp.mail.yahoo.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@yahoo.com
MAIL_PASSWORD=your-app-password
```

## 🔒 **Security Best Practices**

1. **Never commit passwords to Git**
2. **Use environment variables** for all sensitive data
3. **Rotate passwords regularly**
4. **Use App Passwords** instead of regular passwords
5. **Enable 2FA** on all accounts

## 🚀 **Quick Fix for Railway Deployment**

Once you have the App Password:

1. Go to your Railway dashboard
2. Find your project
3. Go to **"Variables"** tab
4. Update `MAIL_PASSWORD` with the new App Password
5. Redeploy your application

## ✅ **Verification**

After updating the password, you should see:

```
✅ EMAIL CONFIGURATION: WORKING
📧 Check your email inbox for the test message.
```

---

*Need help? Check the troubleshooting section in the main deployment checklist.*