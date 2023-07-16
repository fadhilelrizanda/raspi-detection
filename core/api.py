import requests


def send_data(number_detection):
    url = 'https://api-iot-zeta.vercel.app/class/post'
    print("Sending Data",flush=True)
    data = {'total':number_detection}
    response = requests.post(url,json=data)
    print(response.status_code,flush=True)
    print(response.text, flush = True)