# Java知识点整理


## 注解
注解之前用的不多，而且也没有深入了解过它的原理
注解，metadata，可以在编译，类加载，运行的时候被读取，并执行相应的一些处理。


一定程度上。 框架 = 注解 + 反射 + 设计模式

元注解

元标签有 @Retention、@Documented、@Target、@Inherited、@Repeatable 5 种。


1. 类型一 生成文档相关的注解

- author
- version
- return
-exception


2. 类型二 在编译时进行格式检查 jdk内置的三个基本注解

- override

- deprecated

- supresswarning


3. 类型三 跟踪代码依赖性，实现替代配置文件的功能

- servlet 里面的配置

- spring 里面的trasaction配置


- Retention注解

一些关键字

- volatile

- static synchronized

4. 注解与xml


5. alias注解的别名

不仅是一个注解内不同属性可以声明别名，不同注解的属性也可以声明别名（注解可以作用于注解）



## java 新特性

java8 default 
- 默认方法
- 注解的默认值

自定义注解只有一个属性时，且属性名为value时，赋值时value可省略