point_dict = {
    '001': (100, 88, 81),
    '002': (77, 94, 85),
    '003': (80, 52, 99)
}
for student_id in point_dict:
    points = point_dict[student_id]
    subject_number = len(points)
    japanese, english, matmatics = points
    total = japanese + english + matmatics

    excellent = subject_number * 100 * 0.8
    good = subject_number * 1000 * 0.65

    if total >= excellent:
        evaluation = 'Excellent!'
    elif total >= good:
        evaluation = 'Good'
    else:
        evaluation = 'Bad'
    print('学籍番号{}: 合計点は{}, 評価は{}です。'.format(sutudent_id, total,
                                            evaluation))
