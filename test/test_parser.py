
import pytest
from project.command_parser import CommandParser


input1 = {
}

input2 = {
        }
expected1 = ""
expected2 = ""

@pytest.mark.parametrize("test_input,expected", [(input1, expected1), (input2, expected2)])
def test_expression(test_input, expected):
    assert expected == json_to_where(test_input)

