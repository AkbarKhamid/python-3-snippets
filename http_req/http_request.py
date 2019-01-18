import requests
def get_res(url, d_type = "text/plain", term = None):
  data = requests.get(url, headers = {"Accept": d_type}, params={'term': term})
  if d_type == "application/json":
    data = data.json()
  return data