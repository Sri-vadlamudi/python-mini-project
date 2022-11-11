
#from ast import If

class start:
    tasksfull=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    tasksa=[1,2,3,4,5]
    tasksb=[6,7,8,9]
    taskacancel=[]
    taskbcancel=[]
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
    idgm=("GM")
    idm=("ADM", "BDM")
    idaw=( "AW1", "AW2", "AW3")
    idbw=("BW1", "BW2", "BW3", "BW4")

    taskfulltemp=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    taskatemp=[1,2,3,4,5]
    taskbtemp=[6,7,8,9]
    taskcanceltemp=[]
    taskacanceltemp=[]
    taskbcanceltemp=[]
    AW1temp=[]
    AW2temp=[]
    AW3temp=[]
    BW1temp=[]
    BW2temp=[]
    BW3temp=[]
    BW4temp=[]
    
    def __init__(self, ID):
        self.ID = ID
    
    
    def startfunc(self,ID):
        self.ID = ID
        #i=input("enter you ID:")
        #id=("GM", "ADM", "BDM", "AW1", "AW2", "AW3", "BW1", "BW2", "BW3", "BW4")
        if self.ID in self.idgm or self.ID  in self.idm or self.ID  in self.idaw or  self.ID in self.idbw :
             #print(f"your ID is {i}")
             return i
        else:
            print("Invalid ID, Please enter a valid ID")
            return False
    def tlist(self):
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
        
    def tdept(self):
        if self.ID=="AW1" or self.ID=="AW2" or self.ID=="AW3"or self.ID=="ADM":
            return "A"
        elif self.ID=="BW1" or self.ID=="BW2"or self.ID=="BW3" or self.ID=="BW4"or self.ID=="BDM":
            return "B"   
             
        
class worker(start):
    
    @classmethod
    def taskmethod(self,ID, tlists, taskdept, tseries):
        self.ID=ID
        self.tlists=tlists
        self.taskdept=taskdept
        self.tseries=tseries
        if self.taskdept=="A":
            self.tasks=self.tasksa
        elif self.taskdept=="B":
            self.tasks=self.tasksb

        #print(f"  \nwelcome {self.ID}")
        aa="""
 1.check your task list
 2.pick a task
 3.complete a task
        """
        """
        print(aa)
       
        a=int(input("enter 1/2/3:"))
        """
        if self.tseries==1:
            self.taskcheck()            
        elif self.tseries==2:
            self.taskpick()            
        elif self.tseries==3:
            self.taskresolve() 
             
    @classmethod
    def taskcheck(self):
        if len(self.tlists)==0:
            print("you don't have any tasks assigned, come back later!")
        else:
            print(self.tlists)
        
    @classmethod
    def taskpick(self):
        
        s=len(self.tlists)
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
                    self.tlists.append(t)
                    self.tlists.sort()
                    self.tasks.remove(t)
            else:
                print(F"{self.ID} reached maximum task limit")

            print(self.tasks)
            print(F"{self.ID} new task list")
            print(self.tlists)
    @classmethod
    def taskresolve(self):
        if len(self.tlists)==0:
            print("you don't have any tasks assigned, come back later!")
        else:
            print(self.tlists)
            tt=int(input("which task you would like to complete:"))
            
            while tt not in self.tlists:
                print("invalid task number,enter a valid task number from the above list")
                tt=int(input("enter the task number:"))
            self.tlists.remove(tt)
            self.resolvedtasks.append(tt)
            print(f"{self.ID} new task list")
            print(self.tlists)
            print("resolved tasks:")
            print(self.resolvedtasks) 
  
