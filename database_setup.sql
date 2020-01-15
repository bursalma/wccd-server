USE `white_collar`;

DROP TABLE IF EXISTS `conviction`;
DROP TABLE IF EXISTS `convict`;
DROP TABLE IF EXISTS `nationality`;
DROP TABLE IF EXISTS `race`;
DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45),
  `password` VARCHAR(200),
  `full_name` VARCHAR(200),
  `email` VARCHAR(85),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `race` (
  `race_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `race` VARCHAR(20),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`race_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `nationality` (
  `nationality_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nationality` VARCHAR(45),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`nationality_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `convict` (
  `convict_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `last_name` VARCHAR(45),
  `first_name` VARCHAR(45),
  `middle_name` VARCHAR(45),
  `sex` ENUM("male", "female"),
  `race_id` int unsigned,
  `nationality_id` int unsigned,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`convict_id`),
  CONSTRAINT `fk_convict_race` FOREIGN KEY (`race_id`) REFERENCES `race` (`race_id`),
  CONSTRAINT `fk_convict_nationality` FOREIGN KEY (`nationality_id`) REFERENCES `nationality` (`nationality_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `conviction` (
  `conviction_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `convict_id` int unsigned,
  `age_group` enum("young", "adult", "mature", "senior"),
  `company` VARCHAR(85),
  `affiliation` BOOL,
  `charges` INT unsigned,
  `court_type` enum("federal", "state", "international"),
  `sentence` int unsigned,
  `fine` int unsigned,
  `decade` enum("pre-20th century", "1900-09", 
				        "1910-19", "1920-29", "1930-39", 
                "1940-49", "1950-59", "1960-69", 
                "1970-79", "1980-89", "1990-99", 
                "2000-09", "2010-19", "2020-29"),
  `parole` bool,
  `summary` VARCHAR(950),
  `source_name` VARCHAR(85),
  `source_url` VARCHAR(200),
  `source_date` datetime,
  `user_id_initial` int unsigned,
  `initial_create` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id_last` int unsigned,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`conviction_id`),
  CONSTRAINT `fk_conviction_convict` FOREIGN KEY (`convict_id`) REFERENCES `convict` (`convict_id`),
  CONSTRAINT `fk_conviction_user_id_initial` FOREIGN KEY (`user_id_initial`) REFERENCES `user` (`user_id`),
  CONSTRAINT `fk_conviction_user_id_last` FOREIGN KEY (`user_id_last`) REFERENCES `user` (`user_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;
