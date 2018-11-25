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