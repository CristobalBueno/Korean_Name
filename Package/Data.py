def last_name(age: int):
    last_name = {
        0: 'Park', 1: 'Kim', 2: 'Shin', 3: 'Choi', 4: 'Song', 5: 'Kang',
        6: 'Han', 7: 'Lee', 8: 'Sung', 9: 'Jung'
    }
    return last_name[age]


def middle_name(month: int):
    middle_name = {1: 'Yong', 2: 'Ji', 3: 'Je', 4: 'Hye', 5: 'Dong',
                   6: 'Sang', 7: 'Ha', 8: 'Hyo', 9: 'Soo', 10: 'Eun',
                   11: 'Hyun', 12: 'Rae'}
    return middle_name[month]


def first_name(day: int):
    first_name = {1: 'Hwa', 2: 'Woo', 3: 'Joon', 4: 'Hee', 5: 'Kyo', 6: 'Kyung', 7: 'Wook',
                  8: 'Jin', 9: 'Jae', 10: 'Hoon', 11: 'Ra', 12: 'Bin', 13: 'Sun', 14: 'Ri', 15: 'Soo',
                  16: 'Rim', 17: 'Ah', 18: 'Ae', 19: 'Neul', 20: 'Mun', 21: 'In', 22: 'Mi', 23: 'Ki',
                  24: 'Sang', 25: 'Byung', 26: 'Seok', 27: 'Gun', 28: 'Yoo', 29: 'Sup', 30: 'Won', 31: 'Sup'}
    return first_name[day]
