# codesmith连接Mysql报错

## 1.错误详情

“找不到请求的 .Net Framework Data Provider。可能没有安装。"
![详情](pics\报错详情.png)

## 2、解决办法

1. 进入[https://dev.mysql.com/downloads/connector/net/](https://dev.mysql.com/downloads/connector/net/)下载 mysql-connector-net-X.X.X.msi,下载最新版本即可；
![下载](pics\下载.png)

2. 下载后进行安装，**记住安装目录**（我的安装目录是：C:\Program Files (x86)\MySQL\MySQL Connector NET 8.2.0），右键"**MySql.Data.dll**"文件，查看其版本；
![版本信息](pics\版本信息.png)

3. 进入目录"**C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config**"文件夹，打开"**machine.config**"文件，在
"**DbProviderFactories**"结点添加内容：

    注意：其中的版本号需与MySql.Data.dll版本号相同！！！

    ```python
    <DbProviderFactories>
            <remove invariant="MySql.Data.MySqlClient"/>
                <add name="MySQL Data Provider" invariant="MySql.Data.MySqlClient" description=".Net Framework Data Provider for MySQL" type="MySql.Data.MySqlClient.MySqlClientFactory, MySql.Data, Version=8.2.0.0, Culture=neutral, PublicKeyToken=c5687fc88969c44d"/>
    </DbProviderFactories>
    ```

4. 将”MySql.Data.dll"文件复制到codesmith安装目录下的"bin"和"SchemaProviders"下。
![复制](pics\复制.png)

5. 重启codesmith即可。
