"""
### RankingSaveData

2023 CyberYoshi64

NOTE: That part of the save data is basically undocumented, this class is a dummy for now
"""

class RankingSaveData:
    def __init__(self, data=None):
        if data: self.load(data)
    def load(self, data):
        self.data = data
    def pack(self):
        return self.data
    def __str__(self):
        return f"<{__name__} object>"
    def __repr__(self): return str(self)
    