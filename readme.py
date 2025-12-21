"""
GitHub 프로필 README 자동 생성 스크립트 (개선 버전)

티스토리 블로그의 최신 글을 가져와서 README.md를 예쁘게 업데이트합니다.
- 기술 스택 배지 추가
- 블로그 포스트를 주제별 이모지와 함께 표시
- 연락처 정보 및 방문자 카운터 추가
"""

import feedparser

# ============================================================
# 설정
# ============================================================
URL = "https://yurizzy.tistory.com/rss"
MAX_POST_NUM = 10

# ============================================================
# RSS 피드 파싱
# ============================================================
feed = feedparser.parse(URL)

# ============================================================
# 블로그 포스트 리스트 생성 (이모지로 주제 구분)
# ============================================================
latest_blog_post_list = ""

for idx, entry in enumerate(feed["entries"]):
    if idx >= MAX_POST_NUM:
        break

    # 날짜 정보 추출
    feed_date = entry["published_parsed"]
    date_str = f"{feed_date.tm_year}.{feed_date.tm_mon:02d}.{feed_date.tm_mday:02d}"

    # 제목과 링크
    title = entry['title']
    link = entry['link']
    
    # 제목에서 주제 파악해서 이모지 자동 추가
    emoji = "📝"  # 기본 이모지
    title_lower = title.lower()
    
    if "spring" in title_lower or "springframework" in title_lower:
        emoji = "🌱"
    elif "java" in title_lower:
        emoji = "☕"
    elif "oracle" in title_lower or "sql" in title_lower or "database" in title_lower or "mariadb" in title_lower:
        emoji = "💾"
    elif "python" in title_lower:
        emoji = "🐍"
    elif "error" in title_lower or "오류" in title_lower:
        emoji = "🔧"
    elif "기록" in title_lower or "후기" in title_lower or "이야기" in title_lower:
        emoji = "✍️"
    elif "mig" in title_lower or "마이그레이션" in title_lower or "고도화" in title_lower:
        emoji = "🚀"
    
    # 보기 좋은 형식으로 포스트 아이템 생성
    latest_blog_post_list += f"{emoji} **[{title}]({link})**  \n"
    latest_blog_post_list += f"   📅 `{date_str}`\n\n"

