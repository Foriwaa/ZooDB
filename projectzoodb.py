"""
Created on Sun Apr 29 2022

@author: Fori
"""
import sqlite3 as db
from datetime import date
from datetime import timedelta

class projectzooDB:
    def __init__(self):
        self.con = db.connect("projectzoo.db", check_same_thread=False)
    
    def __del__(self):
        self.con.close()
    
    def updateEmployeeInfo(self, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary):
        cur = self.con.cursor()
        params = (FirstName,LastName,Gender,Address,City,State,Zipcode,DepartmentId,Email,Phone,SupervisorId,Salary,FirstName,LastName,)
        cur.execute("UPDATE employee SET FirstName = ?, LastName = ?, Gender = ?, Address = ?, City = ?, State = ?, Zipcode = ?, DepartmentId = ?, Email = ?, Phone = ?, SupervisorId = ?, Salary = ? WHERE FirstName = ? AND LastName = ?", params)
        self.con.commit()
        pr = (FirstName, LastName, Phone,)
        cur.execute("SELECT FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary FROM Employee WHERE FirstName like ? AND LastName like ? AND Phone like ?", pr)
        result = cur.fetchall()
        return(result)
    
    
    def updateVisitorInfo(self,FirstName,LastName,Address,City,State,Zipcode,Birthday,Email):
        cur = self.con.cursor()
        params = (FirstName,LastName,Address,City,State,Zipcode,Birthday,Email)
        cur.execute("UPDATE Visitors SET FirstName =?, LastName =?, Address =?, City =?, State =?, Zipcode =?, Birthday =?, Email =?", params)
        self.con.commit()
        pr = (FirstName, LastName,)
        cur.execute("SELECT FirstName, LastName, Address, City, State, Zipcode, Birthday, Email FROM Visitors WHERE FirstName =? AND LastName =?", pr)
        result = cur.fetchone()
        return(result)
    
    
    def listAnimalInfo(self, animalid):
        cur = self.con.cursor()
        params = (animalid,)
        cur.execute("SELECT AnimalId, Sex, Name, Species, Birthdate, Age, ExtinctionStatus, Origin, LocationName FROM Animal WHERE AnimalId like ?", params)
        result = cur.fetchall()
        return(result)
    
    '''
     result = dbobj.listAnimalInfo(animalid)
     if len(result) == 0:
       print("<h2>%s Animal not found in the database</h2>" % animalid)
     else:
       for row in result:
          print(row)
     print("""
     <br>
     <a href="?">Return Home</a>
     """)
    '''
    
    def listNearbyAnimal(self, zonename):
        cur = self.con.cursor()
        params = (zonename,)
        cur.execute("SELECT a.AnimalId, a.Species, a.LocationName FROM Animal AS a, Location AS l WHERE a.LocationName = l.LocationName AND l.ZoneName like ?", params)
        result = cur.fetchall()
        return(result)

    '''
     result = dbobj.listNearbyAnimal(zonename)
     if len(result) == 0:
       print("<h2>%s Zone not found in the database</h2>" % zonename)
     else:
       for row in result:
           print(row)
     print("""
     <br>
     <a href="?">Return Home</a>
     """)
    '''
    
    def listVisitorBasedOnTier(self, tier):
        cur = self.con.cursor()
        params = (tier,)
        cur.execute("SELECT VisitorId, FirstName, LastName FROM Visitors WHERE MembershipTier like ?", params)
        result = cur.fetchall()
        return(result)

    '''
     result = dbobj.listVisitorBasedOnTier(tier)
     if len(result) == 0:
       print("<h2>%d Tier not valid</h2>" % tier)
     else:
       for row in result:
           print(row)
     print(""" 
      <br>
     <a href="?">Return Home</a>
     """)
    '''
    
    def showOldestAnimal(self):
        cur = self.con.cursor()
        cur.execute("SELECT AnimalId, Name, Species, Age, LocationName FROM Animal WHERE Age = (SELECT MAX(Age) FROM Animal)")
        result = cur.fetchall()
        return(result)

    '''
     result = dbobj.showOldestAnimal()
        for row in result:
          print(row)
     print("""
     <br>
     <a href="?">Return Home</a>
     """)
    '''
    
    def showForeignAnimal(self):
        cur = self.con.cursor()
        cur.execute("SELECT AnimalId, Species, LocationName FROM Animal WHERE Origin != 'Project'")
        result = cur.fetchall()
        return(result)

    '''
     result = dbobj.showForeignAnimal()
     if len(result) == 0:
       print("<h2> No animal from outside</h2>")
     else:
       for row in result:
           print(row)
     print("""
     <br>
     <a href="?">Return Home</a>
     """)
    '''
    
    def showNearbyFeeding(self, zonename):
        cur = self.con.cursor()
        params = (zonename,)
        cur.execute("SELECT f.Time, f.LocationName, a.AnimalId, a.Species FROM Animal AS a, Location AS l, FeedingCalendar AS f WHERE a.LocationName = f.LocationName AND f.LocationName = l.LocationName AND l.ZoneName like %s", params)
        result = cur.fetchall()
        return(result)

    '''
     result = dbobj.showNearbyFeeding(zonename)
     if len(result) == 0:
       print("<h2>%s Zone not found in the database</h2>" % zonename)
     else:
       for row in result:
           print(row)
     print("""
     <br>
     <a href="?">Return Home</a>
     """)
    '''
    
    def createNewVisitorAccount(self, FirstName, LastName, Address, City, State, Zipcode, Birthday, Email):
        cur = self.con.cursor();
        tod = date.today();
        JoinDate = str(date.today());
        exp = tod + timedelta(days = 1825);
        ExpiryDate = str(exp);
        MembershipTier = '0';
        ZoopBalance = 0;
        params = (FirstName, LastName, Address, City, State, Zipcode, Birthday, MembershipTier, Email, ZoopBalance, JoinDate, ExpiryDate, None, )
        cur.execute("INSERT INTO Visitors (FirstName, LastName, Address, City, State, Zipcode, Birthday, MembershipTier, Email, ZoopBalance, JoinDate, ExpiryDate, RepId)Values (?,?,?,?,?,?,?,?,?,?,?,?,?)", params)
        self.con.commit()
        pr = (FirstName, LastName, Email,)
        cur.execute("SELECT FirstName, LastName, Address, City, State, Zipcode, Birthday, MembershipTier, Email, ZoopBalance, JoinDate, ExpiryDate, RepId FROM Visitors WHERE FirstName like ? AND LastName like ? AND Email like ?", pr)
        result = cur.fetchall()
        return (result)
        
    
    def insertNewEmployee(self, SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary):
        cur = self.con.cursor();
        params = (SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary,)
        cur.execute("INSERT INTO Employee (SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", params)
        self.con.commit()
        pr = (SSN,)
        cur.execute("SELECT SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary FROM Employee WHERE SSN like ?", pr)        
        result = cur.fetchall()
        return(result)
    
    
    def visitorIdExist(self, iD):
        cur = self.con.cursor()
        params = (iD,)
        cur.execute("SELECT * FROM Visitors WHERE VisitorId = ?", params)
        if len(cur.fetchall()) == 0:
            return False
        else:
            return True
    
    def deleteVisitorById(self, iD):
        if (self.visitorIdExist(iD)):
            cur = self.con.cursor()
            params = (iD,)
            cur.execute("DELETE FROM Visitors WHERE VisitorId = ?", params)
            self.con.commit()
            print("<p>Visitor deleted</p>")
        else:
            print("<p>Visitor doesn't exist!</p>")
            return
    
    def employeeIdExist(self, iD):
        cur = self.con.cursor()
        params = (iD,)
        cur.execute("SELECT * FROM ES WHERE EmployeeId = ?", params)
        if len(cur.fetchall()) == 0:
            return False
        else:
            return True  
          
    def HasEmployee(self,firstname,lastname):
        cur=self.con.cursor();
        params=(firstname,lastname,)
        cur.execute("SELECT FirstName,LastName FROM Employee WHERE FirstName =? and LastName=?",params)
        result=cur.fetchall()
        return (result)
    
    def deleteEmpById(self, iD):
        if (self.employeeIdExist(iD)):
            cur = self.con.cursor()
            param = (iD, )
            cur.execute("DELETE FROM ES WHERE EmployeeId = ?", param)
            self.con.commit()
            print("<p>Employee deleted</p>")
        else:
            print("Employee doesn't exist")
            return

    def checkAccountType(self, username, password):
        cur = self.con.cursor()
        param = (username,)
        cur.execute("SELECT * FROM Logins WHERE username = ?", param)
        if len(cur.fetchall()) == 0:
            print("Username or password mismatched!")
            return None
        else:
            param = (username, password)
            cur.execute("SELECT * FROM Logins WHERE username = ? AND password = ?", param)
            if len(cur.fetchall()) == 0:
                print("Username or password mismatched!")
                return None
            else:
                cur.execute("SELECT Acc_Type FROM Logins WHERE username = ? AND password = ?", param)
                result = cur.fetchone()
                return result

'''
obj= projectzooDB()
print(obj.showForeignAnimal())
print(obj.visitorIdExist(12))

con = db.connect("projectzoo.db")
cur = con.cursor()
cur.execute("SELECT AnimalId, Name, Species, Age, LocationName FROM Animal WHERE Age = (SELECT MAX(Age) FROM Animal)")
print(cur.fetchall())
con.commit()
con.close()
'''
    