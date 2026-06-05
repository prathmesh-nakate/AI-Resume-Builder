import sqlite3

def create_database():
    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS resumes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    github TEXT,
    linkedin TEXT,
    education TEXT,
    skills TEXT,
    projects TEXT
)
""")
    conn.commit()
    conn.close()


def save_resume(
    name,
    email,
    github,
    linkedin,
    education,
    skills,
    projects
):
    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO resumes(
        name,
        email,
        github,
        linkedin,
        education,
        skills,
        projects
    )
    VALUES(?,?,?,?,?,?,?)
    """, (
        name,
        email,
        github,
        linkedin,
        education,
        skills,
        projects
    ))

    conn.commit()
    conn.close()