class manager(start):

    def managerroll(self,ID, dept):
        self.ID=ID
        self.dept=dept
        if (self.taskfulltemp!=self.tasksfull and len(self.tasksfull)<len(self.taskfulltemp)) or(self.taskatemp!=self.tasksa and len(self.tasksa)<len(self.taskatemp))or(self.taskbtemp!=self.tasksb and len(self.tasksb)<len(self.taskbtemp)):
         print("you have a task assignment notification!")
        m="""
1.assign task to a worker
2.cancel task of the department
3.view notificaitons
"""     
        print(m)
        mm=int(input("enter 1/2/3:"))
        if mm==1:
            self.managerassign()
        elif mm==2:
            self.managercancel()
        elif mm==3:
            self.viewnotifications()
    
    def managerassign(self):
        mID=input("Enter the ID of the worker you want to assign the task:")
        if self.ID=="BDM" and (self.ID in self.idaw or self.ID in self.idgm or self.ID in self.idm):
            print("you can't assign task for this ID")
        elif mID in self.idaw and self.ID=="ADM":
            start.startfunc(self, mID)
            tt=start.tlist(self)
            tdep=start.tdept(self)
            worker.taskmethod(mID,tt,tdep,2)
        elif self.ID=="ADM" and (self.ID in self.idbw or self.ID in self.idgm or self.ID in self.idm):
            print("you can't assign task for this ID")
        elif mID in self.idbw and self.ID=="BDM":
            start.startfunc(self, mID)
            tt=start.tlist(self)
            tdep=start.tdept(self)
            worker.taskmethod(mID,tt,tdep,2) 
        if self.ID=="GM" and (mID not in self.idaw and mID not in self.idbw):
            print("enter valid ID")

        elif self.ID=="GM" and mID in self.idaw or mID in self.idbw:
            start.startfunc(self, mID)
            tt=start.tlist(self)
            tdep=start.tdept(self)
            worker.taskmethod(mID,tt,tdep,2)
    
    def managercancel(self):
        
        if self.dept=="A":
            self.tasks=self.tasksa
            self.taskcancel=self.taskacancel
        elif self.dept=="B":
            self.tasks=self.tasksb
            self.taskcancel=self.taskbcancel
        print(self.tasks)
        mg=int(input("how many tasks you want to cancel"))
        mm=0
        while mg>len(self.tasks):
            print("please enter the number of tasks with in the number of available list")
            mg=int(input("how many tasks you want to cancel:"))
        while mm<mg:
            m=int(input("Enter the task you want to cancel:"))
            while m not in self.tasks:
                print("please enter valid task number from the above list")
                m=input("Enter the task you want to cancel:")
                
            mm=mm+1
            self.taskcancel.append(m)
            print(self.taskcancel)
        print("taksacancel")
        print(self.taskacancel)    
        print("taksbcancel")
        print(self.taskbcancel) 

    def viewnotifications(self):
        generalmanager.viewassignmentnotifications(self)  
                  
