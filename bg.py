import requests
#import pickle

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('B:\mali.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': '9GRHn6K9EHpzqzBtMiHMPKYg'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)


#pickle.dump( open('model1.pkl' , 'wb'))
