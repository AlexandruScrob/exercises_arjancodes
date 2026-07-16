from registry import register_command
from rich import print


@register_command("text", "whisper")
def whisper(text: str) -> None:
    print(f"[bold blue]{text.lower()}...[/bold blue]")
