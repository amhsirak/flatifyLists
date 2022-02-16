import pytest
from flatifyList.flatifyList import flatifyList

pytestmark = pytest.mark.filterwarnings("ignore")

input1 = {'a', 'b', 'c'}
input2 = 2
input3 = 'zzzz'
input4 = [[1,2], [3,[4,[5],6],7],8,9]

class TestInputType:
    def test_input_type(self):
        with pytest.raises(TypeError):
            flatifyList(input1)

        with pytest.raises(TypeError):
            flatifyList(input2)

        with pytest.raises(TypeError):
            flatifyList(input3)

        # correct construction, no errors
        flatifyList(input4)
        