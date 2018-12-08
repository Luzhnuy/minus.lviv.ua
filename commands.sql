ALTER TABLE userprofile  ADD COLUMN is_business INT DAFAULT 0;
ALTER TABLE blurbs_blurb  ADD COLUMN is_user_business INT DAFAULT 0;
UPDATE userprofile SET is_business = 0;
UPDATE blurbs_blurb SET is_user_business = 0;
ALTER TABLE userprofile MODIFY hide_birthdate date DEFAULT 0;
ALTER TABLE userprofile MODIFY is_admin_subscribed INT DEFAULT 0;
ALTER DATABASE minus CHARACTER SET utf8;










Установка redis server
