from tkinter import Tk, Text


class Timer:
    def __init__(self):
        self.active_timer = None
        self.delete_timer = None
        self.time_in_ms = 5000

    def start(self, *args):
        if self.active_timer:
            text_box.config(fg='black')
            window.after_cancel(self.active_timer)
            window.after_cancel(self.delete_timer)
        self.active_timer = window.after(2000, self.count_down)
        self.delete_timer = window.after(self.time_in_ms, self.delete_everything)

    def count_down(self, count=3, grey_num=20):
        if count > 0:
            text_box.config(fg=f'grey{grey_num}')
            self.active_timer = window.after(1000, self.count_down, count-1, grey_num*2)

    def delete_everything(self):
        text_box.delete(1.0, "end")
        text_box.config(fg='black')
        self.active_timer = None


timer = Timer()

window = Tk()
window.config(padx=50, pady=50)
window.title("Don't Stop Typing")

text_box = Text(window, width=60, height=30)
text_box.grid(row=0, column=0)
text_box.bind("<Key>", timer.start)

window.mainloop()
