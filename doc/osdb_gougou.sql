/*
 Navicat MySQL Data Transfer

 Source Server         : GouGou
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : osdb

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 11/04/2023 18:35:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for batching
-- ----------------------------
DROP TABLE IF EXISTS `batching`;
CREATE TABLE `batching`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '配料id',
  `cover_pic` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '配料图片',
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '配料名称',
  `price` double(6, 2) UNSIGNED NOT NULL DEFAULT 0.00 COMMENT '无符号',
  `status` tinyint(1) NULL DEFAULT 1 COMMENT '1:正常  2:停售  9:删除',
  `create_at` datetime(0) NULL DEFAULT NULL,
  `update_at` datetime(0) NULL DEFAULT NULL,
  `radio` tinyint(1) NOT NULL DEFAULT 0 COMMENT '0:可多选 1:单选',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of batching
-- ----------------------------
INSERT INTO `batching` VALUES (1, '', '珍珠', 2.00, 1, '2023-04-11 13:03:07', '2023-04-11 13:04:07', 0);
INSERT INTO `batching` VALUES (2, NULL, '芋圆', 2.00, 1, '2023-04-11 13:03:56', NULL, 0);
INSERT INTO `batching` VALUES (3, NULL, '椰果', 2.00, 1, '2023-04-11 13:04:24', NULL, 0);
INSERT INTO `batching` VALUES (4, NULL, '多肉', 2.00, 1, '2023-04-11 13:04:39', NULL, 0);
INSERT INTO `batching` VALUES (5, NULL, '西米', 2.00, 1, '2023-04-11 13:05:08', NULL, 0);
INSERT INTO `batching` VALUES (6, NULL, '红豆', 2.00, 1, '2023-04-11 13:05:25', NULL, 0);
INSERT INTO `batching` VALUES (7, NULL, '全糖', 0.00, 1, '2023-04-11 13:06:09', NULL, 1);
INSERT INTO `batching` VALUES (8, NULL, '七分糖', 0.00, 1, '2023-04-11 13:06:21', NULL, 1);
INSERT INTO `batching` VALUES (9, NULL, '五分糖', 0.00, 1, '2023-04-11 13:06:37', NULL, 1);
INSERT INTO `batching` VALUES (10, NULL, '三分糖', 0.00, 1, '2023-04-11 13:07:01', NULL, 1);
INSERT INTO `batching` VALUES (11, NULL, '无糖（不额外加糖）', 0.00, 1, '2023-04-11 13:07:30', NULL, 1);

-- ----------------------------
-- Table structure for batching_detail
-- ----------------------------
DROP TABLE IF EXISTS `batching_detail`;
CREATE TABLE `batching_detail`  (
  `id` int(0) NOT NULL COMMENT '主键、自增、无符号',
  `batching_id` int(0) UNSIGNED NOT NULL,
  `order_d_id` int(0) UNSIGNED NOT NULL,
  `product_id` int(0) UNSIGNED NOT NULL,
  `batching_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `batching_price` double(6, 2) UNSIGNED NULL DEFAULT NULL COMMENT '无符号',
  `quantity` int(0) UNSIGNED NULL DEFAULT 1 COMMENT '无符号',
  `status` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1:正常  9:删除',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `orderid`(`order_d_id`) USING BTREE,
  INDEX `productid`(`product_id`) USING BTREE,
  INDEX `batchid`(`batching_id`) USING BTREE,
  CONSTRAINT `orderid` FOREIGN KEY (`order_d_id`) REFERENCES `order_detail` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `productid` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `batchid` FOREIGN KEY (`batching_id`) REFERENCES `batching` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of batching_detail
-- ----------------------------
INSERT INTO `batching_detail` VALUES (1, 1, 36, 20, '珍珠', 2.00, 2, 1);
INSERT INTO `batching_detail` VALUES (2, 10, 36, 20, '三分糖', 0.00, 1, 1);

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '菜品分类id',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '分类名称',
  `status` tinyint(0) NOT NULL DEFAULT 1 COMMENT '状态：1正常 9删除',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES (1, '双拼套餐', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (2, '盖饭', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (3, '小菜', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (4, '汤/饮料', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (5, '双拼套餐', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (6, '盖饭', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (7, '小菜', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (8, '汤/饮料', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (9, '盖饭', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (10, '双拼套餐', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (11, '小炒', 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `category` VALUES (12, '奶茶', 1, '2023-04-11 13:17:33', '2023-04-11 13:17:35');
INSERT INTO `category` VALUES (13, '果茶', 1, '2023-04-11 13:17:47', '2023-04-11 13:17:49');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '会员表id',
  `nickname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '昵称',
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像',
  `mobile` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '电话',
  `level` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1:普通客户 2:月卡用户  ',
  `expiration_at` datetime(0) NULL DEFAULT NULL,
  `credit` int(0) NULL DEFAULT NULL,
  `status` tinyint(0) UNSIGNED NOT NULL DEFAULT 1 COMMENT '状态:1正常/2禁用/9删除',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member
-- ----------------------------
INSERT INTO `member` VALUES (1, 'lixiaofeng', 'moren.png', '11234567899', 1, NULL, NULL, 9, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (2, 'jack', 'moren.png', '12345678965', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (3, 'wo879', 'moren.png', '13456789522', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (4, 'mt100', 'moren.png', '13567895563', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (5, '顾客', 'moren.png', '12345678901', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (6, '顾客', 'moren.png', '12345678902', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (7, '顾客', 'moren.png', '12345678903', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (8, '顾客', 'moren.png', '12345678904', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (9, '顾客', 'moren.png', '12345678905', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (10, '顾客', 'moren.png', '12345678906', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (11, '顾客', 'moren.png', '12345678909', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (12, '顾客', 'moren.png', '18642805564', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (13, '顾客', 'moren.png', '13116051729', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (14, '顾客', 'moren.png', '13161485799', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (15, '顾客', 'moren.png', '11234567888', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `member` VALUES (16, '顾客', 'moren.png', '19919940344', 1, NULL, NULL, 1, '2020-07-25 10:20:30', '2020-07-25 10:20:30');

-- ----------------------------
-- Table structure for migrations
-- ----------------------------
DROP TABLE IF EXISTS `migrations`;
CREATE TABLE `migrations`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT,
  `migration` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for order_detail
-- ----------------------------
DROP TABLE IF EXISTS `order_detail`;
CREATE TABLE `order_detail`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '订单详情id',
  `order_id` int(0) UNSIGNED NOT NULL COMMENT '订单id',
  `product_id` int(0) UNSIGNED NOT NULL COMMENT '菜品id',
  `product_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '菜品名称',
  `price` double(6, 2) UNSIGNED NULL DEFAULT NULL COMMENT '单价',
  `quantity` int(0) UNSIGNED NOT NULL DEFAULT 1 COMMENT '数量',
  `status` tinyint(0) UNSIGNED NOT NULL DEFAULT 1 COMMENT '状态:1正常/9删除',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `orderid_od`(`order_id`) USING BTREE,
  INDEX `productid_od`(`product_id`) USING BTREE,
  CONSTRAINT `orderid_od` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `productid_od` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 36 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '订单详情信息表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_detail
-- ----------------------------
INSERT INTO `order_detail` VALUES (1, 4, 1, '红烧肉+狮子头+饮料', 25.00, 1, 1);
INSERT INTO `order_detail` VALUES (2, 4, 2, '红烧肉+番茄鸡蛋', 22.00, 1, 1);
INSERT INTO `order_detail` VALUES (3, 4, 7, '肥牛饭', 19.00, 1, 1);
INSERT INTO `order_detail` VALUES (4, 5, 1, '红烧肉+狮子头+饮料', 25.00, 1, 1);
INSERT INTO `order_detail` VALUES (5, 6, 3, '梅菜扣肉+番茄鸡蛋', 22.00, 1, 1);
INSERT INTO `order_detail` VALUES (6, 6, 12, '单份香辣笋干烧肉', 15.00, 1, 1);
INSERT INTO `order_detail` VALUES (7, 6, 13, '番茄蛋花汤', 4.00, 1, 1);
INSERT INTO `order_detail` VALUES (8, 7, 2, '红烧肉+番茄鸡蛋', 22.00, 1, 1);
INSERT INTO `order_detail` VALUES (9, 7, 6, '木须肉饭', 16.00, 2, 1);
INSERT INTO `order_detail` VALUES (10, 7, 14, '王老吉', 6.00, 1, 1);
INSERT INTO `order_detail` VALUES (11, 7, 11, '菜心', 6.00, 1, 1);
INSERT INTO `order_detail` VALUES (12, 8, 2, '红烧肉+番茄鸡蛋', 22.00, 1, 1);
INSERT INTO `order_detail` VALUES (13, 8, 5, '梅菜扣肉饭', 19.00, 1, 1);
INSERT INTO `order_detail` VALUES (14, 9, 1, '红烧肉+狮子头+饮料', 25.00, 1, 1);
INSERT INTO `order_detail` VALUES (15, 9, 13, '番茄蛋花汤', 4.00, 1, 1);
INSERT INTO `order_detail` VALUES (16, 10, 1, '红烧肉+狮子头+饮料', 25.00, 1, 1);
INSERT INTO `order_detail` VALUES (17, 10, 2, '红烧肉+番茄鸡蛋', 22.00, 1, 1);
INSERT INTO `order_detail` VALUES (18, 11, 1, '红烧肉+狮子头+饮料', 25.00, 1, 1);
INSERT INTO `order_detail` VALUES (19, 11, 2, '红烧肉+番茄鸡蛋', 22.00, 2, 1);
INSERT INTO `order_detail` VALUES (20, 11, 12, '单份香辣笋干烧肉', 15.00, 1, 1);
INSERT INTO `order_detail` VALUES (21, 11, 13, '番茄蛋花汤', 4.00, 1, 1);
INSERT INTO `order_detail` VALUES (22, 12, 1, '红烧肉+狮子头+饮料', 25.00, 1, 1);
INSERT INTO `order_detail` VALUES (23, 12, 6, '木须肉饭', 16.00, 2, 1);
INSERT INTO `order_detail` VALUES (24, 12, 13, '番茄蛋花汤', 4.00, 1, 1);
INSERT INTO `order_detail` VALUES (25, 13, 1, '红烧肉+狮子头+饮料', 25.00, 2, 1);
INSERT INTO `order_detail` VALUES (26, 13, 6, '木须肉饭', 16.00, 1, 1);
INSERT INTO `order_detail` VALUES (27, 13, 9, '单个肉丸子', 4.00, 2, 1);
INSERT INTO `order_detail` VALUES (28, 13, 14, '王老吉', 6.00, 1, 1);
INSERT INTO `order_detail` VALUES (29, 14, 1, '红烧肉+狮子头+饮料', 25.00, 5, 1);
INSERT INTO `order_detail` VALUES (30, 14, 2, '红烧肉+番茄鸡蛋', 22.00, 7, 1);
INSERT INTO `order_detail` VALUES (31, 14, 6, '木须肉饭', 16.00, 1, 1);
INSERT INTO `order_detail` VALUES (32, 15, 14, '王老吉', 6.00, 2, 1);
INSERT INTO `order_detail` VALUES (33, 15, 9, '木须肉', 12.00, 1, 1);
INSERT INTO `order_detail` VALUES (34, 15, 3, '梅菜扣肉+番茄鸡蛋', 22.00, 1, 1);
INSERT INTO `order_detail` VALUES (35, 15, 6, '木须肉饭', 16.00, 1, 1);
INSERT INTO `order_detail` VALUES (36, 16, 20, '珍珠奶茶', 16.00, 1, 1);

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '订单表id',
  `member_id` int(0) UNSIGNED NULL DEFAULT NULL COMMENT '会员id',
  `user_id` int(0) UNSIGNED NULL DEFAULT NULL COMMENT '操作员id',
  `money` double(8, 2) NULL DEFAULT NULL COMMENT '金额',
  `status` tinyint(0) UNSIGNED NULL DEFAULT NULL COMMENT '订单状态:1过行中/2无效/3已完成',
  `payment_status` tinyint(0) UNSIGNED NULL DEFAULT NULL COMMENT '支付状态:1未支付/2已支付/3已退款',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES (4, 0, 1, 66.00, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (5, 0, 1, 25.00, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (6, 0, 3, 41.00, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (7, 0, 1, 66.00, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (8, 0, 1, 41.00, 1, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (9, 0, 1, 29.00, 2, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (10, 0, 1, 47.00, 1, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (11, 0, 1, 88.00, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (12, 0, 1, 61.00, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (13, 0, 1, 80.00, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (14, 0, 2, 295.00, 2, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (15, 0, 2, 62.00, 1, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `orders` VALUES (16, 0, 1, 20.00, 1, 2, '2023-04-11 13:15:39', '2023-04-11 13:15:34');

-- ----------------------------
-- Table structure for payment
-- ----------------------------
DROP TABLE IF EXISTS `payment`;
CREATE TABLE `payment`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '支付表id',
  `order_id` int(0) UNSIGNED NOT NULL COMMENT '订单id',
  `member_id` int(0) UNSIGNED NOT NULL COMMENT '会员id',
  `money` double(8, 2) UNSIGNED NULL DEFAULT NULL COMMENT '支付金额',
  `type` tinyint(0) UNSIGNED NULL DEFAULT NULL COMMENT '付款方式：1会员付款/2收银收款',
  `bank` tinyint(0) UNSIGNED NULL DEFAULT NULL COMMENT '收款银行渠道:1微信/2余额/3现金/4支付宝',
  `status` tinyint(0) UNSIGNED NULL DEFAULT NULL COMMENT '支付状态:1未支付/2已支付/3已退款',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `orderid_p`(`order_id`) USING BTREE,
  CONSTRAINT `orderid_p` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of payment
-- ----------------------------
INSERT INTO `payment` VALUES (2, 4, 0, 66.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (3, 5, 0, 25.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (4, 6, 0, 41.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (5, 7, 0, 66.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (6, 8, 0, 41.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (7, 9, 0, 29.00, 2, 1, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (8, 10, 0, 47.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (9, 11, 0, 88.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (10, 12, 0, 61.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (11, 13, 0, 80.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (12, 14, 0, 295.00, 2, 4, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');
INSERT INTO `payment` VALUES (13, 15, 0, 62.00, 2, 3, 2, '2020-07-25 10:20:30', '2020-07-25 10:20:30');

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '菜品id',
  `category_id` int(0) UNSIGNED NOT NULL COMMENT '菜品分类id',
  `cover_pic` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '菜品图片',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '菜品名称',
  `price` double(6, 2) UNSIGNED NOT NULL COMMENT '单价',
  `status` tinyint(0) NOT NULL COMMENT '状态：1:正常  2:停售  9:删除',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cateid`(`category_id`) USING BTREE,
  CONSTRAINT `cateid` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (1, 1, '1536657620.5485704.jpg', '红烧肉+狮子头+饮料', 25.00, 1, '2020-07-11 09:20:20', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (2, 1, '1536658352.9341557.jpg', '红烧肉+番茄鸡蛋', 22.00, 1, '2020-07-11 09:32:32', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (3, 1, '1536658415.6838002.jpg', '梅菜扣肉+番茄鸡蛋', 22.00, 1, '2020-07-11 09:33:35', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (4, 1, '1536658574.2847373.jpg', '肥牛+番茄鸡蛋', 22.00, 1, '2020-07-11 09:36:14', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (5, 2, '1536658659.0446993.jpg', '梅菜扣肉饭', 19.00, 1, '2020-07-11 09:37:39', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (6, 2, '1536658824.3976505.jpg', '木须肉饭', 16.00, 1, '2020-07-11 09:40:24', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (7, 2, '1536658863.6732855.jpg', '肥牛饭', 19.00, 1, '2020-07-11 09:41:03', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (8, 2, '1536658960.3954134.jpg', '无骨咖喱鸡饭', 18.00, 1, '2020-07-11 09:42:40', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (9, 3, '1536659114.0440235.jpg', '木须肉', 12.00, 1, '2020-07-11 09:44:25', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (10, 3, '1536659065.7972637.jpg', '番茄鸡蛋', 4.00, 1, '2020-07-11 09:45:14', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (11, 3, '1536659197.7231221.jpg', '青菜', 4.00, 1, '2020-07-11 09:46:37', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (12, 3, '1536659253.8842716.jpg', '单份香辣笋干烧肉', 15.00, 1, '2020-07-11 09:47:33', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (13, 4, '1536659311.8699493.jpg', '番茄蛋花汤', 4.00, 1, '2020-07-11 09:48:31', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (14, 4, '1536659364.7892513.jpg', '王老吉', 6.00, 1, '2020-07-11 09:49:24', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (15, 4, '1536659563.3897648.jpg', '果粒橙', 5.00, 1, '2020-07-11 09:52:43', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (16, 4, '1536659605.5561771.jpg', '矿泉水', 3.00, 1, '2020-07-11 09:53:25', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (17, 4, '1536659688.4856157.jpg', '乌梅汁', 4.00, 1, '2020-07-11 09:54:48', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (18, 7, '1536659065.7972636.jpg', '番茄鸡蛋', 4.00, 1, '2020-07-04 06:17:18', '2020-07-25 10:20:30');
INSERT INTO `product` VALUES (19, 10, '1536658666.8341557.jpg', '红烧肉+西红柿鸡蛋', 24.00, 1, '2020-07-06 08:46:28', '2020-07-25 07:34:07');
INSERT INTO `product` VALUES (20, 12, NULL, '珍珠奶茶', 16.00, 1, '2023-04-11 13:18:56', '2023-04-11 13:18:59');
INSERT INTO `product` VALUES (21, 12, NULL, '杨枝甘露', 18.00, 1, '2023-04-11 13:19:24', '2023-04-11 13:19:25');
INSERT INTO `product` VALUES (22, 13, NULL, '冰鲜柠檬水', 4.00, 1, '2023-04-11 13:19:56', '2023-04-11 13:19:58');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '员工账号id',
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '员工账号',
  `nickname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '昵称',
  `password_hash` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码',
  `password_salt` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码干扰值',
  `status` tinyint(0) UNSIGNED NOT NULL DEFAULT 1 COMMENT '状态:1正常/2禁用/9删除',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'zhangsan', '张三', '1e191d851b3b49a248f4ea62f6b06410', '123456', 6, '2020-07-08 18:18:18', '2020-07-22 08:06:55');
INSERT INTO `user` VALUES (2, 'lisi', '李四', '1e191d851b3b49a248f4ea62f6b06410', '123456', 1, '2020-07-18 08:08:18', '2020-07-22 16:21:18');
INSERT INTO `user` VALUES (3, 'xiaoli', '小李子', 'c8a7ca8b274f29cf2c1147a8e0f685a4', '639776', 6, '2020-07-07 07:53:57', '2020-07-08 20:18:18');
INSERT INTO `user` VALUES (4, 'zhangwuji', '张无忌', 'cbb748964d243e38f032b78886db824c', '437809', 9, '2020-02-18 09:06:54', '2020-01-14 03:36:25');
INSERT INTO `user` VALUES (5, 'zhaomin', '赵敏', '27c744b428b997675c4383e7eae974c3', '486570', 2, '2020-02-18 09:07:40', '2020-02-18 09:07:40');
INSERT INTO `user` VALUES (6, 'cuihua', '翠花', 'b5a7379148116549de083f5076233bef', '810418', 2, '2020-02-18 09:08:35', '2020-03-08 20:18:09');
INSERT INTO `user` VALUES (7, 'zhangle', '张乐', '7177bd35ad232f0830fe5c10dcc24b1c', '350013', 2, '2020-02-19 06:11:16', '2020-02-19 12:33:19');
INSERT INTO `user` VALUES (8, 'uu01', '小优', 'a0811c52452216c63e52da04337e9216', '268818', 1, '2020-01-03 10:27:04', '2020-01-03 10:27:04');
INSERT INTO `user` VALUES (9, 'uu02', '小优2', '56322ead3e2371636ac2395c8399297f', '112245', 1, '2020-01-03 10:37:37', '2020-01-03 10:37:37');
INSERT INTO `user` VALUES (10, 'uu03', '小优3', '8e7d0c4077c73ad60c23367625d4346f', '238764', 1, '2020-01-03 11:24:48', '2020-01-03 11:24:48');
INSERT INTO `user` VALUES (11, 'uu04', '小优4', '5eec167b09ea13497843274969460d67', '642960', 1, '2020-01-03 11:27:00', '2020-01-03 11:27:00');
INSERT INTO `user` VALUES (12, 'uu123', '小优', '5c2e9f69b05413b806dc6951b0f86e51', '102905', 1, '2020-01-13 23:51:01', '2020-01-13 23:51:01');
INSERT INTO `user` VALUES (13, 'uu666', '小优3', '99e89e8245d9f6f0628b5a59299bd9f7', '673778', 1, '2020-01-13 23:52:13', '2020-01-13 23:52:13');
INSERT INTO `user` VALUES (14, 'mm', '小美', '05775bb481d11f0648b158cd40a7929c', '627985', 1, '2020-01-14 01:25:57', '2020-01-14 01:25:57');

SET FOREIGN_KEY_CHECKS = 1;
