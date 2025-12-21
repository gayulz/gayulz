import feedparser
from bs4 import BeautifulSoup

# RSS 피드 주소와 설정
URL = "https://yurizzy.tistory.com/rss"
MAX_POST_NUM = 10  # 최대 표시할 포스트 개수
DEFAULT_IMAGE = "https://via.placeholder.com/400x200/6C63FF/FFFFFF?text=No+Image"  # 대표 이미지가 없을 때 사용할 기본 이미지

# 티스토리 RSS 피드 파싱
feed = feedparser.parse(URL)

def extract_first_image(html_content):
    """
    HTML 콘텐츠에서 첫 번째 이미지의 URL을 추출합니다.

    설명: RSS 피드의 description 필드에는 HTML 형식으로 본문이 들어있습니다.
         BeautifulSoup을 사용해서 이 HTML을 파싱하고,
         첫 번째 <img> 태그의 src 속성 값을 가져옵니다.

    Args:
        html_content: HTML 형식의 문자열

    Returns:
        이미지 URL 문자열 또는 None (이미지가 없는 경우)
    """
    if not html_content:
        return None

    # BeautifulSoup으로 HTML 파싱 (html.parser 사용)
    soup = BeautifulSoup(html_content, 'html.parser')

    # 첫 번째 img 태그 찾기
    img_tag = soup.find('img')

    # img 태그가 있고 src 속성이 있으면 반환
    if img_tag and img_tag.get('src'):
        return img_tag['src']

    return None

# 블로그 포스트 카드 HTML 생성
latest_blog_post_cards = ""

for idx, entry in enumerate(feed["entries"]):
    # 최대 개수 제한
    if idx >= MAX_POST_NUM:
        break

    # 날짜 정보 추출
    feed_date = entry["published_parsed"]
    date_str = f"{feed_date.tm_year}.{feed_date.tm_mon:02d}.{feed_date.tm_mday:02d}"

    # 제목과 링크
    title = entry['title']
    link = entry['link']

    # description에서 이미지 추출 (대표 이미지)
    description = entry.get('description', '') or entry.get('summary', '')
    image_url = extract_first_image(description)

    # 이미지가 없으면 기본 이미지 사용
    if not image_url:
        image_url = DEFAULT_IMAGE

    # HTML 테이블 형식의 카드 생성
    # 각 포스트를 테이블의 한 행으로 만들어서 이미지와 텍스트를 나란히 배치합니다
    card_html = f"""
<tr>
  <td width="400">
    <a href="{link}">
      <img src="{image_url}" alt="{title}" width="400" style="border-radius: 8px;"/>
    </a>
  </td>
  <td width="600" style="padding-left: 20px; vertical-align: top;">
    <h3 style="margin: 0 0 10px 0;">
      <a href="{link}" style="text-decoration: none; color: #333;">
        {title}
      </a>
    </h3>
    <p style="margin: 0; color: #666; font-size: 14px;">
      📅 {date_str}
    </p>
  </td>
</tr>
"""

    latest_blog_post_cards += card_html


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

---

## 🫶 MY Tistory Posts 🫶

<table width="100%" style="border: none;">
"""

# README 파일 생성
readme_text = f"{markdown_text}{latest_blog_post_cards}\n</table>"

# UTF-8 인코딩으로 README.md 파일 작성
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_text)

# 완료 메시지 출력
print("✅ README.md 파일이 성공적으로 업데이트되었습니다!")
print(f"📊 총 {min(len(feed['entries']), MAX_POST_NUM)}개의 블로그 포스트를 가져왔습니다.")
