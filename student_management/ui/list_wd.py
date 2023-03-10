import tkinter.ttk
from student_management.dao.dao_student import StudentDao

dao = StudentDao() #생성자로 초기화 안하면 메서드 사용못함.

list = tkinter.Tk()
list.title("Student List")
list.geometry('540x300+100+100')
list.resizable(False, False)

lbl = tkinter.Label(list, text="Student List")
lbl.pack()

# treeview 표
trv = tkinter.ttk.Treeview(list,
         columns=["stdNo", "이름", "ID"],
         displaycolumns=["stdNo", "이름", "ID"])
trv.pack()

trv.column("#0", width=100)
trv.heading("#0", text="index")

trv.column("#1", width=100, anchor="center")
trv.heading("stdNo", text="stdNo", anchor="center")

trv.column("#2", width=150, anchor="center")
trv.heading("이름", text="이름", anchor="center")

trv.column("#3", width=150, anchor="center")
trv.heading("ID", text="ID", anchor="center")

trv_list = dao.get_all()
if trv_list != None:
  for i in range(len(trv_list)):   # iid =index id
    trv.insert('', 'end', text=i, values=trv_list[i], iid=str(i)+")")

list.mainloop()



