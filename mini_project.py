
class Company_member:
    full_task_list=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    Dept_A_tasks=[1,2,3,4,5]
    Dept_B_tasks=[6,7,8,9]
    Dept_A_cancel_tasks=[]
    Dept_B_cancel_tasks=[]
    resolvedtasks=[]
    AW1=[]
    AW2=[]
    AW3=[]
    BW1=[]
    BW2=[]
    BW3=[]
    BW4=[]
    ADM=[]
    BDM=[]
    GM_ID=("GM")
    DM_ID=("ADM", "BDM")
    Dept_A_ID=( "AW1", "AW2", "AW3")
    Dept_B_ID=("BW1", "BW2", "BW3", "BW4")

    full_task_list_temp=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    Dept_A_tasks_temp=[1,2,3,4,5]
    Dept_B_tasks_temp=[6,7,8,9]
    Cancel_tasks_temp=[]
    Dept_A_cancel_taskstemp=[]
    Dept_B_cancel_taskstemp=[]
    AW1temp=[]
    AW2temp=[]
    AW3temp=[]
    BW1temp=[]
    BW2temp=[]
    BW3temp=[]
    BW4temp=[]
    
    def __init__(self, ID):
        self.ID = ID
    
    
    def ID_verifying_func(self,ID):
        self.ID = ID
        #id_input=input("enter you ID:")
        #id=("GM", "ADM", "BDM", "AW1", "AW2", "AW3", "BW1", "BW2", "BW3", "BW4")
        if self.ID in self.GM_ID or self.ID  in self.DM_ID or self.ID  in self.Dept_A_ID or  self.ID in self.Dept_B_ID :
             #print(f"your ID is {id_input}")
             return id_input
        else:
            print("Invalid ID, Please enter a valid ID")
            return False
    def ID_func(self):
        if self.ID =="AW1":
            return self.AW1
        elif self.ID== "AW2":
            return self.AW2
        elif self.ID=="AW3":
            return self.AW3
        elif self.ID=="BW1":
            return self.BW1
        elif self.ID=="BW2":
            return self.BW2
        elif self.ID=="BW3":
            return self.BW3
        elif self.ID=="BW4":
            return self.BW4
        elif self.ID=="ADM":
            return self.ADM
        elif self.ID=="BDM":
            return self.BDM
        
    def ID_dept_func(self):
        if self.ID=="AW1" or self.ID=="AW2" or self.ID=="AW3"or self.ID=="ADM":
            return "A"
        elif self.ID=="BW1" or self.ID=="BW2"or self.ID=="BW3" or self.ID=="BW4"or self.ID=="BDM":
            return "B"   
             
        
class worker(Company_member):
    
    @classmethod
    def Worker_func(self,ID, ID_funcs, dept_variable, method_number):
        self.ID=ID
        self.ID_funcs=ID_funcs
        self.dept_variable=dept_variable
        self.method_number=method_number
        if self.dept_variable=="A":
            self.tasks=self.Dept_A_tasks
        elif self.dept_variable=="B":
            self.tasks=self.Dept_B_tasks

        #print(f"  \nwelcome {self.ID}")
        print_data_variable="""
 1.check your task list
 2.pick a task
 3.complete a task
        """
        """
        print(print_data_variable)
       
        a=int(input("enter 1/2/3:"))
        """
        if self.method_number==1:
            self.View_assigned_task_func()            
        elif self.method_number==2:
            self.assign_task_func()            
        elif self.method_number==3:
            self.task_resolving_func() 
             
    @classmethod
    def View_assigned_task_func(self):
        if len(self.ID_funcs)==0:
            print("you don't have any tasks assigned, come back later!")
        else:
            print(self.ID_funcs)
        
    @classmethod
    def assign_task_func(self):
        
        s=len(self.ID_funcs)
        #print(s)
        if s<0:
            print("no tasks left to pick, come back later!")
        else:
            print('which task you would like to pick')
            print(self.tasks)
            t=int(input("enter the task number:"))
            
            while t not in self.tasks:
                print("invalid task number,enter a valid task number from the above list")
                t=int(input("enter the task number:"))
                
            if s<3:
                if t in self.tasks:
                    self.ID_funcs.append(t)
                    self.ID_funcs.sort()
                    self.tasks.remove(t)
            else:
                print(F"{self.ID} reached maximum task limit")

            print(self.tasks)
            print(F"{self.ID} new task list")
            print(self.ID_funcs)
    @classmethod
    def task_resolving_func(self):
        if len(self.ID_funcs)==0:
            print("you don't have any tasks assigned, come back later!")
        else:
            print(self.ID_funcs)
            task_number_variable=int(input("which task you would like to complete:"))
            
            while task_number_variable not in self.ID_funcs:
                print("invalid task number,enter a valid task number from the above list")
                task_number_variable=int(input("enter the task number:"))
            self.ID_funcs.remove(task_number_variable)
            self.resolvedtasks.append(task_number_variable)
            print(f"{self.ID} new task list")
            print(self.ID_funcs)
            print("resolved tasks:")
            print(self.resolvedtasks) 
  
