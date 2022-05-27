create table ranking(
    driver_id Varchar (9) not null,
    one_star int default 0,
    two_star int default 0,
    three_star int default 0,
    four_star int default 0,
    five_star int default 0,
    total_stars int default 0,
    total_votes int default 0,
    avg float default 0,
    constraint ranking_fk foreign key (driver_id) references drivers(user_id),
    constraint ranking_pk primary key (driver_id)
);

INSERT INTO tremplus_db.ranking (driver_id, one_star, two_star, three_star, four_star, five_star, total_stars, total_votes, avg) VALUES ('207025990', 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO tremplus_db.ranking (driver_id, one_star, two_star, three_star, four_star, five_star, total_stars, total_votes, avg) VALUES ('207234115', 12, 18, 42, 15, 18, 324, 105, 3.08571);
INSERT INTO tremplus_db.ranking (driver_id, one_star, two_star, three_star, four_star, five_star, total_stars, total_votes, avg) VALUES ('207555332', 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO tremplus_db.ranking (driver_id, one_star, two_star, three_star, four_star, five_star, total_stars, total_votes, avg) VALUES ('207567890', 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO tremplus_db.ranking (driver_id, one_star, two_star, three_star, four_star, five_star, total_stars, total_votes, avg) VALUES ('234345667', 1, 6, 4, 4, 4, 61, 19, 3.21053);
INSERT INTO tremplus_db.ranking (driver_id, one_star, two_star, three_star, four_star, five_star, total_stars, total_votes, avg) VALUES ('318986775', 0, 0, 0, 0, 0, 0, 0, 0);
