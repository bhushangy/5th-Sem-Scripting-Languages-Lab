1) create table employee(SSN number primary key,DeptNo number);

2) create table project(ProjectNo number primary key,ProjectArea varchar);

3) create table assigned_to(USN number,ProjectNo number,foreign key (USN) references employee(SSN),foreign key (ProjectNo) references  project(ProjectNo));

4) insert into employee
   (SSN,Name,DeptNo)
   values
   (123321,'bhushan',2);


5) insert into employee
   (SSN,Name,DeptNo)
   values
   (141411,'brad pitt',6);


6)  insert into employee
    (SSN,Name,DeptNo)
    values
    (141441,'tom hanks',6);
  
7)  insert into employee
    (SSN,Name,DeptNo)
    values
    (333411,'quinten',1);

8)  insert into employee
    (SSN,Name,DeptNo)
    values
    (221411,'tarrantino',4);

 
9)  	INSERT INTO PROJECT (ProjectNo,ProjectArea) VALUES (1,'Database');
	INSERT INTO PROJECT (ProjectNo,ProjectArea) VALUES (2,'Atomic Bomb');
	INSERT INTO PROJECT (ProjectNo,ProjectArea) VALUES (3,'Chemical Weapon');
	INSERT INTO PROJECT (ProjectNo,ProjectArea) VALUES (4,'Microprocessor');
	INSERT INTO PROJECT (ProjectNo,ProjectArea) VALUES (20,'Networking');


10)     INSERT INTO ASSIGNED_TO (SSN,ProjectNo) VALUES (1,4);
	INSERT INTO ASSIGNED_TO (SSN,ProjectNo) VALUES (2,1);
	INSERT INTO ASSIGNED_TO (SSN,ProjectNo) VALUES (3,4);
	INSERT INTO ASSIGNED_TO (SSN,ProjectNo) VALUES (4,3);
	INSERT INTO ASSIGNED_TO (SSN,ProjectNo) VALUES (5,20);
	INSERT INTO ASSIGNED_TO (SSN,ProjectNo) VALUES (6,20);



