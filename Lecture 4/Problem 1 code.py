def visiting_year(date):
    y, m, n = date.split('/')
    if len(y) != 4:
        print('Check the data again.')
    return y

patient_dict = {'JH': '2020/03/02', 'JJ': '193/12/12', 'IW': '2019/02/18'}

for key in patient_dict.keys():
    print(visiting_year(patient_dict[key]))
