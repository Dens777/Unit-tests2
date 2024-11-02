import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        out ={}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                out[k] = str(v)
            print(out)

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усэйн', 10)
        self.andrew = runner_and_tournament.Runner('Андрей', 9)
        self.nick = runner_and_tournament.Runner('Ник', 3)

    def test_start_tour_1(self):
        '''1'''
        tour = runner_and_tournament.Tournament(90, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[self.shortDescription()] = results

    def test_start_tour_2(self):
        '''2'''
        tour = runner_and_tournament.Tournament(90, self.andrew, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[self.shortDescription()] = results

    def test_start_tour_3(self):
        '''3'''
        tour = runner_and_tournament.Tournament(90, self.andrew, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[self.shortDescription()] = results


if __name__ == '__main__':
    unittest.main()
