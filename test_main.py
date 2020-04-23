import main
def test_guru() :
  result=main.multiply(3, 4)
  print('running tests...')
  assert result == 12 #throws an error if result != 12
   
