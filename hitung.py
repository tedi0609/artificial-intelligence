tinggi = 100
sampai = 0
hari = 0

while sampai < tinggi:
    jam = 0;
    while jam <= 24 and sampai < tinggi:
        if jam == 12:
            sampai += 5
            hari += 1
        if jam == 24:
            sampai -= 4
        jam += 12
    print('hari '+str(hari)+' bekicot naik '+ str(sampai) +' meter')
