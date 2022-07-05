# CONFIG
FILE_NAME = "words2.csv" # 저장할 파일의 이름
MEANING_NUMBER = 2 # 가져올 뜻의 개수



import requests
from bs4 import BeautifulSoup

print("성규의 영어 단어 암기용 프로그램 v0.1")
print("영어 단어를 입력하면 단어의 뜻을 찾아 함께 .csv 파일로 저장합니다.")
print("검색하려는 영어 단어를 입력하세요. 입력된 단어는 검색 후 추가됩니다.")
print("- 1을 입력하면 직전에 추가된 단어를 삭제합니다.")
print("- 0을 입력하면 입력된 단어들을 전부 저장한 후, 프로그램을 종료합니다.")

def findWord(w):
  url = "https://small.dic.daum.net/search.do?dic=eng&search_first=Y&q=" + str(w)
  response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
  soup = BeautifulSoup(response.text, "html.parser")

  mean = soup.select("#mArticle > div.search_cont > div:nth-child(2) > div:nth-child(2) > div > ul > li")
  mean = mean + soup.select("#mArticle > div.search_cont > div:nth-child(3) > div:nth-child(2) > div.cleanword_type.kuek_type > ul > li")
  m = []
  for i in range(len(mean)):
    t = mean[i].text.strip()
    if t.startswith(str(i+1) + ".") and i < MEANING_NUMBER:
      m.append(mean[i].text.strip()[2:])
  if not m:
    print("뜻을 찾을 수 없는 단어입니다.\n뜻을 입력하세요. (설정된 뜻의 개수: " + str(MEANING_NUMBER) + ")")
    for i in range(MEANING_NUMBER):
      a = input()
      m.append(a)
      print("뜻이 추가되었습니다. [" + a + "]")
  return {"word": w, "meaning": m}


import csv
def saveCSV(list):
  f = open(FILE_NAME, "w", encoding="utf-8", newline="")
  wr = csv.writer(f)
  for l in list:
    wr.writerow([l["word"]] + l["meaning"])
  f.close()


wlist = []

while True:
  w = input()
  if w == "0":
    saveCSV(wlist)
    print(f"파일이 성공적으로 저장되었습니다. \"{FILE_NAME}\"파일을 확인하세요.")
    break
  elif w == "1":
    if not wlist:
      print("추가된 단어가 없어 삭제할 수 없습니다.")
      continue
    else:
      popWord = wlist.pop()["word"]
      print(f"단어 \"{popWord}\"이(가) 삭제되었습니다.")
      continue
  wm = findWord(w)
  mean = ", ".join(wm["meaning"])
  wlist.append(wm)
  print(f"단어 \"{w}\"이(가) 추가되었습니다. (뜻: {mean})")