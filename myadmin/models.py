from datetime import datetime

from django.db import models

# Create your models here.

"""
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
"""
#员工账号信息模型
class User(models.Model):
    username = models.CharField(max_length=50)    #员工账号
    nickname = models.CharField(max_length=50)    #昵称
    password_hash = models.CharField(max_length=100)#密码
    password_salt = models.CharField(max_length=50)    #密码干扰值
    status = models.IntegerField(default=1)    #状态:1正常/2禁用/6管理员/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间


    def toDict(self):
        return {'id':self.id,'username':self.username,'nickname':self.nickname,'password_hash':self.password_hash,'password_salt':self.password_salt,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "user"  # 更改表名


"""
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category`  (
  `id` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '菜品分类id',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '分类名称',
  `status` tinyint(0) NOT NULL DEFAULT 1 COMMENT '状态：1正常 9删除',
  `create_at` datetime(0) NULL DEFAULT NULL COMMENT '添加时间',
  `update_at` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;


"""

#菜品分类信息模型
class Category(models.Model):
    # shop_id = models.IntegerField()        #店铺id

    name = models.CharField(max_length=50)#分类名称
    status = models.IntegerField(default=1)        #状态:1正常/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    class Meta:
        db_table = "category"  # 更改表名




#菜品信息模型
class Product(models.Model):
    # shop_id = models.IntegerField()        #店铺id
    category_id = models.IntegerField()    #菜品分类id
    cover_pic = models.CharField(max_length=50)    #菜品图片
    name = models.CharField(max_length=50)#菜品名称
    price = models.FloatField()    #菜品单价
    status = models.IntegerField(default=1)        #状态:1正常/2停售/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'category_id':self.category_id,'cover_pic':self.cover_pic,'name':self.name,'price':self.price,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "product"  # 更改表名


"""
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
"""
#会员信息模型
class Member(models.Model):
    nickname = models.CharField(max_length=50)    #昵称
    avatar = models.CharField(max_length=255)    #头像
    mobile = models.CharField(max_length=50)    #电话

    level = models.IntegerField(default=1) # '1:普通客户 2:月卡用户  '
    expiration_at=models.DateTimeField()
    credit=models.IntegerField()

    status = models.IntegerField(default=1)        #状态:1正常/2禁用/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'nickname':self.nickname,'avatar':self.avatar,'mobile':self.mobile,'level':self.level,'expiration_at':self.expiration_at,'credit':self.credit,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "member"  # 更改表名
