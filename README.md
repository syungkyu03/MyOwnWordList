# MyOwnWordList v0.1
매번 영어 단어를 외울 때마다
<blockquote>영단어 입력 -> 사전 검색 -> 뜻 입력 -> 정리 후 파일 저장</blockquote>
같은 귀찮은 과정을 생략하고자 만들었습니다.   

이 프로그램은 영단어를 입력하면 자동으로 사전에서 그 뜻을 찾아 단어와 뜻을 함께 .csv 파일로 저장합니다.   

## 사용법
시작 메시지:
<pre>
성규의 영어 단어 암기용 프로그램 v0.1
영어 단어를 입력하면 단어의 뜻을 찾아 함께 .csv 파일로 저장합니다.   
검색하려는 영어 단어를 입력하세요. 입력된 단어는 검색 후 추가됩니다.
- 1을 입력하면 직전에 추가된 단어를 삭제합니다.
- 0을 입력하면 입력된 단어들을 전부 저장한 후, 프로그램을 종료합니다.
</pre>
또한 찾을 수 없는 단어가 등장한다면, 직접 입력을 받아 입력 받은 뜻으로 단어를 저장합니다.   
<pre>
뜻을 찾을 수 없는 단어입니다.   
뜻을 입력하세요.
</pre>

## 저장 된 파일의 모습
예시:   
<pre>
apple,애플,사과
banana,바나나,바나나
cool,냉각,멋진
drama,드라마,연극
</pre>

## P.S.
개인적인 편의를 위해 제작한 프로그램으로 단어 데이터는
[다음 사전][dictLink]을 이용합니다.

[dictLink]: https://small.dic.daum.net/ "Go Dictionary"
