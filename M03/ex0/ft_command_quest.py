#!/usr/bin/env python3
import sys


def ft_command_quest() -> None:
    argvlen: int = len(sys.argv)
    if argvlen > 1:
        print(f"Arguments received: {argvlen - 1}")
        print(f"Program name: {sys.argv[0]}")
        for i in range(1, argvlen):
            print(f"Argument {i}:", sys.argv[i])
        print(f"Total arguments: {argvlen}\n")
    else:
        print("No arguments provided!")
        print(f"Total arguments: {argvlen}\n")


if __name__ == "__main__":
    ft_command_quest()
