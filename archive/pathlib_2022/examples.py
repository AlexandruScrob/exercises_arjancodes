from os import chdir
from pathlib import Path


def main() -> None:
    # current working directory and home directory
    print(f"Current working directory: {Path.cwd()}.")
    print(f"Home directory: {Path.home()}.")

    # creating paths
    path = Path("/usr/bin/python3")

    # using backslashes on Windows
    path = Path(r"c:\Windows\System32\cmd.exe")
    print(path.exists())

    # using forward slash operator
    path = Path("c:") / "Windows" / "System32" / "cmd.exe"
    print(path.exists())

    # using joinpath
    path = Path("/usr").joinpath("bin", "python3")

    # reading a file from a path
    path = Path.cwd() / "pathlib_2022" / "settings.yaml"
    print(path.exists())
    with path.open() as file:
        print(file.read())

    # reading a file from a path using read_text
    print(path.read_text())

    # resolving a path
    path = Path("pathlib_2022/settings.yaml")
    print(path)
    print(path.resolve())  # absolute

    # parent - relative path
    print(f"Parent: {path.parent}")

    # path member variables
    full_path = path.resolve()
    print(f"Parent: {full_path.parent}")
    print(f"Grand-Parent: {full_path.parent.parent}")
    print(f"Name: {full_path.name}")
    print(f"Stem: {full_path.stem}")
    print(f"Suffix: {full_path.suffix}")

    # check whether a path is a file or a folder
    print(f"Is directory: {full_path.is_dir()}.")
    print(f"Is file: {full_path.is_file()}.")

    # creating and deleting files and directories
    new_file = Path.cwd() / "pathlib_2022" / "new_file.txt"
    new_file.touch()
    new_file.write_text("Hello")
    new_file.unlink()
    new_dir = Path.cwd() / "pathlib_2022" / "new_dir"
    new_dir.mkdir()

    chdir(new_dir)
    print(f"Current working directory: {Path.cwd()}")

    chdir(Path.cwd().parent)
    new_dir.rmdir()


if __name__ == "__main__":
    main()
