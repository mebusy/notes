# MongoDb Tips and Tricks

## set highest value

To set the highest value for a field in MongoDB, you can use the `$max` operator in an update operation. This operator updates the field to the specified value only if the specified value is greater than the current value of the field.

```javascript
await YourModel.updateOne(
  { _id: someDocumentId },
  {
    $max: {
      'eventMaps.1001.2001.highestScore': newScore1,
      'eventMaps.1002.2001.highestScore': newScore2
    },
  }
);
```


## 符合索引排序问题

- 复合索引只有全部方向一致或全部反向时才能用于排序。


## read then set

When you need to read a document and then update it based on the read value, you can use the following pattern:

```javascriptjavascript
// NOT work
$set: {
  [`members.${_id}.role`]: `$members.${targetId}.role`,
}
```

右边不能直接写成 "$members.xxx.role"，因为 $set 里的值不会当作字段引用来解析，而是会被当作一个普通字符串 "${...}" 存进去。

因为 $set 在 update operators 模式( 第二个参数是 `{...}` )下，只接受字面量值。


解决方法: 如果你要把一个字段的值赋给另一个字段，需要用 聚合管道更新（aggregation pipeline update），MongoDB 从 4.2 开始支持。

```javascript
const result = await DanceGroupModel.updateOne(
  { groupId, [`members.${targetId}`]: { $exists: true } },
  [
    {
      $set: {
        [`members.${_id}.role`]: `$members.${targetId}.role`
      }
    }
  ]
)
```

注意: updateOne 的第二个参数这里变成了 数组，这是聚合管道更新的写法。

也就是说，一旦你把更新表达式放进 `[...]`（管道数组），MongoDB 就切换成 aggregation context，右边的 "$xxx" 就会被当成“字段路径”，而不是“字符串”。


