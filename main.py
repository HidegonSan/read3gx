#!/usr/bin/env python3

import struct
import sys

def hex_format(num):
        return "0x" + hex(num)[2:].upper()

with open(sys.argv[1], "rb") as fr:
        data = (fr.read())

magic = data[0:8].decode('UTF-8')
version = f"{data[11]}.{data[10]}.{data[9]}"
reserved = data[12:16]

author_length = struct.unpack('<I', data[12 + 4:16 + 4])[0]
author_offset = struct.unpack('<I', data[16 + 4:20 + 4])[0]
author = data[author_offset : author_offset + author_length].decode("UTF-8")

title_length = struct.unpack('<I', data[20 + 4:24 + 4])[0]
title_offset = struct.unpack('<I', data[24 + 4:28 + 4])[0]
title = data[title_offset : title_offset + title_length].decode("UTF-8")

summary_length = struct.unpack('<I', data[28 + 4:32 + 4])[0]
summary_offset = struct.unpack('<I', data[32 + 4:36 + 4])[0]
summary = data[summary_offset : summary_offset + summary_length].decode("UTF-8")

description_length = struct.unpack('<I', data[36 + 4:40 + 4])[0]
description_offset = struct.unpack('<I', data[40 + 4:44 + 4])[0]
description = data[description_offset : description_offset + description_length].decode("UTF-8")

flags = struct.unpack('<I', data[48:52])[0]

exe_dec_checksum = struct.unpack('<I', data[52:56])[0]

built_in_dec_exe_args0 = struct.unpack('<I', data[56:60])[0]
built_in_dec_exe_args1 = struct.unpack('<I', data[60:64])[0]
built_in_dec_exe_args2 = struct.unpack('<I', data[64:68])[0]
built_in_dec_exe_args3 = struct.unpack('<I', data[68:72])[0]

built_int_swap_enc_dec_args0 = struct.unpack('<I', data[72:76])[0]
built_int_swap_enc_dec_args1 = struct.unpack('<I', data[76:80])[0]
built_int_swap_enc_dec_args2 = struct.unpack('<I', data[80:84])[0]
built_int_swap_enc_dec_args3 = struct.unpack('<I', data[84:88])[0]

code_offset = struct.unpack('<I', data[88:92])[0]
rodata_offset = struct.unpack('<I', data[92:96])[0]
data_offset = struct.unpack('<I', data[96:100])[0]
code_size = struct.unpack('<I', data[100:104])[0]
rodata_size = struct.unpack('<I', data[104:108])[0]
data_size = struct.unpack('<I', data[108:112])[0]
bss_size = struct.unpack('<I', data[112:116])[0]
exe_dec_offset = struct.unpack('<I', data[116:120])[0]
swap_enc_offset = struct.unpack('<I', data[120:124])[0]
swap_dec_offset = struct.unpack('<I', data[124:128])[0]

title_count = struct.unpack('<I', data[128:132])[0]
title_count = struct.unpack('<I', data[132:136])[0]

symbol_count = struct.unpack('<I', data[136:140])[0]
symbol_offset = struct.unpack('<I', data[140:144])[0]
symbol_name_table_offset = struct.unpack('<I', data[144:148])[0]

print("[ 3gx Header ]")
print(f"Magic: {magic}")
print(f"Version: {version}")
print("[ 3gx Executable ]")
print(f"Author Length: {author_length}")
print(f"Author Offset: {hex_format(author_offset)}")
print(f"Author: {author}")

print(f"Title Length: {title_length}")
print(f"Title Offset: {hex_format(title_offset)}")
print(f"Title: {title}")
print(f"Summary Length: {summary_length}")
print(f"Summary Offset: {hex_format(summary_offset)}")
print(f"Summary: {summary}")
print(f"Description Length: {description_length}")
print(f"Description Offset: {hex_format(description_offset)}")
print(f"Description: {description}")

print("flags", flags)
print("1bit embeddedExeDecryptFunc: ", ((flags >> 0) & 1))
print("1bit embeddedSwapEncDecFunc: ", ((flags >> 1) & 1))
print("30bit unused: 0")

print("exeDecCheckSum", hex_format(exe_dec_checksum))
print("built_in_dec_exe_args", hex_format(built_in_dec_exe_args0), hex_format(built_in_dec_exe_args1), hex_format(built_in_dec_exe_args2), hex_format(built_in_dec_exe_args3))
print("built_int_swap_enc_dec_args", hex_format(built_int_swap_enc_dec_args0), hex_format(built_int_swap_enc_dec_args1), hex_format(built_int_swap_enc_dec_args2), hex_format(built_int_swap_enc_dec_args3))

print("code_offset", hex_format(code_offset))
print("rodata_offset", hex_format(rodata_offset))
print("data_offset", hex_format(data_offset))
print("code_size", hex_format(code_size))
print("rodata_size", hex_format(rodata_size))
print("data_size", hex_format(data_size))
print("bss_size", hex_format(bss_size))
print("exeDecOffs", hex_format(exe_dec_offset))
print("swapEncOffs", hex_format(swap_enc_offset))
print("swapDecOffs", hex_format(swap_dec_offset))

print("symbol count", symbol_count)
print("offset to symbols info", hex_format(symbol_offset))
print("symbol name table offs", hex_format(symbol_name_table_offset))

code = data[code_offset : code_offset + code_size] + data[rodata_offset : rodata_offset + rodata_size] + data[data_offset : data_offset + data_size]
