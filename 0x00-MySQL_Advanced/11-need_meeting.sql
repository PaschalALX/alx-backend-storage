-- Need meeting

DROP VIEW IF EXISTS need_meeting; 

CREATE VIEW need_meeting as SELECT name from students 
WHERE score < 80 
AND (last_meeting IS NULL OR DATE(last_meeting) > DATE_ADD(DATE(NOW()), INTERVAL -1 MONTH));
