## 自動化處理Script
這是一個可以跟使用者互動的command line interface，能幫忙加入新host，disable掉不需要的host，列出所有host，以及得到指定的host的某個port的近期流量截圖。此script有兩個大優點，一是使用者不需要去了解如何操作web介面，二是當有場合需要大量新增或刪除host（例如系館網路架構大翻新）時，web介面要一個一個點，script則可一次方便加入多個。執行方式為`python3 main.py`(必須在系上vlan 99的環境下執行)，下面為操作介面：

```
[*] Welcome to Zabbix tool, please enter the ta221 password first :)
Password: 
[-] Select the number of function to use or key 'q' to leave
 [1] Add New Host
 [2] Disable an Existing Host
 [3] List All Existing Hosts
 [4] Screenshot
```

輸入功能編號後四種功能可能會分別問一些需要的資訊，如:
- [1]會問你新主機的ip和名稱
- [2]會列出主機列表後問你要disable哪一台
- [3]列出所有主機列表
- [4]則會問你想要看的主機，列出他所有port後問你想看哪個port，然後再問你截圖要存至哪個檔案。



下面為一個demo使用方式的影片，影片中我們使用此script新增了一台測試用主機，接著把他disable掉，去web介面確認他真的被disable掉了，接著使用screenshot功能，指定CSIE-Core的to NTU CC的port來看看他的近期流量並儲存截圖。

[影片連結](https://drive.google.com/file/d/1qUBVbDKHKtqU1bNq5c6UsPMAz4Xw_Dfk/view?usp=sharing)
