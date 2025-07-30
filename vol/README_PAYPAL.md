# PayPal Integration Setup

## Environment Variables Required

Add these environment variables to your Railway app:

```bash
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_CLIENT_SECRET=your_paypal_client_secret
PAYPAL_MODE=sandbox  # Change to 'live' for production
PAYPAL_RECEIVER_EMAIL=your_paypal_email@example.com
```

## How to Get PayPal API Credentials

1. **Go to PayPal Developer Dashboard**
   - Visit: https://developer.paypal.com/
   - Sign in with your PayPal account

2. **Create a PayPal App**
   - Go to "My Apps & Credentials"
   - Click "Create App"
   - Name it "ResumeBuilder Pro"
   - Select "Business" account type

3. **Get Your Credentials**
   - Copy the "Client ID" and "Secret"
   - Add them to your environment variables

4. **Set Your PayPal Email**
   - Use the email address of your PayPal account
   - This is where payments will be sent

## Testing

- **Sandbox Mode**: Use sandbox credentials for testing
- **Live Mode**: Use live credentials for real payments

## Payment Flow

1. User clicks "Upgrade to Premium"
2. Selects plan (monthly/yearly)
3. Chooses PayPal payment method
4. Redirected to PayPal for payment
5. Payment goes directly to your PayPal account
6. User redirected back to app with premium access

## Security Features

- PayPal handles all payment security
- No credit card data stored in your app
- PayPal webhooks for payment notifications
- Secure API authentication

## Pricing

- **Monthly Plan**: $19.99/month
- **Yearly Plan**: $199.99/year (Save 20%)

All payments go directly to your PayPal account!