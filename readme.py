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
    latest_blog_post_list += f"📅 `{date_str}` : {emoji} **[{title}]({link})**\n\n"

# ============================================================
# README 마크다운 템플릿
# ============================================================
markdown_text = """

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=blur&height=250&color=gradient&text=👩🏻‍💻안녕하세요-nl-Hello%20👋%20Hola&fontAlignY=50&fontColor=FFDD00&fontSize=80&animation=twinkling&section=header&reversal=true&descAlign=47&descAlignY=56&fontAlign=51&rotate=0&strokeWidth=1&stroke=FAF8FF" width="100%"/>

## 끊임없이 배우고 성장하는 것을 즐기는 신입 개발자 입니다 🙋🏻‍♀️

### 🛠️ In My Tech Stack

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

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=gayulz&theme=vision_friendly_dark" width="100%" />

<p align="center">
<img src="http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=gayulz&theme=vision_friendly_dark&exclude=HTML,CSS" width="49%"/>
<img src="http://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=gayulz&theme=vision_friendly_dark&exclude=HTML,CSS" width="49%"/>
</p>

<p align="center">
<img src="http://github-profile-summary-cards.vercel.app/api/cards/stats?username=gayulz&theme=vision_friendly_dark" width="49%"/>
<img src="http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=gayulz&theme=vision_friendly_dark&utcOffset=09" width="49%" />
</p>
</div>


---

<br>

## 📝 Latest Blog Posts

<br>

"""

# ============================================================
# 푸터 생성
# ============================================================
footer = """
<div align="center">
<br>
<br>


---

## 📫 Contact Me
[![Blog](https://img.shields.io/badge/Tech%20Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://yurizzy.tistory.com)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gayulz@kakao.com)

---

<br>
<img width="296" height="168" alt="Image" src="https://github.com/user-attachments/assets/390c69f7-95f0-4b08-b248-8b14384c1957" />

### *"꾸준함이 재능을 이긴다" - Keep learning, Keep growing 🌱*

<br>
<br>
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
