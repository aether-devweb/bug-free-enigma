drop database if exists grails_beta; -- Dev

create database if not exists grails; -- Production
create database grails_beta;
\! clear;

use grails_beta;

create table ticket (
    id int primary key auto_increment,
    user varchar(15) not null, -- 10 Digit Phone + 1-3 Digit Country Code + 2 Whitespace
    dept varchar(20),
    arr varchar(20),
    dept_time time,
    arr_time time
);

-- insert into ticket (user, dept, arr, dept_time, arr_time) values 
--     ('+91 8387990021', 'Jaipur', 'Mumbai', '18:00', '23:00'),
--     ('+91 8387990021', 'Mumbai', 'Coimbatore', '24:00', '06:00');