# main.py

import json
import os

# 기본 프롬프트 데이터
prompts = [
    {
        "title": "고객 상담 메모 → 요청사항 정리",
        "content": "다음은 고객 상담 중 기록된 메모야. 고객이 언급한 요청 사항을 누락 없이 항목별로 정리해서 목록으로 만들어줘.",
        "category": "텍스트 생성",
        "favorite": True,
        "views": 0
    },
    {
        "title": "새벽 침실 씬 이미지 생성 (MORN 광고 씬1)",
        "content": "완전히 어두운 방, 인공조명 전혀 없음. 대형 침대에 헤드보드를 기대고 앉아 창밖을 응시하는 남성의 측면 프로필. 오직 창문을 통해 들어오는 차가운 블루 톤 새벽빛만 존재. 도시 스카이라인이 프레임을 가득 채우는 시네마틱 구도, 초사실적 렌더링.",
        "category": "이미지 생성",
        "favorite": False,
        "views": 0
    },
    {
        "title": "n8n × Make 비교 구현 주제 기획",
        "content": "n8n이랑 Make 두 자동화 도구로 동일한 워크플로우를 구현해서 비교하려고 해. 두 도구 모두에서 무리 없이 구현 가능한 자동화 주제를 추천해줘.",
        "category": "자동화",
        "favorite": False,
        "views": 0
    }
]

categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 프롬프트 수정")
    print("7. 프롬프트 삭제")
    print("8. 즐겨찾기 추가/해제")
    print("9. 즐겨찾기 목록")
    print("10. 조회수 Top 목록")
    print("11. 데이터 저장 (JSON)")
    print("12. 데이터 불러오기 (JSON)")
    print("13. 카테고리별 Markdown 내보내기")
    print("0. 종료")

def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    title = input("제목: ").strip()
    while title == "":
        print("제목을 입력해 주세요.")
        title = input("제목: ").strip()

    content = input("내용: ").strip()
    while content == "":
        print("내용을 입력해 주세요.")
        content = input("내용: ").strip()

    print("\n카테고리 선택:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")
    print(f"{len(categories) + 1}) 직접 입력")

    cat_choice = input("선택: ").strip()
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
        category = categories[int(cat_choice) - 1]
    else:
        category = input("카테고리 직접 입력: ").strip()
        while category == "":
            print("카테고리를 입력해 주세요.")
            category = input("카테고리 직접 입력: ").strip()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0
    }
    prompts.append(new_prompt)

    print(f"\n프롬프트 '{title}'이(가) 추가되었습니다.")

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return 

    for i, prompt in enumerate(prompts, 1):
        star = "★" if prompt["favorite"] else "" 
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star}")

    print(f"\n총 {len(prompts)}개의 프롬프트가 등록되어 있습니다.")

def search_by_category():
    print("\n=== 카테고리별 조회 ===")

    print("\n카테고리 선택:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")

    cat_choice = input("선택: ").strip()
    if not (cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories)):
        print("잘못된 번호입니다.")
        return

    category = categories[int(cat_choice) - 1]
    filtered = [p for p in prompts if p["category"] == category]

    if not filtered:
        print(f"\n'{category}' 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print(f"\n=== [{category}] 프롬프트 목록 ===")
    for i, prompt in enumerate(filtered, 1):
        star = "★" if prompt["favorite"] else ""
        print(f"{i}. {prompt['title']}{star}")

    print(f"\n총 {len(filtered)}개의 프롬프트가 있습니다.")

def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip()
    while keyword == "":
        print("검색어를 입력해 주세요.")
        keyword = input("검색어: ").strip()

    results = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]

    if not results:
        print(f"\n'{keyword}'에 대한 검색 결과가 없습니다.")
        return

    print(f"\n=== '{keyword}' 검색 결과 ===")
    for i, prompt in enumerate(results, 1):
        star = "★" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star}")

    print(f"\n총 {len(results)}개의 프롬프트가 검색되었습니다.")

