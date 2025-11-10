def BMI(height,weight):
    return weight/(height**2)
def PhanLoai(bmi):
    match bmi:
        case bmi if bmi<18.5:
            return "Gầy"
        case bmi if bmi<24.9:
           return "Bình thường"
        case bmi if bmi<29.9:
           return "Hơi béo"
        case bmi if bmi<34.9:
            return "Béo Phì Cấp Độ 1"
        case bmi if bmi<39.9:
            return "Béo Phì Cấp Độ 2"
        case _:
            return "Béo Phì Cấp Độ 3"
def NguyCoBenh(bmi):
    match bmi:
        case bmi if bmi < 18.5:
            return "Thấp"
        case bmi if bmi < 24.9:
            return "Trung Bình"
        case bmi if bmi < 29.9:
            return "Cao"
        case bmi if bmi < 34.9:
            return "Cao"
        case bmi if bmi < 39.9:
            return "Rất Cao"
        case _:
            return "Nguy Hiểm"