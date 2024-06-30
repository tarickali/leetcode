/*
title : 1148_article_views_I.sql
create : @tarickali 23/05/15
update : @tarickali 23/05/15
*/

SELECT DISTINCT author_id AS id
FROM Views
WHERE viewer_id = author_id
ORDER BY author_id;