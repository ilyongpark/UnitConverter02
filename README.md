# UnitConverter02

길이 단위(`meter`, `feet`, `yard`)를 변환하는 Python CLI 프로그램.

`UnitConverter_02d` 세션에서는 Mom Test 기반으로 **모호한 스펙을 PRD에 명시**하고, 요구사항·테스트·코드를 **REQ 단위로 추적 가능하게** 재구현하는 것을 목표로 한다.

---

## 빠른 시작

### 요구 사항

- Python 3.x

### 설치 및 실행

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate

# 실행
python UnitConverter.py
```

### 사용 예

```
Insert value for converting (ex: meter:2.5): meter:2.5
2.5 meter = 2.5 meter
2.5 meter = 8.2 feet
2.5 meter = 2.7 yard
```

---

## 지원 단위 및 변환율

| 변환 | 비율 |
|------|------|
| 1 meter | 3.28084 feet |
| 1 meter | 1.09361 yard |

- 모든 변환은 **meter를 기준 단위**로 환산한다.
- 출력 값은 소수점 **1자리 반올림** (상세: [`docs/PRD.md`](docs/PRD.md))

---

## 입력 형식

| 항목 | 규칙 |
|------|------|
| 형식 | `{unit}:{value}` |
| 예시 | `meter:2.5`, `feet:10`, `yard:3` |
| 지원 단위 | `meter`, `feet`, `yard` (소문자) |

### 오류 처리

| 조건 | 메시지 |
|------|--------|
| 콜론 없음 | `Invalid format. Use unit:value (ex: meter:2.5)` |
| 숫자 아님 | `Invalid number: {value}` |
| 미지원 단위 | `Unknown unit: {unit}` |

---

## 프로젝트 구조

```
UnitConverter02/
├── UnitConverter.py              # CLI 진입점 (현재 구현)
├── docs/
│   └── PRD.md                    # 요구사항 정의 (REQ ID, DoD)
├── UnitConverter_02d_workbook.md # Mom Test · 8계층 워크북
├── Report/
│   └── 01_Report.md
├── Prompting/
│   ├── 01_Exported_Transcript.md
│   └── 01_Exported_Transcript.jsonl
└── README.md
```

---

## 요구사항 요약

상세 스펙은 [`docs/PRD.md`](docs/PRD.md)를 참고한다.

### In Scope (UnitConverter_02d)

- `단위:값` 입력 및 변환 출력
- meter / feet / yard 변환
- 입력 검증 (형식, 음수, 미지원 단위)
- REQ ↔ 테스트 ↔ 코드 추적 (`REQ_TRACE.md` 예정)

### Out of Scope (이번 세션)

- JSON/YAML 설정 외부화
- 동적 단위 등록 (`1 cubit = 0.4572 meter`)
- JSON / CSV / 다중 출력 포맷
- 대규모 OCP/SRP 리팩터링 (테스트 통과 후 최소 변경만)

### 성공 기준 (DoD)

| ID | 내용 |
|----|------|
| SC-1 | PRD 예시 출력·반올림 테스트 통과 |
| SC-2 | 변환 테스트가 리팩터링 전에 존재, 회귀 검출 가능 |
| SC-3 | In scope REQ 매핑 완료, Out of scope 명시 |

---

## 테스트 (예정)

```bash
pip install pytest
pytest tests/ -v
```

Test Loop 스크립트: `scripts/test_loop.ps1` (워크북 참고)

---

## 관련 문서

| 문서 | 설명 |
|------|------|
| [`docs/PRD.md`](docs/PRD.md) | 기능·품질 요구사항, REQ ID, 반올림 규칙 |
| [`UnitConverter_02d_workbook.md`](UnitConverter_02d_workbook.md) | Mom Test 결과, R-G-I-O, Rule/Command/Test Loop |
| [`Report/01_Report.md`](Report/01_Report.md) | 세션 보고서 |

---

## 실습 Activities (6시간 · 참고)

1. 문제 코드 및 기본 요구사항 분석 (0.5시간)
2. 기본·품질 요구사항 구현 (2시간)
3. TC 구현 (0.5시간)
4. 추가 요구사항 구현 (2시간)
5. 회고 및 발표 (1시간)

> UnitConverter_02d 세션에서는 **1~3단계(기본·품질·TC)** 를 우선하며, 추가 요구사항은 PRD Out of Scope로 분리한다.


# Refactorig To-Do List