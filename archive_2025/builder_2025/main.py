from htmlbuilder import HTMLBuilder
from viewer import HTMLViewer


def main() -> None:
    # --- Build UI Page ---
    builder = HTMLBuilder()
    page = (
        builder.add_title(title="My Web Page")
        .add_heading(text="Welcome to My Web Page")
        .add_paragraph("This is a simple HTML page.")
        .add_button(label="Visit ArjanCodes", onclick="https://www.arjancodes.com")
        .build()
    )

    # --- Write to HTML File ---
    file_path = "page.html"
    with open(file_path, "w") as f:
        f.write(page.render())

    # print(page.render())

    print("HTML page written to 'page.html'")

    # --- Start Viewer ---
    viewer = HTMLViewer(filename=file_path)
    viewer.start()


if __name__ == "__main__":
    main()
