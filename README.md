Muscle Nutrition App - Backend Authentication System
Overview
This project is a Django-based backend API for a nutrition app focused on helping users gain muscle through personalized meal plans. The current implementation includes a robust user authentication system with JWT tokens and email verification.
Features Implemented
User Authentication System

User Registration: Secure sign-up process with password confirmation
Email Verification: Verification link sent to users upon registration
JWT Authentication: Secured API endpoints using JWT tokens
User Profile: Extended user model with fitness-related data
Password Security: Password hashing and validation

API Endpoints
Authentication

POST /api/users/register/: Create a new user account
POST /api/users/token/: Obtain JWT token pair (access & refresh)
POST /api/users/token/refresh/: Refresh an expired access token
GET /api/users/verify-email/<uuid:token>/: Verify user email

User Profile

GET /api/users/profile/: Retrieve the authenticated user's profile
PATCH /api/users/profile/: Update the authenticated user's profile

Technical Implementation
Backend Technology Stack

Django: Web framework for building the API
Django REST Framework: Toolkit for building RESTful APIs
Simple JWT: JWT authentication for Django REST Framework
Python Decouple: Environment variables management for secure configuration

Database Schema

User Model: Django's built-in user model (username, email, password, etc.)
UserProfile Model: Extended profile with:

Age
Email verification status
Terms acceptance
Verification token



Environment Configuration
Environment variables are managed through a .env file for secure configuration of:

Django secret key
Email service credentials
Database connection details
Site domain settings

Email Verification Flow

User registers with email and password
System generates a unique verification token
Verification email is sent to user's email address
User clicks verification link to activate account
System validates token and marks email as verified

Next Steps
The next phase of development will focus on:

Creating the questionnaire system to collect user fitness goals and preferences
Implementing the AI integration with Gemini API for personalized meal plans
Building the frontend interface with React and Tailwind CSS

Running the Project
Prerequisites

Python 3.8+
PostgreSQL or SQLite
SMTP email service (like Hostinger)

Setup Instructions

Clone the repository
Create a virtual environment
Install dependencies: pip install -r requirements.txt
Configure the .env file with your environment variables
Run migrations: python manage.py migrate
Start the server: python manage.py runserver
