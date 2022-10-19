num=0
'''
아래의 str1 에 저장된 문자열에서
문장 단위로 list_sentences 에 저장하고
단어(띄어쓰기로 구분함) 단위로 list_words 에 저장하세요

문장 개수와 단어(띄어쓰기로 구분함) 개수도 출력하세요
'''
str1 = '''나는 더조은 입니다
주소는 마포구 입니다
나이는 30세 입니다'''

list_sentences = []
list_words = []

for sentence in str1.split("\n"):
  list_sentences.append(sentence)
  for word in sentence.split(" "):
    list_words.append(word)

print('list_sentences :',list_sentences)
print('list_words     :',list_words)
print('list_sentences :',len(list_sentences),"개")
print('list_words     :',len(list_words),"개")



