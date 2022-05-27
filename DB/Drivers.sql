create table Drivers(
    user_id Varchar (9) not null,
    Fname Varchar (45) not null,
    Lname Varchar (45) not null,
    license_plate Varchar (8) not null,
    car_company Varchar (45) not null,
    car_color Varchar (45) not null,
    licence_driver_pic Varchar (255) not null,
    user_serial_num int not null,
    constraint drivers_fk foreign key (user_serial_num,user_id) references users(user_serial_num,user_id),
    constraint drivers_pk primary key (user_id)
);

INSERT INTO tremplus_db.drivers (user_id, Fname, Lname, license_plate, car_company, car_color, licence_driver_pic,user_serial_num) VALUES ('205505951', 'רוית', 'עמוס', '12366558', 'מיצובישי', 'אדום', 'ililil.jpg',1);
INSERT INTO tremplus_db.drivers (user_id, Fname, Lname, license_plate, car_company, car_color, licence_driver_pic,user_serial_num) VALUES ('207025990', 'שי', 'פירעם', '11111111', 'רנו', 'כחול', 'ililil.jpg',2);
INSERT INTO tremplus_db.drivers (user_id, Fname, Lname, license_plate, car_company, car_color, licence_driver_pic,user_serial_num) VALUES ('207234115', 'טלי', 'אמיר', '12344321', 'סקודה', 'לבן', 'ililil.jpg',3);
INSERT INTO tremplus_db.drivers (user_id, Fname, Lname, license_plate, car_company, car_color, licence_driver_pic,user_serial_num) VALUES ('207555332', 'אביב', 'אסולין', '34566789', 'פיאט 500', 'סגול', '',4);
INSERT INTO tremplus_db.drivers (user_id, Fname, Lname, license_plate, car_company, car_color, licence_driver_pic,user_serial_num) VALUES ('207567890', 'אלמה', 'כהן', '12344133', 'פיאט 500', 'לבן', '../../static/media/img/users_licence_driver_pic/207567890_ld.jpg',5);
INSERT INTO tremplus_db.drivers (user_id, Fname, Lname, license_plate, car_company, car_color, licence_driver_pic,user_serial_num) VALUES ('234345667', 'ירין', 'אבוטבול', '98755443', 'מיצובישי', 'לבן', 'ililil.jpg',9);
INSERT INTO tremplus_db.drivers (user_id, Fname, Lname, license_plate, car_company, car_color, licence_driver_pic,user_serial_num) VALUES ('318986775', 'גל ', 'לוי', '67855654', 'מרצדס', 'כסף', '',11);