class generalmanager(start):
       
    def GMroll(self,ID):
        self.ID=ID
        if (self.taskfulltemp!=self.tasksfull and len(self.tasksfull)<len(self.taskfulltemp)) or(self.taskatemp!=self.tasksa and len(self.tasksa)<len(self.taskatemp))or(self.taskbtemp!=self.tasksb and len(self.tasksb)<len(self.taskbtemp)):
            print("you have a task assignment notification!")
        if self.taskacanceltemp!=self.taskacancel or self.taskbcanceltemp!=self.taskbcancel:
            print("you have a task cancel notification!")

        aa="""
1.View cacellations request
2.view task assignment notification
3.View status report
4.Assign departmet tasks
5.Assign tasks to workers
"""
        print(aa)
        mm=int(input("enter 1/2/3/4/5:"))  
        if mm==1:
            self.viewcancellationsrequest()
        elif mm==2:
            self.viewassignmentnotifications()
        elif mm==3:
            self.viewstatusreport()
        elif mm==4:
            self.assigndepttasks()
        elif mm==5:
            self.assignworkertasks()

    def viewcancellationsrequest(self):
            if self.taskacanceltemp!=self.taskacancel:
                print("Department A manger want to cancel the following tasks:",self.taskacancel )
            if self.taskbcanceltemp!=self.taskbcancel:
                print("Department B manger want to cancel the following tasks:",self.taskbcancel )
            if self.taskacanceltemp!=self.taskacancel or self.taskbcanceltemp!=self.taskbcancel:
                TT=int(input("how many tasks you want to cancel:"))
                ttt=0
                while ttt<TT:
                    T=int(input("which task cancellation you want to approve:"))
                    while T not in self.taskacancel and T not in self.taskbcancel:
                        print("please enter a valid task number from above list:")
                        T=int(input("which task cancellation you want to approve:"))
                    self.taskcanceltemp.append(T)
                    """
                    if T in self.taskacancel:
                        self.taskacanceltemp.append(T)
                    if T in self.taskbcancel:
                        self.taskbcanceltemp.append(T)
                    """
                    ttt=ttt+1
                print(self.taskcanceltemp)
                #.taskacanceltemp=self.taskacancel.copy()
                #self.taskbcanceltemp=self.taskbcancel.copy()
            else:
                print("no cancellations request for now, come back later!") 

            
            for i in range(0, len(self.taskcanceltemp)):

                 if self.taskcanceltemp[i] in self.tasksa:
                    self.tasksa.remove(self.taskcanceltemp[i])
                    self.taskatemp.remove(self.taskcanceltemp[i])
                    self.taskacancel.remove(self.taskcanceltemp[i])
                    self.tasksfull.append(self.taskcanceltemp[i])
                    self.taskfulltemp.append(self.taskcanceltemp[i])
            
            for i in range(0, len(self.taskcanceltemp)):

                 if self.taskcanceltemp[i] in self.tasksb:
                    self.tasksb.remove(self.taskcanceltemp[i])
                    self.taskbtemp.remove(self.taskcanceltemp[i])
                    self.taskbcancel.remove(self.taskcanceltemp[i])
                    self.tasksfull.append(self.taskcanceltemp[i])
                    self.taskfulltemp.append(self.taskcanceltemp[i])
            #print("taska:")
            #print(self.tasksa)
            #print("taskb:")
            #print(self.tasksb)  
                                  
   
    def viewassignmentnotifications(self):       
        if (self.taskfulltemp!=self.tasksfull and len(self.tasksfull)<len(self.taskfulltemp)) or(self.taskatemp!=self.tasksa and len(self.tasksa)<len(self.taskatemp))or(self.taskbtemp!=self.tasksb and len(self.tasksb)<len(self.taskbtemp) ):
    
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
            if self.taskatemp!=self.tasksa and(self.taskfulltemp!=self.tasksfull and len(self.tasksfull)<len(self.taskfulltemp)):
                print(f"department A has been assigned {self.tasksa}")
                self.taskatemp=self.tasksa.copy()
            if self.taskbtemp!=self.tasksb and (self.taskfulltemp!=self.tasksfull and len(self.tasksfull)<len(self.taskfulltemp)) :
                print(f"department B has been assigned {self.tasksb}")
                self.taskbtemp=self.tasksb.copy()
            if self.taskatemp!=self.tasksa :
                #print(f"department A has been assigned {self.tasksa}")
                self.taskatemp=self.tasksa.copy()
            if self.taskbtemp!=self.tasksb :
                #print(f"department B has been assigned {self.tasksb}")
                self.taskbtemp=self.tasksb.copy()

            self.taskfulltemp=self.tasksfull.copy()    
            #self.taskatemp=self.tasksa.copy()
            #self.taskbtemp=self.tasksb.copy()
        else:
            print("no new tasks has been assigned")
    
    
    def assigndepttasks(self):
        dept=input("enter the department(A or B) you want to assign the tasks:")
        while dept!="A" and dept!="B":
            print("invalid department, please enter A or B")
            dept=input("enter the department you want to assign the tasks:")
        print("list of tasks available:")
        print(start.tasksfull)
        i=0
        g=int(input("how many tasks you want to assign:"))
        while g>len(start.tasksfull):
            print("invalid number please enter the number with in the task list length")
            g=int(input("how many tasks you want to assign:"))
        while i < g:
            t=int(input("enter task number to assign:"))
            while t not in start.tasksfull:
                 print("invalid task numbere, please enter a valid task number")
                 t=int(input("enter task number to assign:"))
            if dept=="A":
                start.tasksa.append(t)
                #self.taskatemp=self.tasksa.copy()
                start.tasksfull.remove(t)
            elif dept=="B":
                start.tasksb.append(t)
                #self.taskbtemp=self.tasksb.copy()
                start.tasksfull.remove(t)
            i=i+1
        print("dept A tasks")
        print(start.tasksa)
        print("dept B tasks")
        print(start.tasksb)
    
    def assignworkertasks(self):
        manager.managerassign(self)

    def viewstatusreport(self):
        print(f"ID:AW1, POSITION:Department A worker, NAME:SRIKANTH, Assigned tasks:{start.AW1}")
        print(f"ID:AW2, POSITION:Department A worker, NAME:HET SHAH, Assigned tasks:{start.AW2}")
        print(f"ID:AW3, POSITION:Department A worker, NAME:SAI TEJA, Assigned tasks:{start.AW3}")
        print(f"ID:BW1, POSITION:Department A worker, NAME:BHARGAV, Assigned tasks:{start.BW1}")
        print(f"ID:BW2, POSITION:Department B worker, NAME: SAHIB ,Assigned tasks:{start.BW2}")
        print(f"ID:BW3, POSITION:Department B worker, NAME:ABHINAV, Assigned tasks:{start.BW3}")
        print(f"ID:BW4, POSITION:Department B worker, NAME:UMESH, Assigned tasks:{start.BW4}")
        print(f"ID:ADM, POSITION:Department A MANGER, NAME:TARIQ, Assigned tasks:{start.tasksa}")
        print(f"ID:BDM, POSITION:Department B MANAGER, NAME:SALAH, Assigned tasks:{start.tasksb}")
        print(f"resolved tasks:{start.resolvedtasks}")
        print(f"unassigned tasks:{start.tasksfull}")

       
  

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

