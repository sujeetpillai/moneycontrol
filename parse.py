__author__ = 'sujeet'
import requests
import BeautifulSoup

SEC_ID = '534249'

while True:
    r = requests.get('http://www.moneycontrol.com/mccode/common/get_pricechart_div.php?bse_id=Y&nse_id=Y&sc_id=%s&BNsetick=53.682|02.682&ins=&sc_mapindex=23' % SEC_ID)

    if r.status_code == 200:
        b=BeautifulSoup.BeautifulSoup(r.text)
        BSE_Quote = b.find('span',dict(id='Bse_Prc_tick')).findChild('strong').text
        NSE_Quote = b.find('span',dict(id='Nse_Prc_tick')).findChild('strong').text

        BSE_Bid_Price_Qty = [k for k in b.findAll('div',{'class':'PT3 PB3 UC gL_10'}) if k.text=='Bid PRICE (QTY.)'][0].findNextSibling().text

        print "BSE SBI - %s | NSE SBI - %s | Bid Price (Qty) %s" % (BSE_Quote,NSE_Quote, BSE_Bid_Price_Qty)
    import time
    time.sleep(10)


