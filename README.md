# MathModelBuilding
ModelBuilding
#统计信息
对于每一个位点统计其编码对个数，编码对包括16个:
```python
{'AA','AG','AC'...'TA','TG','TC','TT'}
```
对500个健康样本，和500非健康样本分开统计

> unhealty.txt healthy.txt 不带位点信息的统计结果

> out.txt, out2.txt 带位点信息的统计结果

对于每一个位点rs, 其编码只有三种。通过统计发现，任何位点rs上对应的`健康样本`的统计信息s1,与`非健康样本`的统计信息s2有：
`sum(s1-s2) === 500`
