# 🚀 ResumeBuilder SaaS

A comprehensive resume building and career management platform with AI-powered features, premium templates, and professional tools.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)](https://github.com/yourusername/resumebuilder)

## 🌟 Features

### ✨ Core Features
- **📄 Resume Builder** - Create professional resumes with multiple templates
- **✉️ Cover Letter Generator** - AI-powered cover letter creation
- **📥 PDF Export** - Download resumes and cover letters in PDF format
- **🤖 AI Chatbot** - Get instant tips and suggestions while building resumes
- **🔐 User Authentication** - Secure login and registration system
- **⭐ Premium System** - Upgrade for advanced features and templates

### 🛠️ Career Tools
- **🎨 Portfolio Builder** - Create and host professional portfolios
- **🌐 Website Generator** - Generate personal websites from resume data
- **📊 Interview Prep** - Practice with mock interviews and questions
- **📈 Job Tracker** - Track your job applications and progress
- **🔗 Networking Tools** - Email templates and LinkedIn message generator
- **📋 Resume Checker** - ATS optimization and content analysis

### 💰 Monetization
- **📱 Google AdSense** - Strategic ad placements for revenue
- **⭐ Premium Subscriptions** - Ad-free experience with advanced features
- **🎯 Affiliate System** - Referral program for user growth

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/resumebuilder.git
   cd resumebuilder
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r vol/requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Edit .env with your configuration
   nano .env
   ```

5. **Initialize database**
   ```bash
   python vol/init_db.py
   ```

6. **Run the application**
   ```bash
   python vol/app.py
   ```

7. **Open your browser**
   ```
   http://localhost:5000
   ```

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# Database Configuration
DATABASE_URL=sqlite:///instance/vol.db

# Email Configuration (for password reset)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Stripe Configuration (for payments)
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key
STRIPE_MONTHLY_PRICE_ID=price_monthly_id
STRIPE_YEARLY_PRICE_ID=price_yearly_id
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret

# AI API Keys
GEMINI_API_KEY=your_gemini_api_key
OPENROUTER_API_KEY=your_openrouter_api_key

# Application Settings
APP_NAME=ResumeBuilder
APP_URL=http://localhost:5000
```

### Google AdSense Setup
1. Sign up for [Google AdSense](https://adsense.google.com)
2. Get your Publisher ID
3. Create ad units in AdSense dashboard
4. Update ad slot IDs in `vol/templates/base.html`
5. See `ADSENSE_SETUP_GUIDE.md` for detailed instructions

## 📁 Project Structure

```
resumebuilder/
├── vol/                          # Main application
│   ├── app.py                   # Flask application
│   ├── config.py                # Configuration settings
│   ├── requirements.txt         # Python dependencies
│   ├── init_db.py              # Database initialization
│   ├── templates/              # HTML templates
│   │   ├── base.html          # Base template with AdSense
│   │   ├── landing.html       # Landing page
│   │   ├── dashboard.html     # User dashboard
│   │   └── ...                # Other templates
│   └── static/                # Static files (CSS, JS, images)
├── docs/                       # Documentation
├── scripts/                    # Utility scripts
├── logs/                       # Application logs
├── instance/                   # Database files (gitignored)
├── .env                        # Environment variables (gitignored)
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
└── ADSENSE_SETUP_GUIDE.md     # AdSense setup guide
```

## 🎯 Key Features Explained

### AI-Powered Resume Builder
- **Smart Suggestions**: AI provides real-time tips while building resumes
- **Content Optimization**: Automatic keyword suggestions for ATS systems
- **Professional Templates**: Modern, clean designs that stand out

### Premium Features
- **Ad-Free Experience**: Premium users enjoy distraction-free interface
- **Advanced Templates**: Exclusive premium resume and cover letter templates
- **Unlimited Downloads**: No restrictions on PDF exports
- **Portfolio Hosting**: Professional portfolio websites
- **Advanced Analytics**: Detailed job application tracking

### Monetization Strategy
- **Google AdSense**: Strategic ad placements for non-premium users
- **Premium Subscriptions**: Monthly/yearly plans with exclusive features
- **Affiliate Program**: User referral system for growth

## 🚀 Deployment

### Local Development
```bash
python vol/app.py
```

### Production Deployment
1. **Set up production environment**
   ```bash
   export FLASK_ENV=production
   export FLASK_DEBUG=False
   ```

2. **Use Gunicorn (recommended)**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 vol.app:app
   ```

3. **Deploy to platforms**
   - **Heroku**: Use `Procfile` and `runtime.txt`
   - **DigitalOcean**: Use App Platform or Droplets
   - **AWS**: Use Elastic Beanstalk or EC2
   - **Vercel**: Use Python runtime

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## 📊 Performance & Analytics

### Key Metrics
- **User Engagement**: Average session duration, pages per session
- **Conversion Rate**: Free to premium user conversion
- **Revenue Metrics**: AdSense earnings, subscription revenue
- **Technical Performance**: Page load times, error rates

### Monitoring
- **Application Logs**: Check `logs/vol.log` for errors
- **Database Performance**: Monitor query performance
- **User Analytics**: Track user behavior and preferences

## 🔒 Security

### Security Features
- **CSRF Protection**: All forms protected against CSRF attacks
- **Password Hashing**: Secure password storage with bcrypt
- **Rate Limiting**: API endpoints protected against abuse
- **Input Validation**: All user inputs validated and sanitized
- **HTTPS Ready**: Configured for secure connections

### Best Practices
- Keep dependencies updated
- Use environment variables for sensitive data
- Regular security audits
- Monitor for suspicious activity

## 📈 Roadmap

### Upcoming Features
- [ ] **Mobile App**: Native iOS and Android applications
- [ ] **Advanced AI**: More sophisticated resume analysis
- [ ] **Team Collaboration**: Multi-user resume editing
- [ ] **Integration APIs**: Connect with job boards
- [ ] **Advanced Analytics**: Detailed career insights

### Planned Improvements
- [ ] **Performance Optimization**: Faster page loads
- [ ] **Enhanced Templates**: More design options
- [ ] **Better Mobile Experience**: Responsive improvements
- [ ] **Internationalization**: Multi-language support

## 📞 Support

### Getting Help
- **Documentation**: Check the `docs/` folder
- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact support@resumebuilder.com

### Community
- **Discord**: Join our community server
- **Twitter**: Follow for updates and tips
- **Blog**: Career advice and platform updates

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask Community**: For the amazing web framework
- **Bootstrap**: For the responsive UI components
- **Google AdSense**: For monetization platform
- **Stripe**: For payment processing
- **OpenAI/Gemini**: For AI capabilities

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/resumebuilder&type=Date)](https://star-history.com/#yourusername/resumebuilder&Date)

---

**Made with ❤️ by the ResumeBuilder Team**

*Help us reach 1000 stars! ⭐* 