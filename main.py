import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()
app.title("AI Resume Builder")
app.geometry("900x600")

# Title
title_label = ctk.CTkLabel(
    app,
    text="AI Resume Builder",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)

# Name
name_label = ctk.CTkLabel(app, text="Full Name")
name_label.pack()

name_entry = ctk.CTkEntry(app, width=400)
name_entry.pack(pady=5)

# Email
email_label = ctk.CTkLabel(app, text="Email")
email_label.pack()

email_entry = ctk.CTkEntry(app, width=400)
email_entry.pack(pady=5)

# Skills
skills_label = ctk.CTkLabel(app, text="Skills")
skills_label.pack()

skills_entry = ctk.CTkEntry(app, width=400)
skills_entry.pack(pady=5)

# Generate Button
generate_btn = ctk.CTkButton(
    app,
    text="Generate Resume"
)
generate_btn.pack(pady=20)

app.mainloop()