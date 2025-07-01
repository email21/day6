# 과제1
# 매일 생성되는 log.txt file 정리하기
# 정상 로그와 에러 로그가 섞여있으며, 에러로그는 [ERROR] 로 시작한다.
# 결과물 : error_log.txt 로 에러로그만 따로 모아서 저장하기

# 1. 파일 읽어오기 - 예외처리
try:
    with open("log.txt","r") as f: # r : 읽기 모드 (파일이 존재해야 함)
        lines=f.readlines()   # 파일의 모든 줄을 리스트로 읽어오기, 줄 끝에는 보통 \n(줄바꿈 문자)이 포함
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
    exit()

# 2. 에러 추출하기
error_lines = [line for line in lines if line[0:7] == "[ERROR]" ]

# 추가 - info, warning 에 대해서도 따로 저장하기
info_lines = [line for line in lines if line.startswith("[INFO]")]
warning_lines = [line for line in lines if line.startswith("[warning]")]

# 3. 추출한 내용 파일에 쓰기
with open("error_log.txt","w") as f: # w : 쓰기 모드 (파일이 없으면 생성, 기존 파일이 있으면 덮어씀)
    f.writelines(error_lines)
    
with open("info_log.txt","w") as f:
    f.writelines(info_lines)
    
with open("warning_log.txt", "w") as f:
    f.writelines(warning_lines)