# ============================================================
# README 마크다운 템플릿
# ============================================================
markdown_text = """
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=Cylinder&color=timeGradient&height=120&section=header&text=My%20name%20is👋%20Gayul%20Kim&fontSize=50&animation=twinkling" width="100%"/>

### 안녕하세요! Spring 백엔드 개발자 김가율입니다 🙇‍♀️

> 레거시 코드 고도화와 Spring Framework 학습에 열정을 가진 주니어 개발자입니다.  
> 끊임없이 배우고 성장하는 것을 즐깁니다. 

---

### 🛠️ Tech Stack

**Backend**  
![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white)
![Spring](https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![MyBatis](https://img.shields.io/badge/MyBatis-000000?style=for-the-badge&logo=mybatis&logoColor=white)

**Database**  
![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)

**Frontend**  
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**Tools**  
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Eclipse](https://img.shields.io/badge/Eclipse-2C2255?style=for-the-badge&logo=eclipse&logoColor=white)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJ%20IDEA-000000?style=for-the-badge&logo=intellijidea&logoColor=white)

---

### 📊 GitHub Stats

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=gayulz&theme=2077" width="100%" />

<p align="center">
<img src="http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=gayulz&theme=2077&exclude=HTML,CSS" width="49%"/>
<img src="http://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=gayulz&theme=2077&exclude=HTML,CSS" width="49%"/>
</p>

<p align="center">
<img src="http://github-profile-summary-cards.vercel.app/api/cards/stats?username=gayulz&theme=2077" width="49%"/>
<img src="http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=gayulz&theme=2077&utcOffset=09" width="49%" />
</p>

---

<details>
<summary><b>💼 경험한 기술 스토리 (Click to expand)</b></summary>
<br>

> **☕ JAVA**   
> 🔗 [너만가냥 나도가개](https://github.com/gayulz/JAVAGUI_project.git)    
> 🔗 [EMBAD](https://github.com/gayulz/EMBAD_project.git)         
> ```
> 가장 자신있는 언어 중 1가지 입니다 
> 학부 시절에도 즐겁게 배웠으며, 국비 교육 과정에서도 열정적으로 학습한 언어입니다.
> 클래스, 상속, 다형성, 인터페이스를 사용해 본 경험이 있으며 , oracle DB와 연결하여 CRUD를 구현해본 경험이 있습니다.
> ```
>
> **🌼 HTML5 / CSS3**   
> 🔗 [MiniGame](https://github.com/gayulz/JSMiniGame_project.git)    
> 🔗 [EMBAD](https://github.com/gayulz/EMBAD_project.git)  
> 🔗 [TODOWeather](https://github.com/gayulz/TODOLIST_project.git)   
> ```
> 프로젝트를 진행 하면서 웹 페이지의 뼈대(골격)을 만들며 색상이나 스타일을 입히는 것으로 사용 했습니다. 
> HTML은 시멘틱 태그를 사용 하여 섹션을 나누었고 
> CSS는 주로 정렬이나 이미지, 컬러 등 스타일 위주로 사용 했습니다
> 추후 Spring 프로젝트에선 JSP파일에 사용도 함 
> ``` 
>
> **💾 Oracle**   
> 🔗 [OracleCLI](https://github.com/gayulz/ORACLECLI_project.git) 
> ```
> 학부생 때 오라클과 mssql 수업을 들어보며 오라클이 어렵지만 재밌었던 기억이 있었습니다.
> 국비학원에서 다시 오라클을 만졌을 때, 더 즐겁게 했던 것 같습니다
> 특히 PL/SQL문법을 스스로 공부를 하면서 프로시저와 트리거를 구현하며 핸들링 해본 경험이있습니다.
> ```
>
> **🍑 Javascript / Node js**    
> 🔗 [TODOWeather](https://github.com/gayulz/TODOLIST_project.git)   
> 🔗 [MiniGame](https://github.com/gayulz/JSMiniGame_project.git)    
> ```
> JS와 Node.js는 제가 가장 자신 있는 언어는 아니지만, 
> WEB-TODOLIST 프로젝트를 통해 보다 심도 있게 경험해본 언어입니다
> 프로젝트에서 비동기 통신을 적용하며 promise, async , await ~ fetch  문법과 .then.catch 문법을 사용해본 경험이 있습니다.
> ```
>
> **🌱 Springframework**  
> 🔗 [EMBAD](https://github.com/gayulz/EMBAD_project.git)  
> ```
> Spring Boot가 아닌 레거시 스프링 프레임워크를 사용하며 웹 서버 아키텍처와 흐름에 대해 배웠습니다
> IoC/DI와 POJO에 대해 공부하며 프로젝트에 최대한 적용하려 노력하였으며
> DB와 연결 할 때 퍼시스던트 프레임워크인 Mybatis를 사용경험이 있습니다.
> MVC2 패턴을 사용 하여 컨트롤러와 서비스, 뷰에 대한 비즈니스로직을 구현한 경험이 있습니다.
> 사용자의 로그인 로직에 따라 세션을 부여하고 삭제하는 기능도 구현 했습니다.
> ```
>
> **🔌 Open API**    
> 🔗 [TODOWeather](https://github.com/gayulz/TODOLIST_project.git)   
> 🔗 [EMBAD](https://github.com/gayulz/EMBAD_project.git)  
> ```
> - 카카오지도API , Geolocation API  
> 위치기반 프로젝트를 진행할 때 사용 하였음, 비동기 통신으로 사용 하였으며 서비스키 관리 및 사용 경험이 있음
>
> - 공공데이터포털 open API 
> EMBAD프로젝트때 사용 함 , API의 동기방식 통신과 비동기방식 통신 모두 적용 하여 사용해본 경험이 있음
> Springframework의 서버단에 API호출 로직을 구현하였으며 properties로 서비스키 관리될 수 있도록 적용함  
> ```

</details>

---

### 📝 Latest Blog Posts

"""

# ============================================================
# 푸터 생성
# ============================================================
footer = """
<div align="center">

---

### 📫 Contact Me

[![Blog](https://img.shields.io/badge/Tech%20Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://yurizzy.tistory.com)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gayulz@kakao.com)

---

![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgayulz&count_bg=%236C63FF&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Profile+Views&edge_flat=false)

*"꾸준함이 재능을 이긴다" - Keep learning, Keep growing 🌱*

</div>
"""

# ============================================================
# README 파일 생성
# ============================================================
readme_text = f"{markdown_text}{latest_blog_post_list}{footer}"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_text)

print("✅ README.md 파일이 성공적으로 업데이트되었습니다!")
print(f"📊 총 {min(len(feed['entries']), MAX_POST_NUM)}개의 블로그 포스트를 가져왔습니다.")
print()
print("💡 개선된 기능:")
print("   - 기술 스택 배지 추가")
print("   - 블로그 포스트에 주제별 이모지 자동 추가")
print("   - 연락처 정보 및 방문자 카운터 추가")
print("   - 더 깔끔한 레이아웃")
