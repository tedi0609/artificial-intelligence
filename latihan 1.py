{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rubby\n"
     ]
    }
   ],
   "source": [
    "nama = \"Rubby\"\n",
    "print(nama)"
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
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nama :  Mahidin \n",
      " Alamat :\n"
     ]
    }
   ],
   "source": [
    "nama = \"Mahidin \\n\"\n",
    "alamat = \"Jl. Basuki Rahmat\"\n",
    "\n",
    "print(\"Nama : \", nama, \"Alamat :\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "nilai_matematik = 85\n",
    "nilai_bahasa = 65\n",
    "\n",
    "avg = (nilai_matematik+nilai_bahasa)/2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "75.0"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[45.         12.5        35.          9.66666667]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np #mengaktifkan tipe data array\n",
    "ipk = np.array([90, 50, 70, 29])\n",
    "ipk2 = np.array([2, 4, 2, 3])\n",
    "hasil = ipk / ipk2\n",
    "\n",
    "print (hasil)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pisang\n"
     ]
    }
   ],
   "source": [
    "nama_buah = ['pisang', 'semangka', 'mangga', 'melon']\n",
    "print(nama_buah[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "001 => rekayasa Perangkat Lunak\n",
      "price01 => rekayasa Perangkat Lunak\n",
      "002 => rekayasa Perangkat Lunak\n",
      "price02 => rekayasa Perangkat Lunak\n"
     ]
    }
   ],
   "source": [
    "buku = {\n",
    "    \"001\" : \"rekayasa Perangkat Lunak\",\n",
    "    \"price01\" : \"2000\",\n",
    "    \n",
    "    \"002\" : \"Machine Learning\",\n",
    "    \"price02\" : \"25000\",\n",
    "}\n",
    "for key in buku:\n",
    "    print(key, '=>', buku[\"001\"])"
   ]
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
