import tkinter as tk
from code import generate_game_idea

def create_border_frame(master, border_width=5, padx=10, pady=10):
    bg_color = master.cget("bg")
    frame = tk.Frame(master, highlightthickness=border_width, padx=padx, pady=pady, bg=bg_color, highlightbackground=bg_color)
    frame.pack(padx=padx, pady=pady, fill='both', expand=True)

def generate_and_display_idea():
    for widget in generated_frame.winfo_children():
        widget.destroy()

    game_idea = generate_game_idea()

    generated_label = tk.Label(generated_frame, text=game_idea, font=("Arial", 15), bg="#FFFFFF", fg="#13293D", wraplength=700, justify="left", highlightthickness=2, highlightbackground="#424B54")
    generated_label.pack(pady=10, anchor='center')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("InnoGameLab Game Generator")
    root.geometry("450x650")
    root.configure(bg="#9DB4C0")

    top_frame = tk.Frame(root, bg="#9DB4C0")
    top_frame.pack(side="top", fill='x')

    labels_text = ["I", "N", "N", "O", "G", "A", "M", "E", "L", "A", "B"]
    label_colors = ["#CA3C25","#CFFFB0", "#4D5382", "#C9C5BA", "#698996", "#ACEDFF", "#E9FF70", "#FBFEF9", "#F4AFB4", "#315C2B", "#BA324F"]
    for text, color in zip(labels_text, label_colors):
        label = tk.Label(top_frame, text=text, font=("Arial", 23), bg="#9DB4C0", fg=color)
        label.pack(side="left", padx=(5, 10))
    create_border_frame(root, border_width=5)

    generated_frame = tk.Frame(root, bg="#9DB4C0")
    generated_frame.pack(fill='x', padx=10, pady=10)

    button_frame = tk.Frame(root, bg="#9DB4C0")
    button_frame.pack(fill='x', padx=10, pady=10)

    generate_button = tk.Button(button_frame, text="Generate Game Idea", font=("Arial", 15), command=generate_and_display_idea)
    generate_button.pack()

    root.mainloop()