class manager(Company_member):

    def Manager_func(self,ID, dept):
        self.ID=ID
        self.dept=dept
        if (self.full_task_list_temp!=self.full_task_list and len(self.full_task_list)<len(self.full_task_list_temp)) or(self.Dept_A_tasks_temp!=self.Dept_A_tasks and len(self.Dept_A_tasks)<len(self.Dept_A_tasks_temp))or(self.Dept_B_tasks_temp!=self.Dept_B_tasks and len(self.Dept_B_tasks)<len(self.Dept_B_tasks_temp)):
         print("you have a task assignment notification!")
        print_data_variable="""
1.assign task to a worker
2.cancel task of the department
3.view notificaitons
"""     
        print(print_data_variable)
        method_number_variable=int(input("enter 1/2/3:"))
        if method_number_variable==1:
            self.manager_task_assign_func()
        elif method_number_variable==2:
            self.manager_cancel_tasks_func()
        elif method_number_variable==3:
            self.view_notifications()
    
    def manager_task_assign_func(self):
        worker_ID=input("Enter the ID of the worker you want to assign the task:")
        if self.ID=="BDM" and (self.ID in self.Dept_A_ID or self.ID in self.GM_ID or self.ID in self.DM_ID):
            print("you can't assign task for this ID")
        elif worker_ID in self.Dept_A_ID and self.ID=="ADM":
            Company_member.ID_verifying_func(self, worker_ID)
            ID_return_variable=Company_member.ID_func(self)
            dept_return_variable=Company_member.ID_dept_func(self)
            worker.Worker_func(worker_ID,ID_return_variable,dept_return_variable,2)
        elif self.ID=="ADM" and (self.ID in self.Dept_B_ID or self.ID in self.GM_ID or self.ID in self.DM_ID):
            print("you can't assign task for this ID")
        elif worker_ID in self.Dept_B_ID and self.ID=="BDM":
            Company_member.ID_verifying_func(self, worker_ID)
            ID_return_variable=Company_member.ID_func(self)
            dept_return_variable=Company_member.ID_dept_func(self)
            worker.Worker_func(worker_ID,ID_return_variable,dept_return_variable,2) 
        if self.ID=="GM" and (worker_ID not in self.Dept_A_ID and worker_ID not in self.Dept_B_ID):
            print("enter valid ID")

        elif self.ID=="GM" and worker_ID in self.Dept_A_ID or worker_ID in self.Dept_B_ID:
            Company_member.ID_verifying_func(self, worker_ID)
            ID_return_variable=Company_member.ID_func(self)
            dept_return_variable=Company_member.ID_dept_func(self)
            worker.Worker_func(worker_ID,ID_return_variable,dept_return_variable,2)
    
    def manager_cancel_tasks_func(self):
        
        if self.dept=="A":
            self.tasks=self.Dept_A_tasks
            self.taskcancel=self.Dept_A_cancel_tasks
        elif self.dept=="B":
            self.tasks=self.Dept_B_tasks
            self.taskcancel=self.Dept_B_cancel_tasks
        print(self.tasks)
        task_number_variable=int(input("how many tasks you want to cancel"))
        method_number_variable=0
        while task_number_variable>len(self.tasks):
            print("please enter the number of tasks with in the number of available list")
            task_number_variable=int(input("how many tasks you want to cancel:"))
        while method_number_variable<task_number_variable:
            m=int(input("Enter the task you want to cancel:"))
            while m not in self.tasks:
                print("please enter valid task number from the above list")
                m=input("Enter the task you want to cancel:")
                
            method_number_variable=method_number_variable+1
            self.taskcancel.append(m)
            print(self.taskcancel)
        print("taksacancel")
        print(self.Dept_A_cancel_tasks)    
        print("taksbcancel")
        print(self.Dept_B_cancel_tasks) 

    def view_notifications(self):
        general_manager.view_assignment_notifications(self)  
                  
