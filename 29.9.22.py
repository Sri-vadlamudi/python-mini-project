


class start:
    """
    def __init__(self, ID, tasklist):
        self.ID=ID
        self.tasklist=tasklist
        """

    tasksa=[1,2,3,4,5,6,7,8,9]
    tasksb=[10,11,12,13,14,15,16,17,18,19,20,21]

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
    

    def startfunc(self):
        #i=input("enter you ID:")
        #id=("GM", "ADM", "BDM", "AW1", "AW2", "AW3", "BW1", "BW2", "BW3", "BW4")
        if i in self.idgm or i in self.idm or i in self.idaw or i in self.idbw :
             print(f"your ID is {i}")
             return i
        else:
            print("Invalid ID, Please enter a valid ID")
            return False
    def tlist(self):
        if i =="AW1":
            return self.AW1
        elif i== "AW2":
            return self.AW2
        elif i=="AW3":
            return self.AW3
        elif i=="BW1":
            return self.BW1
        elif i=="BW2":
            return self.BW2
        elif i=="BW3":
            return self.BW3
        elif i=="BW4":
            return self.BW4
    def tdept(self):
        if i=="AW1" or i=="AW2" or i=="AW3":
            return "A"
        elif i=="BW1" or i=="BW2"or i=="BW3" or i=="BW4":
            return "B"
    
             
        


class worker(start):
    
    @classmethod
    def taskmethod(self,ID, tmethod, taskdept):
        self.ID=ID
        self.tmethod=tmethod
        self.taskdept=taskdept
        if self.taskdept=="A":
            self.tasks=self.tasksa
        elif self.taskdept=="B":
            self.tasks=self.tasksb


     
        print(f"  \nwelcome{self.ID}")
        aa="""
 1.check your task list
 2.pick a task
 3.complete a task
        """
        print(aa)
        a=int(input("enter 1/2/3:"))
        if a==1:
            self.taskcheck()
        elif a==2:
            self.taskpick()
        elif a==3:
            self.taskresolve()
    @classmethod
    def taskcheck(self):
        print(self.tmethod)
        
    @classmethod
    def taskpick(self):
        s=len(self.tmethod)
        print(s)
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
                print("you have reached your maximum task limit")

            print(self.tasks)
            print("your new task list")
            print(self.tmethod)
            
   

            
         
            
        
    
    

        
        

a="""enter your ID, ID should be any of the following:
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
aw2=worker(i)
aw3=worker(i)
bw1=worker(i)
bw2=worker(i)
bw3=worker(i)
bw4=worker(i)


#z= st.startfunc()
while True:
    
    i=input("enter you ID:")
 
    z= st.startfunc()
    while z==False:
        i=input("enter you ID:")
        z= st.startfunc()
    if z!=False and i=="AW1":
        tt=st.tlist()
        tdep=st.tdept()
        print("tt:")    
        print(tt)    
        zz=aw1.taskmethod(z, tt, tdep)
    if z!=False and i=="AW2":
        tt=st.tlist()
        tdep=st.tdept()
        print("tt:")    
        print(tt)    
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="AW3":
        tt=st.tlist()
        tdep=st.tdept()
        print("tt:")    
        print(tt)    
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="BW1":
        tt=st.tlist()
        tdep=st.tdept()
        print("tt:")    
        print(tt)    
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="BW2":
        tt=st.tlist()
        tdep=st.tdept()
        print("tt:")    
        print(tt)    
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="BW3":
        tt=st.tlist()
        tdep=st.tdept()
        print("tt:")    
        print(tt)    
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="BW4":
        tt=st.tlist()
        print("tt:")    
        print(tt)    
        zz=aw2.taskmethod(z, tt, tdep)
    if z!=False and i=="ADM":
        tt=st.tlist()
       # agm.managerroll(z)


  
    
    