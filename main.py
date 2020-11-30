# v201130-0954

import qrcode
import sys

def paperSize2qrSize(paper_size=''):
    print(f'paper_size: {paper_size}')
    qr_box_size = 1
    qr_size = (54, 54)
    if paper_size != '':
        if paper_size in {'A4', 'A3'}:
            qr_box_size = 2
            qr_size = (54, 54)
        elif paper_size == 'A2':
            qr_box_size = 3
            qr_size = (81, 81)
        elif paper_size == 'A1':
            qr_box_size = 4
            qr_size = (108, 108)
        elif paper_size == 'A0':
            qr_box_size = 6
            qr_size = (162, 162)
    return qr_box_size, qr_size

def createQrImg(qr_texts, qr_box_size=1, qr_size=''):
    print(f'qr_texts: {qr_texts}, qr_size: {qr_size}')
    qr_base = qrcode.QRCode(box_size=qr_box_size)
    qr_base.add_data(qr_texts)
    qr_base.make()
    result_qr = qr_base.make_image()
    #result_qr = result_qr.resize(qr_size) #画素の荒れがすごい
    return result_qr

def main(args):
    print(f'args: {args}')
    qr_texts = ''
    paper_size = ''
    if len(args) >= 2:
        qr_texts = args[1]
    if len(args) >= 3:
        paper_size = args[2]
    qr_box_size, qr_size = paperSize2qrSize(paper_size)
    result_qr = createQrImg(qr_texts, qr_box_size, qr_size)
    result_qr.save(f'C:\\TEMP\\{qr_texts}.tif', 'tiff')

if __name__ == "__main__":
    main(sys.argv)