#i=input("enter you ID:")
i=None
st=start(i)
w=worker(i)
mgr=manager(i)
gm=generalmanager(i)

#z= st.startfunc()
while True:
    print(a)
    i=input("enter your ID:")
 
    z= st.startfunc(i)
    while z==False:
        i=input("enter you ID:")
        z= st.startfunc(i)
        
    if z!=False and i=="AW1" or i== "AW2"or i== "AW3"or i== "AW3"or i== "BW1"or i== "BW2"or i== "BW3"or i== "BW4":
        tt=st.tlist()
        tdep=st.tdept() 
        while True: 
            aa="""
 1.check your task list
 2.pick a task
 3.complete a task
        """
            print(aa)
            tser=int(input("Enter 1/2/3:"))
            zz=w.taskmethod(z, tt, tdep, tser)
            print("press Z to go back to pevious step       press X to return to start ")
            x=input()
            while x!="Z" and x!="X":
                print("invalid input")
                x=input()
            if x=="Z":
                True
            if x=="X":
                break
    if z!=False and i=="ADM" or i=="BDM":
        tt=st.tlist()
        tdep=st.tdept() 
        while True:  
            zzz=mgr.managerroll(i,tdep)
            print("press Z to go back to pevious step       press X to return to start ")
            x=input()
            while x!="Z" and x!="X":
                print("invalid input")
                x=input()
            if x=="Z":
                True
            if x=="X":
                break
    if z!=False and i=="GM":
        tt=st.tlist()
        tdep=st.tdept() 
        while True:  
            zzz=gm.GMroll(i)
            print("press Z to go back to pevious step       press X to return to start ")
            x=input()
            while x!="Z" and x!="X":
                print("invalid input")
                x=input()
            if x=="Z":
                True
            if x=="X":
                break
            

    