def detail_prompt():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        star = "★" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star}")

    choice = input("\n번호 선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[int(choice) - 1]
    prompt["views"] += 1

    star = "★" if prompt["favorite"] else ""
    print(f"\n제목: {prompt['title']}{star}")
    print(f"카테고리: {prompt['category']}")
    print(f"내용: {prompt['content']}")
    print(f"조회수: {prompt['views']}")

def update_prompt():
    print("\n=== 프롬프트 수정 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        star = "★" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star}")

    choice = input("\n수정할 번호 선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[int(choice) - 1]

    print("\n수정할 내용을 입력하세요. (그대로 두려면 Enter)")

    title = input(f"제목 ({prompt['title']}): ").strip()
    if title != "":
        prompt["title"] = title

    content = input(f"내용 ({prompt['content']}): ").strip()
    if content != "":
        prompt["content"] = content

    print("\n카테고리 선택:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")

    cat_choice = input(f"선택 (현재: {prompt['category']}, 그대로 두려면 Enter): ").strip()
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
        prompt["category"] = categories[int(cat_choice) - 1]
    elif cat_choice != "":
        prompt["category"] = cat_choice

    print(f"\n프롬프트 '{prompt['title']}'이(가) 수정되었습니다.")

def delete_prompt():
    print("\n=== 프롬프트 삭제 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        star = "★" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star}")

    choice = input("\n삭제할 번호 선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[int(choice) - 1]

    confirm = input(f"'{prompt['title']}'을(를) 삭제하시겠습니까? (y/n): ").strip().lower()
    if confirm != "y":
        print("삭제가 취소되었습니다.")
        return

    prompts.pop(int(choice) - 1)
    print(f"\n프롬프트 '{prompt['title']}'이(가) 삭제되었습니다.")

def manage_favorite():
    print("\n=== 즐겨찾기 추가/해제 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, 1):
        star = "★" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star}")

    choice = input("\n번호 선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[int(choice) - 1]
    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print(f"\n프롬프트 '{prompt['title']}'이(가) 즐겨찾기에 추가되었습니다.")
    else:
        print(f"\n프롬프트 '{prompt['title']}'이(가) 즐겨찾기에서 해제되었습니다.")

def show_favorite_list():
    print("\n=== 즐겨찾기 목록 ===")

    favorites = [p for p in prompts if p["favorite"]]

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(favorites, 1):
        print(f"{i}. [{prompt['category']}] {prompt['title']}★")

    print(f"\n총 {len(favorites)}개의 즐겨찾기 프롬프트가 있습니다.")

def show_top_viewed():
    print("\n=== 조회수 Top 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    sorted_prompts = sorted(prompts, key=lambda p: p["views"], reverse=True)

    for i, prompt in enumerate(sorted_prompts, 1):
        star = "★" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']}{star} (조회수: {prompt['views']})")

def save_to_json():
    print("\n=== 데이터 저장 (JSON) ===")

    filename = input("저장할 파일명 (기본: prompts.json): ").strip()
    if filename == "":
        filename = "prompts.json"
    if not filename.endswith(".json"):
        filename += ".json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)

    print(f"\n{len(prompts)}개의 프롬프트가 '{filename}'에 저장되었습니다.")

def load_from_json():
    print("\n=== 데이터 불러오기 (JSON) ===")

    filename = input("불러올 파일명 (기본: prompts.json): ").strip()
    if filename == "":
        filename = "prompts.json"
    if not filename.endswith(".json"):
        filename += ".json"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            loaded = json.load(f)
    except FileNotFoundError:
        print(f"'{filename}' 파일을 찾을 수 없습니다.")
        return
    except json.JSONDecodeError:
        print(f"'{filename}' 파일의 형식이 올바르지 않습니다.")
        return

    prompts.clear()
    prompts.extend(loaded)

    print(f"\n'{filename}'에서 {len(prompts)}개의 프롬프트를 불러왔습니다.")

def export_to_markdown():
    print("\n=== 카테고리별 Markdown 내보내기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    os.makedirs("export", exist_ok=True)

    grouped = {}
    for prompt in prompts:
        grouped.setdefault(prompt["category"], []).append(prompt)

    for category, items in grouped.items():
        filename = os.path.join("export", f"{category}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {category}\n\n")
            for prompt in items:
                star = " ★" if prompt["favorite"] else ""
                f.write(f"## {prompt['title']}{star}\n\n")
                f.write(f"{prompt['content']}\n\n")
                f.write(f"- 조회수: {prompt['views']}\n\n")

    print(f"\n{len(grouped)}개의 카테고리 파일이 'export' 폴더에 저장되었습니다.")

def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            detail_prompt()
        elif choice == "6":
            update_prompt()
        elif choice == "7":
            delete_prompt()
        elif choice == "8":
            manage_favorite()
        elif choice == "9":
            show_favorite_list()
        elif choice == "10":
            show_top_viewed()
        elif choice == "11":
            save_to_json()
        elif choice == "12":
            load_from_json()
        elif choice == "13":
            export_to_markdown()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()