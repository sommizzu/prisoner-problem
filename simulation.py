def run_simulation():
boxes = initialize_boxes()  # 상자를 초기화 (1.상자를 초기화 하는 함수)
return all(prisoner_strategy(boxes, prisoner_number) for prisoner_number in range(1, 101))  # 모든 감옥수에 대한 세운 규칙 실행 (2.죄수의 상자선택과 번호확인 함수)