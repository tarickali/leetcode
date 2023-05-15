/*
title : 0595_big_countries.sql
create : @tarickali 23/05/15
update : @tarickali 23/05/15
*/

SELECT name, population, area
FROM World 
WHERE area >= 3000000 || population >= 25000000;