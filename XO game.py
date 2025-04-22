# Tic-Tac-Toe . nagwa
#اللعبه عباره عن 8 خانات وكل لاعب بدوره حيث اول خانه تبدأ بصفر 
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
            return board[a]
    return None

# أخذ أسماء اللاعبين
player1_name = input("أدخل اسم اللاعب الأول: ")
player2_name = input("أدخل اسم اللاعب الثاني: ")

# اختيار اللاعب الذي يبدأ
while True:
    player_choice = input(f"{player1_name}, اختر X أو O لتبدأ اللعب: ").upper()
    if player_choice in ["X", "O"]:
        break
    else:
        print("يرجى اختيار X أو O فقط.")

# تثبيت رموز اللاعبين
player_symbols = {
    player1_name: player_choice,
    player2_name: "O" if player_choice == "X" else "X"
}

turn = player1_name  # نبدأ دائماً باللاعب الأول

# بداية اللعب
while True:
    # إنشاء اللوحة المبدئية
    board = [" "] * 9

    while True:
        # عرض اللوحة
        print(f"\n{' | '.join(board[:3])}\n{'-'*9}\n{' | '.join(board[3:6])}\n{'-'*9}\n{' | '.join(board[6:])}")

        # أخذ المدخلات من اللاعب الحالي
        try:
            move = int(input(f"{turn} ({player_symbols[turn]}), اختر موضع (0-8): "))
            if board[move] != " ":
                print("المكان مشغول، حاول مرة أخرى.")
                continue
        except (ValueError, IndexError):
            print("إدخال غير صالح، حاول مرة أخرى.")
            continue

        # تحديث اللوحة
        board[move] = player_symbols[turn]

        # فحص الفوز
        winner = check_winner(board)
        if winner:
            print(f"\n{' | '.join(board[:3])}\n{'-'*9}\n{' | '.join(board[3:6])}\n{'-'*9}\n{' | '.join(board[6:])}")
            winning_player = [player for player, symbol in player_symbols.items() if symbol == winner][0]
            print(f"تهانينا! {winning_player} ({winner}) فاز!")
            break

        # فحص التعادل
        if " " not in board:
            print("اللعبة انتهت بالتعادل!")
            break

        # تبديل الدور
        turn = player2_name if turn == player1_name else player1_name

    # سؤال: هل تريدان اللعب مرة ثانية؟
    play_again = input("هل تريدان اللعب مرة أخرى؟ (نعم/لا): ").lower()
    if play_again != "نعم":
        print("شكرًا للعب! إلى اللقاء!")
        break
    else:
        turn = player1_name  # نبدأ دائماً باللاعب الأول









    

          
      
          
