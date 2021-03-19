# Jackson
java 里面用来帮助处理json字符串，方便将json和java类互转的工具

一些注解
 
## JsonInclude
JsonInclude  是一个类级别的设置，JsonInclude.Include.NON_EMPTY标识只有非NULL的值才会被纳入json string之中，其余的都被忽略，比如这里的location属性，并没有出现在最终的结果字符串中。

## JsonFormat
@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")  将Date转换成String  一般后台传值给前台时

## DateTimeFormat
@DatetimeFormat是将String转换成Date，一般前台给后台传值时用

