import discriminant

def test_positive_discriminant():
    #Положительный тест: D > 0
    assert discriminant.discriminant(1, 5, 6) == 1

def test_zero_discriminant():
    #Положительный тест: D = 0
    assert discriminant.discriminant(1, 2, 1) == 0

def test_negative_discriminant():
    #Негативный тест: D < 0
    assert discriminant.discriminant(5, 2, 3) == -56