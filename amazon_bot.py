import time
from datetime import datetime
from selenium import webdriver

LOGIN_ID="メールアドレス"
LOGIN_PASSWORD="パスワード"

ITEM_URL="購入したい商品のURL"

ACCEPT_SHOP="Amazon"

def l(str):
    print("%s : %s"%(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),str))

if __name__=="__main__":
    #ブラウザの起動
    try:
        b=webdriver.Edge(executable_path="./msedgedriver.exe")
        b.get(ITEM_URL)
    
    except:
        l("Failed to open browser.")
        exit()

    while True:
        #ログイン手続き
        try:
            b.get("購入したい商品のページからログイン画面に飛び、そのページのURLをここに貼る")
            b.find_element_by_id("ap_email").send_keys(LOGIN_ID)
            b.find_element_by_id("continue").click()
            b.find_element_by_id("ap_password").send_keys(LOGIN_PASSWORD)
            b.find_element_by_id("signInSubmit").click()
        
        except:
            l("LOGIN PASS.")
            pass

        #在庫確認
        while True:
            try:
                #販売元確認
                shop = b.find_element_by_id('merchant-info').text
                shop = shop.split('が販売')[0].split('この商品は、')[1]
            
                if ACCEPT_SHOP not in shop:
                    raise Exception("not Amazon.")
            
                #今すぐ買うボタンクリック
                b.find_element_by_id('buy-now-button').click()
                break

            #在庫がない場合10秒ごとにページ更新
            except:
                time.sleep(10)
                b.refresh()

        #注文の確定
        b.find_element_by_name('placeYourOrder1').click()
        break
    
    l("ALL DONE.")