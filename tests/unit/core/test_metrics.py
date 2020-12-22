import fixtures
import mock
import testtools
from mock import MagicMock
from bandit.core.metrics import Metrics

class BanditCoreMetricsTests(testtools.TestCase):
    
    def test_begin_begins_collection(self):
        metrics = Metrics()
        fname = "test"
        metrics.begin(fname)
        expected =  {'loc': 0, 'nosec': 0}
        self.assertEqual(expected, metrics.data[fname])

    def test_note_nosec_increments_count(self):
        metrics = Metrics()
        metrics.current = {}
        metrics.current['nosec'] = 1
        num = 2
        expected = 3
        metrics.note_nosec(num)
        self.assertEqual(expected, metrics.current['nosec'])
    
    # def test_count_locs(self):
    #     metrics = Metrics()
    #     metrics.current = {}
    #     metrics.current['loc'] = 0
    #     lines = "test"
    #     metrics.count_locs(lines)

    def test_count_issues(self):
        metrics = Metrics()
        scores = {}
        metrics.current = {}
        metrics.count_issues(scores)

    def test_aggregate(self):
        metrics = Metrics()
        scores = {}
        metrics.data = {}
        metrics.aggregate()
    
    def test_get_issue_counts(self):
        metrics = Metrics()
        scores = {}
        metrics._get_issue_counts(scores)

