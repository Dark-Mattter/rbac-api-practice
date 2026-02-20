# rbac-api-practice
Role Based Access Control API Practice

Project Overview

This project is a Role-Based Access Control (RBAC) API built using FastAPI, SQLAlchemy, and JWT authentication. It demonstrates secure user authentication, permission-based authorization, and admin-controlled role management backed by a relational database.

The API supports:
	•	User registration and login
	•	JWT-based authentication
	•	Role-based and permission-based access control
	•	Admin-managed role updates
	•	Protected endpoints
	•	Database persistence using SQLAlchemy

⸻

File-by-File Breakdown

main.py

This is the core FastAPI application.

It defines:
	•	The FastAPI app instance
	•	Database session dependency (get_db)
	•	Authentication logic (get_current_user)
	•	Admin guard (require_admin)
	•	API endpoints:
	•	/register – creates new users with hashed passwords
	•	/login – authenticates users and returns a JWT
	•	/me – returns the currently authenticated user
	•	/admin-only – admin-protected route
	•	/profile – permission-based route
	•	/users – permission-protected route
	•	/users/{username}/role – allows admins to update user roles

This file wires together authentication, authorization, and database operations.

⸻

models.py

Defines the SQLAlchemy database models.

Includes:
	•	User model with:
	•	id
	•	username
	•	password_hash
	•	role

This model represents persisted users in the database.

⸻

database.py

Handles database configuration.

Includes:
	•	SQLAlchemy engine setup
	•	Base model declaration
	•	SessionLocal factory
	•	Table creation logic

This file manages database connections and sessions.

⸻

auth.py

Implements authentication utilities.

Includes:
	•	Password hashing (secure password storage)
	•	Password verification
	•	JWT creation (create_access_token)
	•	JWT decoding (decode_token)

This file handles all authentication-related security logic.

⸻

rbac.py

Defines the role-to-permission mapping.

Contains:
	•	ROLE_PERMISSIONS dictionary
	•	Maps roles (e.g., admin, user) to allowed permissions
	•	Used to enforce fine-grained access control

This file separates authorization rules from business logic.

⸻

dependencies.py

Implements reusable authorization guards.

Includes:
	•	require_permission(permission)
	•	Validates that a user has the required permission
	•	Returns 403 if permission is missing

This file enables permission-based route protection using FastAPI’s dependency injection system.

⸻

🔐 Security Architecture

Authentication:
	•	Users log in via /login
	•	A JWT access token is returned
	•	Protected routes require a valid Bearer token

Authorization:
	•	Roles are stored in the database
	•	Permissions are mapped to roles
	•	Routes are protected using:
	•	require_admin
	•	require_permission

Only admins can:
	•	Update other users’ roles

⸻

Key Concepts Demonstrated
	•	OAuth2 password flow
	•	JWT-based authentication
	•	Role-Based Access Control (RBAC)
	•	Permission-based authorization
	•	Dependency injection
	•	Secure password storage
	•	SQLAlchemy ORM integration
	•	HTTP status code handling (401 vs 403)
