# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.BadStudent import BadStudent


class TestBadStudent:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Львовов Игорь Владимирович": [
                ("Math", 10),
                ("Sociology", 10),
                ("Chemistry", 100),
                ("Physics", 97)
            ],
            "Петров Игорь Владимирович": [
                ("Math", 100),
                ("Sociology", 100),
                ("Chemistry", 1),
                ("Physics", 97)
            ],
            "Абрамов Петр Сергеевич": [
                ("Math", 50),
                ("Programming", 91),
                ("Literature", 40),
                ("Biology", 76),
                ("Technology", 80)
            ],
            "Сидоров Петр Сергеевич": [
                ("Math", 50),
                ("Programming", 91),
                ("Literature", 40),
                ("Biology", 10),
                ("Technology", 5)
              ]

        }
        expected_students_with_debts_count = 2
        return data, expected_students_with_debts_count

    def test_init_bad_students(self, input_data: tuple[DataType, int]) -> None:
        bad_students = BadStudent(input_data[0])
        assert input_data[0] == bad_students.data

    def test_calc_students_with_debts(
        self, input_data: tuple[DataType, int]
    ) -> None:
        bad_students = BadStudent(input_data[0])
        students_with_debts_count = bad_students.calc()
        assert students_with_debts_count == input_data[1]