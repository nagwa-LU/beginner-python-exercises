# Tic-Tac-Toe . nagwa
#اللعبه عباره عن 8 خانات وكل لاعب بدوره حيث اول خانه تبدأ بصفر والجميل انه تعتمد علي 
# جانب رقمي بحيث ينتبه اللاعب بأي خانه سيضع بها
def check_winner(board):
    """تفحص إذا كان هناك فائز"""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # الصفوف
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # الأعمدة
        [0, 4, 8], [2, 4, 6]  # الأقطار
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  # اللاعب الفائز (X أو O)
    return None

# إنشاء اللوحة المبدئية (قائمة بطول 9)
board = [" "] * 9  
# اختيار اللاعب الذي يبدأ
while True:
    current_player = input("اختر X أو O لتبدأ اللعب: ").upper()
    if current_player in ["X", "O"]:
        break
    else:
        print("يرجى اختيار X أو O فقط.")

while True:
    # عرض اللوحة
    print(f"\n{' | '.join(board[:3])}\n{'-'*9}\n{' | '.join(board[3:6])}\n{'-'*9}\n{' | '.join(board[6:])}")

    # أخذ المدخلات من اللاعب
    try:
        move = int(input(f"اللاعب {current_player}, اختر موضع (0-8): "))
        if board[move] != " ":
            print("المكان مشغول، حاول مرة أخرى.")
            continue
    except (ValueError, IndexError):
        print("إدخال غير صالح، حاول مرة أخرى.")
        continue

    # تحديث اللوحة بالحركة الجديدة
    board[move] = current_player

    # فحص إذا كان هناك فائز
    winner = check_winner(board)
    if winner:
        print(f"\n{' | '.join(board[:3])}\n{'-'*9}\n{' | '.join(board[3:6])}\n{'-'*9}\n{' | '.join(board[6:])}")
        print(f"تهانينا! اللاعب {winner} فاز!")
        break

    # فحص التعادل
    if " " not in board:
        print("اللعبة انتهت بالتعادل!")
        break

    # تبديل الدور إلى اللاعب الآخر
    current_player = "O" if current_player == "X" else "X"









    

          
      
          
