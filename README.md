# MapGeocoder
通过网络地图（高德地图/百度地图/腾讯地图）将字符串地址转为xy坐标

---
## 调用程序
- easyExcel

	windows环境下的Excel简单读写操作，需要安装[pywin32][0]

    **注意**
 1. 读写excel操作需要pywin32
 2. 需要使用excel文件的完整路径
 3. 只支持97-2000文件（后缀.xls）
 4. 下标均从1开始

- gcs2wgs84

    火星坐标系转换，参考 [wandergis/coordTransform_py][1]

- MapGeocoder
    网络地图转换（地址到坐标），需要申请地图API：
    + [高德地图API控制台][2]
      申请应用，服务平台勾选 **Web服务**，最后获得key
    + [百度地图][3]
      申请应用，应用类型选浏览器端，**地理编码**，最后获得key
    + [腾讯地图][4]
      申请应用，启用产品勾选，**WebServiceAPI** ，最后获得key

**all source code follow the [Apache][5] license.**

[0]: https://github.com/mhammond/pywin32/releases/tag/b227
[1]: https://github.com/wandergis/coordTransform_py
[2]: https://console.amap.com/dev/key/app
[3]: http://lbsyun.baidu.com/apiconsole/key#/home
[4]: https://lbs.qq.com/dev/console/application/mine
[5]: https://zh.wikipedia.org/wiki/Apache%E8%AE%B8%E5%8F%AF%E8%AF%81 