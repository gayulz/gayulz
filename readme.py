"""
GitHub 프로필 README 자동 생성 스크립트

티스토리 블로그의 최신 글을 가져와서 README.md를 자동으로 업데이트합니다.
"""

import feedparser
import re

# 설정
URL = "https://yurizzy.tistory.com/rss"
MAX_POST_NUM = 10

# RSS 피드 파싱
feed = feedparser.parse(URL)

# 블로그 포스트 리스트 생성
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
    emoji = "📝"
    title_lower = title.lower()

    if "실무" in title_lower:
        emoji = "📖"
    elif "mig" in title_lower or "마이그레이션" in title_lower or "고도화" in title_lower:
        emoji = "🚀"
    elif "spring" in title_lower or "springframework" in title_lower:
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



    # 포스트 아이템 생성
    latest_blog_post_list += f"📅 `{date_str}` : {emoji} **[{title}]({link})**\n\n"

# 기존 README.md 내용 읽기
with open("README.md", "r", encoding="utf-8") as f:
    readme_text = f.read()

# 정규표현식을 사용하여 마커 사이의 내용 교체
# 마커: <!-- BLOG-POST-LIST:START --> 와 <!-- BLOG-POST-LIST:END -->
pattern = r"(<!-- BLOG-POST-LIST:START -->\n)[\s\S]*?(<!-- BLOG-POST-LIST:END -->)"
# re.sub에서 \g<1>은 첫 번째 그룹, \g<2>는 두 번째 그룹을 의미합니다.
replacement = rf"\g<1>{latest_blog_post_list}\g<2>"
new_readme_text = re.sub(pattern, replacement, readme_text)

# README 파일 업데이트
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme_text)

print("✅ README.md 파일이 성공적으로 업데이트되었습니다!")
print(f"📊 총 {min(len(feed['entries']), MAX_POST_NUM)}개의 블로그 포스트를 가져왔습니다.")
