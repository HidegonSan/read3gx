# read3gx

Read 3gx headers (3GX V2~ only)

## Usage

```sh
python main.py <FILE>
```

**Result:**


```
[ 3gx Header ]
Magic: 3GX$0002
Version: 0.7.2
[ 3gx Executable ]
Author Length: 10
Author Offset: 0xAB
Author: Nanquitas
Title Length: 23
Title Offset: 0x94
Title: CTRPF - Blank Template
Summary Length: 36
Summary Offset: 0xB5
Summary: A CTRPF Plugin, with a lot of tools
Description Length: 238
Description Offset: 0xD9
Description: This plugin gives you access to a set of tools to edit your games

Features:
  - Memory searcher
  - Hex Editor
  - Code creator
  - Code import from file
  - Action Replay engine with extra capabilities
  - Super fast screenshot engine

flags 35
1bit embeddedExeDecryptFunc:  1
1bit embeddedSwapEncDecFunc:  1
30bit unused: 0
exeDecCheckSum 0xB29B8E85
built_in_dec_exe_args 0x0 0x0 0x0 0x0
built_int_swap_enc_dec_args 0x0 0x0 0x0 0x0
code_offset 0x240
rodata_offset 0x6A140
data_offset 0x88FE0
code_size 0x69F00
rodata_size 0x1EEA0
data_size 0x1C80
bss_size 0x31D8
exeDecOffs 0x1C7
swapEncOffs 0x1EB
swapDecOffs 0x20F
symbol count 2812
offset to symbols info 0x8AC60
symbol name table offs 0x93030

```
