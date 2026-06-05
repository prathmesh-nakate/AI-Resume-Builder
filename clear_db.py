import sqlite3

conn = sqlite3.connect("resume.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM resumes WHERE id = 1")

conn.commit()
conn.close()

print("Record deleted.")