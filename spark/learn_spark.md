# Spark 问题集锦

- spark.executor.cores的问题
本来为2，设置为8的时候就报错 ioexception，failed to send RPC closed channelexception
这个问题需要研究下spark.executor.cores这个参数的含义

-  "spark.dynamicAllocation.enabled=true" \

- "spark.dynamicAllocation.minExecutors=10" \
- "spark.dynamicAllocation.maxExecutors=50" \
这个参数每次设置大了也会出错，不知道具体含义
- "spark.executor.memoryOverhead=2g" \‘
这个参数不知道干什么用的

- driver-memory 2g \
这个参数感觉是driver的内存设置，不知道上限在哪，加多少合适
- executor-memory 12g \
这个同理 