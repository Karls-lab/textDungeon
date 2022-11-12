class MonsterManual():
    def __init__(self):
        self.goblinStats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHAR": 0, "AC": 10, "HP": 10}
        self.playerStats = {"STR": 10, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHAR": 0, "AC": 10, "HP": 10}

    def getGoblinStats(self):
        stats = dict(self.goblingStats)
        return stats

    def getPlayerStats(self):
        stats = dict(self.playerStats)
        return stats
