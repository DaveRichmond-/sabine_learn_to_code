import review_chpt1_8


def test_1():
  value_penny = 0.01
  value_nickel = 0.05
  value_dime = 0.10
  value_quarter = 0.25
  value_dollar = 1.0
  TOTAL = 7*value_dollar + 34*value_quarter + 71*value_dime + 112*value_nickel + 42*value_penny
  
  assert review_chpt1_8.TOTAL == TOTAL, f"The value of TOTAL should be {TOTAL}"


if __name__ == '__main__':
  test_1()

  print("Congratulations!  Everything passed :) ")