"""
RSS 피드 구조를 파일로 저장하는 간단한 스크립트
"""
import feedparser
from bs4 import BeautifulSoup

URL = "https://yurizzy.tistory.com/rss"

# RSS 피드 가져오기
feed = feedparser.parse(URL)

# 결과를 파일로 저장
with open("rss_check_result.txt", "w", encoding="utf-8") as f:
    f.write("=" * 80 + "\n")
    f.write("티스토리 RSS 피드 분석 결과\n")
    f.write("=" * 80 + "\n\n")
    
    f.write(f"총 포스트 개수: {len(feed.entries)}\n\n")
    
    if feed.entries:
        f.write("-" * 80 + "\n")
        f.write("첫 번째 포스트 상세 정보\n")
        f.write("-" * 80 + "\n\n")
        
        first = feed.entries[0]
        f.write(f"제목: {first.get('title', 'N/A')}\n")
        f.write(f"링크: {first.get('link', 'N/A')}\n\n")
        
        f.write("Description 필드 내용:\n")
        f.write("-" * 40 + "\n")
        desc = first.get('description', '') or first.get('summary', '')
        f.write(desc[:1000] + "\n\n")
        f.write("-" * 40 + "\n\n")
        
        # 이미지 추출 시도
        soup = BeautifulSoup(desc, 'html.parser')
        img_tag = soup.find('img')
        
        if img_tag:
            f.write("✅ 이미지 발견!\n")
            f.write(f"이미지 src: {img_tag.get('src', 'N/A')}\n")
        else:
            f.write("❌ description 필드에 이미지 태그가 없습니다.\n")
        
        f.write("\n")
        f.write("-" * 80 + "\n")
        f.write("처음 3개 포스트의 이미지 정보\n")
        f.write("-" * 80 + "\n\n")
        
        for idx, entry in enumerate(feed.entries[:3]):
            f.write(f"\n{idx + 1}. {entry.get('title', 'N/A')}\n")
            desc = entry.get('description', '') or entry.get('summary', '')
            soup = BeautifulSoup(desc, 'html.parser')
            img = soup.find('img')
            if img and img.get('src'):
                f.write(f"   이미지: {img.get('src')}\n")
            else:
                f.write(f"   이미지: 없음\n")

print("✅ 분석 완료! rss_check_result.txt 파일을 확인하세요.")