class general_manager(Company_member):
       
    def GM_func(self,ID):
        self.ID=ID
        if (self.full_task_list_temp!=self.full_task_list and len(self.full_task_list)<len(self.full_task_list_temp)) or(self.Dept_A_tasks_temp!=self.Dept_A_tasks and len(self.Dept_A_tasks)<len(self.Dept_A_tasks_temp))or(self.Dept_B_tasks_temp!=self.Dept_B_tasks and len(self.Dept_B_tasks)<len(self.Dept_B_tasks_temp)):
            print("you have a task assignment notification!")
        if self.Dept_A_cancel_taskstemp!=self.Dept_A_cancel_tasks or self.Dept_B_cancel_taskstemp!=self.Dept_B_cancel_tasks:
            print("you have a task cancel notification!")

        print_data_variable="""
1.View cacellations request
2.view task assignment notification
3.View status report
4.Assign departmet tasks
5.Assign tasks to workers
"""
        print(print_data_variable)
        method_number_variable=int(input("enter 1/2/3/4/5:"))  
        if method_number_variable==1:
            self.view_cancellations_request()
        elif method_number_variable==2:
            self.view_assignment_notifications()
        elif method_number_variable==3:
            self.view_status_report()
        elif method_number_variable==4:
            self.assign_dept_tasks()
        elif method_number_variable==5:
            self.assign_worker_tasks()

    def view_cancellations_request(self):
            if self.Dept_A_cancel_taskstemp!=self.Dept_A_cancel_tasks:
                print("Department A manger want to cancel the following tasks:",self.Dept_A_cancel_tasks )
            if self.Dept_B_cancel_taskstemp!=self.Dept_B_cancel_tasks:
                print("Department B manger want to cancel the following tasks:",self.Dept_B_cancel_tasks )
            if self.Dept_A_cancel_taskstemp!=self.Dept_A_cancel_tasks or self.Dept_B_cancel_taskstemp!=self.Dept_B_cancel_tasks:
                TT=int(input("how many tasks you want to cancel:"))
                ttt=0
                while ttt<TT:
                    T=int(input("which task cancellation you want to approve:"))
                    while T not in self.Dept_A_cancel_tasks and T not in self.Dept_B_cancel_tasks:
                        print("please enter a valid task number from above list:")
                        T=int(input("which task cancellation you want to approve:"))
                    self.Cancel_tasks_temp.append(T)
                    """
                    if T in self.Dept_A_cancel_tasks:
                        self.Dept_A_cancel_taskstemp.append(T)
                    if T in self.Dept_B_cancel_tasks:
                        self.Dept_B_cancel_taskstemp.append(T)
                    """
                    ttt=ttt+1
                print(self.Cancel_tasks_temp)
                #.Dept_A_cancel_taskstemp=self.Dept_A_cancel_tasks.copy()
                #self.Dept_B_cancel_taskstemp=self.Dept_B_cancel_tasks.copy()
            else:
                print("no cancellations request for now, come back later!") 

            
            for i in range(0, len(self.Cancel_tasks_temp)):

                 if self.Cancel_tasks_temp[i] in self.Dept_A_tasks:
                    self.Dept_A_tasks.remove(self.Cancel_tasks_temp[i])
                    self.Dept_A_tasks_temp.remove(self.Cancel_tasks_temp[i])
                    self.Dept_A_cancel_tasks.remove(self.Cancel_tasks_temp[i])
                    self.full_task_list.append(self.Cancel_tasks_temp[i])
                    self.full_task_list_temp.append(self.Cancel_tasks_temp[i])
            
            for i in range(0, len(self.Cancel_tasks_temp)):

                 if self.Cancel_tasks_temp[i] in self.Dept_B_tasks:
                    self.Dept_B_tasks.remove(self.Cancel_tasks_temp[i])
                    self.Dept_B_tasks_temp.remove(self.Cancel_tasks_temp[i])
                    self.Dept_B_cancel_tasks.remove(self.Cancel_tasks_temp[i])
                    self.full_task_list.append(self.Cancel_tasks_temp[i])
                    self.full_task_list_temp.append(self.Cancel_tasks_temp[i])
            #print("taska:")
            #print(self.Dept_A_tasks)
            #print("taskb:")
            #print(self.Dept_B_tasks)  
                                  
   
    def view_assignment_notifications(self):       
        if (self.full_task_list_temp!=self.full_task_list and len(self.full_task_list)<len(self.full_task_list_temp)) or(self.Dept_A_tasks_temp!=self.Dept_A_tasks and len(self.Dept_A_tasks)<len(self.Dept_A_tasks_temp))or(self.Dept_B_tasks_temp!=self.Dept_B_tasks and len(self.Dept_B_tasks)<len(self.Dept_B_tasks_temp) ):
    
            if self.AW1temp!=self.AW1:
                print(f"AW1 has been assigned {self.AW1}")
                self.AW1temp=self.AW1.copy()
            if self.AW2temp!=self.AW2:
                print(f"AW2 has been assigned {self.AW2}")
                self.AW2temp=self.AW2.copy()
            if self.AW3temp!=self.AW3:
                print(f"AW3 has been assigned {self.AW3}")
                self.AW3temp=self.AW3.copy()
            if self.BW1temp!=self.BW1:
                print(f"BW1 has been assigned {self.BW1}")
                self.BW1temp=self.BW1.copy()
            if self.BW2temp!=self.BW2:
                print(f"BW2 has been assigned {self.BW2}")
                self.BW2temp=self.BW2.copy()
            if self.BW3temp!=self.BW3:
                print(f"BW3 has been assigned {self.BW3}")
                self.BW3temp=self.BW3.copy()
            if self.BW4temp!=self.BW4:
                print(f"BW4 has been assigned {self.BW4}")
                self.BW4temp=self.BW4.copy()
            if self.Dept_A_tasks_temp!=self.Dept_A_tasks and(self.full_task_list_temp!=self.full_task_list and len(self.full_task_list)<len(self.full_task_list_temp)):
                print(f"department A has been assigned {self.Dept_A_tasks}")
                self.Dept_A_tasks_temp=self.Dept_A_tasks.copy()
            if self.Dept_B_tasks_temp!=self.Dept_B_tasks and (self.full_task_list_temp!=self.full_task_list and len(self.full_task_list)<len(self.full_task_list_temp)) :
                print(f"department B has been assigned {self.Dept_B_tasks}")
                self.Dept_B_tasks_temp=self.Dept_B_tasks.copy()
            if self.Dept_A_tasks_temp!=self.Dept_A_tasks :
                #print(f"department A has been assigned {self.Dept_A_tasks}")
                self.Dept_A_tasks_temp=self.Dept_A_tasks.copy()
            if self.Dept_B_tasks_temp!=self.Dept_B_tasks :
                #print(f"department B has been assigned {self.Dept_B_tasks}")
                self.Dept_B_tasks_temp=self.Dept_B_tasks.copy()

            self.full_task_list_temp=self.full_task_list.copy()    
            #self.Dept_A_tasks_temp=self.Dept_A_tasks.copy()
            #self.Dept_B_tasks_temp=self.Dept_B_tasks.copy()
        else:
            print("no new tasks has been assigned")
    
    
    def assign_dept_tasks(self):
        dept=input("enter the department(A or B) you want to assign the tasks:")
        while dept!="A" and dept!="B":
            print("invalid department, please enter A or B")
            dept=input("enter the department you want to assign the tasks:")
        print("list of tasks available:")
        print(Company_member.full_task_list)
        id_input=0
        g=int(input("how many tasks you want to assign:"))
        while g>len(Company_member.full_task_list):
            print("invalid number please enter the number with in the task list length")
            g=int(input("how many tasks you want to assign:"))
        while id_input < g:
            t=int(input("enter task number to assign:"))
            while t not in Company_member.full_task_list:
                 print("invalid task numbere, please enter a valid task number")
                 t=int(input("enter task number to assign:"))
            if dept=="A":
                Company_member.Dept_A_tasks.append(t)
                #self.Dept_A_tasks_temp=self.Dept_A_tasks.copy()
                Company_member.full_task_list.remove(t)
            elif dept=="B":
                Company_member.Dept_B_tasks.append(t)
                #self.Dept_B_tasks_temp=self.Dept_B_tasks.copy()
                Company_member.full_task_list.remove(t)
            id_input=id_input+1
        print("dept A tasks")
        print(Company_member.Dept_A_tasks)
        print("dept B tasks")
        print(Company_member.Dept_B_tasks)
    
    def assign_worker_tasks(self):
        manager.manager_task_assign_func(self)

    def view_status_report(self):
        print(f"ID:AW1, POSITION:Department A worker, NAME:SRIKANTH, Assigned tasks:{Company_member.AW1}")
        print(f"ID:AW2, POSITION:Department A worker, NAME:HET SHAH, Assigned tasks:{Company_member.AW2}")
        print(f"ID:AW3, POSITION:Department A worker, NAME:SAI TEJA, Assigned tasks:{Company_member.AW3}")
        print(f"ID:BW1, POSITION:Department A worker, NAME:BHARGAV, Assigned tasks:{Company_member.BW1}")
        print(f"ID:BW2, POSITION:Department B worker, NAME: SAHIB ,Assigned tasks:{Company_member.BW2}")
        print(f"ID:BW3, POSITION:Department B worker, NAME:ABHINAV, Assigned tasks:{Company_member.BW3}")
        print(f"ID:BW4, POSITION:Department B worker, NAME:UMESH, Assigned tasks:{Company_member.BW4}")
        print(f"ID:ADM, POSITION:Department A MANGER, NAME:TARIQ, Assigned tasks:{Company_member.Dept_A_tasks}")
        print(f"ID:BDM, POSITION:Department B MANAGER, NAME:SALAH, Assigned tasks:{Company_member.Dept_B_tasks}")
        print(f"resolved tasks:{Company_member.resolvedtasks}")
        print(f"unassigned tasks:{Company_member.full_task_list}")

       
  

