# 🌍 Environment Variables Guide

## 📋 **Should You Use a .env File?**

### **✅ YES - For Local Development**

**Use a .env file when:**
- 🖥️ **Developing locally** on your computer
- 🔧 **Testing features** before deployment
- 🔐 **Storing sensitive data** (API keys, passwords)
- 👥 **Working with a team** (share config without secrets)

### **❌ NO - For Production Deployment**

**Don't use .env files when:**
- 🚀 **Deploying to Railway** (use Railway's environment variables)
- 📤 **Pushing to Git** (never commit .env files)
- 🔄 **CI/CD pipelines** (use platform environment variables)

---

## 🛠️ **How to Set Up .env File**

### **Step 1: Create .env File**
```bash
# Copy the example file
cp env.example .env

# Or create manually
touch .env
```

### **Step 2: Add Your Configuration**
```bash
# Edit the .env file
nano .env
# or
code .env
```

### **Step 3: Add Your Real Values**
```bash
# Flask Configuration
SECRET_KEY=your-actual-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# Database Configuration
DATABASE_URL=sqlite:///instance/vol.db

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-actual-email@gmail.com
MAIL_PASSWORD=your-actual-gmail-app-password

# PayPal Configuration
PAYPAL_CLIENT_ID=Abk2ZKE-opBQXgi2LjsmMbUVbnDTENcqoyY8IqOAafdOve7amuOb1oof-GspnnGZ9SYWkSSa3K3wk6-j
PAYPAL_CLIENT_SECRET=EM8r8GSqDb3DNQHM0mm5vbp5pw2Oi9sdqe7SKhLeDVdMEDJl3Y12JTrcNwXq9CVtq_WOMnKXqmw0V6-c
PAYPAL_MODE=sandbox
PAYPAL_RECEIVER_EMAIL=kevohmutwiri35@gmail.com

# AI API Keys (optional)
GEMINI_API_KEY=your_gemini_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Application Settings
APP_NAME=ResumeBuilder Pro
APP_URL=http://localhost:5000
```

---

## 🔒 **Security Best Practices**

### **✅ DO:**
- 🔐 **Use strong secret keys** (32+ characters)
- 🏠 **Use different keys** for development vs production
- 🗂️ **Keep .env files local** (never commit to Git)
- 🔄 **Rotate keys regularly** in production
- 📝 **Document required variables** in env.example

### **❌ DON'T:**
- 📤 **Commit .env files** to Git repository
- 🔗 **Share .env files** with others
- 📱 **Use production keys** in development
- 💾 **Store keys in code** or comments
- 🔍 **Log sensitive data** to console

---

## 🚀 **Production vs Development**

### **🖥️ Local Development (.env file)**
```bash
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URL=sqlite:///instance/vol.db
PAYPAL_MODE=sandbox
```

### **🚀 Production (Railway Environment Variables)**
```bash
FLASK_ENV=production
FLASK_DEBUG=False
DATABASE_URL=postgresql://... (Railway provides this)
PAYPAL_MODE=live
```

---

## 🔧 **Testing Your .env Setup**

### **1. Check if .env is loaded:**
```python
import os
print("SECRET_KEY:", os.getenv('SECRET_KEY'))
print("PAYPAL_CLIENT_ID:", os.getenv('PAYPAL_CLIENT_ID'))
```

### **2. Run the application:**
```bash
cd vol
python app.py
```

### **3. Test PayPal configuration:**
Visit: `http://localhost:5000/paypal-test`

---

## 📁 **File Structure**
```
your-project/
├── .env                    # Your local environment variables (gitignored)
├── .env.example           # Template for other developers
├── .gitignore             # Excludes .env from Git
├── vol/
│   ├── app.py             # Uses os.getenv() to read variables
│   └── config.py          # Configuration class
└── Railway Dashboard      # Production environment variables
```

---

## 🚨 **Troubleshooting**

### **Problem: Variables not loading**
**Solution:** Check if `python-dotenv` is installed and `.env` file exists

### **Problem: PayPal not working locally**
**Solution:** Ensure PayPal variables are set in `.env` file

### **Problem: Email not sending**
**Solution:** Check MAIL_USERNAME and MAIL_PASSWORD in `.env`

### **Problem: Database connection issues**
**Solution:** Verify DATABASE_URL in `.env` for local development

---

## 📚 **Next Steps**

1. **Create your .env file** using the template
2. **Add your real API keys** and credentials
3. **Test locally** before deploying
4. **Keep .env file secure** and never commit it
5. **Use Railway environment variables** for production

**Your .env file is for local development only!** 🎯