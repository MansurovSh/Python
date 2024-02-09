def tel_l(tel_list,file_name):
    f = open(file_name,"r",encoding='UTF-8')
    for i in f:
        tel_sl(tel_list,list(i.split()))
    f.close()


def tel_sl(tel_list,str_):
    sl_ = {"Фамилия":str_[0],"Имя":str_[1],"Отчество":str_[2],"Телефон":str_[3]}
    tel_list.append(sl_)

def Add_asus(tel_list,file_name):
    f = open(file_name,"a",encoding='UTF-8')
    str_ = input("Напишите пользователч: ")
    f.write(f"{str_}\n")
    tel_sl(tel_list,str_)
    f.close()

def del_list_asus(tel_list,str_):
    for i in range(len(tel_list)):
        for values in tel_list[i].values():
            if values == str_:
                tel_list.pop(i)
                return i + 1
    return 0

def del_asus(tel_list,file_name,str_):
    lines = open(file_name,'r',encoding='UTF-8').readlines()
    print(lines)
    row = del_list_asus(tel_list,str_)
    if row > 0:
        open(file_name,'w',encoding='UTF-8').writelines(lines[:row - 1])
        open(file_name,'a',encoding='UTF-8').writelines(lines[row:])


def copy(file_name,row):
    lines = open("tel_sprav.txt",'r',encoding='UTF-8').readlines()
    f = open(file_name,'a',encoding='UTF-8')
    f.writelines(lines[row - 1:row])


def get(tel_list,famil,key = "Фамилия"):
    # f = open("file.txt","r")
    # for i in f:
    #     for nam,j in enumerate(i.split()):
    #         if nam == 0 and j == famil:
    #             print(i)

    # f.close()  
   for i in tel_list:
        for val in i.values():
            #if val == famil:
            if i[key] == famil:
                print(*i.values())
                return None


def main():
    file_name = "tel_sprav.txt"
    tel_list = []


    tel_l(tel_list,file_name)
    while True:
        print("Что хотите сделать: ")
        print("0.Выйти")
        print("1.Добавить пользователя")
        print("2.Искать пользователя по фамилии")
        print("3.Икать пользователя по имении")
        print("4.Искать пользователя по Отчеству")
        print("5.Искать пользователя по номеру телефона")
        print("6.Удалить пользователя по фамилии")
        print("7.Копировать в другой файл строку")


        n = int(input())
        if n == 0:
            break
        if n == 1:
            Add_asus(tel_list,file_name)
        if n == 2:
            famil = input("Введите фамилию пользователя: ").capitalize()
            get(tel_list,famil)
        if n == 3:
            name = input("Введите имя пользователя: ").capitalize()
            get(tel_list,name,"Имя")
        if n == 4:
            otva = input("Введите Отчества пользователя: ").capitalize()
            get(tel_list,otva,"Отчества")
        if n == 5:
            number = input("Введите номер тел пользователя: ")
            get(tel_list,number,"Телефон")
        if n == 6:
            famil = input("Введите фамилию пользователя: ")
            del_asus(tel_list,file_name,famil)
        if n == 7:
            row = int(input("Введите номер строки: "))
            copy("new_file.txt",row)

if __name__ == "__main__":
    main()