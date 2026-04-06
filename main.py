import tkinter as tk
import random

def get_answer():
    question = entry.get()
    if not question:
        label_answer.config(text="Posez une question d'abord !")
        return
    
    answers = [
        "Oui, absolument !",
        "Non, pas du tout.",
        "Peut-être...",
        "Demande plus tard.",
        "C'est très probable.",
        "C'est impossible.",
        "Les astres disent que oui.",
        "La réponse est floue.",
        "Oublie ça.",
        "Absolument pas !"
    ]
    answer = random.choice(answers)
    label_answer.config(text=answer)

root = tk.Tk()
root.title("Boule de Cristal")
root.geometry("400x300")

label_title = tk.Label(root, text="La Boule de Cristal", font=("Helvetica", 18, "bold"))
label_title.pack(pady=20)

label_instr = tk.Label(root, text="Posez votre question :")
label_instr.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

btn = tk.Button(root, text="Consulter la boule", command=get_answer)
btn.pack(pady=10)

label_answer = tk.Label(root, text="", font=("Helvetica", 14, "italic"), fg="blue")
label_answer.pack(pady=20)

root.mainloop()
