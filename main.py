# main.py

# 기본 프롬프트 데이터
prompts = [
    {
        "title": "",
        "content": "",
        "category": "",
        "favorite": ""
    }, {
        "title": "",
        "content": "",
        "category": "",
        "favorite": ""
    }, {
        "title": "",
        "content": "",
        "category": "",
        "favorite": ""
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
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def add_prompt():
    print("\n=== 프롬프트 추가 ===")

def show_list():
    print("\n=== 프롬프트 목록 ===")

def search_by_category():
    print("\n=== 카테고리별 조회 ===")

def search_prompt():
    print("\n=== 프롬프트 검색 ===")

def detail_prompt():
    print("\n=== 프롬프트 상세 보기 ===") 

def manage_favorite():
    print("\n=== 즐겨찾기 관리 ===")

def show_favorite_list():
    print("\n=== 즐겨찾기 목록 ===")

def main():
    while True:
        show_menu()
        choice = input("선택: ")

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
            manage_favorite()
        elif choice == "7":
            show_favorite_list()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()