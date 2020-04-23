import main
def test_guru() :
  result=main.multiply(3, 4)
  result_2=main.multiply(13, 4)
  print('running tests...')
  assert result==12 #throws an error if result != 12
  assert result_2==13
