# PostgreSQL

## features

1. 事务支持 表结构修改语句
2. 支持部分唯一索引
    - 即这个索引只对满足某个条件的行生效, 被逻辑删除的行不影响唯一性约束
3. 支持可延迟约束
4. 表达式索引
    - `ON users (lower(email))`
    - MySQL 8.0.13 才支持, 但是 mysql 版本越高，性能越差（8.0.36 - 8.4.0 性能降地非常厉害）

## 介绍

- database -> schema -> table 
    - 比 mysql 多了一层 schema
- Object-relational database
    - 传统关系型数据数据存在于一个2维表格中
    - 对象关系型数据库，对象之间通过组合和继承,形成复杂的网状的层次化关系,把负责的对象压扁到二维表格中
- 多种数据类型
    - 网段: cidr, inet, macaddr
    - 几何运算: point, line, lseg, box, path, polygon, circle
        - 简单几何运算和查询
    - 数组,多维数组
    - `CREATE TYPE` 自定义类型
    - JSONB
        - 可以对json的某个字段创建 表达式索引
        - 或者对整个JSONB 创建 GIN 通用倒排索引
            - `@>` 某个字段 满足某个值
            - `?` 存在某个字段
- 操作符
    - `>>` cidr包含
    - `->>` 获取 json 对象字段
- GiST
    - 一个通用索引结构,可以支持多种数据类型的索引
    - 支持范围查询
    - 查找距离最相近的元素
    - 支持全文检索
    - postgre 内置类型中，支持 GiST 的有
        - 几何类型
        - 范围类型
        - 全文检索 tsvector
- 全文检索(原生方案)
    - tsvector 文本搜索向量, tsquery
        - to_tsvector, to_tsquery
    - GIN 通用倒排索引
    - 替换 elasticsearch
    - `@@` 包含
    - 中文分词需要安装中文分词器插件, 让向量化支持中文
- [awesome-postgres 插件](https://github.com/dhamaniasad/awesome-postgres?tab=readme-ov-file#extensions)
- AI知识库
    - RAG (Retrieval-Augmented Generation) 检索增强生成
- 高速内存缓存(模拟redis)
    - `CREATE UNLOGGED TABLE` 非持久化表
    - 扩大 shared_buffers = 128MB
    - 配合 postgre cron 定时任务,定期把过期数据删除
- 其他扩展
    - Apache AGE 图数据库
    - TimeScaleDB 时序数据库


