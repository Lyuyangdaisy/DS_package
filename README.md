# Old Algorithm

`Intro`: This repo consists of the algorithm which are packaged in the specific form.
`Algorithm`:
+ clustering:  
  1.DBSCAN  
  2.KMeans  
  3.Mean Shift  
  4.Affinity Propagation  
+ Classifer:
  1.SVM
+ Graph in 3D
+ Others

`PS`: The building of this repo is in process and the classification of these algorithms are not the final structure. 

## code specification
### I. Documentation
1. Use UTF-8 encoding for files.
2. No special circumstances, the #-*-coding:utf-8-*- logo must be added to the file header.
3.Header comments contain: author, time, file name, version.
### Ⅱ. Code format
1. Indentation: uniform use of 4 spaces for indentation.
2. Line width: a single line should not exceed 80 characters (in special circumstances, it may slightly exceed 80, but the maximum should not exceed 120).  
3.line connection:
+ a) Do not use a backslash to connect rows.
+ b) Python implicitly joins lines in parentheses, brackets, and curly braces, and you can take advantage of this feature. If necessary, you can add an extra pair of parentheses around the expression.
+ c) Prohibit compound statements, i.e. multiple statements in a line.
+ d) if/for/while must be a line break.
4.quote：
+ a)Double quotes for natural language, single quotes for machine markings.
+ b) Use string quotation marks consistently in the same file. Use either 'single quotes' or "double quotes" to refer to a string, and use them in the same file. You can use a different type of quotation marks within a string to avoid using the same type of quotation marks.
5.blank line：  
+ a)two empty lines between module-level functions and class definitions.
+ b)an empty line between class member functions.
+ c)functions can use empty lines to separate logically related code.
### Ⅲ. Import statement
1.The import statement should be written in lines.  
2.The import statement should use absolute import.  
3.The import statement should be placed in the header of the file, after module comments and document strings, and before module global variables and constants.  
4.The import statements should be in order, with each group separated by a blank line.  
5.The imports should be grouped in order from most common to least common.
### Ⅳ. Space
1.One empty cell on each side of the binary operator [=,-,+=,==,>,in,is not, and].  
2.In the argument list of the function, followed by a space.  
3.In the argument list of the function, don't add a space between the default value and the equals sign.  
4.After the left parentheses, no extra spaces before the right parentheses.  
5.No extra spaces before the left bracket of the dictionary object.  
6.Don't use extra spaces to align assignment statements.  
7.Don't put spaces before commas, semicolons, and colons, but after them (except at the end of a line).  
### Ⅴ. Comment
1.Block notes: one space after "#" and separate paragraphs with blank lines (also need "#").  
2.Line notes: use at least two spaces and separate statements.  
3. At critical (or complex) parts of the code, comment as much as you can.  
4. Document comments: start and end with """, include: file name, author, time, version.  
5.Method comments: comment before definition, describing the implementation function, input and output, parameter meaning and exception description.
### Ⅵ. Naming
1. Use the CamelCase naming style, separated by an underscore if there are multiple words.
2. Variable names are lowercase as much as possible, separated by underscores if there are multiple words.
3. Constants are capitalized and separated by underscores if there are multiple words.




`简介`: 该仓库主要存储已经封装好的旧算法

`算法分类`
+ 聚类算法：
    1. DBSCAN
    2. Kmeans
    3. Mean Shift
    4. Affinity Propagation
+ 分类器：
    1. SVM
+ 3D图形输出
+ 其他


**说明**
仓库持续建设中，算法分类方式并非最终结构


## 代码规范V1

### 一、	文件
+ 文件使用 UTF-8 编码
+ 无特殊情况, 文件头部必须加入#-*-coding:utf-8-*-标识
+ 文件头注释包含：作者、时间、文件名、版本
### 二、	代码格式
+ 缩进：统一使用4个空格进行缩进
+ 行宽：单行不要超过 80 个字符(在特殊情况下可以略微超过 80 ，但最长不得超过 120)
+ 行连接：
	* 不要使用反斜杠连接行
	* Python会将 圆括号, 中括号和花括号中的行隐式的连接起来 , 你可以利用这个特点。如果需要, 你可以在表达式外围增加一对额外的圆括号
	* 禁止复合语句，即一行中包含多个语句
	* if/for/while一定要换行
+ 引号：
	* 自然语言使用双引号，机器标示使用单引号
	* 同一个文件中, 保持使用字符串引号的一致性. 使用单引号'或者双引号"之一用以引用字符串, 并在同一文件中沿用. 在字符串内可以使用另外一种引号, 以避免在字符串中使用
+ 空行：
	* 模块级函数和类定义之间空两行
	* 类成员函数之间空一行
	* 函数中可以使用空行分隔出逻辑相关的代码
### 三、	Import语句
+ import 语句应该分行书写
+ import语句应该使用 absolute import
+ import语句应该放在文件头部，位于模块注释和文档字符串之后, 模块全局变量和常量之前
+ import语句应该按照顺序排列，每组之间用一个空行分隔
+ 导入应该按照从最通用到最不通用的顺序分组
### 四、	空格
+ 在二元运算符两边各空一格[=,-,+=,==,>,in,is not, and]
+ 函数的参数列表中，,之后要有空格
+ 函数的参数列表中，默认值等号两边不要添加空格
+ 左括号之后，右括号之前不要加多余的空格
+ 字典对象的左括号之前不要多余的空格
+ 不要为对齐赋值语句而使用的额外空格
+ 不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾)
### 五、	注释
+ 块注释：“#”号后空一格，段落间用空行分开（同样需要“#”号
+ 行注释：至少使用两个空格和语句分开
+ 在代码的关键部分(或比较复杂的地方), 能写注释的要尽量写注释
+ 文档注释：以 """ 开头和结尾, 包含内容：文件名、作者、时间、版本
+ 方法注释：定义前对其进行注释，描述实现功能、输入输出、参数含义、抛出异常说明
### 六、	命名
+ 使用大驼峰(CamelCase)命名风格，如有多个单词，用下划线隔开
+ 变量名尽量小写, 如有多个单词，用下划线隔开
+ 常量采用全大写，如有多个单词，使用下划线隔开




