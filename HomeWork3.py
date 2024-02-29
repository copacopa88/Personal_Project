# ----- 코드 정의 ------
import hashlib


members = []
posts = []

class Member:
    username=None
    def __init__(self, name, username, password):
        self.name=name
        self.username=username
        self.username
        self.password=password
        self.encoded_password = self.password.encode('utf-8') #인코딩 과정
        self.sha256_hash = hashlib.sha256(self.encoded_password).hexdigest()
    def names(self):
        return self.name
    def usernames(self):
        return self.username
    def passwords(self):
        return self.sha256_hash
    def display(self):
        return print(self.name,self.username)





class Post:
     def __init__(self, title, content, author):
            self.title=title
            self.content=content
            self.author=author
     def titles(self):
        return self.title
     def contents(self):
        return self.content
     def authors(self):
        return self.author
     def display_post(self):
        return print(self.title, self.content,self.author)
     def display_titles(self):
        return print(self.title)
    


# ----- 코드 실행 ------


# TODO : 코드 구현이 필요합니다.

a=Member('김똘복','ddolbok', 'q1w2e3r4')
b=Member('박나나', 'nanapark', '123234')
c=Member('이태백', 'teakbeak2', '9i8u7y6t')
d=Member(input('이름을 입력해 주세요 '), input('아이디를 입력해 주세요 '), input('비밀번호를 입력해 주세요 '))


Post1=Post('안녕하세요', '반갑습니다', a.usernames())
Post2=Post('광고글', '싸다싸 특가', b.usernames())
Post3=Post('안녕갑디', '위에 광고글 지워줘', c.usernames())
Post4=Post('날씨가 춥네요', '감기 조심하세요', a.usernames())
Post5=Post('날씨가 추운 오늘', '오리털 점퍼 특가', b.usernames())
Post6=Post('방장 누구냐', '관리좀 해라', c.usernames())
Post7=Post('제가 방장인데요', '피곤해서 안합니다', a.usernames())
Post8=Post('피곤하시다고요?', '종합 비타민 특가', b.usernames())
Post9=Post('XXXX', '내가 나가고 만다 XX', c.usernames())
post10=Post(input('게시물 제목을 입력해 주세요 '), input('게시물 내용을 입력해 주세요 '), d.usernames())




# for sum_menbers in (a,b,c,d):
#     members.append(sum_menbers.names())
#     members.append(sum_menbers.usernames())
#     members.append(sum_menbers.passwords())
#     print(members)
#     #members 리스트에 한번에 집어넣기

    
# for sum_redit in (Post1,Post2,Post3, Post4, Post5, Post6, Post7, Post8, Post9):
#     posts.append(sum_redit.titles())
#     posts.append(sum_redit.contents())
#     posts.append(sum_redit.authors())
#     print(posts)
#     #posts 리스트에 한번에 집어넣기    
        
for titles_s in (Post1,Post2,Post3, Post4, Post5, Post6, Post7, Post8, Post9, post10):
    if titles_s.authors() == d.usernames():
        print(titles_s.titles())
        
        # 특정 유저가 작성한 게시글 제목 찾기

for content_s in (Post1,Post2,Post3, Post4, Post5, Post6, Post7, Post8, Post9, post10):
    if  "특가" in content_s.contents():
        print(content_s.titles())
        
        # 특정 단어가 내용에 포함된 게시글의 제목 찾기
