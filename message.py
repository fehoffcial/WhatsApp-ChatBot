from time import sleep
class Message():
    def __init__(self,twms,SendMessage,TrainingPhrases,SendFeedBack):
        self.twms = twms
        self.SendMessage = SendMessage
        self.TrainingPhrases = TrainingPhrases
        self.SendFeedBack = SendFeedBack
        try:
            notification = twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("[class=_2Q3SY]").click()
            if notification.text:
                checkmsg = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("[class=tSmQ1]").find_elements_by_css_selector("[data-id^=false]")[-1].text.lower()
                if self.TrainingPhrases.lower() in checkmsg:
                    send = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.SendMessage)
                    send_msg = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("[class=_3qpzV]").click()
                    # finish = twms.find_element_by_css_selector("[id=pane-side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()
                    sleep(0.5)
                else:
                    send = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.SendFeedBack)
                    send_msg = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("[class=_3qpzV]").click()
                    sleep(0.5)
            else:
                checkmsg = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector(
                    "[class=tSmQ1]").find_elements_by_css_selector("[data-id^=false]")[-1].text.lower()
                if self.TrainingPhrases.lower() in checkmsg:
                    send = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.SendMessage)
                    send_msg = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("[class=_3qpzV]").click()
                    # finish = twms.find_element_by_css_selector("[id=pane-side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()
                    sleep(0.5)
                else:
                    send = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.SendFeedBack)
                    send_msg = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("[class=_3qpzV]").click()
                    sleep(0.5)
        except:
            self.twms.refresh()
            sleep(10)
