import argparse
import os
import shutil
import stat
import time
from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser(description = "移除PDF写密码")
parser.add_argument('path', help='文件/文件夹 路径')
args = parser.parse_args()

def remove_pdf_password(src:str, dst:str):
    with open(src, 'rb') as fin:
        reader = PdfReader(fin)
        print(f"处理文件：{src}，页数：{len(reader.pages)}")
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        with open(dst, "wb") as fout:
            writer.write(fout)

if os.path.isfile(args.path) and args.path.lower().endswith('.pdf'):
    base, ext = os.path.splitext(args.path)
    remove_pdf_password(args.path, f"{base}_stripped{ext}")
elif os.path.isdir(args.input):
    # TODO：处理文件夹
    pass
else:
    raise ValueError("非有效文件路径")
