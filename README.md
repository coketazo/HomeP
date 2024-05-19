# HomeP DEMO

HomeP는 write-up 동아리의 개발 중인 홈페이지 프로젝트입니다.  Flask를 기반으로 개발하였습니다.

### 기능

1. Markdown 파일을 통한 페이지 내용 관리
2. 사용자 인증 및 권한 관리
3. 각 페이지의 동적 라우팅

### 사용 기술

- Flask: 파이썬 웹 프레임워크
- Jinja2: 템플릿 엔진
- Flask-Login: 사용자 인증 관리
- Markdown: 페이지 내용 작성을 위한 경량 마크업 언어
- HTML, CSS, JavaScript: 웹 프론트엔드 디자인 및 동작 구현

### 프로젝트 구조

```
HomeP/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── easymd.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── index.js
│   │   └── md/
│   │       ├── index/
│   │       │   ├── section0_About_Us.md
│   │       │   ├── section1_Events.md
│   │       │   ├── section2_Member.md
│   │       │   ├── section3_Blog.md
│   │       │   ├── section4_Resources.md
│   │       │   └── section5_Contact.md
│   │       └── tmp/
│   └── templates/
│       ├── index.html
│       ├── login.html
│       ├── profile.html
│       └── register.html
│
├── .gitignore
├── config.py
├── run.py
├── README.md
└── requirements.txt
```

### 설치 및 실행

1. Git 저장소를 클론합니다.

   ```
   $ git clone https://github.com/coketazo/HomeP.git
   ```

2. 가상환경을 생성하고 활성화합니다.

   ```
   [Linux OS terminal]
   $ cd HomeP
   $ python3 -m venv venv
   $ source venv/bin/activate
   ```
   ```
   [Windows OS cmd]
   $ cd HomeP
   $ python3 -m venv venv
   $ venv\Scripts\activate.bat
   ```
3. 필요한 패키지를 설치합니다.

   ```
   $ pip install -r requirements.txt
   ```

4. 애플리케이션을 실행합니다.

   ```
   $ flask run
   ```

5. 웹 브라우저에서 `http://localhost:5000`을 열어 애플리케이션을 확인합니다.

### 개발자

- 개발자: [Coketazo](https://github.com/coketazo), [gdect](https://github.com/gdect)

### 라이선스

MIT 라이선스를 따릅니다.
