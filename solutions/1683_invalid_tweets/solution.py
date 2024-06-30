/*
title : 1683_invalid_tweets.sql
create : @tarickali 23/05/15
update : @tarickali 23/05/15
*/

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;