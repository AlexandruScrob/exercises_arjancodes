from hypothesis import given, example, settings
from hypothesis.strategies import text

from property_based_testing.example import from_ascii_codes, to_ascii_codes


@given(text())
@example("")
@settings(max_examples=100)
def test_decode_inverts_encode(test_str: str) -> None:
    assert from_ascii_codes(to_ascii_codes(test_str)) == test_str


@given(text())
def test_list_length_same_as_input_str(test_str: str) -> None:
    encoded = to_ascii_codes(test_str)
    assert len(encoded) == len(test_str)
