from botcity.core import DesktopBot
from IBGEBot import resources
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
        
        if not self.find( "selecione", matching=0.97, waiting_time=10000):
            self.not_found("selecione")
        self.click_relative(264, 9)
        #self.click()
        self.paste(local)
        self.enter()
        self.wait(5000)

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

    def load_image(self):
        self.add_image("selecione", self.get_resource_abspath("selecione.png"))
        self.add_image("exportar", self.get_resource_abspath("exportar.png"))
        self.add_image("baixar", self.get_resource_abspath("baixar.png"))


if __name__ == '__main__':
    Bot.main()













