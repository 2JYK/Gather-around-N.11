### Ai - Gather-around-N.11
***
## 팀원
- 김경수
- 윤슬기
- 정대근
- 정주현
***
# 컨벤션

- 브랜치 관리 전략 (git flow)
    - 참고
  
![image](https://user-images.githubusercontent.com/89643366/169194210-7acb7256-91e9-43cd-b02f-8fbf30b829d6.png)  
        
	```jsx
        main(master) : 테스트 서버에서 테스트가 끝나고 운영서버로 배포 할 수 있는 브랜치
        feature : 기능을 개발하는 브랜치
        hotfix  : 운영중인 버전에서 발생한 버그를 수정 하는 브랜치
	```
        

- 브랜치
    - F/main>html
    - F/sub (버튼)
    - B/API
    - B/deep
    - 보류 F/main/hotfix

- 커밋 메세지

```jsx
Commit Type
- Feat: 새로운 기능 추가/수정/삭제
- Fix: 버그 수정
- Docs: 문서 수정
- Design : CSS 등 사용자 UI 디자인 변경
- Style: 코드에 영향을 주지 않는 변경사항 /  코드 포맷 변경, 새미 콜론 누락, 코드 수정이 없는 경우
- Comment : 필요한 주석 추가 및 변경
- Refactor: 코드 리팩토링
- Test: 테스트 코드/기능 추가
- Chore: 기타 변경사항, 패키지 매니저 수정
- !BREAKING CHANGE : API를 크게 변경하는 경우
- Rename : 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우
- Remove : 파일을 삭제하는 작업만 수행한 경우

Subject
- 50자를 넘기지 않고, 커밋 타입을 준수함.

 Body
- 72자를 넘기지 않고, 모든 커밋에 본문 내용을 작성할 필요는 없음.

```

### 💚 변수명 규칙

- HTML (CSS)
    
    ```html
    클래스명 : - 사용 ; form-control  
    아이디명 : 카멜 케이스 ; navbarNav
    따옴표 : "" (부트스트랩에서만 다른곳은 '')
    button type="button"
    하이퍼링크 사용시 a 태그 포함
    img 의 alt="" 꼭 표시
    ‘id’ : id (: 나 =) 띄어쓰기 양쪽으로 
    ```
    
- JavaScript
    
    <aside>
    💡 Ex) mac book, num
    
    1. 파스칼 케이스 : MacBook, Num
    
    2. 카멜 케이스 : macBook, num
    
    3. 스네이크 케이스 : _macBook, _num
    
    4. 헝가리안 케이스 : isMacBook, isNum, strMacBook, strNum
    
    </aside>
    
    <aside>
    💡 1. 파스칼 케이스
    
    </aside>
    
    ```jsx
    // 클래스
    class MyStudent {
    		...
    };
    ```
    
    ```jsx
    // 객체를 export 할 때
    const MyObject = {
    		...
    };
    export default MyObject;
    ```
    
    <aside>
    💡 2. 카멜 케이스
    
    </aside>
    
    ```jsx
    // 변수와 상수
    let num = 123;;
    let str = 'hello';
    
    // 함수
    function myFunction() {
    	...
    }
    
    // 객체
    const thisIsMyObject = {
    	...
    };
    ```
    
- Python
    
    <aside>
    💡 1. 일반 변수
    
    </aside>
    
    ```python
    a = 'MacBook'
    
    # 스네이크 케이스
    my_num = 3
    ```
    
    <aside>
    💡 2. 함수
    
    </aside>
    
    ```python
    def get_user_info():
      ....내용.....
    ```
    
    <aside>
    💡 3. 클래스
    
    </aside>
    
    ```python
    class CatchFish():
    	...내용...
    ```
    

# **DATABASE**
![image](https://user-images.githubusercontent.com/89643366/169194157-4a64aa66-d791-4052-ad73-d579509eaa21.png)



```json
fish {
	"fish_id" : "물고기 아이디",
	"name" : "이름",
	"desc" : "설명",
	"image" : "사진",
	"datetime" : "등록시간"
}
log {
	"log_id" : "로그 아이디",
	"fish_id" : "물고기 아이디",
	"name" : "이름",
	"desc" : "설명",
	"image" : "사진",
	"datetime" : "등록시간"
}
```
