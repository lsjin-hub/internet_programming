class Word:
    count=1
    correct=0
    incorrect=0

    def __init__(self, korean, english):
        self.korean=korean
        self.english=english

    def question(self):
        return "{}".format(self.korean)

    def to_string(self):
        return "정답 >{}".format(self.english)

correct_qs=[]
incorrect_qs=[]

words=[
    Word("추가의","additional"),
    Word("비밀의","confidential"), 
    Word("경제의","economic"),
    Word("유익한","informative"),
    Word("설득력 있는","persuative"),
    Word("신뢰할 만한","reliable"),
    Word("~에 책임이 있는","responsible for"),
    Word("성공적인","successful"),
    Word("민감한","sensitible"),
    Word("각각의","respective")
]
print("시작")
for word in words:
    print("문제 {}번".format(Word.count))
    print(word.question())
    my_answer=input("답변> ")
    if my_answer.lower()==word.english:
        print("정답입니다.")
        print()
        Word.correct+=1
        correct_qs.append(Word.count)
    else:
        print("오답입니다.")
        print(word.to_string())
        print()
        Word.incorrect+=1
        incorrect_qs.append(Word.count)
    Word.count+=1

print()
print("수고하셨습니다.")
print("맞춘 문제 개수는 {}개이고, 틀린 문제 개수는 {}개 입니다.".format(Word.correct,Word.incorrect))
if Word.correct>=(Word.count*0.8):
  print("이번 시험은 pass입니다.")
  print("맞은 번호 ",correct_qs)
  print("틀린 번호 ",incorrect_qs)
else:
  print("아쉽게도 fail입니다. 더 공부하세요")
  print("맞은 번호 ",correct_qs)
  print("틀린 번호 ",incorrect_qs)

wordbook_open=input("단어장을 오픈하시겠습니까?(y or n)")
if wordbook_open in ["y","Y"]:
  with open("wordbook.txt","r") as file:
      for line in file:
          (num, korean, english)=line.strip().split(",")
          print("{}. 뜻: {}, 영어: {}".format(num, korean,english))
