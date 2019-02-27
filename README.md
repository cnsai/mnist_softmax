# 과제1. mnist softmax 회귀 

- 과제 개요
  - ~~2019년 2월 25일까지(연장)~~
  - 2019년 3월 1일 까지
  - softmax Regression 를 활용한 mnist 데이터 예측 실습
  - 참고 링크 : http://solarisailab.com/archives/303

---
- Git 올리기 규칙
  - 자신의 이름으로 폴더를 생성하여 그안에 파일을 집어 넣기.
    - ex) cnsai/mnist_softmax/KimJuHyeon/main.py
  - 업로드 시, 개인 branch 생성하여 git push 할 것.
  - 브랜치 merge는 제가(JuHyeon_Kim) 스터디 전에 하겠읍니다.
---
- Git 다운로드 및 업로드 방법
  - 기본적인 git 사용법은 따로 언급하지 않습니다.
  - 정말 모르곘으면 경우 질문하거나 만났을 때 배우기
  1. 처음 받아올 경우
     1. 원하는 프로젝트 "Clone or Download" 버튼 선택 후, 주소 복사
     2. "git clone (주소)" - 현재 github에 업로드된 최신 버전 받아오기
     3. "git branch (원하는 브랜치이름)" - 타인에게 영향을 주지않는 작업환경을 개설하는 명령어
     4. "git checkout (자신의 브랜치)" - 자신의 작업환경으로 이동
  2. 남의 프로젝트가 궁금할 때.(주인장이 업데이트 했을 경우.)
     1. 자신의 프로젝트 git push하기 (go to 3)
     2. "git checkout master" - 마스터 브랜치로 이동하기
     3. "git pull" - 업데이트 된 내용 내려 받기
  3. git push 명령어
     1. "git push origin (자신의 브랜치 이름)"
