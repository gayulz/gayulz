import feedparser

URL = "https://yurizzy.tistory.com/rss"
MAX_POST_NUM = 10
latest_blog_post_list = ""

# 피드 파서 객체 생성
feed = feedparser.parse(URL)

# 피드 항목 출력
# for entry in feed.entries:
#     print("제목:", entry.title)
#     print("링크:", entry.link)


for idx, feed in enumerate(feed["entries"]):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed["published_parsed"]
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"


markdown_text = """
<p align="center"> 
<img src="https://capsule-render.vercel.app/api?type=Cylinder&color=timeGradient&height=120&section=header&text=My%20name%20is👋%20Gayul%20Kim&fontSize=50&animation=twinkling" width="100%"/> </p>
<p align="center"> 
<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=gayulz&theme=2077" width="100%" />
<img src="http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=gayulz&theme=2077&exclude=HTML,CSS" width="49%"/>
<img src="http://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=gayulz&theme=2077&exclude=HTML,CSS" width="49%"/>
<img src="http://github-profile-summary-cards.vercel.app/api/cards/stats?username=gayulz&theme=2077" width="49%"/>
<img src="http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=gayulz&theme=2077&utcOffset=09" width="49%" />
</p>
<details><summary>경험한 기술 스토리 🐥 Click ⭐️</summary>

> **✨ JAVA**   
🔗 [너만가냥 나도가개](https://github.com/gayulz/JAVAGUI_project.git)    
🔗 [EMBAD](https://github.com/gayulz/EMBAD_project.git)         
```
가장 자신있는 언어 중 1가지 입니다 
학부 시절에도 즐겁게 배웠으며, 국비 교육 과정에서도 열정적으로 학습한 언어입니다.
클래스, 상속, 다형성, 인터페이스를 사용해 본 경험이 있으며 , oracle DB와 연결하여 CRUD를 구현해본 경험이 있습니다.
```
> **🌼 HTML5 / CSS3**   
🔗 [MiniGame](https://github.com/gayulz/JSMiniGame_project.git)    
🔗 [EMBAD](https://github.com/gayulz/EMBAD_project.git)  
🔗 [TODOWeather](https://github.com/gayulz/TODOLIST_project.git)   
```
프로젝트를 진행 하면서 웹 페이지의 뼈대(골격)을 만들며 색상이나 스타일을 입히는 것으로 사용 했습니다. 
HTML은 시멘틱 태그를 사용 하여 섹션을 나누었고 
CSS는 주로 정렬이나 이미지, 컬러 등 스타일 위주로 사용 했습니다
추후 Spring 프로젝트에선 JSP파일에 사용도 함 
``` 
> **🛢️ Oracle**   
🔗 [OracleCLI](https://github.com/gayulz/ORACLECLI_project.git) 
```
학부생 때 오라클과 mssql 수업을 들어보며 오라클이 어렵지만 재밌었던 기억이 있었습니다.
국비학원에서 다시 오라클을 만졌을 때, 더 즐겁게 했던 것 같습니다
특히 PL/SQL문법을 스스로 공부를 하면서 프로시저와 트리거를 구현하며 핸들링 해본 경험이있습니다.
```
> **🍑 Javascript / Node js**    
🔗 [TODOWeather](https://github.com/gayulz/TODOLIST_project.git)   
🔗 [MiniGame](https://github.com/gayulz/JSMiniGame_project.git)    
```
JS와 Node.js는 제가 가장 자신 있는 언어는 아니지만, 
WEB-TODOLIST 프로젝트를 통해 보다 심도 있게 경험해본 언어입니다
프로젝트에서 비동기 통신을 적용하며 promise, async , await ~ fetch  문법과 .then.catch 문법을 사용해본 경험이 있습니다.
```
> **🌱 Springframework**  
🔗 [EMBAD](https://github.com/gayulz/EMBAD_project.git)  
```
Spring Boot가 아닌 레거시 스프링 프레임워크를 사용하며 웹 서버 아키텍처와 흐름에 대해 배웠습니다
IoC/DI와 POJO에 대해 공부하며 프로젝트에 최대한 적용하려 노력하였으며
DB와 연결 할 때 퍼시스던트 프레임워크인 Mybatis를 사용경험이 있습니다.
MVC2 패턴을 사용 하여 컨트롤러와 서비스, 뷰에 대한 비즈니스로직을 구현한 경험이 있습니다.
사용자의 로그인 로직에 따라 세션을 부여하고 삭제하는 기능도 구현 했습니다.
```
> **🕹️ open API**    
🔗 [TODOWeather](https://github.com/gayulz/TODOLIST_project.git)   
🔗 [EMBAD](https://github.com/gayulz/EMBAD_project.git)  
```
- 카카오지도API , Geolocation API  
위치기반 프로젝트를 진행할 때 사용 하였음, 비동기 통신으로 사용 하였으며 서비스키 관리 및 사용 경험이 있음

- 공공데이터포털 open API 
EMBAD프로젝트때 사용 함 , API의 동기방식 통신과 비동기방식 통신 모두 적용 하여 사용해본 경험이 있음
Springframework의 서버단에 API호출 로직을 구현하였으며 properties로 서비스키 관리될 수 있도록 적용함  
```

</details>
</div>

---
# 🚧 Latest Blog Post 🚧

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_text)
