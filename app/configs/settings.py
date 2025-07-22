import yaml
import os
from pathlib import Path

class Config(object):
    """
    配置类，用于读取和访问应用配置文件
    """
    def __init__(self):
        self.config_data = None
        self.load_config()
    
    def load_config(self):
        """
        加载配置文件
        """
        config_path = os.path.join(os.path.dirname(__file__), 'application.yaml')
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config_data = yaml.safe_load(f)
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            self.config_data = {}
    
    def get(self, key, default=None):
        """
        获取配置项
        :param key: 配置键，支持点号分隔的多级键，如 'app.name'
        :param default: 默认值，当配置项不存在时返回
        :return: 配置值
        """
        if not self.config_data:
            return default
            
        keys = key.split('.')
        value = self.config_data
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
                
        return value

# 创建全局配置实例
config = Config()