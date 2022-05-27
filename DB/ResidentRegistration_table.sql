create table ResidentRegistration_table(
    id_Number Varchar (10) not null,
    First_Name Varchar (45) not null,
    Last_Name Varchar (45) not null,
    kibutz Varchar (45) not null,
    constraint ResidentRegistration_pk primary key (id_Number)
);

insert into ResidentRegistration_table(id_Number,First_Name,Last_Name,kibutz) values ('208931774','ליר','אמסלם','ניר עם');
insert into ResidentRegistration_table(id_Number,First_Name,Last_Name,kibutz) values ('207025990','שי','פירעם','מפלסים');
insert into ResidentRegistration_table(id_Number,First_Name,Last_Name,kibutz) values ('234345667','ירין','אבוטבול','יכיני');
insert into ResidentRegistration_table(id_Number,First_Name,Last_Name,kibutz) values ('302455653','אסף','פישר','גבים');


