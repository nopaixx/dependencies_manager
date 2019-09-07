
import pytest
from project.manager import Manager

input1 = 'test01.json'
input2 = 'test02.json'

expected1 = "DEPEND TCPIP"
expected2 = "DEPEND TCPIP"

@pytest.mark.parametrize("test_input,expected", [(input1, expected1), (input2, expected2)])
def test_expression(test_input, expected):
    manager = Manager(test_input)
    assert expected = manager.run()
