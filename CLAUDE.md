# 약 챙김이 작업 규칙

## 파일 구조
- `src.html`: 원본 코드. 수정은 항상 이 파일에서 한다. 사진 자리는 `__CAT__`, `__SLAP__` 표시로 둔다.
- `cat.jpg`, `slap.jpg`: 앱에 들어가는 사진.
- `build.py`: `src.html`에 사진을 넣어 완성본 `index.html`을 만든다.
- `index.html`: 빌드 결과물. 직접 고치지 않는다.

## 수정할 때마다 반드시 할 일
1. `src.html`을 고친다.
2. `python3 build.py --artifact <Artifact용 파일 경로>`로 빌드한다.
3. 브라우저로 기능을 시험한다.
4. 앱 링크(Artifact)를 다시 게시한다: https://claude.ai/artifact/HWG5r2qhtaJaJmfPE39wAQ
   - 같은 링크를 유지하려면 이 URL을 `url`로 넘겨 업데이트한다.
5. 바뀐 파일을 커밋해서 이 저장소의 `main` 브랜치에 push한다. (사용자 요청: 업데이트할 때마다 GitHub에 자동으로 올리기)

## 사용자 선호
- 존댓말로, 고등학생도 이해하기 쉽게 설명한다.
- 코드에는 무슨 동작을 하는지 한국어 주석을 단다.
