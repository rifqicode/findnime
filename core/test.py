import requests

url = "https://www.anjay.info/cartographic-processing-in-gis/"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"eastsafelink_id\"\r\n\r\nVWErNWlBZmpCUlMvT0pxVHE3YS84cEZjSjFxTHBjTHEzTU5ZRy9XbXY2NnFLSUgrVzNiekljSVkzRkFmbjJKdg==\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.content)
