USE `white_collar`;

DROP TABLE IF EXISTS `source_type_conviction`;
DROP TABLE IF EXISTS `source_type`;
DROP TABLE IF EXISTS `location_conviction`;
DROP TABLE IF EXISTS `location`;
DROP TABLE IF EXISTS `scheme_conviction`;
DROP TABLE IF EXISTS `scheme`;
DROP TABLE IF EXISTS `crime_conviction`;
DROP TABLE IF EXISTS `crime`;
DROP TABLE IF EXISTS `occupation_conviction`;
DROP TABLE IF EXISTS `occupation`;
DROP TABLE IF EXISTS `sector_conviction`;
DROP TABLE IF EXISTS `sector`;
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
  `privilege` ENUM('admin', 'specialist', 'viewer'),
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
  `race_id` INT UNSIGNED,
  `nationality_id` INT UNSIGNED,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`convict_id`),
  CONSTRAINT `fk_convict_race` FOREIGN KEY (`race_id`) REFERENCES `race` (`race_id`),
  CONSTRAINT `fk_convict_nationality` FOREIGN KEY (`nationality_id`) REFERENCES `nationality` (`nationality_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `conviction` (
  `conviction_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `convict_id` INT UNSIGNED,
  `age_group` ENUM("young", "adult", "mature", "senior"),
  `company` VARCHAR(85),
  `affiliation` BOOL,
  `charges` INT UNSIGNED,
  `court_type` ENUM("federal", "state", "international"),
  `sentence` INT UNSIGNED,
  `fine` INT UNSIGNED,
  `decade` ENUM("pre-20th century", "1900-09", 
				        "1910-19", "1920-29", "1930-39", 
                "1940-49", "1950-59", "1960-69", 
                "1970-79", "1980-89", "1990-99", 
                "2000-09", "2010-19", "2020-29"),
  `parole` BOOL,
  `summary` VARCHAR(950),
  `source_name` VARCHAR(85),
  `source_url` VARCHAR(200),
  `source_date` DATETIME,
  `user_id_initial` INT UNSIGNED,
  `initial_create` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id_last` INT UNSIGNED,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`conviction_id`),
  CONSTRAINT `fk_conviction_convict` FOREIGN KEY (`convict_id`) REFERENCES `convict` (`convict_id`),
  CONSTRAINT `fk_conviction_user_id_initial` FOREIGN KEY (`user_id_initial`) REFERENCES `user` (`user_id`),
  CONSTRAINT `fk_conviction_user_id_last` FOREIGN KEY (`user_id_last`) REFERENCES `user` (`user_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `sector` (
  `sector_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `sector` VARCHAR(85),
  `sector_desc` VARCHAR(85),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`sector_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `sector_conviction` (
  `conviction_id` INT UNSIGNED NOT NULL,
  `sector_id` INT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT `fk_sector_conviction_conviction` FOREIGN KEY (`conviction_id`) REFERENCES `conviction` (`conviction_id`),
  CONSTRAINT `fk_sector_conviction_sector` FOREIGN KEY (`sector_id`) REFERENCES `sector` (`sector_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `occupation` (
  `occupation_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `occupation` VARCHAR(45),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`occupation_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `occupation_conviction` (
  `conviction_id` INT UNSIGNED NOT NULL,
  `occupation_id` INT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT `fk_occupation_conviction_conviction` FOREIGN KEY (`conviction_id`) REFERENCES `conviction` (`conviction_id`),
  CONSTRAINT `fk_occupation_conviction_occupation` FOREIGN KEY (`occupation_id`) REFERENCES `occupation` (`occupation_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `crime` (
  `crime_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `crime` VARCHAR(45),
  `crime_desc` VARCHAR(950),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`crime_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `crime_conviction` (
  `conviction_id` INT UNSIGNED NOT NULL,
  `crime_id` INT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT `fk_crime_conviction_conviction` FOREIGN KEY (`conviction_id`) REFERENCES `conviction` (`conviction_id`),
  CONSTRAINT `fk_crime_conviction_crime` FOREIGN KEY (`crime_id`) REFERENCES `crime` (`crime_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `scheme` (
  `scheme_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `scheme` VARCHAR(45),
  `scheme_desc` VARCHAR(950),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`scheme_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `scheme_conviction` (
  `conviction_id` INT UNSIGNED NOT NULL,
  `scheme_id` INT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT `fk_scheme_conviction_conviction` FOREIGN KEY (`conviction_id`) REFERENCES `conviction` (`conviction_id`),
  CONSTRAINT `fk_scheme_conviction_scheme` FOREIGN KEY (`scheme_id`) REFERENCES `scheme` (`scheme_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `location` (
  `location_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(45),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`location_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `location_conviction` (
  `conviction_id` INT UNSIGNED NOT NULL,
  `location_id` INT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT `fk_location_conviction_conviction` FOREIGN KEY (`conviction_id`) REFERENCES `conviction` (`conviction_id`),
  CONSTRAINT `fk_location_conviction_location` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `source_type` (
  `source_type_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `source_type` VARCHAR(45),
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`source_type_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `source_type_conviction` (
  `conviction_id` INT UNSIGNED NOT NULL,
  `source_type_id` INT UNSIGNED NOT NULL,
  `last_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT `fk_source_type_conviction_conviction` FOREIGN KEY (`conviction_id`) REFERENCES `conviction` (`conviction_id`),
  CONSTRAINT `fk_source_type_conviction_source_type` FOREIGN KEY (`source_type_id`) REFERENCES `source_type` (`source_type_id`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;