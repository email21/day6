## 예시 log.txt file 만들기 ##

from datetime import datetime

log_lines=[]

for i in range(1,21):
    if i%5==0:
        log_lines.append(f"[ERROR] 오류 발생 at line {i}\n")
    elif i%3==0:
        log_lines.append(f"[WARNING] 경고 발생 at line {i}\n")
    else:
        log_lines.append(f"[INFO] 정상 처리 at line {i}\n")
        
with open("log.txt", "w") as f:
    f.write(f"### 에러 로그 생성 시간:{datetime.now()}\n\n")
    f.writelines(log_lines)
    
print("✅ log.txt 파일 생성 완료")