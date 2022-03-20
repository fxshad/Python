class Check(Exception):
    def __init__(self, numb, check_list: list):
        self.n = numb
        self.check_list = check_list
        if not n.isdigit():
            print("not number")
        else:
            self.n = int(n)
            self.check_list.append(self.n)


if __name__ == '__main__':
    # int_list = [2, "4", None]
    int_list = []
    while True:
        try:
            n = input("введите число: ")
            if n == 'stop':
                print(int_list)
                break
            else:
                raise Check(n, int_list)
        except Check as e:
            pass




