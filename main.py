# v201225-0831

import sys
import barcode
from barcode.writer import ImageWriter
barcode.base.Barcode.default_writer_options['write_text'] = False

def createBarcodeImg(bar_texts):
    print(f'bar_texts: {bar_texts}')
    bar_cls = barcode.codex.Code39(code=bar_texts, writer=ImageWriter(format='BMP', mode='1'), add_checksum=False)
    bar_render = bar_cls.render()
    bar_render.save('C:\\TEMP\\BAR.bmp')

def main(args):
    print(f'args: {args}')
    bar_texts = ''
    paper_size = ''
    if len(args) >= 2:
        bar_texts = args[1]
    if len(args) >= 3:
        paper_size = args[2]
    createBarcodeImg(bar_texts)

if __name__ == "__main__":
    main(sys.argv)
