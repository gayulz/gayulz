"""
티스토리 RSS 피드 테스트 스크립트

이 스크립트는 실제로 RSS 피드에서 어떤 정보를 가져오는지 확인하는 용도입니다.
readme.py를 실행하기 전에 이 스크립트로 먼저 테스트해보세요.
"""

import feedparser
from bs4 import BeautifulSoup

# 티스토리 RSS URL
URL = "https://yurizzy.tistory.com/rss"

print("=" * 80)
print("티스토리 RSS 피드 테스트 시작")
print("=" * 80)
print()

# RSS 피드 파싱
print("📡 RSS 피드를 가져오는 중...")
feed = feedparser.parse(URL)

# 피드를 제대로 가져왔는지 확인
if not feed.entries:
    print("❌ 오류: RSS 피드를 가져오지 못했거나 비어있습니다.")
    print(f"   피드 상태: {feed.get('status', '알 수 없음')}")
    exit(1)

print(f"✅ 성공! 총 {len(feed.entries)}개의 포스트를 가져왔습니다.")
print()

# 첫 번째 포스트 상세 정보 확인
print("-" * 80)
print("📝 첫 번째 포스트 상세 정보")
print("-" * 80)

first_entry = feed.entries[0]

print(f"제목: {first_entry.get('title', '제목 없음')}")
print(f"링크: {first_entry.get('link', '링크 없음')}")

if 'published_parsed' in first_entry:
    date = first_entry.published_parsed
    print(f"날짜: {date.tm_year}.{date.tm_mon:02d}.{date.tm_mday:02d}")

print()
print("본문 내용 (description):")
description = first_entry.get('description', '') or first_entry.get('summary', '')
if description:
    print(description[:300])  # 처음 300자만 출력
    print("...")
else:
    print("본문 내용이 없습니다.")

print()

# 이미지 추출 테스트
print("-" * 80)
print("🖼️  이미지 추출 테스트")
print("-" * 80)

def extract_first_image(html_content):
    """HTML에서 첫 번째 이미지 URL 추출"""
    if not html_content:
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tag = soup.find('img')
    
    if img_tag and img_tag.get('src'):
        return img_tag['src']
    
    return None

# 첫 3개 포스트의 이미지 확인
for idx, entry in enumerate(feed.entries[:3]):
    print(f"\n포스트 {idx + 1}: {entry.get('title', '제목 없음')}")
    
    description = entry.get('description', '') or entry.get('summary', '')
    image_url = extract_first_image(description)
    
    if image_url:
        print(f"  ✅ 이미지 발견: {image_url[:80]}...")
    else:
        print(f"  ⚠️  이미지 없음 (기본 이미지 사용)")

print()
print("=" * 80)
print("테스트 완료!")
print("=" * 80)
print()
print("💡 다음 단계:")
print("   1. 이미지가 제대로 추출되는지 위의 결과를 확인하세요")
print("   2. 이미지가 없다면 티스토리 설정에서 RSS 피드에 이미지가 포함되도록 설정해야 합니다")
print("   3. 모든 것이 정상이면 readme.py를 실행하세요: python3 readme.py")
