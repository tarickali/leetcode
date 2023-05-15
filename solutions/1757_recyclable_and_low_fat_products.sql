/*
title : 1757_recyclable_and_low_fat_products.sql
create : @tarickali 23/05/15
update : @tarickali 23/05/15
*/

SELECT product_id FROM Products WHERE low_fats = 'Y' && recyclable = 'Y';