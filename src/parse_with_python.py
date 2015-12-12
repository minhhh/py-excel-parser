#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import xlrd

def parse():
    file = sys.argv[1]
    in_code = sys.argv[2]
    out_code = sys.argv[3]
    book = xlrd.open_workbook(file, encoding_override=in_code)
    for sheet_id in range(book.nsheets):
        sheet = book.sheet_by_index(sheet_id)
        print "__SHEET:"+sheet.name.encode(out_code)
        for row_id in range(sheet.nrows):
            cols = sheet.row(row_id)
            values = []
            for cell in cols:
                val = None
                if cell.ctype == 0 or cell.ctype == 1 or cell.ctype == 6:
                    val = cell.value.encode(out_code).replace("\n", "\\n")
                elif cell.ctype == 2 or cell.ctype == 3:
                    if (cell.value - int(cell.value) > 0):
                        val = str(cell.value)
                    else:
                        val = str(int(cell.value))
                else:
                    val = str(cell.value)
                values.append(val);
            print "\t".join(values)
