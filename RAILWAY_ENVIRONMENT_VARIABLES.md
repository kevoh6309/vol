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

### **Stripe Configuration (Required for Payments):**

```bash
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key
STRIPE_MONTHLY_PRICE_ID=price_your_monthly_price_id
STRIPE_YEARLY_PRICE_ID=price_your_yearly_price_id
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret
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
- **Stripe keys are required for the upgrade functionality to work**

## 🔧 **How to Add Variables in Railway:**

1. Go to your Railway project dashboard
2. Click on your project
3. Go to the **"Variables"** tab
4. Click **"New Variable"** for each variable above
5. Enter the **Name** and **Value**
6. Click **"Add"**
7. Repeat for all variables
8. Railway will automatically redeploy your app

## 🎯 **Stripe Setup Instructions:**

### **1. Create Stripe Account:**
- Go to [stripe.com](https://stripe.com) and create an account
- Complete your business verification

### **2. Get Your API Keys:**
- Go to Stripe Dashboard → Developers → API Keys
- Copy your **Publishable Key** and **Secret Key**
- Use **test keys** for development, **live keys** for production

### **3. Create Products and Prices:**
- Go to Stripe Dashboard → Products
- Create two products:
  - **Monthly Premium** ($19.99/month)
  - **Yearly Premium** ($199.99/year)
- Copy the **Price IDs** (start with `price_`)

### **4. Set Up Webhooks:**
- Go to Stripe Dashboard → Developers → Webhooks
- Add endpoint: `https://your-domain.railway.app/stripe-webhook`
- Select events: `checkout.session.completed`
- Copy the **Webhook Secret**

### **5. Add to Railway:**
- Add all Stripe variables to your Railway environment
- Wait for redeployment

## ✅ **After Setting Variables:**

1. **Wait for Railway to redeploy** (usually 1-2 minutes)
2. **Test your application** at your Railway URL
3. **Log in as admin** with:
   - Username: `admin`
   - Password: `admin123456`
4. **Test maintenance mode** from the admin dashboard
5. **Test Stripe payments** using test card numbers:
   - **Success**: `4242 4242 4242 4242`
   - **Decline**: `4000 0000 0000 0002`
6. **Test PayPal payments** (if configured)

## 🎯 **Expected Results:**

After setting these variables, your application will be:
- ✅ **Production-ready** with proper security
- ✅ **Email notifications** working
- ✅ **Maintenance mode** fully functional
- ✅ **Admin controls** accessible
- ✅ **HTTPS cookies** enabled
- ✅ **Debug mode** disabled
- ✅ **Stripe payments** working
- ✅ **PayPal payments** ready (if configured)
- ✅ **Upgrade functionality** fully operational

## 🚨 **Troubleshooting:**

### **If Upgrade Doesn't Work:**
1. **Check Stripe Keys**: Ensure all Stripe variables are set
2. **Verify Price IDs**: Make sure price IDs match your Stripe products
3. **Test Mode**: Use test keys for development
4. **Webhook URL**: Ensure webhook URL is correct
5. **Check Logs**: Monitor Railway logs for errors

### **Common Issues:**
- **"Error creating checkout session"**: Missing or invalid Stripe keys
- **"Price not found"**: Incorrect price IDs
- **"Webhook signature verification failed"**: Wrong webhook secret

---

**Status:** Ready for production deployment! 🚀