# Flask application for ResumeBuilder Pro - Latest deployment: 2025-08-03 14:45 UTC
# Fixed: Email templates, service worker route, PayPal API issues
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file, g, session, make_response
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone, timedelta
import os

from flask_mail import Mail, Message
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Length, EqualTo
import requests
import json
import re
# Import config directly
import os
try:
    from config import config
except ImportError:
    # If config import fails, create a basic config
    class Config:
        SECRET_KEY = os.getenv('SECRET_KEY', 'kevoh2071M@')
        FLASK_ENV = os.getenv('FLASK_ENV', 'development')
        FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:////tmp/vol.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        
        # Enhanced Security Configuration
        SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'True').lower() == 'true'
        SESSION_COOKIE_HTTPONLY = True
        SESSION_COOKIE_SAMESITE = 'Lax'
        PERMANENT_SESSION_LIFETIME = 86400  # 24 hours
        SESSION_COOKIE_MAX_AGE = 86400
        SESSION_REFRESH_EACH_REQUEST = True
        
        # CSRF Protection
        WTF_CSRF_ENABLED = True
        WTF_CSRF_TIME_LIMIT = 3600  # 1 hour
        
        # Rate Limiting
        RATELIMIT_STORAGE_URL = os.getenv('REDIS_URL', 'memory://')
        RATELIMIT_DEFAULT = "200 per day;50 per hour;10 per minute"
        
        # Security Headers
        SECURITY_HEADERS = {
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'SAMEORIGIN',
            'X-XSS-Protection': '1; mode=block',
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
            'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://pagead2.googlesyndication.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net https://pagead2.googlesyndication.com; img-src 'self' data: https://cdn.jsdelivr.net https://pagead2.googlesyndication.com; font-src 'self' https://fonts.gstatic.com https://cdn.jsdelivr.net; connect-src 'self' https://openrouter.ai https://generativelanguage.googleapis.com https://api.openai.com https://api.sandbox.paypal.com https://api.paypal.com; frame-src 'self' https://www.paypal.com https://sandbox.paypal.com; object-src 'none'; base-uri 'self'; form-action 'self' https://www.paypal.com https://sandbox.paypal.com; upgrade-insecure-requests; report-uri /csp-violation-report-endpoint/",
        }
        
        # Mail Configuration
        MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
        MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
        MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
        MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your-email@gmail.com')
        MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your-gmail-app-password')
        MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', 'your-email@gmail.com')
        
        # PayPal Configuration
        PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID')
        PAYPAL_CLIENT_SECRET = os.environ.get('PAYPAL_CLIENT_SECRET')
        PAYPAL_MODE = os.environ.get('PAYPAL_MODE', 'sandbox')
        PAYPAL_RECEIVER_EMAIL = os.environ.get('PAYPAL_RECEIVER_EMAIL')
        
        # AI API Configuration
        GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'your_gemini_api_key_here')
        GEMINI_API_URL = os.getenv('GEMINI_API_URL', 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent')
        COHERE_API_KEY = os.getenv('COHERE_API_KEY', 'your_cohere_api_key_here')
        OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', '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')
        OPENROUTER_API_URL = os.getenv('OPENROUTER_API_URL', 'https://openrouter.ai/api/v1/chat/completions')
        
        # Application Configuration
        APP_NAME = os.getenv('APP_NAME', 'ResumeBuilder Pro')
        APP_URL = os.getenv('APP_URL', 'https://resume-builder-saas.railway.app')
        
        # Logging Configuration
        LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
        LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        
        # Maintenance Mode Configuration
        MAINTENANCE_MODE = os.getenv('MAINTENANCE_MODE', 'False').lower() == 'true'
        MAINTENANCE_MESSAGE = os.getenv('MAINTENANCE_MESSAGE', 'We are currently performing scheduled maintenance to improve your experience.')
        MAINTENANCE_ESTIMATED_COMPLETION = os.getenv('MAINTENANCE_ESTIMATED_COMPLETION', 'Shortly')
    class DevelopmentConfig(Config):
        DEBUG = True
        SESSION_COOKIE_SECURE = False  # Allow HTTP in development
    class ProductionConfig(Config):
        DEBUG = False
        APP_URL = os.getenv('APP_URL', 'https://resume-builder-saas.railway.app')
        SESSION_COOKIE_SECURE = True
    config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
    }
import secrets
import time
from collections import Counter
import datetime as dt
import tempfile
# WeasyPrint will be imported locally in functions where needed
WEASYPRINT_AVAILABLE = None  # Will be set when first needed

# Remainder of file unchanged...