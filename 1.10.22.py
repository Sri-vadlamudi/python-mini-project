

class start:
    tasksa=[1,2,3,4,5,6,7,8,9]
    tasksb=[10,11,12,13,14,15,16,17,18,19,20,21]
    taskcancel=[]

    resolvedtasks=[]
    AW1=[]
    AW2=[]
    AW3=[]
    BW1=[]
    BW2=[]
    BW3=[]
    BW4=[]
    idgm=("GM")
    idm=("ADM", "BDM")
    idaw=( "AW1", "AW2", "AW3")
    idbw=("BW1", "BW2", "BW3", "BW4")
    
    def __init__(self, ID):
        self.ID = ID
    
    
    def startfunc(self,ID):
        self.ID = ID
        #i=input("enter you ID:")
        #id=("GM", "ADM", "BDM", "AW1", "AW2", "AW3", "BW1", "BW2", "BW3", "BW4")
        if self.ID in self.idgm or i in self.idm or i in self.idaw or i in self.idbw :
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
    def tdept(self):
        if self.ID=="AW1" or self.ID=="AW2" or self.ID=="AW3":
            return "A"
        elif self.ID=="BW1" or self.ID=="BW2"or self.ID=="BW3" or self.ID=="BW4":
            return "B"
    
             
        


class worker(start):
    
    @classmethod
    def taskmethod(self,ID, tmethod, taskdept, tseries):
        self.ID=ID
        self.tmethod=tmethod
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
        if len(self.tmethod)==0:
            print("you don't have any tasks assigned, come back later!")
        else:
            print(self.tmethod)
        
    @classmethod
    def taskpick(self):
        
        s=len(self.tmethod)
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
                    self.tmethod.append(t)
                    self.tmethod.sort()
                    self.tasks.remove(t)
            else:
                print(F"{self.ID} reached maximum task limit")

            print(self.tasks)
            print(F"{self.ID} new task list")
            print(self.tmethod)
    @classmethod
    def taskresolve(self):
        if len(self.tmethod)==0:
            print("you don't have any tasks assigned, come back later!")
        else:
            print(self.tmethod)
            tt=int(input("which task you would like to complete:"))
            
            while tt not in self.tmethod:
                print("invalid task number,enter a valid task number from the above list")
                tt=int(input("enter the task number:"))
            self.tmethod.remove(tt)
            self.resolvedtasks.append(tt)
            print(f"{self.ID} new task list")
            print(self.tmethod)
            print("resolved tasks:")
            print(self.resolvedtasks)   

class manager(start):
   
    def managerroll(self,ID):
        self.ID=ID
        m="""
#1.assign task to a worker
#2.cancel task of a worker
"""     
        print(m)
        mm=int(input("enter 1/2:"))
        if mm==1:
            self.managerassign()
        elif mm==2:
            self.managercancel()
    
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
    
    def managercancel(self):
        mID=input("Enter the ID of the worker you want to assign the task:")
        if self.ID=="BDM" and (self.ID in self.idaw or self.ID in self.idgm or self.ID in self.idm):
                print("you can't cancel task for this ID")
        elif mID in self.idaw and self.ID=="ADM":
            start.startfunc(self, mID)
            tt=start.tlist(self)
            tdep=start.tdept(self)
            #worker.taskmethod(mID,tt,tdep,2)            
                
           

class generalmanager(start):
    taskatemp=[1,2,3,4,5,6,7,8,9]
    taskbtemp=[10,11,12,13,14,15,16,17,18,19,20,21]
    AW1temp=[]
    AW2temp=[]
    AW3temp=[]
    BW1temp=[]
    BW2temp=[]
    BW3temp=[]
    BW4temp=[]
    
    def GMroll(self,ID):
        self.ID=ID

        aa="""
1.View notifications
2.View status report
"""
        print(aa)
        mm=int(input("enter 1/2:"))
    def viewreport():
        pass   
    def viewnotifications(self):
        """
        print(self.tasksa)
        print(self.taskatemp)
        print(self.tasksb)
        print(self.taskbtemp)
        """
         
        if self.taskatemp!=self.tasksa or self.taskbtemp!=self.tasksb:
            print("you have a task assignment notification!")
            print("1.task cancellation notification 2.task assignment notification")
            x=int(input("Enter 1/2:"))
            if x==1:
                pass
            elif x==2:
            # print(self.AW1)
                
                
                if self.taskatemp!=self.tasksa or self.taskbtemp!=self.tasksb:
                
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
                    self.taskatemp=self.tasksa.copy()
                    self.taskbtemp=self.tasksb.copy()
                else:
                    print("no new tasks has been assigned")
        else:
            print("you don't have any new notifications,come back later!")

   

            
         
            
        
    
    

        
        

a="""Enter your ID, ID should be any of the following:
GM= general manager\nADM=department A a manager
BDM=department B a manager
AW1=department A worker 1
AW2=department A worker 2
AW3=department A worker 3
BW1=department B worker 1
BW2=department B worker 2
BW3=department B worker 3
BW4 department B worker 4
"""
print(a)
#i=input("enter you ID:")



print(a)
i=None
st=start(i)
aw1=worker(i)
mgr=manager(i)
gm=generalmanager(i)
"""aw2=worker(i)
aw3=worker(i)
bw1=worker(i)
bw2=worker(i)
bw3=worker(i)
bw4=worker(i)
"""


#z= st.startfunc()
while True:
    
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
            zz=aw1.taskmethod(z, tt, tdep, tser)
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
            zzz=mgr.managerroll(i)
            print("press Z to go back to pevious step       press X to reuturn to start ")
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
            zzz=gm.viewnotifications()
            print("press Z to go back to pevious step       press X to reuturn to start ")
            x=input()
            while x!="Z" and x!="X":
                print("invalid input")
                x=input()
            if x=="Z":
                True
            if x=="X":
                break
            

    """
    if z!=False and i=="AW2":
        tt=st.tlist()
        tdep=st.tdept()    
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="AW3":
        tt=st.tlist()
        tdep=st.tdept()   
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="BW1":
        tt=st.tlist()
        tdep=st.tdept()   
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="BW2":
        tt=st.tlist()
        tdep=st.tdept()   
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="BW3":
        tt=st.tlist()
        tdep=st.tdept()   
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="BW4":
        tt=st.tlist()    
        zz=aw2.taskmethod(z, tt, tdep)
    """
    


  
    