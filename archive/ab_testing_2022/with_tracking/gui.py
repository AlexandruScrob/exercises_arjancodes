from typing import Callable
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

DEFAULT_FILENAME = "untitled.txt"


class WorsePad(tk.Tk):
    def __init__(
        self, post_event: Callable[[str], None], show_save_button: bool = True
    ) -> None:
        super().__init__()
        self.title("Worsepad")
        self.geometry("400x250+300+300")
        self.file_path = Path.cwd() / DEFAULT_FILENAME
        self.show_save_button = show_save_button
        self.post_event = post_event
        self.create_ui()

    def create_ui(self) -> None:
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        for label, command in (
            ("Open", self.on_open),
            ("Clear", self.on_clear),
            ("Save", self.on_save),
            ("Exit", self.quit),
        ):
            file_menu.add_command(label=label, command=command)

        menubar.add_cascade(label="File", menu=file_menu)

        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=1)

        if self.show_save_button:
            save_button = tk.Button(frame, text="Save", command=self.on_button_save)
            save_button.pack(anchor="e", padx=5, pady=5)

        self.text = tk.Text(frame)
        self.text.pack(fill=tk.BOTH, expand=1)

        result: str = messagebox.askquestion(  # type: ignore
            "Privacy check",
            "Do you want to share usage statistics with us?",
            icon="warning",
        )

        if result == "no":
            self.post_event = lambda _: None

    def on_open(self) -> None:
        file_str = filedialog.askopenfilename(title="Select file")

        if not file_str:
            return

        self.file_path = Path(file_str)
        text_content = self.file_path.read_text(encoding="latin-1")

        self.on_clear()
        self.text.insert(tk.END, text_content)

    def on_clear(self) -> None:
        self.text.delete(1.0, tk.END)

    def on_button_save(self) -> None:
        self.post_event("save_button_clicked")
        self.save()

    def save(self) -> None:
        self.file_path.write_text(self.text.get(1.0, tk.END), encoding="latin-1")
