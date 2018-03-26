from comm.utils.read_excel import Read_Excel
from comm.utils.Req import Req
from setting import ENVIRONMENT_CONFIG


class GetCaseData():
    def __init__(self):
        self.id=''
        self.url=''
        self.method=''
        self.request=''
        self.input=''
        self.expect=''

    def get_excel_data(self,file_name,index,row_index):
        excel=Read_Excel(file_name)
        sheet=excel.get_sheet_by_index(index)
        data_list=excel.get_row_values(sheet,row_index)
        self.id = data_list[0]
        self.url=ENVIRONMENT_CONFIG['host']+data_list[1]
        self.method=data_list[2]
        self.input=data_list[3]
        self.expect=data_list[4]


    def get_resp_data(self):
        req = Req()
        resp = req.get_response(url = self.url, data=self.input, method=self.method)
        return resp

    def get_case_data(self):
        exp_case_data=self.expect
        resp_case_data=self.get_resp_data()
        return exp_case_data,resp_case_data



if __name__ == '__main__':
    req = GetCaseData()
    file_name='../../data/test_shop.xlsx'
    index=0
    row_index = 1
    req.get_excel_data(file_name, index, row_index)
    r=req.get_case_data()
    print(r)