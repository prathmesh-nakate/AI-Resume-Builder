import customtkinter as ctk

from ai_helper import generate_summary
from resume_generator import create_resume
from database import save_resume
from database import create_database

create_database()

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("900x700")
app.title("AI Resume Builder")

title = ctk.CTkLabel(
    app,
    text="AI Resume Builder",
    font=("Arial", 30, "bold")
)

title.pack(pady=15)

entries = {}

fields = [
    "Name",
    "Email",
    "Role",
    "Education",
    "Skills",
    "Projects"
]

for field in fields:

    label = ctk.CTkLabel(app,
                         text=field)

    label.pack()

    entry = ctk.CTkEntry(
        app,
        width=500
    )

    entry.pack(pady=5)

    entries[field] = entry


def build_resume():

    name = entries["Name"].get()
    email = entries["Email"].get()
    role = entries["Role"].get()
    education = entries["Education"].get()
    skills = entries["Skills"].get()
    projects = entries["Projects"].get()

    summary = generate_summary(
        role,
        skills
    )

    create_resume(
        f"resumes/{name}.pdf",
        name,
        email,
        education,
        skills,
        projects,
        summary
    )

    save_resume(
        name,
        email,
        education,
        skills,
        projects
    )

    result.configure(
        text="Resume Generated Successfully!"
    )


btn = ctk.CTkButton(
    app,
    text="Generate Resume",
    command=build_resume
)

btn.pack(pady=20)

result = ctk.CTkLabel(
    app,
    text=""
)

result.pack()

app.mainloop()