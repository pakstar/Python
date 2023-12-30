odd_numbers = []
even_numbers = []
kratno_3 = []

for x in range(0, 21):
    if x % 2 == 0:
        odd_numbers.append(x)
    else:
       even_numbers.append(x)
    if x %3 == 0:
        kratno_3.append(x)


print(f"{odd_numbers} Broi: {len(odd_numbers)} Suma: {sum(odd_numbers)}")
print(f"{even_numbers} Broi: {len(even_numbers)} Suma: {sum(even_numbers)}")
print(f"{kratno_3} Broi: {len(kratno_3)} Suma: {sum(kratno_3)}")

    




    