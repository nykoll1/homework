class Player:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.stats = {}  
    def add_stat(self, stat_name, value):
        self.stats[stat_name] = value
    def show_info(self):
        print(f"{self.name} ({self.age} წლის  {self.nationality}) სტატისტიკა: {self.stats}")

class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        print(f"{player.name} დაემატა გუნდს {self.team_name}")

    def remove_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                print(f"{player_name} წაიშალა გუნდიდან {self.team_name}")
                return
        print(f"მოთამაშე {player_name} ვერ მოიძებნა ")

    def find_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                return p
        return None

    def show_team_info(self):
        
        print(f"\n გუნდის სახელი: {self.team_name}")
        print(f"მწვრთნელი: {self.coach}")
        print("მოთამაშეები:")
        for p in self.players:
            print(f"  {p.name} ({p.age} წლის {p.nationality})")

team = FootballTeam("Barcelona", "Xavi Hernandez")
player1 = Player("Pedri", 21, "Spain")
player2 = Player("Lewandowski", 36, "Poland")
team.add_player(player1)
team.add_player(player2)
team.show_team_info()
p = team.find_player("Pedri")
if p:
    p.add_stat("goal", 8)
    p.add_stat("assist", 12)
    p.show_info()
team.remove_player("Lewandowski")
team.show_team_info()