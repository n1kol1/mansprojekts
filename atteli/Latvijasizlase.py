import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
questions = [ 
    {"question": "Kurā gadā Latvija hokeja izlase pirmo reizi piedalījās Pasaules čempionātā pēc neatkarības atgūšanas?",
     "options": ["1990", "1997", "1994", "1992"],
     "answer": "1992",
     "image": "image1.jpg"},
    {"question": "Kurš ir Latvijas hokeja izlases visu laiku rezultatīvākais spēlētājs?",
     "options": ["Kaspars Daugaviņš", "Helmuts Balderis", "Sandis Ozoliņš", "Leonīds Tambijevs"],
     "answer": "Leonīds Tambijevs",
     "image": "image2.jpg"},
    {"question": "Kurš šobrīd ir Latvijas izlases galvenais treneris?",
     "options": ["Artis Ābols", "Artūrs Irbe", "Harijs Vītoliņš", "Aigars Kalvītis"],
     "answer": "Harijs Vītoliņš",
     "image": "image3.jpg"},
    {"question": "Ar kuru numuru spēlēja Sergejs Žoltoks?",
     "options": ["33", "17", "8", "91"],
     "answer": "33",
     "image": "image4.jpg"},
    {"question": "Kurš no mūsu hokejistiem pirmais ir izcīnījis Stenlija kausu?",
     "options": ["Sandis Ozoliņš", "Sergejs Žoltoks", "Kārlis Skrastiņš", "Teodors Bļugers"],
     "answer": "Sandis Ozoliņš",
     "image": "image5.jpg"},
    {"question": "Kāda ir Latvijas izlases lielākā uzvara Pasaules čempionātā?",
     "options": ["21 : 1", "15 : 2", "27 : 0", "32 : 0"],
     "answer": "32 : 0",
     "image": "image6.jpg"},
    {"question": "Cik Olimpiskajās spēlēs ir piedalījusies Latvijas hokeja izlase?",
     "options": ["2", "6", "8", "1"],
     "answer": "6",
     "image": "image7.jpg"},
    {"question": "Kurš no šiem spēlētāju numuriem nav iemūžinātais numurs?",
     "options": ["1", "7", "19", "25"],
     "answer": "25",
     "image": "image8.jpg"},
    {"question": "Kurš spēlētājs Latvijas izlasē ir aizvadījis visvairāk spēļu (230 spēles)?",
     "options": ["Aleksandrs Ņiživijs", "Kaspars Daugaviņš", "Rodrigo Laviņš", "Leonīds Tambijevs"],
     "answer": "Rodrigo Laviņš",
     "image": "image9.jpg"},
    {"question": "Kurš spēlētājs bija pats pirmais kapteinis Latvijas izlasē?",
     "options": ["Arvīds Jurgens", "Leonīds Vedējs", "Oļegs Znaroks", "Harijs Vītoliņš"],
     "answer": "Arvīds Jurgens",
     "image": "image10.jpg"}
]
class Hockeytest:
    def __init__(self, root):
        self.root = root
        self.root.title("Latvijas hokeja izlases zināšanu tests")
        self.root.geometry("600x500")
        self.root.configure(bg="#800000")
        self.current_question = 0
        self.score = 0
        self.start_img = Image.open("sakums.jpg")
        self.start_img = self.start_img.resize((600, 350))
        self.start_photo = ImageTk.PhotoImage(self.start_img)
        self.start_label = tk.Label(self.root, image=self.start_photo, bg="#800000")
        self.start_label.pack()
        self.setup_ui()
    def setup_ui(self):
        self.label = tk.Label(self.root, text="Latvijas hokeja izlases zināšanu tests", font=("Arial", 45, "bold"), fg="white", bg="#800000")
        self.label.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Sākt testu", font=("Arial", 20), bg="#ffffff", fg="#800000", width=15, command=self.start_quiz)
        self.start_button.pack()
    def start_quiz(self):
        self.start_label.destroy()
        self.start_button.pack_forget()
        self.show_question()
    def show_question(self):
        if self.current_question < len(questions):
            question_data = questions[self.current_question]
            self.label.config(text=question_data["question"], font=("Arial", 20, "bold"))
            if hasattr(self, 'question_image_label'):
                self.question_image_label.destroy()
            img = Image.open(question_data["image"])
            img = img.resize((300, 200))
            self.question_photo = ImageTk.PhotoImage(img)
            self.question_image_label = tk.Label(self.root, image=self.question_photo, bg="#800000")
            self.question_image_label.pack()
            self.var = tk.StringVar()
            self.var.set(None)
            if hasattr(self, 'options_frame'):
                self.options_frame.destroy()
            self.options_frame = tk.Frame(self.root, bg="#800000")
            self.options_frame.pack()
            for option in question_data["options"]:
                tk.Radiobutton(self.options_frame, text=option, variable=self.var, value=option, font=("Arial", 18), bg="#800000", fg="white", selectcolor="black").pack(anchor="w", pady=5)
            if hasattr(self, 'submit_button'):
                self.submit_button.destroy()
            self.submit_button = tk.Button(self.root, text="Iesniegt", font=("Arial", 18), bg="#ffffff", fg="#800000", width=15, command=self.check_answer)
            self.submit_button.pack(pady=10)
        else:
            self.show_results()
    def check_answer(self):
        selected_answer = self.var.get()
        if selected_answer == questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        self.show_question()
    def show_results(self):
        messagebox.showinfo("Tests pabeigts", f"Jūsu rezultāts: {self.score}/{len(questions)}")
if __name__ == "__main__":
    root = tk.Tk()
    app = Hockeytest(root)
    root.mainloop()