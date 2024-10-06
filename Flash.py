import flet as ft
import random
import time

def main(page: ft.Page):

###タイトルへ戻る###
    def restart(clear_container, Announcement_container, restart_container):
        page.controls.remove(clear_container)
        page.controls.remove(Announcement_container)
        page.controls.remove(restart_container)
        page.add(title_container, result_container,flash_container, start_container)
        page.update()

###結果発表###
    def score_announcement(e):
        global clear,miss
        end_time = time.time()
        page.controls.remove(screen)
        page.update()
        result_time = end_time - start_time
        #print(f"経過時間{result_time}")

        clear = page.client_storage.get("clear")
        miss = page.client_storage.get("miss")

###0.5秒以下なら合格###
        if result_time <= 0.5:
            flag  = "合格!!"
            clear = clear + 1
            print(clear)
        else:
            flag = "不合格"
            miss = miss + 1

        page.client_storage.set("clear", clear)
        page.client_storage.set("miss", miss)

### クリア回数と失敗回数を更新 ###
        clear_result.value = f"本日クリアした回数：{page.client_storage.get('clear')}"
        miss_result.value = f"本日クリアできなかった回数：{page.client_storage.get('miss')}"


###合否と秒数とタイトルへ戻るボタンを表示###
        clear_container = ft.Container(
        content = ft.Text(flag,
                        weight = ft.FontWeight.W_900,
                        size = 80,
                        ),
        alignment = ft.alignment.center
    )
        
        Announcement_container = ft.Container(
        content = ft.Text(f"あなたの反射神経は{result_time}秒でした",
                        weight = ft.FontWeight.W_900,
                        size = 20,
                        ),
        alignment = ft.alignment.center
    )
        
        restart_container = ft.Container(
        content = ft.ElevatedButton(
                                    text = "タイトルへ戻る",
                                    on_click=lambda e: restart(clear_container, Announcement_container, restart_container)
                                   ),
        alignment = ft.alignment.bottom_center,
    )
        

        page.controls.append(clear_container)
        page.controls.append(Announcement_container)
        page.controls.append(restart_container)
        page.update()
        
            


###時間経過で円が出現###
    def game(e):
        global screen,start_time,random_time
        page.controls.remove(title_container)
        page.controls.remove(result_container)
        page.controls.remove(flash_container)
        page.controls.remove(start_container)
        page.update()

        random_time = random.uniform(1,5)
        time.sleep(random_time)


        screen = ft.Container(
            width = page.width,
            height = page.height,
            bgcolor = ft.colors.TRANSPARENT,
            on_click=score_announcement,
            content = ft.CircleAvatar(
            radius = 50,
            color = ft.colors.BLUE,
            )
        )
        start_time = time.time()
        page.controls.append(screen)
        page.update()


    
    global clear,miss,clear_result,miss_result
    
    #clear = 0
    #miss = 0

    page.client_storage.set("clear", 0)
    page.client_storage.set("miss", 0)

    page.title = "Flash"
    page.window.width = 360
    page.window.height = 640

###タイトル文字###
    title_container = ft.Container(
        content = ft.Text("Flash",
                          weight = ft.FontWeight.W_900,
                          size = 100,
                         ),
        alignment = ft.alignment.center
    ) 

###クリア回数の表示###
    clear_result = ft.Text(f"本日クリアした回数：0")
    miss_result  = ft.Text(f"本日クリアできなかった回数：0")

    result_container = ft.Container(
        content=ft.Column([clear_result, miss_result], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
    )
    
###Flash説明###
    flash_container = ft.Container(
        content = ft.Text("円が出現するので0.5秒以内にクリックしてください!"),
        alignment=ft.alignment.center,
    )



###スタートボタン###
    start_container = ft.Container(
        content = ft.ElevatedButton(
                                    text = "start",
                                    on_click = game,
                                   ),
        alignment = ft.alignment.bottom_center,
    )

    page.add(title_container,result_container,flash_container,start_container)

ft.app(target=main)

