
from triple_extraction import *
import re
import xlrd
import xlwt


def exceltest():
    extractor = TripleExtractor()
    workbook = xlrd.open_workbook(r'data\CQMdatas.xlsx')
    sheet1 = workbook.sheet_by_index(0)
    wbk = xlwt.Workbook()
    sheetwrite = wbk.add_sheet('Sheet 1',cell_overwrite_ok=True)

    ###################################
    ######excel 操作############
    for i in range(0,9503):
        contentt=sheet1.cell(i,8).value
        paperid=sheet1.cell(i,0).value
        svos = extractor.triples_main(contentt)
        print(i)
        # print(contentt)
        # print(svos)
        saot=" "
        for sao in svos:
            sao_convert="#".join(sao)
            saot=saot+"$"+sao_convert
        print(saot)
        sheetwrite.write(i, 0, paperid)
        sheetwrite.write(i, 1, contentt)
        sheetwrite.write(i, 2, saot)


    wbk.save(r'data\CQMdata_with_SAO.xlsx')
    contenteng="successful!"
    # svos = extractor.triples_main(contenteng)
    print(contenteng)
exceltest()
