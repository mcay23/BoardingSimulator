import BenchmarkTools
import models

# BenchmarkTools.write("Random", "random.txt")
# BenchmarkTools.write("BackToFront", "btf.txt")
# BenchmarkTools.write("FrontToBack", "ftb.txt")
# BenchmarkTools.write("WindowMA", "wma.txt")
# BenchmarkTools.write("WMAGroups", "wmagroups.txt")
# BenchmarkTools.write("SteffenOptimal", "steffen.txt")
# BenchmarkTools.write("SteffenModified", "steffenmod.txt")

# BenchmarkTools.benchmark("Random", 100)
# BenchmarkTools.benchmark("BackToFront", 100)
# BenchmarkTools.benchmark("FrontToBack", 100)
# BenchmarkTools.benchmark("WindowMA", 100)
BenchmarkTools.benchmark("WMAGroups", 100)
# BenchmarkTools.benchmark("SteffenModified", 100)
