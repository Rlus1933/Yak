"""약 챙김이 빌드 스크립트

src.html(원본 코드)의 사진 자리 표시(__CAT__, __SLAP__)에
cat.jpg, slap.jpg를 글자(base64)로 바꿔 넣어서,
사진까지 들어 있는 완성본 index.html 한 파일을 만든다.

사용법:
    python3 build.py                     # index.html 만들기
    python3 build.py --artifact 경로      # 앱 링크(Artifact)용 파일도 함께 만들기
"""
import base64
import sys
from pathlib import Path

ROOT = Path(__file__).parent   # 이 파일이 있는 폴더(저장소 맨 위)

# Artifact는 문서 머리말(doctype 등)을 스스로 붙이므로, Artifact용 파일에서는 이 4줄을 뺀다
HEADER = (
    '<!doctype html>\n'
    '<html lang="ko">\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
)


def data_uri(name):
    """사진 파일을 HTML 안에 바로 넣을 수 있는 data: 주소 글자로 바꾼다."""
    raw = (ROOT / name).read_bytes()
    return 'data:image/jpeg;base64,' + base64.b64encode(raw).decode()


def main():
    src = (ROOT / 'src.html').read_text(encoding='utf-8')
    if not src.startswith(HEADER):
        sys.exit('src.html 맨 앞의 문서 머리말 4줄이 바뀌었습니다. build.py의 HEADER도 맞춰 주세요.')

    # 자리 표시를 실제 사진으로 바꾼 완성본
    built = src.replace('__CAT__', data_uri('cat.jpg')).replace('__SLAP__', data_uri('slap.jpg'))
    (ROOT / 'index.html').write_text(built, encoding='utf-8')
    print('index.html 만듦')

    # --artifact 경로가 있으면, 머리말을 뺀 Artifact용 파일도 만든다
    if '--artifact' in sys.argv:
        out = Path(sys.argv[sys.argv.index('--artifact') + 1])
        out.write_text(built[len(HEADER):], encoding='utf-8')
        print(f'{out} 만듦 (Artifact용)')


if __name__ == '__main__':
    main()
