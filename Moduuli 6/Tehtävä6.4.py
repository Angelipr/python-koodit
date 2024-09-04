
def laske_summa(luvut):
    sum =0
    for n in range(len(luvut)):
        sum += luvut[n]
    return sum

kokonaisluvut = [4,4,5]
print(laske_summa(kokonaisluvut))