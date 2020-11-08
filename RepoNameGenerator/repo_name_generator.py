#!/usr/bin/env/python3
import random
import argparse

style_options = ['camel', 'space', 'snake']
parser = argparse.ArgumentParser(description='Generate a name for a repository.')
parser.add_argument('--style', default='space', choices=style_options,
                    help='choose name style')
args = parser.parse_args()


def list_from_txt(filename: str):
    """ Generate list from lines in a given text file """
    file = open(filename, 'r')
    result = [line.rstrip() for line in file.readlines()]
    file.close()
    return result


adj = list_from_txt('adjectives.txt')

noun = list_from_txt('nouns.txt')

adj2 = ['' for i in range(300)]
adj2.extend(adj)
noun2 = ['' for i in range(500)]
noun2.extend(noun)

randoms = [random.choice(adj2), random.choice(adj), random.choice(noun2), random.choice(noun)]
randoms = [r for r in randoms if r]


def generate_name_camel_case() -> str:
    """ Generate name using camel case, ex. MightyBeaver"""
    return ''.join(s.capitalize() for s in randoms)


def generate_name_white_space() -> str:
    """ Generate name separated by spaces, ex. dear abby """
    return ' '.join(randoms)


def generate_name_snake_case() -> str:
    """ Generate name using snake case, ex. uh_oh_mountain """
    return '_'.join(s.lower() for s in randoms)


switch = {
    'camel': generate_name_camel_case(),
    'space': generate_name_white_space(),
    'snake': generate_name_snake_case()
}

print(switch[args.style])
