记录一下新遇到的概念和使用方法等
关于springboot的学习，一开始我尝试了去听视频，讲得很好很细，但是内容太多，没有时间全部听完，而且前面听后面忘，没有动手实操，很快就没有印象了。 有的时候老师会开始深入讲解原理，由于连基本的使用还不会，听到原理就一头雾水。

现在计划这样学习springboot
1. 在项目中留意springboot的基本用法，比较多个service来找共同点。
2. 总结常用的一些用法，包括注解啊之类
3. 等把基本用法玩熟了，能够熟练阅读代码和写出代码之后，开始尝试研究底层原理。

# 注解
spring中大量的应用注解，感觉用起来很方便，但是其背后的工作原理一直不是非常的了解，在使用的时候总有种靠蒙靠试的感觉，打算借着做目前这个项目的机会学习一下。

- 注解只有成员变量，没有方法 

## JsonInclude
JsonInclude  是一个类级别的设置，JsonInclude.Include.NON_EMPTY标识只有非NULL的值才会被纳入json string之中，其余的都被忽略，比如这里的location属性，并没有出现在最终的结果字符串中。

## FeignClient
- 用来修饰接口类型
- 看起来像是一个方便封装了远程调用的接口，给程序提供一个代码接口，同时将相应的远程调用绑定起来。
没有研究很深入，第一感觉是方便进行远程调用。

OpenFeign是什么？
OpenFeign是一个声明式的web服务客户端，让编写web服务客户端变的非常容易，只需要创建一个接口并在接口上添加注解即可，openFeign的前身是Feign，后者目前已经停更了，openFeign是SpringCloud在Feign的基础上支持了Spring MVC的注解，并通过动态代理的方式产生实现类来做负载均衡并进行调用其他服务。

## CronTrigger


## ConfigurationProperties
可以直接将外部的属性转换为内部的类，比如application.yml，或者.properties文件

## Configuration

## Retention

## EnableScheduling

开发人员使用注解 @EnableScheduling;
注解@EnableScheduling导入SchedulingConfiguration;
SchedulingConfiguration定义基础设施bean ScheduledAnnotationBeanPostProcessor scheduledAnnotationProcessor;
ScheduledAnnotationBeanPostProcessor在容器启动时做如下事情
登记所有使用@Scheduled注解的bean方法到一个ScheduledTaskRegistrar，供调度任务执行器TaskScheduler执行。
为ScheduledTaskRegistrar指定任务执行器TaskScheduler,该任务执行器来自容器中的bean TaskScheduler/ScheduledExecutorService(如果不指定,ScheduledTaskRegistrar自己会本地创建一个ConcurrentTaskScheduler)
告诉ScheduledTaskRegistrar将所注册的调度任务，也就是使用@Scheduled注解的bean方法，调度到任务执行器TaskScheduler执行。
————————————————
版权声明：本文为CSDN博主「安迪源文」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/andy_zhang2007/article/details/96612243

### Scheduled

可以设定定期执行任务，注解在method上，可以直接定期执行该方法


## Target

## Component

## PostConstruct
用来在bean被加载后立刻调用该函数

## AliasFor
这个很重要，在定义新的注解的时候，可以产生一种类似于继承的效果

## @interface
这个东西也很特别，他使用来定义一个注解类，它本身是一个interface，所以他的定义应该是遵从interface的规则。 然后它extend Annotation接口。

下面的定义是借口的方法，可以使用default


# Springboot 的启动过程
1. springboot run application后，会默认componentscan（也可手动指定路径）在application所在的路径下的bean
