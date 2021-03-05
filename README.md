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
-MyFormat # This is a format
[类型] {第一项}.{第二项}.{第三项} ...
...
-Myformat2
...
```
其中
- 第N项为项名，为你要导入的项名
- 名称即该格式的名称
- .是分割符号，还可能是, / :等等，也可能没有
- 要输入[]{}()#\ -符号时请使用转义字符\
- ()中为根据后面的项是否出现来决定本身是否出现的项
- -Format名称下面全部为该Format下的所有格式类型

示例：

参考文献格式为

```
-MyFormat
[杂志] {Author}.{Title}\[{Type}\]{VolNo}
[Conference] {Author}.{Title}\[{Type}\]{Addr}:{VolNo}(,){Href}
```

要导入的参考文献为

```
-杂志 # -类型表示一个参考文献的起始，上一参考文献的结束
Author: an author
Title: a title
Type: J
VolNo: 30
# This is a comment
-Conference
Author: another author
Title: another title
Type: C
Addr: Hebei,China
VolNo: 40
```
生成的参考文献为

```
an author.a title.[J].30
another author.another title[C]Hebei,China:40
```

## 自定义爬虫爬取规则

```
-href
-[类型]
项目1: css选择器
项目2: css选择器
项目3: css选择器
...
-href2
...
```
其中
- href为要爬取的域名，实际上可以是url链接，采用最长匹配算法
- 项目N对应格式的Author,Title等项目
- css选择器即BeautifulSoup要提取的css项
- 第二项类型用于对应于上面的类型
