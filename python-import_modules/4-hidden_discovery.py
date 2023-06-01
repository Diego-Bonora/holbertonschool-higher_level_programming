#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4.pyc
    list = dir(hidden_4.pyc)
    list_no_ = []
    for i in list:
        if i[0] != '_' and i[1] != '_':
            list_no_.append(i)
    list_no_.sort()
    for i in list_no_:
        print(i)
