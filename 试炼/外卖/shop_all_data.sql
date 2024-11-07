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

 Date: 10/11/2023 11:50:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for shop_all
-- ----------------------------
DROP TABLE IF EXISTS `shop_all`;
CREATE TABLE `shop_all`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商铺名称',
  `city` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '城市',
  `location` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商圈',
  `longtitude` double NULL DEFAULT NULL COMMENT '经度',
  `latitude` double NULL DEFAULT NULL COMMENT '纬度',
  `shop_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商铺类型',
  `pay_cnt` bigint(20) NULL DEFAULT NULL COMMENT '订单数',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 51 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shop_all
-- ----------------------------
INSERT INTO `shop_all` VALUES (1, ' 尚东便利店', ' 盐城市', ' 建湖县秀夫南路书香苑1幢110室，7天酒店', 119.888045, 33.515936, 'A', 747);
INSERT INTO `shop_all` VALUES (2, ' 冻吃冷食（梦想城店）', ' 菏泽市', ' 山东省菏泽市鄄城县舜耕路与运河街交叉口向东300米路南菜篮子超级市场25号', 115.560342, 35.518051, 'A', 671);
INSERT INTO `shop_all` VALUES (3, ' 福贵烧烤', ' 台州市', ' 解放北路118号', 121.43856, 28.67979, 'A', 492);
INSERT INTO `shop_all` VALUES (4, ' 冻吃冷食（梦想城店）', ' 菏泽市', ' 山东省菏泽市鄄城县舜耕路与运河街交叉口向东300米路南菜篮子超级市场25号', 115.560342, 35.518051, 'A', 671);
INSERT INTO `shop_all` VALUES (5, ' 御喜玛蛋糕', ' 常州市', ' 天宁区茶山街道光华世家19-14号', 119.971325, 31.760784, 'A', 550);
INSERT INTO `shop_all` VALUES (6, ' 爱芙园（摩尔店）', ' 广安市', ' 广安市广安区滨河路一段国际商业中心97号，98号', 106.631565, 30.45434, 'A', 874);
INSERT INTO `shop_all` VALUES (7, ' 冻吃冷食（梦想城店）', ' 菏泽市', ' 山东省菏泽市鄄城县舜耕路与运河街交叉口向东300米路南菜篮子超级市场25号', 115.560342, 35.518051, 'A', 671);
INSERT INTO `shop_all` VALUES (8, ' 爱牛杂', ' 南宁市', ' 隆安城厢镇城内街878号', 107.691627, 23.173789, 'A', 259);
INSERT INTO `shop_all` VALUES (9, ' 冻吃冷食（梦想城店）', ' 菏泽市', ' 山东省菏泽市鄄城县舜耕路与运河街交叉口向东300米路南菜篮子超级市场25号', 115.560342, 35.518051, 'A', 671);
INSERT INTO `shop_all` VALUES (10, ' 镖师红糖馒头（射阳店）', ' 盐城市', ' 射阳县合德镇双拥路95号由南向北第四间门市', 120.26509, 33.76999, 'A', 185);
INSERT INTO `shop_all` VALUES (11, ' 尚一品炸鸡', ' 十堰市', ' 城关镇人民路（城西村99号103号）', 110.225616, 32.228175, 'A', 847);
INSERT INTO `shop_all` VALUES (12, ' 宠乐屋', ' 东莞市', ' 广州市增城区新塘镇东街道居委会石新大道88号', 113.689157, 23.152139, 'A', 700);
INSERT INTO `shop_all` VALUES (13, ' 德克士（定西半岛店）-清真', ' 定西市', ' 甘肃省定西市安定区中华路街道办友谊北路半岛广场一层', 104.617487, 35.582796, 'A', 867);
INSERT INTO `shop_all` VALUES (14, ' 尚一品炸鸡', ' 十堰市', ' 城关镇人民路（城西村99号103号）', 110.225616, 32.228175, 'A', 847);
INSERT INTO `shop_all` VALUES (15, ' 东北特色小吃', ' 定西市', ' 甘肃省定西市渭源县清源镇平桥路西侧粮食贸易楼15号商铺', 104.212697, 35.13288, 'A', 117);
INSERT INTO `shop_all` VALUES (16, ' 一日三餐煎肉饭', ' 天津市', ' 天津市津南区咸水沽镇体育场路东侧，津沽路北侧惠安花园13-07一层', 117.38991, 38.989377, 'A', 467);
INSERT INTO `shop_all` VALUES (17, ' 河风精致寿司', ' 苏州市', ' 苏州工业园区尼盛广场F202a', 120.60855, 31.373326, 'A', 817);
INSERT INTO `shop_all` VALUES (18, ' 尚一品炸鸡', ' 十堰市', ' 城关镇人民路（城西村99号103号）', 110.225616, 32.228175, 'A', 847);
INSERT INTO `shop_all` VALUES (19, ' 神威大药房圣诺十五店', ' 石家庄市', ' 石家庄市新华区和平路561号', 114.454538, 38.103462, 'A', 637);
INSERT INTO `shop_all` VALUES (20, ' 聚一聚菜馆（青海东路店）', ' 上海市', ' 海门经济技术开发区通源新村807幢106号（苏洪鲜食对面）', 121.191459, 31.898365, 'A', 376);
INSERT INTO `shop_all` VALUES (21, ' 桥头排骨', ' 哈尔滨市', ' 方正县方正镇城北新区博汇商服二号楼一层北数第40门（门洞南侧北数第17屋）T40', 128.831279, 45.845872, 'A', 423);
INSERT INTO `shop_all` VALUES (22, ' 甘雨亭（工农兵大道店）', ' 吉安市', ' 澄江镇工农兵大道水电公司旁', 114.888483, 26.792531, 'A', 704);
INSERT INTO `shop_all` VALUES (23, ' 屈臣氏（新都会广场店）', ' 合肥市', ' 安徽省合肥市马鞍山南路100号新都会环球广场1层', 117.323779, 31.87103, 'A', 188);
INSERT INTO `shop_all` VALUES (24, ' 广州美佳香食品', ' 东莞市', ' 广州市南沙区东涌镇三沙村三沙公路11号4号铺', 113.554799, 22.933029, 'A', 180);
INSERT INTO `shop_all` VALUES (25, ' 爱花居鲜花（金卉花园店）', ' 赣州市', ' 赣州市于都县贡江镇古田塘尾', 115.433535, 25.960573, 'B', 141);
INSERT INTO `shop_all` VALUES (26, ' RoyBlteB皇茶（广厦店）', ' 哈尔滨市', ' 哈尔滨市利民开发区学院路泓林金色地标12号楼1号商服', 126.508006, 45.91907, 'B', 598);
INSERT INTO `shop_all` VALUES (27, ' ?客莱黄焖鸡米饭&木桶饭（禾盛广场店）', ' 苏州市', ' 常熟市辛庄镇新阳大道80号禾盛商业广场3幢118', 120.680701, 31.537706, 'B', 994);
INSERT INTO `shop_all` VALUES (28, ' 克洛里斯花店（生日花，鲜花，绿植）', ' 盐城市', ' 东台市新街镇九总村一组34号', 120.858684, 32.645386, 'B', 296);
INSERT INTO `shop_all` VALUES (29, ' H100 BBKERY（九御皇城店）', ' 孝感市', ' 仙女山街道办事处九御皇城S1-3号', 113.824223, 30.65666, 'B', 378);
INSERT INTO `shop_all` VALUES (30, ' 美味阁过桥米线黄焖鸡米饭（圩塘店）', ' 常州市', ' 春江镇圩塘新业街33', 119.994394, 31.942961, 'B', 527);
INSERT INTO `shop_all` VALUES (31, ' 陕北味道（金泽店）', ' 延安市', ' 东关街24号', 109.495758, 36.599807, 'B', 673);
INSERT INTO `shop_all` VALUES (32, ' 老兵烧烤', ' 宁波市', ' 浙江省慈溪市逍林镇新园村逍林大道58号', 121.314001, 30.160072, 'B', 998);
INSERT INTO `shop_all` VALUES (33, ' 疯狂炸串店', ' 南京市', ' 南京市栖霞区迈皋桥街道寅春农贸市场', 118.837394, 32.12511, 'B', 315);
INSERT INTO `shop_all` VALUES (34, ' 米图花厨（常州店）', ' 常州市', ' 清潭路93号国光?1937科技文化创意园（中天钢铁体育馆）', 119.941602, 31.767388, 'B', 355);
INSERT INTO `shop_all` VALUES (35, ' 川渝骨汤冒菜', ' 巴中市', ' 四川省巴中市平昌县金宝新区御江名门4栋1-4号', 107.086105, 31.575311, 'B', 877);
INSERT INTO `shop_all` VALUES (36, ' 佳和超市', ' 唐山市', ' 丰润区祥润底商20号', 118.10387, 39.732035, 'B', 141);
INSERT INTO `shop_all` VALUES (37, ' 九二九精酿鲜啤', ' 南京市', ' 南京市江北新区泰山街道天华南路5号天润城第十六街区商业2幢103室', 118.640486, 32.251633, 'B', 991);
INSERT INTO `shop_all` VALUES (38, ' 重庆小面（春晓店）', ' 宁波市', ' 北仑区春晓洋沙山路80-1号4幢80-1号', 121.902708, 29.759695, 'A', 187);
INSERT INTO `shop_all` VALUES (39, ' 星巴克咖啡代购（滨湖万达茂商圈店）', ' 合肥市', ' 安徽省合肥市包河区庐州大道商圈', 117.195536, 31.674731, 'A', 831);
INSERT INTO `shop_all` VALUES (40, ' 诚记甜品（常熟万达店）', ' 苏州市', ' 珠海路8号万达广场3030A', 120.837806, 31.56396, 'A', 974);
INSERT INTO `shop_all` VALUES (41, ' 福建特色小吃', ' 宁波市', ' 奉化市江口街道方桥新建东路6号', 121.456682, 29.758052, 'A', 537);
INSERT INTO `shop_all` VALUES (42, ' 过桥米线（开关厂店）', ' 南昌市', ' 南昌市新建区长?镇长征西路637号中国联通西北80米', 115.876804, 28.690419, 'A', 710);
INSERT INTO `shop_all` VALUES (43, ' 南昌喜来登酒店', ' 南昌市', ' 江西省南昌市红谷滩新区红谷中大道1669号', 115.859297, 28.700795, 'A', 302);
INSERT INTO `shop_all` VALUES (44, ' 过桥米线（开关厂店）', ' 南昌市', ' 南昌市新建区长?镇长征西路637号中国联通西北80米', 115.876804, 28.690419, 'A', 710);
INSERT INTO `shop_all` VALUES (45, ' 茶巢（龙湖医学院店）', ' 厦门市', ' 厦门市集美区灌口镇鱼福三里98号', 118.118397, 24.519161, 'A', 457);
INSERT INTO `shop_all` VALUES (46, ' 伴青半茶', ' 苏州市', ' 昆山市玉山镇城北娄苑路194号', 120.937633, 31.366936, 'A', 442);
INSERT INTO `shop_all` VALUES (47, ' 过桥米线（开关厂店）', ' 南昌市', ' 南昌市新建区长?镇长征西路637号中国联通西北80米', 115.876804, 28.690419, 'A', 710);
INSERT INTO `shop_all` VALUES (48, ' 1919酒类直供（梦时代店）', ' 南昌市', ' 江西省南昌市青山湖区北京东路308号恒茂国际都会商业?A107、B107室', 116.018716, 28.597294, 'A', 670);
INSERT INTO `shop_all` VALUES (49, ' 过桥米线（开关厂店）', ' 南昌市', ' 南昌市新建区长?镇长征西路637号中国联通西北80米', 115.876804, 28.690419, 'A', 710);
INSERT INTO `shop_all` VALUES (50, ' 尚德快新浏阳菜馆', ' 宜春市', ' 上塘镇矿务局梅苑小区', 115.746779, 28.29246, 'A', 426);

SET FOREIGN_KEY_CHECKS = 1;
