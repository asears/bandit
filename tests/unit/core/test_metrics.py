# SPDX-License-Identifier: Apache-2.0

import testtools
from bandit.core.metrics import Metrics


class BanditCoreMetricsTests(testtools.TestCase):

    def test_begin_begins_collection(self):
        metrics = Metrics()
        fname = "test"
        expected = {'loc': 0, 'nosec': 0}

        metrics.begin(fname)  # act

        self.assertEqual(expected, metrics.data[fname])

    def test_note_nosec_increments_count(self):
        metrics = Metrics()
        metrics.current = {}
        metrics.current['nosec'] = 1
        num = 2
        expected = 3

        metrics.note_nosec(num)  # act

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

        metrics.count_issues(scores)  # act

    def test_aggregate(self):
        metrics = Metrics()
        metrics.data = {}

        metrics.aggregate()  # act

    def test_get_issue_counts(self):
        metrics = Metrics()
        scores = {}

        metrics._get_issue_counts(scores)  # act
