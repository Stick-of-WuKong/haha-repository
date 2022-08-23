# PHP

[PHP 教程 (w3school.com.cn)](https://www.w3school.com.cn/php/index.asp)

**PHP 是一种创建动态交互性站点的强有力的服务器端脚本语言。**

## PHP简介

- PHP在服务器上执行

- PHP 是 "PHP Hypertext Preprocessor" 的首字母缩略词

- PHP 文件能够包含文本、HTML、CSS 以及 PHP 代码
- PHP 代码在服务器上执行，而结果以纯文本返回浏览器
- PHP 文件的后缀是 ".php"

### PHP能做什么

- PHP 能够生成动态页面内容
- PHP 能够创建、打开、读取、写入、删除以及关闭服务器上的文件
- PHP 能够接收表单数据
- PHP 能够发送并取回 cookies
- PHP 能够添加、删除、修改数据库中的数据
- PHP 能够限制用户访问网站中的某些页面
- PHP 能够对数据进行加密

通过 PHP，您可以不受限于只输出 HTML。您还能够输出图像、PDF 文件、甚至 Flash 影片。您也可以输出任何文本，比如 XHTML 和 XML。

### 为什么使用PHP

- PHP 运行于各种平台（Windows, Linux, Unix, Mac OS X 等等）
- PHP 兼容几乎所有服务器（Apache, IIS 等等）
- PHP 支持多种数据库
- PHP 是免费的。请从官方 PHP 资源下载：[www.php.net](http://www.php.net/)
- PHP 易于学习，并可高效地运行在服务器端

## PHP安装

- 使用支持 PHP 和 MySQL 的 web 主机
- 在您的 PC 上安装 web 服务器，然后安装 PHP 和 MySQL。

**使用支持 PHP 的 Web 主机**

如果您的服务器支持 PHP，那么您无需做任何事情。

只要创建 .php 文件，然后上传到 web 目录中即可。服务器会自动对它们进行解析。

您无需编译或安装任何额外的工具。

因为 PHP 是免费的，大多数 web 主机都支持 PHP。

**在PC上运行PHP**

不过如果您的服务器不支持 PHP，那么您必须：

- 安装 web 服务器
- 安装 PHP
- 安装数据库，比如 MySQL

官方的 PHP 网站 (PHP.net) 提供了 PHP 的安装说明：http://php.net/manual/zh/install.php

### 注释

**提示：**如需在 Windows 平台设置并立即运行 PHP，您还可以：

[下载 WebMatrix](http://www.microsoft.com/web/webmatrix/)

## PHP语法

**PHP 脚本在服务器上执行，然后向浏览器发送回纯 HTML 结果。**

### 基础PHP语法

PHP 脚本可放置于文档中的任何位置。

PHP 脚本以 *<?php* 开头，以 *?>* 结尾：

```php
<?php
// 此处是 PHP 代码
?>
```

PHP 文件的默认文件扩展名是 ".php"。

PHP 文件通常包含 HTML 标签以及一些 PHP 脚本代码。

例子：

其中包含了使用内建 PHP 函数 "echo" 在网页上输出文本 "Hello World!" 的一段 PHP 脚本：

```php+HTML
<!DOCTYPE html>
<html>
<body>

<h1>我的第一张 PHP 页面</h1>

<?php
echo "Hello World!";
?>

</body>
</html>
```

**注释：**PHP 语句以分号结尾（;）。PHP 代码块的关闭标签也会自动表明分号（因此在 PHP 代码块的最后一行不必使用分号）。

### PHP 中的注释

PHP 代码中的注释不会被作为程序来读取和执行。它唯一的作用是供代码编辑者阅读。

注释用于：

- 使其他人理解您正在做的工作 - 注释可以让其他程序员了解您在每个步骤进行的工作（如果您供职于团队）
- 提醒自己做过什么 - 大多数程序员都曾经历过一两年后对项目进行返工，然后不得不重新考虑他们做过的事情。注释可以记录您在写代码时的思路。

PHP支持3中注释：

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
// 这是单行注释

# 这也是单行注释

/*
这是多行注释块
它横跨了
多行
*/
?>

</body>
</html>
```

### PHP 大小写的敏感问题

在 PHP 中，所有用户定义的函数、类和关键词（例如 if、else、echo 等等）都对大小写不敏感。

不过在 PHP 中，所有变量都对大小写敏感。

## PHP变量

变量是存储信息的容器：

```php+HTML
<?php
$x=5;
$y=6;
$z=$x+$y;
echo $z;
?>
```

类似代数，在代数中我们使用字母（比如 x）来保存值（比如 5）。

在 PHP 中，起到代数作用的被称为*变量*。

**注释：**请把变量视为存储数据的容器。

正如代数，PHP 变量可用于保存值（x=5）和表达式（z=x+y）。

变量的名称可以很短（比如 x 和 y），也可以取更具描述性的名称（比如 carname、total_volume）。

### PHP 变量规则：

- 变量以 $ 符号开头，其后是变量的名称
- 变量名称必须以字母或下划线开头
- 变量名称不能以数字开头
- 变量名称只能包含字母数字字符和下划线（A-z、0-9 以及 _）
- 变量名称对大小写敏感（$y 与 $Y 是两个不同的变量）

**注释：**PHP 变量名称对大小写敏感！

### 创建 PHP 变量

PHP 没有创建变量的命令。

变量会在首次为其赋值时被创建：

```php+HTML
<?php
$txt="Hello world!";
$x=5;
$y=10.5;
?>
```

以上语句执行后，变量 txt 会保存值 Hello world!，变量 x 会保存值 5，变量 y 会保存值 10.5。

**注释：**如果您为变量赋的值是文本，请用引号包围该值。

### PHP 是一门类型松散的语言

在上面的例子中，请注意我们不必告知 PHP 变量的数据类型。

PHP 根据它的值，自动把变量转换为正确的数据类型。

在诸如 C 和 C++ 以及 Java 之类的语言中，程序员必须在使用变量之前声明它的名称和类型。

### PHP 变量作用域

在 PHP 中，可以在脚本的任意位置对变量进行声明。

变量的作用域指的是变量能够被引用/使用的那部分脚本。

PHP 有三种不同的变量作用域：

- local（局部）
- global（全局）
- static（静态）

### Local 和 Global 作用域

函数*之外*声明的变量拥有 Global 作用域，只能在函数以外进行访问。

函数*内部*声明的变量拥有 LOCAL 作用域，只能在函数内部进行访问。

```php+HTML
<?php
$x=5; // 全局作用域

function myTest() {
  $y=10; // 局部作用域
  echo "<p>测试函数内部的变量：</p>";
  echo "变量 x 是：$x";
  echo "<br>";
  echo "变量 y 是：$y";
} 

myTest();

echo "<p>测试函数之外的变量：</p>";
echo "变量 x 是：$x";
echo "<br>";
echo "变量 y 是：$y";
?>
```

在上例中，有两个变量 $x 和 $y，以及一个函数 myTest()。$x 是全局变量，因为它是在函数之外声明的，而 $y 是局部变量，因为它是在函数内声明的。

如果我们在 myTest() 函数内部输出两个变量的值，$y 会输出在本地声明的值，但是无法 $x 的值，因为它在函数之外创建。

然后，如果在 myTest() 函数之外输出两个变量的值，那么会输出 $x 的值，但是不会输出 $y 的值，因为它是局部变量，并且在 myTest() 内部创建。

**注释：**您可以在不同的函数中创建名称相同的局部变量，因为局部变量只能被在其中创建它的函数识别。

### PHP global 关键词

global 关键词用于在函数内访问全局变量。

要做到这一点，请在（函数内部）变量前面使用 global 关键词：

```php
<?php
$x=5;
$y=10;

function myTest() {
  global $x,$y;
  $y=$x+$y;
}

myTest();
echo $y; // 输出 15
?
```

PHP 同时在名为 $GLOBALS[index] 的数组中存储了所有的全局变量。下标存有变量名。这个数组在函数内也可以访问，并能够用于直接更新全局变量。

上式可重写：

```php
<?php
$x=5;
$y=10;

function myTest() {
  $GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y'];
} 

myTest();
echo $y; // 输出 15
?>
```

### PHP static 关键词

通常，当函数完成/执行后，会删除所有变量。不过，有时我需要不删除某个局部变量。实现这一点需要更进一步的工作。

要完成这一点，请在您首次声明变量时使用 *static* 关键词：

```php
<?php

function myTest() {
  static $x=0;
  echo $x;
  $x++;
}

myTest();
myTest();
myTest();

?>
```

然后，每当函数被调用时，这个变量所存储的信息都是函数最后一次被调用时所包含的信息。

**注释：**该变量仍然是函数的局部变量。

## PHP 5 echo 和 print 语句

**在 PHP 中，有两种基本的输出方法：echo 和 print。**

### PHP echo 和 print 语句

echo 和 print 之间的差异：

- echo - 能够输出一个以上的字符串
- print - 只能输出一个字符串，并始终返回 1

**提示：**echo 比 print 稍快，因为它不返回任何值。

### PHP echo 语句

echo 是一个语言结构，有无括号均可使用：echo 或 echo()。

#### 显示字符串

下面的例子展示如何用 echo 命令来显示不同的字符串（同时请注意字符串中能包含 HTML 标记）：

```php+HTML
<?php
echo "<h2>PHP is fun!</h2>";
echo "Hello world!<br>";
echo "I'm about to learn PHP!<br>";
echo "This", " string", " was", " made", " with multiple parameters.";
?>
```

运行结果：

![image-20220822180456072](http://cdn.ayusummer233.top/img/image-20220822180456072.png)

#### 显示变量

```php
<?php
$txt1="Learn PHP";
$txt2="W3School.com.cn";
$cars=array("Volvo","BMW","SAAB");

echo $txt1;
echo "<br>";
echo "Study PHP at $txt2";
echo "My car is a {$cars[0]}";
?>
```

![image-20220822180905330](http://cdn.ayusummer233.top/img/image-20220822180905330.png)

### PHP print 语句

print 也是语言结构，有无括号均可使用：print 或 print()。

#### 显示字符串

下面的例子展示如何用 print 命令来显示不同的字符串（同时请注意字符串中能包含 HTML 标记）：

```php
<?php
print "<h2>PHP is fun!</h2>";
print "Hello world!<br>";
print "I'm about to learn PHP!";
?>
```

![image-20220822181048454](http://cdn.ayusummer233.top/img/image-20220822181048454.png)

#### 显示变量

```php
<?php
$txt1="Learn PHP";
$txt2="W3School.com.cn";
$cars=array("Volvo","BMW","SAAB");

print $txt1;
print "<br>";
print "Study PHP at $txt2";
print "My car is a {$cars[0]}";
?>
```

![image-20220822181159146](http://cdn.ayusummer233.top/img/image-20220822181159146.png)

## PHP数据类型

**字符串、整数、浮点数、逻辑、数组、对象、NULL。**

### PHP 字符串

字符串是字符序列，比如 "Hello world!"。

字符串可以是引号内的任何文本。您可以使用单引号或双引号：

```php
<?php 
$x = "Hello world!";
echo $x;
echo "<br>"; 
$x = 'Hello world!';
echo $x;
?>
```

![image-20220822181404818](http://cdn.ayusummer233.top/img/image-20220822181404818.png)

### PHP 整数

整数是没有小数的数字。

整数规则：

- 整数必须有至少一个数字（0-9）
- 整数不能包含逗号或空格
- 整数不能有小数点
- 整数正负均可
- 可以用三种格式规定整数：十进制、十六进制（前缀是 0x）或八进制（前缀是 0）

在下面的例子中，我们将测试不同的数字。PHP var_dump() 会返回变量的数据类型和值：

```php
<?php 
$x = 5985;
var_dump($x);
echo "<br>"; 
$x = -345; // 负数
var_dump($x);
echo "<br>"; 
$x = 0x8C; // 十六进制数
var_dump($x);
echo "<br>";
$x = 047; // 八进制数
var_dump($x);
?>
```

![image-20220822181456105](http://cdn.ayusummer233.top/img/image-20220822181456105.png)

### PHP 浮点数

浮点数是有小数点或指数形式的数字。

在下面的例子中，我们将测试不同的数字。PHP var_dump() 会返回变量的数据类型和值：

```php
<?php 
$x = 10.365;
var_dump($x);
echo "<br>"; 
$x = 2.4e3;
var_dump($x);
echo "<br>"; 
$x = 8E-5;
var_dump($x);
?>
```

![image-20220822181853802](http://cdn.ayusummer233.top/img/image-20220822181853802.png)

### PHP逻辑

逻辑是 true 或 false。

```php
$x=true;
$y=false;
```

逻辑常用于条件测试。

### PHP 数组

数组在一个变量中存储多个值。

在下面的例子中，我们将测试不同的数组。PHP var_dump() 会返回变量的数据类型和值：

```php
<?php 
$cars=array("Volvo","BMW","SAAB");
var_dump($cars);
?>
```

![image-20220822182027215](http://cdn.ayusummer233.top/img/image-20220822182027215.png)

### PHP 对象

对象是存储数据和有关如何处理数据的信息的数据类型。

在 PHP 中，必须明确地声明对象。

首先我们必须声明对象的类。对此，我们使用 class 关键词。类是包含属性和方法的结构。

然后我们在对象类中定义数据类型，然后在该类的实例中使用此数据类型：

```php
<?php
class Car
{
  var $color;
  function Car($color="green") {
    $this->color = $color;
  }
  function what_color() {
    return $this->color;
  }
}
?>
```

![image-20220822182149453](http://cdn.ayusummer233.top/img/image-20220822182149453.png)

### PHP NULL 值

特殊的 NULL 值表示变量无值。NULL 是数据类型 NULL 唯一可能的值。

NULL 值标示变量是否为空。也用于区分空字符串与空值数据库。

可以通过把值设置为 NULL，将变量清空：

```php
<?php
$x="Hello world!";
$x=null;
var_dump($x);
?>
```

![image-20220822190507646](http://cdn.ayusummer233.top/img/image-20220822190507646.png)

## PHP字符串函数

**字符串是字符序列，比如 "Hello world!"。**

### strlen()函数

返回字符串的长度，以字符记。

strlen() 常用于循环和其他函数， 在确定字符串何时结束很重要时。（例如，在循环中，我们也许需要在字符串的最后一个字符之后停止循环）。

### str_word_count() 函数

对字符串中的单词进行计数

###  strrev() 函数

反转字符串

### strpos() 函数

strpos() 函数用于检索字符串内指定的字符或文本。

如果找到匹配，则会返回首个匹配的字符位置。如果未找到匹配，则将返回 FALSE。（从首字符的位置0开始）

```php
<?php
echo strpos("Hello world!","world");
?>
```



###  str_replace() 函数

一些字符串替换字符串中的另一些字符

用 "Kitty" 替换文本 "world"：

```php
<?php
echo str_replace("world", "Kitty", "Hello world!"); // 输出 Hello Kitty!
?>
```

## PHP常量

**常量类似变量，但是常量一旦被定义就无法更改或撤销定义。**

常量是单个值的标识符（名称）。在脚本中无法改变该值。

有效的常量名以字符或下划线开头（常量名称前面没有 $ 符号）。

**注释：**与变量不同，常量贯穿整个脚本是自动全局的。

### 设置 PHP 常量

如需设置常量，请使用 `define()` 函数 - 它使用三个参数：

1. 首个参数定义常量的名称
2. 第二个参数定义常量的值
3. 可选的第三个参数规定常量名是否对大小写不敏感。默认是 false。

下例创建了一个*对大小写敏感的常量*，值为 "Welcome to W3School.com.cn!"：

```php
<?php
define("GREETING", "Welcome to W3School.com.cn!");
echo GREETING;
?>
```

创建一个*对大小写不敏感的常量*，值为 "Welcome to W3School.com.cn!"：

```php
<?php
define("GREETING", "Welcome to W3School.com.cn!", true);
echo greeting;
?>
```

### 常量是全局的

常量是自动全局的，而且可以贯穿整个脚本使用。

下面的例子在函数内使用了一个常量，即使它在函数外定义：

```php
<?php
define("GREETING", "Welcome to W3School.com.cn!");

function myTest() {
    echo GREETING;
}
 
myTest();
?>
```

## PHP运算符

### PHP 算数运算符

| 运算符 | 名称 | 例子    | 结果            | 显示结果                                                     |
| :----- | :--- | :------ | :-------------- | :----------------------------------------------------------- |
| +      | 加法 | $x + $y | $x 与 $y 求和   | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_addition) |
| -      | 减法 | $x - $y | $x 与 $y 的差数 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_subtraction) |
| *      | 乘法 | $x * $y | $x 与 $y 的乘积 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_multiplication) |
| /      | 除法 | $x / $y | $x 与 $y 的商数 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_division) |
| %      | 取模 | $x % $y | $x 除 $y 的余数 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_modulus) |

```php
<?php 
$x=17; 
$y=8;
echo ($x + $y); // 输出 25
echo ($x - $y); // 输出 9
echo ($x * $y); // 输出 136
echo ($x / $y); // 输出 2.125
echo ($x % $y); // 输出 1
?>
```

### PHP 赋值运算符

PHP 赋值运算符用于向变量写值。

PHP 中基础的赋值运算符是 "="。这意味着右侧赋值表达式会为左侧运算数设置值。

| 赋值   | 等同于    | 描述                           | 显示结果                                                     |
| :----- | :-------- | :----------------------------- | :----------------------------------------------------------- |
| x = y  | x = y     | 右侧表达式为左侧运算数设置值。 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_set) |
| x += y | x = x + y | 加                             | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_addition2) |
| x -= y | x = x - y | 减                             | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_subtraction2) |
| x *= y | x = x * y | 乘                             | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_multiplication2) |
| x /= y | x = x / y | 除                             | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_division2) |
| x %= y | x = x % y | 模数                           | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_modulus2) |

下例展示了使用不同赋值运算符的不同结果：

```php
<?php 
$x=17; 
echo $x; // 输出 17

$y=17; 
$y += 8;
echo $y; // 输出 25

$z=17;
$z -= 8;
echo $z; // 输出 9

$i=17;
$i *= 8;
echo $i; // 输出 136

$j=17;
$j /= 8;
echo $j; // 输出 2.125

$k=17;
$k %= 8;
echo $k; // 输出 1
?>
```

### PHP 字符串运算符

| 运算符 | 名称     | 例子                                      | 结果                           | 显示结果                                                     |
| :----- | :------- | :---------------------------------------- | :----------------------------- | :----------------------------------------------------------- |
| .      | 串接     | $txt1 = "Hello" $txt2 = $txt1 . " world!" | 现在 $txt2 包含 "Hello world!" | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_string1) |
| .=     | 串接赋值 | $txt1 = "Hello" $txt1 .= " world!"        | 现在 $txt1 包含 "Hello world!" | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_string2) |

下例展示了使用字符串运算符的结果：

```php
<?php
$a = "Hello";
$b = $a . " world!";
echo $b; // 输出 Hello world!

$x="Hello";
$x .= " world!";
echo $x; // 输出 Hello world!
?>
```

### PHP 递增/递减运算符

| 运算符 | 名称   | 描述                      | 显示结果                                                     |
| :----- | :----- | :------------------------ | :----------------------------------------------------------- |
| ++$x   | 前递增 | $x 加一递增，然后返回 $x  | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_pre_increment) |
| $x++   | 后递增 | 返回 $x，然后 $x 加一递增 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_post_increment) |
| --$x   | 前递减 | $x 减一递减，然后返回 $x  | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_pre_decrement) |
| $x--   | 后递减 | 返回 $x，然后 $x 减一递减 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_post_decrement) |

下例展示了使用不同递增/递减运算符的不同结果：

```php
<?php
$x=17; 
echo ++$x; // 输出 18

$y=17; 
echo $y++; // 输出 17

$z=17;
echo --$z; // 输出 16

$i=17;phpphp
echo $i--; // 输出 17
?>
```

### PHP 比较运算符

PHP 比较运算符用于比较两个值（数字或字符串）：

| 运算符 | 名称               | 例子      | 结果                                               | 显示结果                                                     |
| :----- | :----------------- | :-------- | :------------------------------------------------- | :----------------------------------------------------------- |
| ==     | 等于               | $x == $y  | 如果 $x 等于 $y，则返回 true。                     | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_equal) |
| ===    | 全等（完全相同）   | $x === $y | 如果 $x 等于 $y，且它们类型相同，则返回 true。     | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_identical) |
| !=     | 不等于             | $x != $y  | 如果 $x 不等于 $y，则返回 true。                   | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_not_equal) |
| <>     | 不等于             | $x <> $y  | 如果 $x 不等于 $y，则返回 true。                   | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_not_equal2) |
| !==    | 不全等（完全不同） | $x !== $y | 如果 $x 不等于 $y，或它们类型不相同，则返回 true。 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_not_identical) |
| >      | 大于               | $x > $y   | 如果 $x 大于 $y，则返回 true。                     | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_greater_than) |
| <      | 小于               | $x < $y   | 如果 $x 小于 $y，则返回 true。                     | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_less_than) |
| >=     | 大于或等于         | $x >= $y  | 如果 $x 大于或者等于 $y，则返回 true.              | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_greater_than2) |
| <=     | 小于或等于         | $x <= $y  | 如果 $x 小于或者等于 $y，则返回 true。             | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_less_than2) |

下例展示了使用某些比较运算符的不同结果：

```php
<?php
$x=17; 
$y="17";

var_dump($x == $y);
echo "<br>";
var_dump($x === $y);
echo "<br>";
var_dump($x != $y);
echo "<br>";
var_dump($x !== $y);
echo "<br>";

$a=17;
$b=8;

var_dump($a > $b);
echo "<br>";
var_dump($a < $b);
?>
```

### PHP 逻辑运算符

| 运算符 | 名称 | 例子       | 结果                                             | 显示结果                                                     |
| :----- | :--- | :--------- | :----------------------------------------------- | :----------------------------------------------------------- |
| and    | 与   | $x and $y  | 如果 $x 和 $y 都为 true，则返回 true。           | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_and) |
| or     | 或   | $x or $y   | 如果 $x 和 $y 至少有一个为 true，则返回 true。   | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_or) |
| xor    | 异或 | $x xor $y  | 如果 $x 和 $y 有且仅有一个为 true，则返回 true。 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_xor) |
| &&     | 与   | $x && $y   | 如果 $x 和 $y 都为 true，则返回 true。           | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_and2) |
| \|\|   | 或   | $x \|\| $y | 如果 $x 和 $y 至少有一个为 true，则返回 true。   | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_or2) |
| !      | 非   | !$x        | 如果 $x 不为 true，则返回 true。                 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_not) |

### PHP 数组运算符

PHP 数组运算符用于比较数组：

| 运算符 | 名称   | 例子      | 结果                                                         | 显示结果                                                     |
| :----- | :----- | :-------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| +      | 联合   | $x + $y   | $x 和 $y 的联合（但不覆盖重复的键）                          | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_union) |
| ==     | 相等   | $x == $y  | 如果 $x 和 $y 拥有相同的键/值对，则返回 true。               | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_equality) |
| ===    | 全等   | $x === $y | 如果 $x 和 $y 拥有相同的键/值对，且顺序相同类型相同，则返回 true。 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_identity) |
| !=     | 不相等 | $x != $y  | 如果 $x 不等于 $y，则返回 true。                             | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_inequality) |
| <>     | 不相等 | $x <> $y  | 如果 $x 不等于 $y，则返回 true。                             | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_inequality2) |
| !==    | 不全等 | $x !== $y | 如果 $x 与 $y 完全不同，则返回 true。                        | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_non_identity) |

下例展示了使用不同数组运算符的不同结果：

```php
<?php
$x = array("a" => "apple", "b" => "banana"); 
$y = array("c" => "orange", "d" => "peach"); 
$z = $x + $y; // $x 与 $y 的联合
var_dump($z);
var_dump($x == $y);
var_dump($x === $y);
var_dump($x != $y);
var_dump($x <> $y);
var_dump($x !== $y);
?>
```

![image-20220823094043424](http://cdn.ayusummer233.top/img/image-20220823094043424.png)

- [PHP 常量](https://www.w3school.com.cn/php/php_constants.asp)
- [PHP If...Else](https://www.w3school.com.cn/php/php_if_else.asp)

## PHP if...else....elseif语句

**条件语句用于基于不同条件执行不同的动作**

### PHP 条件语句

在您编写代码时，经常会希望为不同的决定执行不同的动作。您可以在代码中使用条件语句来实现这一点。

在 PHP 中，我们可以使用以下条件语句：

- *if 语句* - 如果指定条件为真，则执行代码
- *if...else 语句* - 如果条件为 true，则执行代码；如果条件为 false，则执行另一端代码
- *if...elseif....else 语句* - 根据两个以上的条件执行不同的代码块
- *switch 语句* - 选择多个代码块之一来执行

### PHP - if 语句

if 语句用于*在指定条件为 true 时*执行代码。

### 语法

```
if (条件) {
  当条件为 true 时执行的代码;
}
```

下例将输出 "Have a good day!"，如果当前时间 (HOUR) 小于 20：

```php
<?php
$t=date("H");

if ($t<"20") {
  echo "Have a good day!";
}
?>
```

### PHP - if...else 语句

请使用 if....else 语句*在条件为 true 时执行代码*，*在条件为 false 时执行另一段代码*。

```
if (条件) {
  条件为 true 时执行的代码;
} else {
  条件为 false 时执行的代码;
}
```

### PHP - if...elseif....else 语句

请使用 if....elseif...else 语句来*根据两个以上的条件执行不同的代码*。

### 语法

```
if (条件) {
  条件为 true 时执行的代码;
} elseif (condition) {
  条件为 true 时执行的代码;
} else {
  条件为 false 时执行的代码;
}
```

## PHP Switch 语句

**switch 语句用于基于不同条件执行不同动作。**

### Switch 语句

如果您希望有选择地执行若干代码块之一，请使用 Switch 语句。

使用 Switch 语句可以避免冗长的 if..elseif..else 代码块。

```
switch (expression)
{
case label1:
  expression = label1 时执行的代码 ;
  break;  
case label2:
  expression = label2 时执行的代码 ;
  break;
default:
  表达式的值不等于 label1 及 label2 时执行的代码;
}
```

工作原理：

1. 对表达式（通常是变量）进行一次计算
2. 把表达式的值与结构中 case 的值进行比较
3. 如果存在匹配，则执行与 case 关联的代码
4. 代码执行后，*break 语句*阻止代码跳入下一个 case 中继续执行
5. 如果没有 case 为真，则使用 default 语句

## PHP while 循环

**PHP while 循环在指定条件为 true 时执行代码块。**





##### [PHP 参考手册](https://www.w3school.com.cn/php/php_ref.asp)

##### [PHP 测验](https://www.w3school.com.cn/php/php_quiz.asp)