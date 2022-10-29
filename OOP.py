class Tomato:
    states = {1: 'First stage of maturity', 2: 'Second stage of maturity',
              3: 'Mature'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Tomato {self._index} - {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            return True
        return False


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('The gardener started work')
        self._plant.grow_all()
        print('The gardener finished fertilizing the tomatoes')

    def harvest(self):
        print('Checking tomato ripeness')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('All tomatoes are ripe!')
        else:
            print('Not all tomatoes are ripe, we still have to work and wait...')

    @staticmethod
    def knowledge_base():
        print('''Gardening tip: Pick tomatoes when they're all ripe
        Don't forget to fertilize and tend
        A good tomato is scarlet, firm''')


if __name__ == '__main__':
    Gardener.knowledge_base()
    tomato = TomatoBush(4)
    gardener = Gardener('Dan', tomato)
    # 3. Using an object of the Gardener class, take care of a tomato bush.
    # 4. Try to harvest
    # 5. If the tomatoes are not yet ripe, continue tending them
    # 6. Harvest the crop
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

