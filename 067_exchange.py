import requests
import json
# site artık geçerli değil. öğrenmeye devam ettiğim için bu kodu yazmaya devam ediyorum
api_url="https://api.exchangeratesapi.io/latest?base="


bozulan_doviz= "USD"#normal uygulamada inputla alıyorduk ama siteye ulaşılmadığı için aşağıda sadece dolar kuruyla yaptım
alinan_doviz= input("alınan döviz türü: ")
miktar=int((input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz?: ")))

result=requests.get(api_url+bozulan_doviz)
result=json.loads(result.text)
# sitede yazanların güncel halini yazdım
result={'rates': {'CAD': 1.35, 'HKD': 7.82, 'ISK': 139.97, 'PHP': 55.71, 
                  'DKK': 6.89, 'HUF': 347.57, 'CZK': 21.99, 'GBP': 0.80, 
                  'RON': 4.61, 'SEK': 10.53, 'IDR': 14927.00, 'INR': 82.87, 
                  'BRL': 5.00, 'RUB': 80.55, 'HRK': 6.98, 'JPY': 137.99, 
                  'THB': 34.35, 'CHF': 0.90, 'EUR': 0.93, 'MYR': 4., 
                  'BGN': 1.81, 'TRY': 19.81, 'CNY': 7.01, 'NOK': 10.88, 
                  'NZD': 1.59, 'ZAR': 19.43, 'USD': 1.0, 'MXN': 17.75, 
                  'SGD': 1.35, 'AUD': 1.50, 'ILS': 3.65, 'KRW': 1326.89, 
                  'PLN': 4.20
                  }, 
        'base': 'USD', 
        'date': '2023-05-19'}
print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*result["rates"][alinan_doviz],alinan_doviz))