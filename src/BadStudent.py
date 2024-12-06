# -*- coding: utf-8 -*-
from Types import DataType


class BadStudent:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        count_with_debts = 0

        for key in self.data:
            bad_mark_count = 0
            for subject in self.data[key]:
                if subject[1] < 61:
                    bad_mark_count += 1

            if bad_mark_count == 2:
                count_with_debts += 1

        return count_with_debts
