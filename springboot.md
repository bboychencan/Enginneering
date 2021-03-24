记录一下新遇到的概念和使用方法等
关于springboot的学习，一开始我尝试了去听视频，讲得很好很细，但是内容太多，没有时间全部听完，而且前面听后面忘，没有动手实操，很快就没有印象了。 有的时候老师会开始深入讲解原理，由于连基本的使用还不会，听到原理就一头雾水。

现在计划这样学习springboot
1. 在项目中留意springboot的基本用法，比较多个service来找共同点。
2. 总结常用的一些用法，包括注解啊之类
3. 等把基本用法玩熟了，能够熟练阅读代码和写出代码之后，开始尝试研究底层原理。

# Feign 和 Hystrix

## FeignClient
- 用来修饰接口类型
- 看起来像是一个方便封装了远程调用的接口，给程序提供一个代码接口，同时将相应的远程调用绑定起来。
没有研究很深入，第一感觉是方便进行远程调用。

OpenFeign是什么？
OpenFeign是一个声明式的web服务客户端，让编写web服务客户端变的非常容易，只需要创建一个接口并在接口上添加注解即可，openFeign的前身是Feign，后者目前已经停更了，openFeign是SpringCloud在Feign的基础上支持了Spring MVC的注解，并通过动态代理的方式产生实现类来做负载均衡并进行调用其他服务。

## Hystrix
是做各种熔断管理的，防止雪崩等。 在patrolman这个项目中引入了。 在调试的时候hystrix一直报错，后来发现是因为配置设的不对。 所以一定要对代码中使用的工具和库熟悉才行。 

# 注解
spring中大量的应用注解，感觉用起来很方便，但是其背后的工作原理一直不是非常的了解，在使用的时候总有种靠蒙靠试的感觉，打算借着做目前这个项目的机会学习一下。

- 注解只有成员变量，没有方法 


## 注入bean
几种方法
- ComponentScan 注册指定包里的bean Spring容器会扫描@ComponentScan配置的包路径，找到标记@Component注解的类加入到Spring容器
我们经常用到的类似的（注册到IOC容器）注解还有如下几个：

@Configuration：配置类
@Controller ：web控制器
@Repository ：数据仓库
@Service： 业务逻辑

- @Bean注解直接注册
注解@Bean被声明在方法上，方法都需要有一个返回类型，而这个类型就是注册到IOC容器的类型，接口和类都是可以的，介于面向接口原则，提倡返回类型为接口。

- @Import注册Bean
这种方法最为直接，直接把指定的类型注册到IOC容器里，成为一个java bean，可以把@Import放在程序的入口，它在程序启动时自动完成注册bean的过程。

## Autowired 注入接口
在代码中遇到这种情况，有点好奇这个时候，怎么知道该注入哪个实现
- 如果接口只有一个实现类的话，spring会自动找到这个实现类
- 如果接口有多个实现类的话，@Primary注解会用来被优先使用，或者用Qualifier来指定注入的bean

## Primary

## Qualifier
今天遇到一个exception，栈非常的长，底层大量的spring，然后接口，从idea里面跟几下子就找不到代码了。 后来研究了下才发现，原来接口定义
用了个Qualifier的注解，所以来学习一下。



## SpringQueryMap
如果我们是Get请求，但是请求的参数又很多， 比如我在查询并分页的时候，我们的入参只有一个查询的keyword, 但是又有分页的一些信息pageNum, pageSize, totalSize, 这时候我们一般会把这些数据封装有一个pojo, 但是feign的get方式又不支持，这里我们可以使用openfeign提供的@SpringQueryMap来解决这个问题，传递对象参数，让框架自动解析

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
