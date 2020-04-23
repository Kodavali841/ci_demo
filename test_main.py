import main
def test_guru() :
  result=main.multiply(3, 4)
  print('running tests...')
  assert result==12 #throws an error if result != 12

def test_addn():
  result_3= main.addition(4,7)
  assert result_3 == 1
  
