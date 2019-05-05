DROP TABLE IF EXISTS `unit`;

CREATE TABLE `unit` (
  `id` INT NOT NULL DEFAULT '0' PRIMARY KEY,
  `name` VARCHAR(256) NOT NULL DEFAULT ''
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `idol`;

CREATE TABLE `idol` (
  `id` INT NOT NULL DEFAULT '0' PRIMARY KEY,
  `name` VARCHAR(256) NOT NULL DEFAULT '',
  `unit_id` INT NOT NULL DEFAULT '1'
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `produce_card`;

CREATE TABLE `produce_card` (
  `id` INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `name` VARCHAR(256) NOT NULL DEFAULT '',
  `rarity` INT NOT NULL DEFAULT '1',
  `idol_id` INT NOT NULL DEFAULT '1',
  `release_date` DATE NOT NULL DEFAULT '0000-00-00',
  `icon_hash` CHAR(64) DEFAULT NULL,
  `card_hash` CHAR(64) DEFAULT NULL,
  `fes_card_hash` CHAR(64) DEFAULT NULL,
  INDEX `rarity_idol_id_release_date_index` (`rarity`, `idol_id`, `release_date`),
  INDEX `idol_id_index` (`idol_id`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `support_card`;

CREATE TABLE `support_card` (
  `id` INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `name` VARCHAR(256) NOT NULL DEFAULT '',
  `rarity` INT NOT NULL DEFAULT '1',
  `idol_id` INT NOT NULL DEFAULT '1',
  `release_date` DATE NOT NULL DEFAULT '0000-00-00',
  `icon_hash` CHAR(64) DEFAULT NULL,
  `card_hash` CHAR(64) DEFAULT NULL,
  `vocal` INT NOT NULL DEFAULT '0',
  `dance` INT NOT NULL DEFAULT '0',
  `visual` INT NOT NULL DEFAULT '0',
  `mental` INT NOT NULL DEFAULT '0',
  `max_vocal` INT NOT NULL DEFAULT '0',
  `max_dance` INT NOT NULL DEFAULT '0',
  `max_visual` INT NOT NULL DEFAULT '0',
  `max_mental` INT NOT NULL DEFAULT '0',
  `idea` INT NOT NULL DEFAULT '1',
  INDEX `rarity_idol_id_release_date_index` (`rarity`, `idol_id`, `release_date`),
  INDEX `idol_id_index` (`idol_id`),
  INDEX `idea_index` (`idea`)
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `cartoon`;
DROP TABLE IF EXISTS `character`;

CREATE TABLE `character` (
  `name` varchar(255) PRIMARY KEY
) ENGINE=Mroonga DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='default_tokenizer "TokenDelimit"';

CREATE TABLE `cartoon` (
  `id` INT NOT NULL DEFAULT '0' PRIMARY KEY,
  `type` INT NOT NULL DEFAULT '0',
  `episode` INT NOT NULL DEFAULT '0',
  `title` VARCHAR(256) NOT NULL DEFAULT '',
  `release_date` DATE NOT NULL DEFAULT '0000-00-00',
  `characters` TEXT COMMENT 'flags "COLUMN_VECTOR", type "character"',
  `thumbnail_hash` CHAR(64) DEFAULT NULL,
  `image_hash` CHAR(64) DEFAULT NULL,
  `tweet_id` BIGINT unsigned DEFAULT NULL,
  `comment` VARCHAR(256) NOT NULL DEFAULT '',
  UNIQUE INDEX `type_episode_index` (`type`, `episode`),
  FULLTEXT INDEX `title_index` (`title`),
  FULLTEXT INDEX `characters_index` (`characters`) COMMENT 'table "character"'
) ENGINE=Mroonga DEFAULT CHARSET=utf8;