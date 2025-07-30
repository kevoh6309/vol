# ResumeBuilder SaaS

A modern, AI-powered resume and cover letter builder with job application tracking, interview prep, analytics, and premium features.

## Features
- Resume Builder (CRUD, PDF/Word export, templates)
- Cover Letter Builder (CRUD, AI generation, templates, analytics)
- Job Application Tracker (CRUD, stats, attachments)
- Interview Preparation (practice sessions, question bank)
- Stripe integration for premium subscriptions
- Referral and affiliate system
- User management (register, login, profile, password reset, delete account)
- Analytics dashboard
- Modern UI with Bootstrap 5
- Gemini API integration for AI features

## Setup
1. Clone the repo and `cd` into the project directory.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your secrets (see `config.py` for required keys).
5. Initialize the database:
   ```bash
   python init_db.py
   ```
6. Run the app:
   ```bash
   python app.py
   ```

## Deployment
- Use `gunicorn` for production: `gunicorn -w 4 app:app`
- Set environment variables for Stripe, Gemini, and Flask secret keys.
- Configure a production-ready database if needed.

## License
MIT 