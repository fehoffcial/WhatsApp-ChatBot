from time import sleep
class Notification():
    def __init__(self,twms):
        self.twms = twms
        try:
            x = True
            while x:
                ## Notification ##
                noti = self.twms.find_element_by_css_selector("[id=pane-side]").find_elements_by_css_selector("[class=_2Q3SY]")
                for notis in noti:
                    if notis.text == notis.text:
                        # print(notis.text)
                        click = notis.click()
                        sleep(1)
                        x = False
        except:
            self.twms.refresh()
            sleep(10)
