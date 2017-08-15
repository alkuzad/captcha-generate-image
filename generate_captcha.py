#!/usr/bin/env python

import os
from pathlib import Path
from argparse import ArgumentParser

from captcha.image import ImageCaptcha

DEFAULT_WIDTH = 160
DEFAULT_HEIGHT = 40 

def test_path(path):
    p = Path(path)
    if not p.exists() or (p.exists() and p.is_file()):
        return p
    else:
        raise ValueError("Path '%s' does exists already or is not file" % p)

def test_path_exists(path):
    p = Path(path)
    if p.exists():
        return os.path.realpath(p)
    else:
        raise ValueError("Path '%s' does not exist" % p)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('input_text', type=str)
    parser.add_argument('output_file', type=test_path)
    parser.add_argument('--width', type=int, default=DEFAULT_WIDTH)
    parser.add_argument('--height', type=int, default=DEFAULT_HEIGHT)
    parser.add_argument('--font', type=test_path_exists)
    return parser.parse_args()

def write_captcha_file(text, output_file, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, font=None):
    fonts = None
    if font is not None:
        fonts = [font]
    image = ImageCaptcha(width=width, fonts=fonts, height=height)
    image.write(text, output_file)

def main():
    args = parse_args()
    write_captcha_file(args.input_text, args.output_file, width=args.width, height=args.height, font=args.font)
    
if __name__ == '__main__':
    main()
