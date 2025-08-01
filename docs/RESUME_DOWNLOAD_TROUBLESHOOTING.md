# Resume Download Troubleshooting Guide

## 🚨 **Issue: Cannot Download Resume**

If you're experiencing problems downloading your resume, this guide will help you identify and resolve the issue.

## ✅ **What's Working**

Based on our testing, the following components are functioning correctly:
- ✅ PDF generation (WeasyPrint)
- ✅ Database connectivity
- ✅ Resume data storage
- ✅ Download route functionality
- ✅ User authentication system

## 🔍 **Common Issues and Solutions**

### **1. User Authentication Issues**

**Problem:** You're not logged in or your session has expired.

**Symptoms:**
- Redirected to login page when trying to download
- "Access denied" messages
- Download button doesn't work

**Solutions:**
```bash
# Check if you're logged in
1. Go to the login page
2. Enter your credentials
3. Try downloading again
```

### **2. Resume Ownership Issues**

**Problem:** The resume doesn't belong to your account.

**Symptoms:**
- "Resume not found" error
- 404 error when accessing download link
- Download button missing

**Solutions:**
```bash
# Verify resume ownership
1. Go to "My Resumes" page
2. Check if the resume appears in your list
3. If not, create a new resume or contact support
```

### **3. Browser Issues**

**Problem:** Browser-specific problems preventing downloads.

**Symptoms:**
- Download starts but fails
- Browser shows "blocked" message
- File downloads as HTML instead of PDF

**Solutions:**
```bash
# Try these browser fixes:
1. Clear browser cache and cookies
2. Disable ad blockers temporarily
3. Try a different browser (Chrome, Firefox, Safari)
4. Check browser download settings
5. Allow pop-ups for the site
```

### **4. Network/Server Issues**

**Problem:** Server-side or network connectivity issues.

**Symptoms:**
- Timeout errors
- "Server error" messages
- Download never starts

**Solutions:**
```bash
# Check server status:
1. Try refreshing the page
2. Wait a few minutes and try again
3. Check your internet connection
4. Contact support if issue persists
```

## 🛠️ **Diagnostic Steps**

### **Step 1: Check Browser Console**

1. Open browser developer tools (F12)
2. Go to Console tab
3. Try to download resume
4. Look for any error messages

**Common Console Errors:**
```
- "Failed to load resource"
- "CORS error"
- "Network error"
- "JavaScript error"
```

### **Step 2: Check Network Tab**

1. Open browser developer tools (F12)
2. Go to Network tab
3. Try to download resume
4. Look for failed requests

**What to look for:**
- HTTP status codes (200 = success, 404 = not found, 500 = server error)
- Request/response headers
- Response content

### **Step 3: Verify Resume Data**

```bash
# Check if resume exists and has data:
1. Go to "My Resumes" page
2. Click "Edit" on the resume
3. Verify all fields have content
4. Save the resume
5. Try downloading again
```

### **Step 4: Test Different Formats**

```bash
# Try different download formats:
1. Try PDF format first
2. If PDF fails, try Word format
3. If both fail, the issue is likely server-side
```

## 🔧 **Technical Solutions**

### **For Developers/Advanced Users:**

#### **1. Check Application Logs**
```bash
# View application logs for errors:
tail -f logs/vol.log

# Look for these error patterns:
- "PDF generation failed"
- "Database connection error"
- "User authentication failed"
- "Resume not found"
```

#### **2. Test PDF Generation**
```bash
# Run the test script:
source venv/bin/activate
python scripts/test_resume_download.py
```

#### **3. Check Database**
```bash
# Verify resume exists in database:
python -c "
from vol.app import app, db, Resume
with app.app_context():
    resumes = Resume.query.all()
    for r in resumes:
        print(f'ID: {r.id}, Name: {r.name}, User: {r.user_id}')
"
```

#### **4. Test Download Route**
```bash
# Test the download endpoint directly:
curl -H "Cookie: session=YOUR_SESSION_ID" \
     "https://your-domain.com/download-resume/1?format=pdf"
```

## 📋 **Quick Checklist**

Before contacting support, try these steps in order:

- [ ] **Are you logged in?** (Check if you see your username in the header)
- [ ] **Does the resume exist?** (Check "My Resumes" page)
- [ ] **Is the resume complete?** (Edit and save the resume)
- [ ] **Try a different browser** (Chrome, Firefox, Safari)
- [ ] **Clear browser cache** (Ctrl+Shift+Delete)
- [ ] **Disable ad blockers** (Temporarily)
- [ ] **Try different format** (PDF vs Word)
- [ ] **Check internet connection** (Try other websites)
- [ ] **Wait and retry** (Server might be busy)

## 🆘 **When to Contact Support**

Contact support if:

1. **All diagnostic steps fail**
2. **Error persists across different browsers**
3. **You see specific error messages**
4. **Resume data is missing or corrupted**
5. **Download works for some resumes but not others**

## 📞 **Support Information**

When contacting support, please provide:

1. **Error messages** (screenshot or copy/paste)
2. **Browser and version** (Chrome 120, Firefox 115, etc.)
3. **Operating system** (Windows, Mac, Linux)
4. **Steps to reproduce** (exact steps you followed)
5. **Resume ID** (if known)
6. **Console errors** (from browser developer tools)

## 🔄 **Alternative Solutions**

If download continues to fail:

1. **Use the preview feature** and print to PDF
2. **Copy resume content** and paste into a document
3. **Use browser print function** (Ctrl+P, save as PDF)
4. **Export from "My Resumes"** page instead of individual resume

## 🎯 **Prevention Tips**

To avoid download issues in the future:

1. **Keep browser updated**
2. **Clear cache regularly**
3. **Use supported browsers** (Chrome, Firefox, Safari, Edge)
4. **Ensure stable internet connection**
5. **Complete all resume fields** before downloading
6. **Save resume frequently** while editing

---

**💡 Need immediate help?** Check the browser console for specific error messages and try the diagnostic steps above. Most issues can be resolved with these troubleshooting steps.