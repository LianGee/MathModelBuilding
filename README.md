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

###tools
每个基因位点包含3中编码方式，使用0,1,2进行编码（对于那个编码对使用0,1,2无所谓）本实验编码方式：

`AA：2`, `AT,TA：1`, `TT:0`对于missing alleles使用-1
如果使用 HWE, 输入数据如下
```python
1 1 1 1 0 0 0 0				<--disease status, two identical status per individual, 1: case, 0: control
1 0 0 0 1 1 0 0				<--marker 1, alleles are denoted by 0 and 1.
1 1 0 0 1 0 1 1				<--marker 2
0 0 0 1 0 0 0 1				<--marker 3
0 1 1 1 0 -1 -1				<--marker 4, "-1" denotes missing allele
1 1 0 1 1 0 1 0				<--marker 5
```
一列表示一个样本，第一行表示样本疾病状态
- 参数设置
`"burnin", "mcmc", "thin"`依赖样本中位点个数
如，有L个位点则：
```matlab
burin = 10~100 L 
mcmc = L^2
thin = L
```
算法先从joint posterior分布中找到一个loacl mode，然后MCMC从这个mode开始运行。这比从随机mode出发要有优势，特别是对于高阶interactions。
`set INITIALTRYS = (e.g. 10 ~ 100)`,这样BEAM会先从10~100样本中寻找local modes。`TRY_LENGTH = 10L`表示每个样本迭代次数。如果BEAM找到一个概率比开始mode大的local mode，BEAM链会从这个mode重新执行。`set AUTORESTART = 5~10`

If the user let BEAM to 
search for some local modes first (by setting INITIALTRYS to a positive integer), we then 
set burnin = 10L. The length of each initial trial (TRY_LENGTH) is 20L by default

使用默认参数：
```matlab
BURNIN		0
MCMC		0
THIN		0
TRY_LENGTH	0
```




