class Settings:
    def __init__(self):
        self.__PROJECT_NAME = "Porfolio"
        self.__PROJECT_VERSION = "v1.0"

    def get_project_config(self):
        return self.__PROJECT_NAME, self.__PROJECT_VERSION
    
setting = Settings()