from typing import Callable
import pytest

from hypothesis import given
from hypothesis.strategies import integers, composite, SearchStrategy
from property_based_testing.office import (
    Employee,
    fire_random_employee,
    generate_random_team,
)


@composite
def teams(
    draw: Callable[[SearchStrategy[int]], int], min_value: int = 1, max_value: int = 20
):
    random_val = draw(integers(min_value, max_value))
    return generate_random_team(random_val)


@given(integers(max_value=0))
def test_negative_team_size(team_size: int):
    with pytest.raises(ValueError):
        generate_random_team(team_size)


@given(integers(min_value=1, max_value=20))
def test_team_size(team_size: int):
    assert len(generate_random_team(team_size)) == team_size


@given(teams())
def test_team_has_ceo(team: list[Employee]) -> None:
    assert Employee.CEO in team


@given(teams())
def test_fire_employee(team: list[Employee]) -> None:
    team_copy = team.copy()
    fire_random_employee(team_copy)
    assert len(team_copy) == len(team) - 1