a="""Enter your ID, ID should be any of the following:
GM= general manager\nADM=department A a manager
BDM=department B a manager
AW1=department A worker 1
AW2=department A worker 2
AW3=department A worker 3
BW1=department B worker 1
BW2=department B worker 2
BW3=department B worker 3
BW4 department B worker 4"""

#id_input=input("enter you ID:")
id_input=None
member_object=Company_member(id_input)
worker_object=worker(id_input)
Manager_object=manager(id_input)
General_manager_object=general_manager(id_input)

#ID_verify_variable= member_object.ID_verifying_func()
while True:
    print(a)
    id_input=input("enter your ID:")
 
    ID_verify_variable= member_object.ID_verifying_func(id_input)
    while ID_verify_variable==False:
        id_input=input("enter you ID:")
        ID_verify_variable= member_object.ID_verifying_func(id_input)
        
    if ID_verify_variable!=False and id_input=="AW1" or id_input== "AW2"or id_input== "AW3"or id_input== "AW3"or id_input== "BW1"or id_input== "BW2"or id_input== "BW3"or id_input== "BW4":
        ID_return_variable=member_object.ID_func()
        dept_return_variable=member_object.ID_dept_func() 
        while True: 
            print_data_variable="""
 1.check your task list
 2.pick a task
 3.complete a task
        """
            print(print_data_variable)
            tser=int(input("Enter 1/2/3:"))
            empty_variable=worker_object.Worker_func(ID_verify_variable, ID_return_variable, dept_return_variable, tser)
            print("Z to go back to pevious step       press X to return to start ")
            go_back_variable=input()
            while go_back_variable!="Z" and go_back_variable!="X":
                print("invalid input")
                go_back_variable=input()
            if go_back_variable=="Z":
                True
            if go_back_variable=="X":
                break
    if ID_verify_variable!=False and id_input=="ADM" or id_input=="BDM":
        ID_return_variable=member_object.ID_func()
        dept_return_variable=member_object.ID_dept_func() 
        while True:  
            empty_variable=Manager_object.Manager_func(id_input,dept_return_variable)
            print("Z to go back to pevious step       press X to return to start ")
            go_back_variable=input()
            while go_back_variable!="Z" and go_back_variable!="X":
                print("invalid input")
                go_back_variable=input()
            if go_back_variable=="Z":
                True
            if go_back_variable=="X":
                break
    if ID_verify_variable!=False and id_input=="GM":
        ID_return_variable=member_object.ID_func()
        dept_return_variable=member_object.ID_dept_func() 
        while True:  
            empty_variable=General_manager_object.GM_func(id_input)
            print("Z to go back to pevious step       press X to return to start ")
            go_back_variable=input()
            while go_back_variable!="Z" and go_back_variable!="X":
                print("invalid input")
                go_back_variable=input()
            if go_back_variable=="Z":
                True
            if go_back_variable=="X":
                break
            

    