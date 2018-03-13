#!/usr/bin/env python
#coding:utf-8

from __future__ import print_function, unicode_literals
import time
import os,sys
import random

class Matrix:
    def __init__(self, col=0, height=30):
        self.height = height
        self.headcolor = 37 # white
        self.bodycolor = 32 # green
        self.bgcolor = 40 # black
        self.col = col
        self.raw = random.randrange(self.height)
        self.lenth = random.randrange(self.height/2)
        self.char = ''
        self.string = u"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()-_=+[{]}\|;:'",<.>/?ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎゐゑをんうかけゝゞ?わ"""
        self.stringlen = len(self.string)
        self.heightrange = set(range(self.height))

    def fall(self):
        headraw = self.raw
        bodyraw = headraw - 1
        tailraw = headraw - self.lenth
        # print body
        if bodyraw in self.heightrange:
            print(u'\033[{};{}H\033[{};{}m{}\033[0m'.format(bodyraw, self.col, self.bgcolor, self.bodycolor, self.char))
        # print head
        if headraw in self.heightrange:
            self.char = self.getchar()
            print(u'\033[{};{}H\033[{};{}m{}\033[0m'.format(headraw, self.col, self.bgcolor, self.headcolor, self.char))
        # print tail
        if tailraw in self.heightrange:
            print(u'\033[{};{}H\033[{};{}m \033[0m'.format(tailraw, self.col, self.bgcolor, self.bodycolor))
        if tailraw == self.height:
            self.raw = - random.randrange(self.height)
            self.lenth = random.randrange(self.height/2)
        else:
            self.raw += 1

    def getchar(self):
        char = self.string[random.randrange(self.stringlen)]
        return char

def main():
    height = 30
    width = 100
    # height, width = list(map(int, os.popen('stty size', 'r').read().split()))
    os.system('clear')
    matrixes = []
    for raw in range(height):
        print(u'\033[{};0H\033[40;32m{}'.format(raw, ' '*width))
    for col in range(width):
        matrix = Matrix(col, height)
        matrixes.append(matrix)

    while True:
        time.sleep(0.05)
        for matrix in matrixes:
            matrix.fall()

if __name__ == '__main__':
     main()
