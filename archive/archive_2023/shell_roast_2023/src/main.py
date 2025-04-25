"""

Author: Hossin azmoud (Moody0101)
Date: 10/18/2022
LICENCE: MIT
Language: Python3.10

"""

from time import sleep
from colorama import Fore as f
from hedshell.core import add_command, run_shell
from hedshell.api import (
    hashing_algos,
    encoding_algos,
    decoding_algos,
    has_hashing_algo,
    hash_val,
    has_encoding_algo,
    encode,
    has_decoding_algo,
    decode,
)

DOC = f"""{f.YELLOW}

	Author: Hossin azmoud (Moody0101)
	Date: 10/18/2022
	LICENCE: MIT
	Language: {f.CYAN}Python3.10 {f.YELLOW}
	Descripion: A tool to hash, encode, decode text.
	command: hash, encode, decode, help, exit
	Usage: 
		To encode/Decode:
			Encode/Decode <Text> <Algorithm>
			Encode/Decode only for help.
		To hash:
			Hash <Text> <Algorithm>
			Hash only for help.
"""


HELP_DOC = """

	To encode/Decode:
		Encode/Decode <Text> <Algorithm>
		Encode/Decode only for help.
	To hash:
		Hash <Text> <Algorithm>
		Hash only for help.

		"""


HASH_DOC = f"""
  Syntax: Hash <InputText> < {" | ".join(hashing_algos())} >
	"""

ENCODE_DOC = f"""
Syntax: Encode <InputText> < {" | ".join(encoding_algos())} >
"""

DECODE_DOC = f"""
Syntax: Decode <InputText> < {" | ".join(decoding_algos())} >
"""


def help_shell(_: list[str]) -> None:
    print(HELP_DOC)


def exit_shell(_: list[str]) -> None:
    for i in [".", "..", "..."]:
        print(f"  Exiting{i}", end="\r")
        sleep(1)
    exit(0)


def hash_shell(args: list[str]) -> None:
    if len(args) != 2:
        print(HASH_DOC)
        return

    text, hashing_algo = args

    if not has_hashing_algo(hashing_algo):
        print(f"{f.RED}unknown algorithm name, {hashing_algo}")
        print(HASH_DOC)
        return

    hashed_text = hash_val(text, hashing_algo)

    print(hashed_text)


def encode_shell(args: list[str]) -> None:
    if len(args) != 2:
        print(ENCODE_DOC)
        return

    text, encoding_algo = args

    if not has_encoding_algo(encoding_algo):
        print(f"{f.RED}unknown algorithm name, {encoding_algo}")
        print(ENCODE_DOC)
        return

    encoded_text = encode(text, encoding_algo)

    print(encoded_text)


def decode_shell(args: list[str]) -> None:
    if len(args) != 2:
        print(DECODE_DOC)
        return

    text, decoding_algo = args

    if not has_decoding_algo(decoding_algo):
        print(f"{f.RED}unknown algorithm name, {decoding_algo}")
        print(DECODE_DOC)
        return

    decoded_text = decode(text, decoding_algo)

    print(decoded_text)


def main():
    add_command("help", help_shell)
    add_command("exit", exit_shell)
    add_command("hash", hash_shell)
    add_command("encode", encode_shell)
    add_command("decode", decode_shell)
    print(DOC)
    run_shell()


if __name__ == "__main__":
    main()
