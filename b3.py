import sys

name_patient = input("Nhập tên bệnh nhân: ")
age = int(input("Nhập tuổi bệnh nhân: "))

if name_patient.strip() == "" or age < 0 or age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    sys.exit()

if age < 6:
    send_messenger = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."

elif age >= 80:
    send_messenger = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."

else:
    send_messenger = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

# dữ liệu đầu vào gồm: tên bệnh nhân, tuổi, 
# đầu ra là chia tuổi theo điều kkiệnddeer xác định độ ưu tiên 
# mô tả phân luồng: kiểm tra điều kiện lỗi trước, nếu thuộc 1 trong các điều kiện sai -> dừng chương trình luôn
# nếu thuộc điều kiện đúng thì thuộc hiện chia mức độ ưu tiên

print(f"""
===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====

Tên bệnh nhân: {name_patient}
Tuổi: {age}

Kết quả phân luồng:
{send_messenger}

==================================
""")
