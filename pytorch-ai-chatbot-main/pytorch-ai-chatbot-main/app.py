from tkinter import *
import tkinter as tk
from chat import get_response, bot_name

BG_GRAY = "#11d9f0"
BG_COLOR = "#fcfcfc"
TEXT_COLOR = "#070808"

FONT = "Calibri 14"
FONT_BOLD = "Serif 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def restore_down():
        root.attributes('-zoomed', True)
        root = tk.Tk()
        restore_button = tk.Button(root, text="Restore Down")
        restore_button.pack()
        root.mainloop()

    def scroll_bar():
       root = tk.Tk()
       output_text = tk.Text(root)
       output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       scrollbar = tk.Scrollbar(root)
       scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       output_text.config(yscrollcommand=scrollbar.set)
       scrollbar.config(command=output_text.yview)
       root.mainloop()
    
   

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="NSB Chat Assistant", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)



        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry = Entry(bottom_label, bg="#f0f0f0", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg="#f03554",
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
    
    def _insert_message(self, msg, sender):
        # sourcery skip: extract-duplicate-method
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()