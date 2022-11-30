from gui import WorsePad
from dotenv import load_dotenv

from feature import read_config
from event import post_event


def main():
    load_dotenv()
    config = read_config()
    app = WorsePad(post_event=post_event, show_save_button=config.show_save_button)
    app.mainloop()


if __name__ == "__main__":
    main()
