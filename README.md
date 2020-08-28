# Certbot Manual DNS

使用 DNS 验证方式为 Certbot 续约 Let's Encrypt 通配符证书的自动化脚本 

> python 版本需要 > 3.5

## 使用

克隆该项目

```shell script
git clone https://github.com/kainonly/certbot-manual-dns.git
```

为脚本安装依赖，并增加执行权限

- `requests`
- `aliyun-python-sdk-core` 阿里云SDK核心库
- `aliyun-python-sdk-alidns` 阿里云DNS解析库

```shell script
pip install requests aliyun-python-sdk-core aliyun-python-sdk-alidns
chmod +x ./bootstrap.py
```

以 `example.config.ini` 为例，在项目更目录中设置 `config.ini` 配置文件，其中 section 对应主域名，例如 `kainonly.com`

- **platform** 为云服务商类型，当前支持：`qcloud` 腾讯云 `aliyun` 阿里云
- **id** 为云服务商访问密钥ID
- **key** 为云服务商访问密钥内容
- **ttl** 解析TTL，默认 `600`

执行续约任务

```shell script
certbot renew --manual-auth-hook ./bootstrap.py
```

也可以为其编写定时脚本，例如：新建 `/etc/letsencrypt/task.sh`

```shell script
#!/bin/sh
uptime >> /var/log/certbot.log
certbot renew --manual-auth-hook /opt/certbot-manual-dns/bootstrap.py --deploy-hook "docker-compose -f /opt/compose/docker-compose.yml restart nginx" >> /var/log/certbot.log
```

添加执行权，将其加入定时任务

```shell script
chmod +x /etc/letsencrypt/task.sh

crontab -e
0 */12 * * * /etc/letsencrypt/task.sh
```