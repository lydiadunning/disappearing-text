from tkinter import Tk, Text


class Timer:
    def __init__(self):
        self.gray_timer = None
        self.deletion_timer = None
        self.ms_until_delete = 5000
        self.ms_until_gray = 2000

    def start(self, *args):
        if self.gray_timer:
            text_box.config(fg='black')
            window.after_cancel(self.gray_timer)
            window.after_cancel(self.deletion_timer)
        self.gray_timer = window.after(self.ms_until_gray, self.count_down)
        self.deletion_timer = window.after(self.ms_until_delete, self.delete_text)

    def count_down(self, count=3, grey_num=20):
        gray_increment_ms = 1000
        if count > 0:
            text_box.config(fg=f'grey{grey_num}')
            self.gray_timer = window.after(gray_increment_ms, self.count_down, count - 1, grey_num * 2)

    def delete_text(self):
        text_box.delete(1.0, 'end')
        window.after_cancel(self.gray_timer)
        window.after_cancel(self.deletion_timer)
        text_box.config(fg='black')
        self.gray_timer = None


timer = Timer()

window = Tk()
window.config(padx=50, pady=50)
window.title("Don't Stop Typing")

text_box = Text(window, width=60, height=30)
text_box.grid(row=0, column=0)
text_box.bind("<Key>", timer.start)

window.mainloop()
