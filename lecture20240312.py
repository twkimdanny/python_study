from openpyxl import Workbook

# 엑셀파일 쓰기
write_wb = Workbook()

write_ws = write_wb.create_sheet('테스트1')
write_ws = write_wb.active
write_ws['A1'] = '학번'
write_ws['A2'] = '이름'
write_wb.save('aaa.xlsx')


