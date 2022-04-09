{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "()\n",
      "(1,)\n",
      "(1, 2, 3)\n",
      "('hello', [1, 2, 3], (4, 5, 6))\n",
      "1 2 3\n"
     ]
    }
   ],
   "source": [
    "#membuat tuple kosong\n",
    "#Output: ( )\n",
    "my_tuple = ()\n",
    "print(my_tuple)\n",
    "\n",
    "# tuple dengan 1 elemen\n",
    "# Output: (1,)\n",
    "my_tuple = (1,)\n",
    "\n",
    "print (my_tuple)\n",
    "\n",
    "# tuple berisi integer\n",
    "# output = (1, 2, 3)\n",
    "my_tuple = (1, 2, 3)\n",
    "print(my_tuple)\n",
    "\n",
    "# tuple bersarang \n",
    "# Output: (\"hello\", [1, 2, 3], (4, 5, 6))\n",
    "my_tuple = (\"hello\", [1, 2, 3], (4, 5, 6))\n",
    "print(my_tuple)\n",
    "\n",
    "# Tuple bisa tidak menggunakan tanda ()\n",
    "# output (1, 2, 3)\n",
    "my_tuple = 1, 2, 3\n",
    "\n",
    "# memasukkan anggota tuple ke variabel yang bersesuaian\n",
    "# a akan berisi 1, b berisi 2, dan c berisi 3\n",
    "# output 1 2 3\n",
    "a, b, c = my_tuple\n",
    "print(a, b, c)"
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
      "p\n",
      "y\n",
      "n\n",
      "o\n"
     ]
    }
   ],
   "source": [
    "my_tuple = ('p', 'y', 't', 'o', 'n')\n",
    "# output: 'p'\n",
    "print(my_tuple[0])\n",
    "\n",
    "# output: 'y'\n",
    "print(my_tuple[1])\n",
    "\n",
    "# output: 'n'\n",
    "print(my_tuple[-1])\n",
    "\n",
    "# output: 'o'\n",
    "print(my_tuple[-2])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3, 4, [7, 6])\n",
      "('p', 'y', 't', 'h', 'o', 'n')\n"
     ]
    }
   ],
   "source": [
    "my_tuple = (2, 3, 4, [5, 6])\n",
    "# kita tidak bisa mengubah anggota tuple\n",
    "# bila kita hilangkan tanda komentar # pada baris 6\n",
    "# akan muncul error: # Typeerror: 'tuple' object does not support item assignment\n",
    "# my_tuple[1] = 8\n",
    "\n",
    "# tapi list dalam tuple bisa diubah\n",
    "# output : (2, 3, 4, [7, 6])\n",
    "my_tuple[3][0] = 7\n",
    "print(my_tuple)\n",
    "\n",
    "# tuple bisa diganti secara keseluruhan dengan penugasan kembali\n",
    "# output: ('p', 'y', 't', 'h', 'o', 'n')\n",
    "my_tuple = ('p', 'y', 't', 'h', 'o', 'n')\n",
    "print(my_tuple)\n",
    "\n",
    "# anggota tuple juga tidak bisaa dihapus menggunakan del\n",
    "# perintah berikut akan menghasilkan error typeerror\n",
    "# kalau anda menghilangkan tanda komentar #\n",
    "\n",
    "# del my_tuple[0]\n",
    "\n",
    "# kita bisa menghapus tuple keseluruhan\n",
    "\n",
    "del my_tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "my_tuple = (1, 2, 3, 'a', 'b', 'c')\n",
    "\n",
    "# menggunakan in\n",
    "# output: True\n",
    "print('3' in my_tuple)\n",
    "\n",
    "# output: false\n",
    "print('e' in my_tuple)\n",
    "\n",
    "# menggunakan not in\n",
    "# output True\n",
    "print('k' not in my_tuple)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi Galih\n",
      "Hi Ratna\n"
     ]
    }
   ],
   "source": [
    "# output:\n",
    "# Hi Galih\n",
    "# Hi Ratna\n",
    "nama = ('Galih', 'Ratna')\n",
    "for name in nama:\n",
    "    print('Hi', name)\n"
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
      "2\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "my_tuple = ('p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o')\n",
    "# count\n",
    "# output: 2\n",
    "print(my_tuple.count('n'))\n",
    "\n",
    "# index\n",
    "# Output 4\n",
    "print(my_tuple.index('n'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3}\n",
      "{1, 2, 3}\n",
      "{1, 2.0, (3, 4, 5), 'Phyton'}\n",
      "{1, 2, 3}\n"
     ]
    }
   ],
   "source": [
    "# set integer\n",
    "my_set = {1,2,3}\n",
    "print(my_set)\n",
    "\n",
    "# set dengan menggunakan fungsi set()\n",
    "my_set = set([1,2,3])\n",
    "print(my_set)\n",
    "\n",
    "#set data campuran\n",
    "my_set = {1, 2.0, \"Phyton\", (3,4,5)}\n",
    "print(my_set)\n",
    "\n",
    "# bila kita mengisi duplikasi, set akan menghilangkan salah satu\n",
    "# output: {1,2,3}\n",
    "my_set = {1,2,2,3,3,3}\n",
    "print(my_set)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4}\n",
      "{1, 2, 3, 4, 5, 6}\n"
     ]
    }
   ],
   "source": [
    "# bila kita hilangkan tanda # dari baris 9 akan muncul error TypeError\n",
    "# my_set[0]\n",
    "\n",
    "# menambah satu anggota\n",
    "# output: {1,2,3,4}\n",
    "my_set.add(4)\n",
    "print(my_set)\n",
    "\n",
    "# menambah beberapa anggota\n",
    "# set akan menghilankan duplikasi\n",
    "# output: {1,2,3,4,5,6}\n",
    "my_set.update([3,4,5,6])\n",
    "print(my_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5}\n",
      "{1, 2, 3, 5}\n",
      "{1, 2, 3}\n"
     ]
    }
   ],
   "source": [
    "# membuat set baru\n",
    "my_set = {1, 2, 3, 4, 5}\n",
    "print(my_set)\n",
    "\n",
    "# menghapus 4 dengan discard\n",
    "# output: {1, 2, 3, 5}\n",
    "my_set.discard(4)\n",
    "print(my_set)\n",
    "\n",
    "#menghapus 5 dengan remove\n",
    "# output : {1, 2, 3}\n",
    "my_set.remove(5)\n",
    "print(my_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'o', 't', 'l', 'h', 'e', 'n', 'P'}\n",
      "o\n",
      "t\n",
      "set()\n"
     ]
    }
   ],
   "source": [
    "# membuat set baru\n",
    "# output: set berisi anggota yang unik\n",
    "my_set = set(\"helloPhthon\")\n",
    "print(my_set)\n",
    "\n",
    "# pop anggota\n",
    "# output: anggota acak\n",
    "print(my_set.pop())\n",
    "\n",
    "# pop anggota lainnya\n",
    "# output: anggota acak\n",
    "print(my_set.pop())\n",
    "\n",
    "# mengosongkan set\n",
    "# output: set()\n",
    "my_set.clear()\n",
    "print(my_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5, 6, 7, 8}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6, 7, 8}"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# membuat set A and B\n",
    "A = {1, 2, 3, 4, 5}\n",
    "B = {4, 5, 6, 7, 8}\n",
    "\n",
    "#Gabungan menggunakan operator |\n",
    "# output: {1, 2, 3, 4, 5, 6, 7, 8}\n",
    "print(A | B)\n",
    "\n",
    "# Menggunakan fungsi union()\n",
    "# output: {1, 2, 3, 4, 5, 6, 7, 8}\n",
    "A.union(B)\n",
    "\n",
    "# output: {1, 2, 3, 4, 5, 6, 7, 8}\n",
    "B.union(A)"
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
      "{4, 5}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{4, 5}"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# membuat set A and B\n",
    "A = {1, 2, 3, 4, 5}\n",
    "B = {4, 5, 6, 7, 8}\n",
    "\n",
    "#irisan menggunkan operator &\n",
    "# output: {4,5}\n",
    "print(A & B)\n",
    "# menggunakan fungsi intersection()\n",
    "#output: {4,5}\n",
    "A.intersection(B)\n",
    "\n",
    "#output: {4,5}\n",
    "B.intersection(A)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3}\n",
      "{8, 6, 7}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{6, 7, 8}"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# membuat A and B\n",
    "A = {1, 2, 3, 4, 5}\n",
    "B = {4, 5, 6, 7, 8}\n",
    "\n",
    "# Menggunakan operator - pada A\n",
    "# Output: {1, 2, 3}\n",
    "print(A - B)\n",
    "\n",
    "# output: {1, 2, 3}\n",
    "A.difference(B)\n",
    "\n",
    "# menggunakan operator - pada B\n",
    "# output: {8, 6, 7}\n",
    "print(B - A)\n",
    "\n",
    "#output: {8, 6, 7}\n",
    "B.difference(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 6, 7, 8}\n",
      "{1, 2, 3, 6, 7, 8}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 6, 7, 8}"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# membuat A and B\n",
    "A = {1, 2, 3, 4, 5}\n",
    "B = {4, 5, 6, 7, 8}\n",
    "\n",
    "# menggunakan operator ^ pada A\n",
    "# output: {1, 2, 3, 6, 7, 8}\n",
    "print(A ^ B)\n",
    "\n",
    "#output: {1, 2, 3, 6, 7, 8}\n",
    "A.symmetric_difference(B)\n",
    "\n",
    "# menggunakan operator ^ pada B\n",
    "# output: {1, 2, 3, 6, 7, 8}\n",
    "print(B ^ A)\n",
    "\n",
    "# output: {1, 2, 3, 6, 7, 8}\n",
    "B.symmetric_difference(A)"
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
