import review_chpt1_8


def test_1():
  
  value_penny = 1
  value_nickel = 5
  value_dime = 10
  value_quarter = 25
  value_dollar = 100
  
  TOTAL = (7*value_dollar + 34*value_quarter + 71*value_dime + 112*value_nickel + 42*value_penny) / 100
  
  assert hasattr(review_chpt1_8, 'TOTAL'), f"The variable TOTAL doesn't exist"
  assert review_chpt1_8.TOTAL == TOTAL, f"The value of TOTAL should be {TOTAL}"


if __name__ == '__main__':
  test_1()

  print("Congratulations!  Everything passed :) ")