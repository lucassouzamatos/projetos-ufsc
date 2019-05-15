from environs import Env as Envi

class Env:
    def __init__(self, key):
        env = Envi()
        env.read_env()
        self.value = env.str('MONGODB_URL') 