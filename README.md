# GitHub Connector API

This project is a simple backend service built to demonstrate how to integrate with the GitHub API in a clean and structured way. The goal was to design a connector that can authenticate securely and expose useful actions through REST endpoints.

Instead of overcomplicating things, the focus here is on clarity, real API interaction, and maintainable code.

---

## What this project does

The API connects to GitHub using a Personal Access Token and allows you to:

- Retrieve repositories of a given user
- View issues from any repository
- Create a new issue in a repository

All operations are backed by real GitHub API calls.

---

## Tech Stack

- Python
- FastAPI
- Requests

---

## Project Structure

.
├── main.py
├── requirements.txt
└── README.md

---

## Setup Instructions

git clone https://github.com/Rakhi29/github-connector-api.git
cd github-connector-api

python -m venv venv

Windows:
venv\Scripts\activate

Linux / Mac:
source venv/bin/activate

pip install -r requirements.txt

---

## Running the Application

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs

---

## Authentication

Authorization: Bearer YOUR_GITHUB_TOKEN

---

## API Endpoints

GET /repos?username=<github_username>

GET /issues?owner=<owner>&repo=<repo>

POST /create-issue?owner=<owner>&repo=<repo>&title=<title>&body=<body>

---

## Design Choices

- Used FastAPI for simplicity and performance
- Kept authentication secure and flexible
- Focused on clean and readable structure
- Implemented basic error handling for real API responses

---

## Future Improvements

- OAuth 2.0 authentication
- Pagination support
- Logging and monitoring
- Unit and integration testing

---

## Summary

This project demonstrates backend fundamentals including API integration, authentication handling, and clean code practices.
