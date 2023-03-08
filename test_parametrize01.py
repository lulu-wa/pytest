import pytest
@pytest.mark.parametrize('name', ['元宝'])
def test_parametrize01(name):
    print(f'我是{name}')

@pytest.mark.parametrize('name', ['元宝', '小虎'])
def test_parametrize02(name):
    print('我是+name')
    assert name == '元宝'

@pytest.mark.parametrize('name, age',(['元宝', '7months'], ['小虎', '1year old']))
def test_parametrize03(name, age):
    print(f'我是{name}, 我已经{age}了')

@pytest.mark.parametrize('name, age',[['元宝', '7months'], ['小虎', '1year old']])
def test_parametrize04(name, age):
    print(f'我是{name}, 我已经{age}了')

@pytest.mark.parametrize('name',[{'name':'元宝'}, {'name':'小虎'}])
def test_parametrize03(name):
    print(name['name'])
from utils.read_data import get_data


@pytest.mark.parametrize('name', get_data['poem_names'])
def test_parametrize03(name):
    print(name)

@pytest.mark.parametrize('name, poem', get_data['poem_introduction'])
def test_parametrize03(name, poem):
    print(f'{name}-{poem}')

