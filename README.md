node-monitor (节点监视器)
===

设计需求：大数据时代，企业的运维人员的工作量越来越大。因此，实现一个远程自动化的监控工具是很有必要的，可以省去大量手动运维的时间，提高运维效率。


Environment(环境)
---
本项目为python编写的项目。

- python3.6+

用到的库:

- paramiko      (linux ssh库)
- smtplib       (邮件库)
- APScheduler   (定时任务库）
- psutil        (系统信息库）

项目目录结构
---
node-monitor(:smiling_imp:)

    |--config
        |--global.py               (全局变量字典)
        |--init_configs.py      (读取ini初始化配置)
        |--linux_config.ini     (linux服务器配置文件)
        |--mail_settings.ini    (邮箱设置配置文件)
        |--time_config.ini      (cron定时设置配置文件)
    |--mail
        |--mail_sender.py        (发送邮件)
    |--monitor
        |--monitor.py           (监控linux模块,连接linux服务器)
    |--utils
        |--util.py              (工具类)
    |--run.py                   (程序入口)

