{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 lebih besar dibandingkan 8\n"
     ]
    }
   ],
   "source": [
    "nilai = 10\n",
    "\n",
    "if (nilai > 8):\n",
    "    print(\"10 lebih besar dibandingkan 8\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Selamat Anda Lulus\n"
     ]
    }
   ],
   "source": [
    "nilai_ujian = 61\n",
    "\n",
    "if (nilai_ujian > 60):\n",
    "    print(\"Selamat Anda Lulus\")\n",
    "else:\n",
    "    print(\"Maaf Anda Mengulang Semster Depan. !\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masukkan Nilai1\n"
     ]
    }
   ],
   "source": [
    "nilai = int(input(\"Masukkan Nilai\"))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "E\n"
     ]
    }
   ],
   "source": [
    "nilai = 45\n",
    "\n",
    "if(nilai >= 80):\n",
    "    print(\"A\")\n",
    "elif(nilai >=70):\n",
    "    print(\"B\")\n",
    "elif(nilai >=60):\n",
    "    print(\"C\")\n",
    "elif(nilai >=50):\n",
    "    print(\"D\")\n",
    "else:\n",
    "    print(\"E\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Aku suka stmik\n",
      "Aku suka stmik\n",
      "Aku suka stmik\n",
      "Aku suka stmik\n",
      "Aku suka stmik\n",
      "Aku suka stmik\n",
      "Aku suka stmik\n",
      "Aku suka stmik\n",
      "Aku suka stmik\n",
      "Aku suka stmik\n"
     ]
    }
   ],
   "source": [
    "hitung = 0\n",
    "while(hitung < 10):\n",
    "    hitung = hitung + 1\n",
    "    print(\"Aku suka stmik\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jurusan Sistem Informasi\n",
      "Jurusan Sistem Informasi\n",
      "Jurusan Sistem Informasi\n",
      "Jurusan Teknik Informatika\n"
     ]
    }
   ],
   "source": [
    "#while loop dengan kombinasi else\n",
    "hitung = 0\n",
    "while (hitung < 3):\n",
    "    hitung = hitung + 1\n",
    "    print(\"Jurusan Sistem Informasi\")\n",
    "else:\n",
    "    print(\"Jurusan Teknik Informatika\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "#for loop\n",
    "angka = [1,2,3,4,5]\n",
    "for x in angka:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jurusan di STMIK Lombok adalah :  Sistem Informasi\n",
      "Jurusan di STMIK Lombok adalah :  Teknik Informatika\n",
      "Jurusan di STMIK Lombok adalah :  Bisnis Digital\n"
     ]
    }
   ],
   "source": [
    "prodi = [\"Sistem Informasi\", \"Teknik Informatika\", \"Bisnis Digital\"]\n",
    "for jurusan in prodi:\n",
    "    print(\"Jurusan di STMIK Lombok adalah : \", jurusan)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mahidin,  Mengambil Jurusan : Data Mining\n",
      "Mahidin,  Mengambil Jurusan : Kecerdasan Buatan\n",
      "Mahidin,  Mengambil Jurusan : Pemrograman Berorientasi Objek\n",
      "Saikin Mengambil Jurusan : Data Mining\n",
      "Saikin Mengambil Jurusan : Kecerdasan Buatan\n",
      "Saikin Mengambil Jurusan : Pemrograman Berorientasi Objek\n",
      "Ali Mengambil Jurusan : Data Mining\n",
      "Ali Mengambil Jurusan : Kecerdasan Buatan\n",
      "Ali Mengambil Jurusan : Pemrograman Berorientasi Objek\n"
     ]
    }
   ],
   "source": [
    "#nested loop\n",
    "Mahasiswa = [\"Mahidin, \",\"Saikin\",\"Ali\"]\n",
    "Matakuliah = [\"Data Mining\", \"Kecerdasan Buatan\",\"Pemrograman Berorientasi Objek\"]\n",
    "\n",
    "for mhs in Mahasiswa:\n",
    "    for matkul in Matakuliah:\n",
    "        print(mhs, \"Mengambil Jurusan :\", matkul)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah semuanya: 46\n"
     ]
    }
   ],
   "source": [
    "# for\n",
    "# program untuk menemukan jumlah bilangan dalam satu list\n",
    "\n",
    "#list number\n",
    "numbers = [7, 5, 9, 8, 4, 2, 6, 4, 1]\n",
    "\n",
    "#variabel untuk menyimpan jumlah\n",
    "\n",
    "sum = 0\n",
    "\n",
    "# iterasi \n",
    "for each in numbers:\n",
    "    sum = sum + each\n",
    "    \n",
    "#output: Jumlah semuanya: 46\n",
    "print(\"Jumlah semuanya:\", sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Kolak\n",
      "Es Campur\n",
      "Kurma\n",
      "Sirup\n"
     ]
    }
   ],
   "source": [
    "takjil = ['Kolak', 'Es Campur', 'Kurma', 'Sirup']\n",
    "for i in takjil:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 11):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2  adalah bilangan prima\n",
      "3  adalah bilangan prima\n",
      "5  adalah bilangan prima\n",
      "7  adalah bilangan prima\n",
      "11  adalah bilangan prima\n",
      "13  adalah bilangan prima\n",
      "17  adalah bilangan prima\n",
      "19  adalah bilangan prima\n",
      "23  adalah bilangan prima\n",
      "29  adalah bilangan prima\n",
      "Good bye!\n"
     ]
    }
   ],
   "source": [
    "#nested loop / perulangan di dalam perulangan\n",
    "#program untuk menampilkan bilangan prima dari 2 s/d 30\n",
    "\n",
    "i=2\n",
    "while (i<30):\n",
    "    j=2\n",
    "    while(j <= (i/j)):\n",
    "        if not(i%j): break\n",
    "        j = j+1\n",
    "    if (j > i/j) : print (i, \" adalah bilangan prima\")\n",
    "    i = i + 1\n",
    "print (\"Good bye!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Perulangan luar [i] =  0\n",
      "   Perulangan dalam [i, j] =  0, 0\n",
      "   Perulangan dalam [i, j] =  0, 1\n",
      "   Perulangan dalam [i, j] =  0, 2\n",
      "   Perulangan dalam [i, j] =  0, 3\n",
      "   Perulangan dalam [i, j] =  0, 4\n",
      "Perulangan luar [i] =  1\n",
      "   Perulangan dalam [i, j] =  1, 0\n",
      "   Perulangan dalam [i, j] =  1, 1\n",
      "   Perulangan dalam [i, j] =  1, 2\n",
      "   Perulangan dalam [i, j] =  1, 3\n",
      "   Perulangan dalam [i, j] =  1, 4\n",
      "Perulangan luar [i] =  2\n",
      "   Perulangan dalam [i, j] =  2, 0\n",
      "   Perulangan dalam [i, j] =  2, 1\n",
      "   Perulangan dalam [i, j] =  2, 2\n",
      "   Perulangan dalam [i, j] =  2, 3\n",
      "   Perulangan dalam [i, j] =  2, 4\n"
     ]
    }
   ],
   "source": [
    "for i in range(3):\n",
    "  print('Perulangan luar [i] = ', i)\n",
    "\n",
    "  for j in range(5):\n",
    "    print('   Perulangan dalam [i, j] = ', str(i) + ', ' + str(j))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
