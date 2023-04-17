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



# 订单模型
class Orders(models.Model):
    member_id = models.IntegerField() #会员id
    user_id = models.IntegerField()   #操作员id
    money = models.FloatField()     #金额
    status = models.IntegerField(default=1)   #订单状态:1过行中/2无效/3已完成
    payment_status = models.IntegerField(default=1)   #支付状态:1未支付/2已支付/3已退款
    create_at = models.DateTimeField(default=datetime.now)  #创建时间
    update_at = models.DateTimeField(default=datetime.now)  #修改时间
    flow_num=models.IntegerField()

    class Meta:
        db_table = "orders"  # 更改表名


#订单详情模型
class OrderDetail(models.Model):
    order_id = models.IntegerField()  #订单id
    product_id = models.IntegerField()  #菜品id
    product_name = models.CharField(max_length=50) #菜品名称
    price = models.FloatField()     #单价
    quantity = models.IntegerField()  #数量
    status = models.IntegerField(default=1) #状态:1正常/9删除

    class Meta:
        db_table = "order_detail"  # 更改表名


# 支付信息模型
class Payment(models.Model):
    order_id = models.IntegerField()  #订单id号
    member_id = models.IntegerField() #会员id
    money = models.FloatField()     #支付金额
    type = models.IntegerField()      #付款方式：1会员付款/2收银收款
    bank = models.IntegerField(default=1) #收款银行渠道:1微信/2余额/3现金/4支付宝
    status = models.IntegerField(default=1) #支付状态:1未支付/2已支付/3已退款
    create_at = models.DateTimeField(default=datetime.now)  #创建时间
    update_at = models.DateTimeField(default=datetime.now)  #修改时间

    class Meta:
        db_table = "payment"  # 更改表名



class Batchings(models.Model):
    STATUS_CHOICES = (
        (1, '正常'),
        (2, '停售'),
        (9, '删除')
    )
    RADIO_CHOICES = (
        (0, '可多选'),
        (1, '单选')
    )
    id = models.AutoField(primary_key=True, db_column='id')
    cover_pic = models.CharField(max_length=50, db_column='cover_pic')
    name = models.TextField(max_length=255, db_column='name')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0, db_column='price')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1, db_column='status')
    create_at = models.DateTimeField(auto_now_add=True, db_column='create_at')
    update_at = models.DateTimeField(auto_now=True, db_column='update_at')
    radio = models.SmallIntegerField(choices=RADIO_CHOICES, default=0, db_column='radio')

    class Meta:
        db_table = 'batching'
from django.db import models

class BatchingDetail(models.Model):
    STATUS_CHOICES = (
        (1, '正常'),
        (9, '删除')
    )
    id = models.AutoField(primary_key=True, db_column='id')
    batching_id = models.IntegerField(db_column='batching_id', null=False)
    order_d_id = models.IntegerField(db_column='order_d_id', null=False)
    product_id = models.IntegerField(db_column='product_id', null=False)
    batching_name = models.CharField(max_length=50, db_column='batching_name', null=False)
    batching_price = models.DecimalField(max_digits=6, decimal_places=2, db_column='batching_price')
    quantity = models.IntegerField(db_column='quantity', default=1)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1, db_column='status')
    cartid=models.IntegerField(null=False)

    class Meta:
        db_table = 'batching_detail'
