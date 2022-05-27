create table All_Future_Drives(
    drive_id int auto_increment,
    user_id_driver Varchar (9) not null,
    origin Varchar (255) not null,
    destination Varchar (255) not null,
    drive_date date not null,
    departure_hour time not null,
    max_seats int not null ,
    free_seats int not null ,
    constraint All_Future_Drives_fk foreign key (user_id_driver) references drivers(user_id),
    constraint All_Future_Drives_pk primary key (drive_id, user_id_driver,drive_date,departure_hour)
);

INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (1, '207234115', 'שדרות', 'מפלסים', '2022-03-30', '21:36:00', 2, 0);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (2, '207234115', 'שדרות', 'ניר עם', '2022-04-01', '13:37:00', 3, 2);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (3, '207234115', 'ניר עם', 'מפלסים', '2022-04-02', '15:39:00', 1, 1);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (4, '207234115', 'אור הנר', 'יכיני', '2022-04-12', '16:20:00', 3, 1);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (5, '207234115', 'מפלסים', 'רוחמה', '2022-04-10', '17:40:00', 3, 2);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (6, '207234115', 'נחל עוז', 'כפר עזה', '2022-04-09', '20:33:00', 2, 1);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (7, '207234115', 'נחל עוז', 'ניר עם', '2022-03-31', '15:10:00', 3, 2);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (8, '207234115', 'יכיני', 'כפר עזה', '2022-04-28', '15:18:00', 2, 1);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (9, '207234115', 'שדרות', 'כפר עזה', '2022-04-24', '17:18:00', 2, 0);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (10, '207234115', 'כפר עזה', 'שדרות', '2022-04-24', '21:00:00', 1, 0);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (11, '207234115', 'ניר עם', 'אור הנר', '2022-04-24', '11:00:00', 1, 1);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (12, '207234115', 'אור הנר', 'יכיני', '2022-04-21', '12:19:00', 2, 0);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (13, '207234115', 'נחל עוז', 'כפר עזה', '2022-04-21', '10:10:00', 1, 1);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (14, '207025990', 'אור הנר', 'רוחמה', '2022-04-25', '15:52:00', 3, 3);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (15, '234345667', 'ניר עם', 'יכיני', '2022-04-20', '21:24:00', 2, 2);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (16, '207234115', 'שדרות', 'כפר עזה', '2022-04-20', '08:18:00', 1, 1);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (17, '207234115', 'שדרות', 'רוחמה', '2022-05-06', '14:05:00', 2, 0);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (18, '207025990', 'ניר עם', 'כפר עזה', '2022-05-11', '14:41:00', 2, 1);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (20, '207025990', 'נחל עוז', 'מפלסים', '2022-05-20', '19:44:00', 3, 2);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (21, '207025990', 'יכיני', 'שדרות', '2022-05-27', '10:57:00', 2, 2);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (22, '207555332', 'יכיני', 'תל אביב', '2022-05-31', '21:32:00', 2, 2);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (24, '318986775', 'שדרות', 'כפר עזה', '2022-05-31', '20:23:00', 3, 3);
INSERT INTO tremplus_db.all_future_drives (drive_id, user_id_driver, origin, destination, drive_date, departure_hour, max_seats, free_seats) VALUES (25, '207234115', 'יכיני', 'ניר עם', '2022-06-01', '15:29:00', 2, 1);
