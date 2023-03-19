import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Razer-Huntsman-Mini-Gaming-Keyboard/dp/B08B3MHYPC/ref=sr_1_16?keywords=gaming+keyboard&pd_rd_r=45a43b17-6940-4525-9a5a-4546c6f58583&pd_rd_w=coNzI&pd_rd_wg=1jadT&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=H731WTCWB7ZQCRHGHE05&qid=1679212667&sr=8-16"


res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("span", {"class":"a-price a-text-price a-size-medium apexPriceToPay"})
  price = info[0].getText()
  print(price)
  print(info)


