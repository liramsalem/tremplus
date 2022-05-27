create table participents_in_drive(
    drive_id int,
    user_id_passenger Varchar (9) not null,
    user_serial_num int not null,
    seat_quantity int not null,
    user_ranking Varchar(1) default 0 not null,
    constraint participents_in_drive_fk1 foreign key (drive_id) references all_future_drives(drive_id),
    constraint participents_in_drive_fk2 foreign key (user_serial_num,user_id_passenger) references users(user_serial_num, user_id),
    constraint participents_in_drive_pk primary key (drive_id, user_id_passenger)
);

INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (1, '207025990',2, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (1, '208931774',7, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (2, '208931774',7, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (4, '208931774',7, 1, '1');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (4, '67844423',12, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (5, '205505951',1, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (6, '67844423',12, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (7, '208931774',7, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (8, '207567890',5, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (9, '208931774',7, 1, '1');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (9, '67844423',12, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (10, '207025990',2, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (12, '207025990',2, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (12, '208931774',7, 1, '1');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (15, '208931774', 7, 1, '1');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (17, '207555332', 4, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (17, '208931774', 7, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (18, '318986775', 11, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (20, '318986775', 11, 1, '0');
INSERT INTO tremplus_db.participents_in_drive (drive_id, user_id_passenger, user_serial_num, seat_quantity, user_ranking) VALUES (25, '208931774', 7, 1, '0');
