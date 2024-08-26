-- SQL script that creates a function SafeDiv
-- Safe divide
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    RETURN IF(b = 0, 0, a / b);
END //
DELIMITER ;
