①実行したSQL
```
INSERT INTO company_info_tbl (会社番号, 会社名, 所在地, 会社概要)
VALUES ('1', 'ステップ情報システム', '東京都文京区湯島1-23-4', '');
```

②結果確認
```
select * from company_info_tbl;

会社番号	会社名	所在地	会社概要
1	ステップ情報システム	東京都文京区湯島1-23-4	
```
