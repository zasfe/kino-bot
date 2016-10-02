
class MessageResource:
    ERROR = "에러가 발생하였습니다."
    CREATE = "등록이 완료되었습니다!"
    EMPTY = "비어있습니다. 새로 등록해주세요!."
    READ = "등록된 리스트입니다."
    UPDATE = "변경이 완료되었습니다."
    DELETE = "삭제 완료!"
    NOTIFIER_START = "Notifier 기능을 시작합니다."
    NOTIFIER_STOP = "Notifier 기능을 중지합니다."

    SCHEDULER_CREATE_START = "알람 등록을 진행합니다."
    SCHEDULER_CREATE_STEP1 = "시간대를 선택해주세요!\n (ex. #1)"
    SCHEDULER_CREATE_STEP2 = "다음으로 주기를 입력해주세요!\n (ex. 30 분)"
    SCHEDULER_CREATE_STEP3 = "사용될 함수는 무엇인가요?\n (ex. send_message, {\"text\"=\"Test!\"})"

    BETWEEN_CREATE_START = "시간대 등록을 진행합니다."
    BETWEEN_CREATE_STEP1 = "시간간격을 입력해주세요!\n(ex. 12:00~19:00)"
    BETWEEN_CREATE_STEP2 = "입력하신 시간대를 설명해주시겠어요?\n (ex. 업무 시간)"

    TIMER_ICON = ":mantelpiece_clock: "
    WHITE_LIST_ICON = ":white_medium_small_square: "
    WHITE_ELEMENT_ICON = "   :white_circle: "
    BLACK_LIST_ICON = ":black_medium_small_square: "
    BLACK_ELEMENT_ICON = "   :black_circle: "
    BLUE_DIAMOND_ICON = ":small_blue_diamond: "
    ORANGE_DIAMOND_ICON = ":small_orange_diamond: "
    SEND_MESSAGE_ICON = ":speech_balloon: "