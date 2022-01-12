import pandas as pd

MD = pd.read_excel('NB_MD.xlsx')
sap = pd.read_excel('SAP_download.xlsx', index_col='자재')

MD.set_index('품목코드(자재코드)', inplace=True)

MD['SAP재고']=sap['주문가능 계']

MD.to_excel('C:/Users/user/Desktop/1.python xl/SAPupdated_MD.xlsx', sheet_name='master_data')
