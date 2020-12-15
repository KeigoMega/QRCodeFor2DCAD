# v201216-0826

import qrcode
import sys

qr_box_size_table = {
    'A4': 2,
    'A3': 2,
    'A2': 3,
    'A1': 4,
    'A0': 6,
}

qr_size_table = {
    'A4': 58, #54,
    'A3': 58, #54,
    'A2': 87, #81,
    'A1': 116, #108,
    'A0': 174, # 162,
}

def paperSize2qrSize(paper_size=''):
    print(f'paper_size: {paper_size}')
    qr_box_size_default = 1
    qr_box_size = qr_box_size_default
    qr_size_default = 54
    qr_size = (qr_box_size_default, qr_box_size_default)
    if paper_size != '':
        qr_box_size = qr_box_size_table.get(paper_size)
        if qr_box_size == None:
            qr_box_size = qr_box_size_default
        qr_size = (qr_size_table.get(paper_size), qr_size_table.get(paper_size))
        if qr_size == (None, None):
            qr_size = (qr_size_default, qr_size_default)
    return qr_box_size, qr_size

def createQrImg(qr_texts, qr_box_size=1, qr_size=''):
    print(f'qr_texts: {qr_texts}, qr_size: {qr_size}')
    qr_base = qrcode.QRCode(box_size=qr_box_size)
    qr_base.add_data(qr_texts)
    qr_base.make()
    result_qr = qr_base.make_image(back_color="#FFFFFF", fill_color="#000000")
    result_qr = result_qr.resize(qr_size)
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
    #result_qr.save(f'C:\\TEMP\\{qr_texts}.tif', 'tiff')
    result_qr.save(f'C:\\TEMP\\QR.tif', 'tiff')

if __name__ == "__main__":
    main(sys.argv)
