# Certbot Manual DNS

使用 DNS 验证方式为 Certbot 续约 Let's Encrypt 通配符证书的自动化脚本 

## 使用

克隆该项目

```shell script
git clone https://github.com/kainonly/certbot-manual-dns.git
```

为脚本安装依赖，并增加执行权限

- `requests`

```shell script
pip install requests
chmod +x ./bootstrap.py
```

以 `example.config.ini` 为例，在项目更目录中设置 `config.ini` 配置文件，其中 section 对应主域名，例如 `kainonly.com`

- **platform** 为云服务商类型，当前支持：`qcloud` 腾讯云
- **id** 为云服务商访问密钥ID
- **key** 为云服务商访问密钥内容
- **ttl** 解析TTL，默认 `600`

执行续约任务

```shell script
certbot renew --manual-auth-hook ./bootstrap.py
```
