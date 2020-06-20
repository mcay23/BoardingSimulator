import BenchmarkTools
import models


BenchmarkTools.benchmark("Random")
BenchmarkTools.benchmark("BackToFront")
BenchmarkTools.benchmark("FrontToBack")
BenchmarkTools.benchmark("WindowMA")
BenchmarkTools.benchmark("WMAGroups")
BenchmarkTools.benchmark("SteffenOptimal")
BenchmarkTools.benchmark("SimulationOptimal")
