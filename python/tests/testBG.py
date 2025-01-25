#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import gyoto.core
import gyoto.std

class TestBGMetric(unittest.TestCase):
   def setUp(self):
       """Set up a BG metric instance before each test"""
       self.metric = gyoto.core.Metric("BG")
       # Set standard parameter values
       self.metric.set("V0", 0.000733333)
       self.metric.set("R", 100.0)
       self.metric.set("r0", 1.0)
       
   def test_parameters(self):
       """Test parameter getting/setting"""
       self.assertAlmostEqual(self.metric.get("V0"), 0.000733333, places=6)
       self.assertAlmostEqual(self.metric.get("R"), 100.0, places=6)
       self.assertAlmostEqual(self.metric.get("r0"), 1.0, places=6)
       
   def test_metric_components(self):
       """Test metric tensor components at a specific point"""
       pos = [0., 50., np.pi/2, 0.]
       
       # Test individual components - keeping 7 significant figures
       self.assertAlmostEqual(self.metric.gmunu(pos, 0, 0), -1.000000, places=6)     # exact
       self.assertAlmostEqual(self.metric.gmunu(pos, 0, 3), 0.02728484, places=8)    # 7 sig figs
       self.assertAlmostEqual(self.metric.gmunu(pos, 1, 1), 1.000000, places=6)      # exact
       self.assertAlmostEqual(self.metric.gmunu(pos, 2, 2), 2500.000, places=3)      # exact
       self.assertAlmostEqual(self.metric.gmunu(pos, 3, 0), 0.02728484, places=8)    # 7 sig figs
       self.assertAlmostEqual(self.metric.gmunu(pos, 3, 3), 2499.999, places=3)      # 7 sig figs

if __name__ == '__main__':
   unittest.main()
