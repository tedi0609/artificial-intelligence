{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Menghitung Luas Lingkaran\n",
      "===========================\n",
      "masukkan jari-jari lingkaran : 3\n",
      "Luas Lingkaran dengan jari-jari 3 adalah 28.26 \n"
     ]
    }
   ],
   "source": [
    "print (\"Menghitung Luas Lingkaran\")\n",
    "print (\"===========================\")\n",
    "\n",
    "r = int(input(\"masukkan jari-jari lingkaran : \"))\n",
    "phi = 3.14\n",
    "L = phi * (r * r)\n",
    "print (\"Luas Lingkaran dengan jari-jari {} adalah {} \".format(r,L))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tulis alas segitiga: 4\n",
      "Tulis tinggi segitiga: 6\n",
      "Luas Segitiga adalah 12.00\n"
     ]
    }
   ],
   "source": [
    "alas = float(input(\"Tulis alas segitiga: \"))\n",
    "tinggi = float(input(\"Tulis tinggi segitiga: \"))\n",
    "luas = (alas * tinggi) / 2\n",
    "print(\"Luas Segitiga adalah %0.2f\" %luas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'numbers' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-f3acea549e1b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;31m#iterasi\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0meach\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mnumbers\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m     \u001b[0msum\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msum\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0meach\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;31m#output: Jumlah semuanya: ...\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'numbers' is not defined"
     ]
    }
   ],
   "source": [
    "#for\n",
    "# program untuk menemukan jumlah bilangan dalam satu list\n",
    "\n",
    "#list number\n",
    "number = [7, 5, 6, 7, 3, 4, 2, 1]\n",
    "\n",
    "#variabel untuk menyimpan jumlah\n",
    "\n",
    "sum = 0\n",
    "\n",
    "#iterasi\n",
    "for each in numbers:\n",
    "    sum = sum + each\n",
    "#output: Jumlah semuanya: ...\n",
    "print(\"Jumlah semuanya:\", sum)"
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
