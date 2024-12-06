# -*- coding: utf-8 -*-
from Types import DataType


class BadStudent:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        count_with_debts = 0

        for key in self.data:  # Перебираем студентов
            bad_mark_count = 0
            for subject in self.data[key]:  # Перебираем предметы студента
                if subject[1] < 61:  # Проверяем, есть ли академическая задолженность
                    bad_mark_count += 1
            
            # Если задолженности ровно по двум предметам
            if bad_mark_count == 2:
                count_with_debts += 1
                print(f"{key} имеет задолженности по двум предметам")  # Для отладки

        print(f"Количество студентов с академической задолженностью по двум предметам: {count_with_debts}")
        return count_with_debts

