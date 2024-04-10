import terminal
import sys

sys.setrecursionlimit(100000)

def blue(text):
    return terminal.bold(terminal.blue(text))

def bold(text):#高亮
    return terminal.bold(text)

def red(text):
    return terminal.bold(terminal.red(text))