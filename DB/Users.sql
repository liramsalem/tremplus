
create table users(
    Fname Varchar (45) not null,
    Lname Varchar (45) not null,
    nickname Varchar(45) not null,
    kibutz Varchar (45) not null,
    user_id Varchar (9) not null,
    phone Varchar (10),
    user_email Varchar (45) not null,
    password Varchar (45) not null,
    profile_pic Varchar (255) default 'Register/media/profile.png',
    user_serial_num int auto_increment,
    constraint users_pk primary key (user_serial_num, user_id)
);


INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('רוית', 'עמוס', 'רויתוש', 'גבים', '205505951', '0523445678', 'Ravit.Amos@gmail.com', '12345678', '../../static/media/img/users_profile_pic/205505951.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('שי', 'פירעם', 'שיקייי', 'מפלסים', '207025990', '0507253261', 'shayp@gmail.com', '11111111', '../../static/media/img/users_profile_pic/207025990.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('טלי', 'אמיר', 'טליי111', 'יכיני', '207234115', '0523334567', 'tali@walla.com', '123412345', '../../static/media/img/users_profile_pic/207234115.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('אביב', 'אסולין', 'אביב', 'גבים', '207555332', '0528669999', 'avivasulin@gmail.com', '99998888', '../../static/media/img/users_profile_pic/207555332.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('אלמה', 'כהן', 'אלמה', 'מפלסים', '207567890', '0526776543', 'alma@gmail.com', '11111111', '../../static/media/img/users_profile_pic/207567890.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('אלונה', 'טל', 'אלוני', 'רוחמה', '207678554', '0524447766', 'alonatal@gmail.com', '12345678', '../../static/media/img/users_profile_pic/207678554.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('ליר', 'אמסלם', 'jj', 'ניר עם', '208931774', 'rr', 'liramsalem@gmail.com', '12345678', '../../static/media/img/users_profile_pic/208931774.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('גל', 'כהן', 'd', 'יכיני', '209000998', '0523779898', 'galc@walla.com', '44444444', 'Register/media/profile.png');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('ירין', 'אבוטבול', 'ירין123', 'יכיני', '234345667', '0435665432', 'yarin@gmail.com', '44553322', '../../static/media/img/users_profile_pic/234345667.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('אסף', 'פישר', 'אסף', 'גבים', '302455653', '0523445678', 'Asaf.Lotz@gmail.com', '11223344', 'Register/media/profile.png');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('גל ', 'לוי', 'גל לוי', 'כפר עזה', '318986775', '0507665678', 'gal_levi@gmail.com', '123123123', '../../static/media/img/users_profile_pic/318986775.jpg');
INSERT INTO tremplus_db.users (Fname, Lname, nickname, kibutz, user_id, phone, user_email, password, profile_pic) VALUES ('מאור', 'לוי', 'לוי', 'ניר עם', '67844423', '0523344555', 'maor@gmail.com', '45673456', 'Register/media/profile.png');
