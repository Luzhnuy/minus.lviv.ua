ALTER TABLE userprofile  ADD COLUMN is_business INT DAFAULT 0;
ALTER TABLE blurbs_blurb  ADD COLUMN is_user_business INT DAFAULT 0;
UPDATE userprofile SET is_business = 0;
UPDATE blurbs_blurb SET is_user_business = 0;
ALTER TABLE userprofile MODIFY hide_birthdate date DEFAULT 0;
ALTER TABLE userprofile MODIFY is_admin_subscribed INT DEFAULT 0;
ALTER DATABASE minus CHARACTER SET utf8;
ALTER TABLE userprofile ADD COLUMN is_user_online TINYINT(1) default 0;
ALTER TABLE useractivitys ADD COLUMN activity_to INT;
ALTER TABLE blurbs_blurb ADD COLUMN cost Char(255) DEFAULT 'Договірна';
ALTER TABLE minusstore_minusrecord ADD COLUMN record_quality_score INT;
ALTER TABLE minusstore_minusrecord ADD COLUMN arrangement_score INT;
ALTER TABLE minusstore_minusrecord ALTER COLUMN record_quality_score SET DEFAULT 0;
ALTER TABLE minusstore_minusrecord ALTER COLUMN arrangement_score SET DEFAULT 0;



Установка redis server
