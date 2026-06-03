# AI Resume Builder

An AI-powered Resume Builder built using Python, CustomTkinter, Gemini AI, SQLite, and ReportLab. Generate professional resumes instantly with AI-generated summaries and export them as PDF files.

## Features

* AI-generated Professional Resume Summary
* Modern Desktop GUI using CustomTkinter
* PDF Resume Generation
* SQLite Database Storage
* Personal Information Management
* Education, Skills, and Projects Sections
* Gemini AI Integration
* Easy-to-Use Interface
* Local Resume Storage

## Tech Stack

* Python
* CustomTkinter
* Gemini AI API
* SQLite3
* ReportLab
* Python Dotenv

## Project Structure

```text
AI-Resume-Builder/
│
├── main.py
├── ai_helper.py
├── database.py
├── resume_generator.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   ├── modern.py
│   └── professional.py
│
├── resumes/
│
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Builder.git
cd AI-Resume-Builder
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Gemini AI Setup

### Step 1: Get a Gemini API Key

1. Visit Google AI Studio
2. Sign in with your Google Account
3. Create a Gemini API Key
4. Copy the generated key

### Step 2: Create a `.env` File

Create a file named `.env` in the project root directory and add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Example:

```env
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Run the Application

```bash
python main.py
```

## How It Works

1. Enter your Name and Email
2. Enter your Education Details
3. Add Skills
4. Add Projects
5. Enter your Desired Role
6. Click **Generate Resume**
7. Gemini AI generates a professional summary
8. Resume is exported as a PDF
9. Data is saved in the SQLite database

## Example AI Summary

### Input

**Role:** Python Developer

**Skills:**

* Python
* Flask
* MySQL
* Git

### Output

> Motivated Python Developer with experience in building efficient applications using Python, Flask, and MySQL. Passionate about developing scalable software solutions and solving real-world problems through technology.

## Database Schema

### Table: resumes

| Column    | Type    |
| --------- | ------- |
| id        | INTEGER |
| name      | TEXT    |
| email     | TEXT    |
| education | TEXT    |
| skills    | TEXT    |
| projects  | TEXT    |

## Requirements

```text
customtkinter
reportlab
Pillow
google-generativeai
python-dotenv
```

## Future Improvements

* ATS Resume Score Checker
* Multiple Resume Templates
* DOCX Export Support
* Profile Photo Upload
* Resume Preview Window
* LinkedIn Profile Import
* AI Skill Recommendations
* AI Project Description Generator
* Cover Letter Generator
* Dark and Light Theme Toggle

## Author

Prathmesh Nakate

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal learning purposes.
