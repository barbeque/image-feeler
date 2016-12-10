import argparse, struct, math
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description = 'Visually explore binary files.')
    parser.add_argument('file')
    args = parser.parse_args()
    with open(args.file, 'rb') as inputbinary:
        mybytes = inputbinary.read()
    #as_ints = map(lambda x: struct.unpack('B', x)[0], mybytes)
    width = 256.0
    height = int(math.ceil(len(mybytes) / width))
    print width, height
    result = Image.new('L', (int(width), height))
    result.putdata(mybytes)
    result.save('foo.bmp')

if __name__ == '__main__': main()
