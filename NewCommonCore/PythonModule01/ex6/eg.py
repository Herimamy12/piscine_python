# ft_garden_analytics.py


class GardenManager:
    """
    Coordinates multiple gardens, nested analytics, and plant hierarchies.
    Organizes all functionality without scattered globals.
    """

    class GardenStats:
        """
        Nested statistics helper for analytics across gardens and per garden.
        """

        def __init__(self, garden):
            self.garden = garden

        def total_plants(self):
            return len(self.garden.plants)

        def total_growth_cm(self):
            return sum(p.cm_grown for p in self.garden.plants)

        def plant_type_breakdown(self):
            regular = sum(
                1 for p in self.garden.plants
                if isinstance(p, GardenManager.Plant)
                and not isinstance(p, GardenManager.FloweringPlant)
            )
            flowering = sum(
                1 for p in self.garden.plants
                if isinstance(p, GardenManager.FloweringPlant)
                and not isinstance(p, GardenManager.PrizeFlower)
            )
            prize = sum(
                1 for p in self.garden.plants
                if isinstance(p, GardenManager.PrizeFlower)
            )
            return regular, flowering, prize

        def total_height_cm(self):
            return sum(p.height_cm for p in self.garden.plants)

        def flowering_count(self):
            return sum(
                1 for p in self.garden.plants
                if isinstance(p, GardenManager.FloweringPlant)
            )

        def total_prize_points(self):
            return sum(
                getattr(p, "prize_points", 0) for p in self.garden.plants
            )

        def garden_score(self):
            return (
                self.total_height_cm()
                + (self.flowering_count() * 10)
                + (self.total_prize_points() * 2)
            )

    class Plant:
        """Base plant in the hierarchy."""

        def __init__(self, name, height_cm):
            self.name = name
            self.height_cm = height_cm
            self.cm_grown = 0

        def grow(self, cm=1):
            if not GardenManager.validate_height(cm):
                return
            self.height_cm += cm
            self.cm_grown += cm
            print(f"{self.name} grew {cm}cm")

        def __str__(self):
            return f"{self.name}: {self.height_cm}cm"

    class FloweringPlant(Plant):
        """Flowering plant with bloom color state."""

        def __init__(self, name, height_cm, flower_color, blooming=True):
            super().__init__(name, height_cm)
            self.flower_color = flower_color
            self.blooming = blooming

        def __str__(self):
            bloom_state = "blooming" if self.blooming else "not blooming"
            return (
                f"{self.name}: {self.height_cm}cm, "
                f"{self.flower_color} flowers ({bloom_state})"
            )

    class PrizeFlower(FloweringPlant):
        """Prize-winning flower with extra scoring points."""

        def __init__(
            self,
            name,
            height_cm,
            flower_color,
            prize_points,
            blooming=True,
        ):
            super().__init__(name, height_cm, flower_color, blooming=blooming)
            self.prize_points = prize_points

        def __str__(self):
            base = super().__str__()
            return f"{base}, Prize points: {self.prize_points}"

    class Garden:
        """Holds plants and delegates analytics to GardenStats."""

        def __init__(self, owner):
            self.owner = owner
            self.plants = []
            self.stats = GardenManager.GardenStats(self)

        def add_plant(self, plant):
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.owner}'s garden")

        def help_all_grow(self, cm=1):
            print(f"\n{self.owner} is helping all plants grow...")
            for plant in self.plants:
                plant.grow(cm)

        def report(self):
            print(f"\n=== {self.owner}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.plants:
                print(f"- {plant}")

            regular, flowering, prize = self.stats.plant_type_breakdown()
            print(
                f"\nPlants added: {self.stats.total_plants()}, "
                f"Total growth: {self.stats.total_growth_cm()}cm"
            )
            print(
                f"Plant types: {regular} regular, "
                f"{flowering} flowering, {prize} prize flowers"
            )

    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        self.gardens.append(garden)

    def total_gardens(self):
        return len(self.gardens)

    @classmethod
    def create_garden_network(cls):
        """
        Class-level factory to build a pre-wired network of gardens.
        """
        manager = cls()

        alice = cls.Garden("Alice")
        oak = cls.Plant("Oak Tree", 100)
        rose = cls.FloweringPlant("Rose", 25, "red", blooming=True)
        sunflower = cls.PrizeFlower(
            "Sunflower", 50, "yellow", prize_points=10, blooming=True
        )

        alice.add_plant(oak)
        alice.add_plant(rose)
        alice.add_plant(sunflower)
        alice.help_all_grow(cm=1)

        bob = cls.Garden("Bob")
        bonsai = cls.Plant("Bonsai", 50)
        prize_daisy = cls.PrizeFlower(
            "Prize Daisy", 12, "white", prize_points=10, blooming=True
        )

        bob.add_plant(bonsai)
        bob.add_plant(prize_daisy)

        manager.add_garden(alice)
        manager.add_garden(bob)
        return manager

    @staticmethod
    def validate_height(value):
        """Utility: simple non-negative height increment validation."""
        return isinstance(value, (int, float)) and value >= 0

    @staticmethod
    def format_cm(value):
        """Utility: format centimeters with unit."""
        return f"{value}cm"

    def garden_scores(self):
        """Instance-level analytics across all managed gardens."""
        return {garden.owner: garden.stats.garden_score()
                for garden in self.gardens}


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()

    for garden in manager.gardens:
        garden.report()

    print("\nHeight validation test:", GardenManager.validate_height(1))

    scores = manager.garden_scores()
    print("Garden scores - Alice: ", end="")
    print(f"{scores.get('Alice')}, Bob: {scores.get('Bob')}")
    print(f"Total gardens managed: {manager.total_gardens()}")
