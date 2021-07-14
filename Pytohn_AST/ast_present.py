from astpy import parseprint    
import argparse 

'''讀參數'''
arg_parse = argparse.ArgumentParser(description='A static Big-O analysis tool base on Big-O AST.')
arg_parse.format_help()
arg_parse.add_argument('filename', type=str, help='target code filename')
args = arg_parse.parse_args()

'''讀檔案'''
source_file_name = args.filename

f = open(source_file_name, "r",encoding="utf-8")


'''AST結構'''
print(parseprint(f.read()))