from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class HTMLPage:
    title: str
    metadata: dict[str, str]
    body: str

    def _render_metadata(self) -> str:
        return "\n".join(
            f'<meta name="{name}" content="{value}">'
            for name, value in self.metadata.items()
        )

    def render(self) -> str:
        return f"""<!DOCTYPE html>
                   <html>
                   <head>
                   <title>{self.title}</title>
                   {self._render_metadata()}
                   </head>
                   <body>
                   {self.body}
                   </body>
                   </html>"""


class HTMLBuilder:
    def __init__(self) -> None:
        self.title = ""
        self.metadata = {}
        self.body_content = []

    def add_title(self, title: str) -> Self:
        self.title = title
        return self

    def add_heading(self, text: str, level: int = 1) -> Self:
        self.body_content.append(f"<h{level}>{text}<h/{level}>")
        return self

    def add_paragraph(self, text: str) -> Self:
        self.body_content.append(f"<p>{text}</p>")
        return self

    def add_metadata(self, name: str, content: str) -> Self:
        self.metadata[name] = content
        return self

    def add_button(self, label: str, onclick: str = "#") -> Self:
        self.body_content.append(
            f"<button onclick=\"location.href='{onclick}'\">{label}</button>"
        )
        return self

    def build(self) -> HTMLPage:
        body = "\n".join(self.body_content)
        return HTMLPage(title=self.title, metadata=self.metadata, body=body)
