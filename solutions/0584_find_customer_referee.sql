/*
title : 0584_find_customer_referee.sql
create : @tarickali 23/05/15
update : @tarickali 23/05/15
*/

SELECT name FROM Customer WHERE referee_id IS NULL || referee_id != 2;