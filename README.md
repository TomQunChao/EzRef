根据自定义参考文献格式生成参考文献

- [ ] 支持自定义格式
- [ ] 预装已有格式
- [ ] 支持导入bibTex
- [ ] 支持按特定格式解析参考文献
- [ ] 使用数据库存储参考文献格式
- [ ] 支持excel批量导入
- [ ] 支持数据库批量导入

## 自定义参考文献格式

```
序号 [名称] [类型] {第一项}.{第二项}.{第三项} ...
```
其中
- 序号即编号
- 第N项为项名，为你要导入的项名
- 名称即该格式的名称
- .是分割符号，还可能是, / :等等，也可能没有
- 要输入[]{}()#\ -符号时请使用转义字符\
- ()中为根据后面的项是否出现来决定本身是否出现的项

示例：

参考文献格式为

```
1 [MyFormat] [J] {Author}.{Title}\[{Type}\]{VolNo}
2 [MyFormat] [C] {Author}.{Title}\[{Type}\]{Addr}:{VolNo}(,){Href}
```

要导入的参考文献为

```
-MyFormat-J # 以-起始，第一个为格式名，第二个为格式类型，比如-GB/T-C
Author: an author
Title: a title
Type: J
VolNo: 30
# This is a comment
-MyFormat-C # 新的一个参考文献，没必要所有都满足，当不满足时，不会出现
Author: another author
Title: another title
Type: C
Addr: Hebei,China
VolNo: 40
```
则当使用MyFormat生成时，生成的参考文献为

```
an author.a title.[J].30
another author.another title[C]Hebei,China:40
```
