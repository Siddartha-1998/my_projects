{
 "cells": [
  {
   "cell_type": "raw",
   "id": "eded2796",
   "metadata": {},
   "source": [
    "FUNCTOINS TOPIC\n",
    "----------------------------\n",
    "- the func is  a reusable code in which we perform to excecute the code.\n",
    "-func can tace any data and return to its data\n",
    "-function is first class object in python\n",
    "- func does not take any thing but it can take parameters.\n",
    "\n",
    "syntax def expression:-\n",
    "----------------------------------\n",
    "        return expression variable\n",
    "        call the func by the variable\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "133f097b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(7, -1, -3, -3)\n"
     ]
    }
   ],
   "source": [
    "def add(x,y):\n",
    "    z = x + y\n",
    "    y = x - y\n",
    "    m = x * y\n",
    "    d = int(x / y)#explict type conversion.\n",
    "    return z,y,m,d\n",
    "\n",
    "result = add(3,4)\n",
    "print(result)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f38172f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total:12,average:4.0\n"
     ]
    }
   ],
   "source": [
    "def sum_avg(x,y,z):\n",
    "    s = x + y + z\n",
    "    a = s/3.0\n",
    "    return s,a\n",
    "\n",
    "total , avg = sum_avg(3,4,5)\n",
    "print(\"total:{},average:{}\".format(total,avg))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "25041583",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def add(x,y,z):\n",
    "    s = x + y + z\n",
    "    return s\n",
    "a = 2\n",
    "b = 4 \n",
    "sum = add(a,b,4)\n",
    "sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0638f0c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "a874b33f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9, 24, -5, 18446744073709551616, 0.16666666666666666)"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def add(x,y,z):\n",
    "\n",
    "    s = x + y + z,x*y*z,x-y-z,x**y**z,x/y/z\n",
    "    \n",
    "    return s\n",
    "\n",
    "#driver code.\n",
    "                        \n",
    "a = 2\n",
    "b = 4 \n",
    "c = 3\n",
    "\n",
    "sum1 = add(a,b,c)\n",
    "sum1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "1d07d512",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "847213da",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e80c88b1",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
