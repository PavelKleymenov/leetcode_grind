-- Write an SQL query to report all the duplicate emails. 
-- Note that it's guaranteed that the email field is not NULL

""" +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | email       | varchar |
    +-------------+---------+   
id is the primary key column for this table.
Each row of this table contains an email. 
The emails will not contain uppercase letters."""

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
