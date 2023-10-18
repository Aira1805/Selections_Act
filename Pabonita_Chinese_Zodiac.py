def chinese_zodiac(year):
    zodiac_animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]
    start_year = 1924  # The first year of the Chinese zodiac cycle
    index = (year - start_year) % 12
    return zodiac_animals[index]

def find_chinese_zodiac_sign(birth_year):
    sign = chinese_zodiac(birth_year)
    return sign

# My birth year
birth_year = 2005

# Calculate my Chinese zodiac sign
zodiac_sign = find_chinese_zodiac_sign(birth_year)

print(f"I was born in the year of {birth_year}, and my Chinese zodiac sign is {zodiac_sign}.")
