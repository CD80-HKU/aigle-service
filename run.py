from aigle_service import create_app
import os

env_dist = os.environ

config = env_dist.get('AIGLE_CONFIG', 'default')
app = create_app(config)
