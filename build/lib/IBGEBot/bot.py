from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
#Author: Wernen Veiga

class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        local = input("Digite o Local: ")
        self.browse("https://www.ibge.gov.br/cidades-e-estados")
        if not self.find( "selecionar", matching=0.97, waiting_time=10000):
            self.not_found("selecionar")
        self.click()
        self.paste(local)
        self.enter()
        #self.wait(10000)

        if not self.find( "exportar", matching=0.97, waiting_time=10000):
            self.not_found("exportar")
        self.click()
        self.wait(3000)

        if not self.find( "baixar", matching=0.97, waiting_time=10000):
            self.not_found("baixar")
        self.click_relative(30, 32)
        self.wait(3000)
        self.click()
        
        
    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()








