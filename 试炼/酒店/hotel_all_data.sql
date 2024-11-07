/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50743 (5.7.43-log)
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50743 (5.7.43-log)
 File Encoding         : 65001

 Date: 10/09/2023 21:44:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for hotel_all
-- ----------------------------
DROP TABLE IF EXISTS `hotel_all`;
CREATE TABLE `hotel_all`  (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '酒店编号',
  `hotel_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '酒店名称',
  `city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '城市',
  `province` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '省份',
  `level` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '星级',
  `room_num` int(10) NULL DEFAULT NULL COMMENT '房间数',
  `score` double NOT NULL COMMENT '评分',
  `shopping` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商圈',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 39 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hotel_all
-- ----------------------------
INSERT INTO `hotel_all` VALUES (1, '上海玩具总动员酒店', '上海', '上海', '高档型', 800, 4.7, '迪士尼');
INSERT INTO `hotel_all` VALUES (2, '上海新天地安达仕酒店', '上海', '上海', '豪华型', 307, 4.5, '淮海路/新天地');
INSERT INTO `hotel_all` VALUES (3, '上海虹口三至喜来登酒店', '上海', '上海', '五星级', 471, 4.6, '四川北路');
INSERT INTO `hotel_all` VALUES (4, '上海国际贵都大饭店', '上海', '上海', '四星级', 506, 4.6, '静安寺/南京西路');
INSERT INTO `hotel_all` VALUES (5, '上海外滩华尔道夫酒店', '上海', '上海', '豪华型', 260, 4.6, '外滩');
INSERT INTO `hotel_all` VALUES (6, '上海利园国际大酒店', '上海', '上海', '高档型', 396, 4.6, '打浦桥');
INSERT INTO `hotel_all` VALUES (7, '维也纳国际酒店(上海国展中心曹安公路店)', '上海', '上海', '舒适型', 233, 4.8, '虹桥机场/国家会展中心');
INSERT INTO `hotel_all` VALUES (8, '中建瑞贝庭臻选公寓酒店(上海彭浦新村地铁站店)', '上海', '上海', '高档型', 212, 4.7, '大宁国际');
INSERT INTO `hotel_all` VALUES (9, '锦江都城酒店(上海徐家汇南华亭宾馆)', '上海', '上海', '高档型', 221, 4.5, '徐家汇');
INSERT INTO `hotel_all` VALUES (10, '锦江都城酒店(上海市北店)', '上海', '上海', '高档型', 142, 4.6, '大宁国际');
INSERT INTO `hotel_all` VALUES (11, '维也纳国际酒店(上海虹桥枢纽青浦地铁站店)', '上海', '上海', '舒适型', 250, 4.8, '青浦城区');
INSERT INTO `hotel_all` VALUES (12, '美豪酒店(上海长寿路店)', '上海', '上海', '高档型', 258, 4.6, '中山公园');
INSERT INTO `hotel_all` VALUES (13, '云和夜泊酒店(上海浦东国际机场店)', '上海', '上海', '高档型', 143, 4.9, '迪士尼|浦东机场核心');
INSERT INTO `hotel_all` VALUES (14, '沪华国际大酒店(上海松江店)', '上海', '上海', '高档型', 192, 4.6, '佘山/松江大学城');
INSERT INTO `hotel_all` VALUES (15, '桔子酒店·精选(上海浦东机场店)', '上海', '上海', '高档型', 141, 4.7, '浦东机场核心');
INSERT INTO `hotel_all` VALUES (16, '北上海大酒店', '上海', '上海', '豪华型', 165, 4.5, '大宁国际');
INSERT INTO `hotel_all` VALUES (17, '麦新格精品酒店(上海东方明珠店)', '上海', '上海', '高档型', 85, 4.9, '新国际博览中心|陆家嘴');
INSERT INTO `hotel_all` VALUES (18, '上海体院体育交流中心', '上海', '上海', '高档型', 176, 4.6, '江湾/五角场');
INSERT INTO `hotel_all` VALUES (19, '上海鲁能JW万豪侯爵酒店', '上海', '上海', '豪华型', 510, 4.6, '陆家嘴');
INSERT INTO `hotel_all` VALUES (20, '上海新世界丽笙大酒店', '上海', '上海', '五星级', 520, 4.5, '人民广场');
INSERT INTO `hotel_all` VALUES (21, '维也纳酒店(上海浦东机场店)', '上海', '上海', '高档型', 236, 4.6, '迪士尼|浦东机场核心');
INSERT INTO `hotel_all` VALUES (22, '维也纳国际酒店(上海浦东机场自贸区店)', '上海', '上海', '高档型', 151, 4.7, '浦东机场核心');
INSERT INTO `hotel_all` VALUES (23, '宿适轻奢酒店(上海长寿路地铁站店)', '上海', '上海', '高档型', 85, 4.5, '长寿路');
INSERT INTO `hotel_all` VALUES (24, '上海金桥中心智选假日酒店', '上海', '上海', '舒适型', 192, 4.7, '浦东金桥');
INSERT INTO `hotel_all` VALUES (25, '沪华云清逸湾酒店(上海国际旅游度假区店)', '上海', '上海', '高档型', 123, 4.8, '南汇/野生动物园');
INSERT INTO `hotel_all` VALUES (26, '上海唐镇智选假日酒店', '上海', '上海', '舒适型', 233, 4.7, '迪士尼');
INSERT INTO `hotel_all` VALUES (27, '上海绿瘦酒店', '上海', '上海', '五星级', 265, 4.7, '七宝');
INSERT INTO `hotel_all` VALUES (28, '锦江都城经典酒店(上海南京路步行街南京饭店 )', '上海', '上海', '高档型', 169, 4.7, '人民广场');
INSERT INTO `hotel_all` VALUES (29, '景莱酒店·臻选(上海徐家汇交大店)', '上海', '上海', '高档型', 143, 4.6, '徐家汇');
INSERT INTO `hotel_all` VALUES (30, '桔子水晶上海外滩金陵东路酒店', '上海', '上海', '高档型', 170, 4.8, '外滩|淮海路/新天地');
INSERT INTO `hotel_all` VALUES (31, '上海陆家嘴万信酒店', '上海', '上海', '高档型', 216, 4.6, '陆家嘴');
INSERT INTO `hotel_all` VALUES (32, '美豪丽致酒店(上海交大东川路店)', '上海', '上海', '高档型', 108, 4.7, '交大/闵行开发区');
INSERT INTO `hotel_all` VALUES (33, '上海国际旅游度假区万怡酒店', '上海', '上海', '高档型', 355, 4.5, '迪士尼');
INSERT INTO `hotel_all` VALUES (34, '丽柏酒店(上海武宁路店)', '上海', '上海', '舒适型', 164, 4.9, '长风公园');
INSERT INTO `hotel_all` VALUES (35, '和颐至尊酒店(上海南京路步行街店)', '上海', '上海', '高档型', 188, 4.6, '人民广场|静安寺/南京西路');
INSERT INTO `hotel_all` VALUES (36, '上海协信莎玛长风服务式公寓', '上海', '上海', '高档型', 404, 4.7, '长风公园');
INSERT INTO `hotel_all` VALUES (37, '上海国际饭店', '上海', '上海', '四星级', 261, 4.4, '人民广场');
INSERT INTO `hotel_all` VALUES (38, '白玉兰酒店(上海新天地店)', '上海', '上海', '舒适型', 114, 4.7, '打浦桥');

SET FOREIGN_KEY_CHECKS = 1;
