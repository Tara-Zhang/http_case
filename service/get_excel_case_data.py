from utils.read_excel import Read_Excel
from setting import ENVIRONMENT_CONFIG


class GetExcelCaseData:
    def __init__(self):
        self.id=''
        self.url=''
        self.request=''
        self.input=''
        self.expect=''

    def get_case_data(self,file_name,index):
        excel=Read_Excel(file_name)
        sheet=excel.get_sheet_by_index(index)
        data_list=sheet.get_row_values()
        self.id = data_list[0]
        self.url=ENVIRONMENT_CONFIG['host']+data_list[1]
        self.request=data_list[2]
        self.input=data_list[3]
        self.expect=data_list[4]