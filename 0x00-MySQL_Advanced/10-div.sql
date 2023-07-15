-- Division

DROP FUNCTION IF EXISTS SafeDiv

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC

IF b = 0 THEN
	RETURN 0;
END IF;

RETURN (a / b); 