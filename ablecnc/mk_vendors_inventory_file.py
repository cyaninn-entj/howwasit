import pandas as pd

vendors_sap = pd.read_excel('vendors_SAP.xlsx')
empty = pd.read_excel('empty.xlsx')

empty['품목코드(자재코드)']=vendors_sap['품목코드(자재코드)']
empty['자재명(KO)']=vendors_sap['자재명(KO)']

empty.to_excel('C:/Users/user/Desktop/1.python xl/vendors_inven_list.xlsx', sheet_name='sheet1')


inven=pd.read_excel('vendors_inven_list.xlsx')
sap = pd.read_excel('vendors_SAP.xlsx', index_col='품목코드(자재코드)')
MD = pd.read_excel('SAPupdated_MD.xlsx', index_col='품목코드(자재코드)') 

inven.set_index('품목코드(자재코드)', inplace=True)

inven['구 ERP 코드']=sap['구 ERP 코드'] #vendors_SAP파일의 '구 ERP 코드' 컬럼 vlookup
inven['SAP재고']=MD['SAP재고'] #SAPupdated_MD파일의 'SAP재고' 컬럼 vlookup
inven['업체코드']=sap['대표공급업체'] #vendors_SAP파일의 '대표공급업체' 컬럼 vlookup
inven['공급업체명']=MD['공급업체명'] #SAPupdated_MD파일의 '공급업체명' 컬럼 vlookup
inven['운영상태']=sap['운영상태']#vendors_SAP파일의 '운영상태' 컬럼 vlookup
inven['평균원가']=MD['평균원가'] #SAPupdated_MD파일의 '평균원가' 컬럼 vlookup

inven.to_excel('C:/Users/user/Desktop/1.python xl/vendors_inven_list_export.xlsx', sheet_name='sheet1')
