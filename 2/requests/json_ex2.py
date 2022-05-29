import json

dict_data = {'Name':'Gwon', 'Department':'IOT', 'Gender':'Male'}

with open('data.json', 'w') as f:
    json.dump(dict_data, f) 
    # 파이썬 딕셔너리를 JSON 포맷으로