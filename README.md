# BoardingSimulator
A model to visualize and benchmark different plane boarding methods

The default boarding types are:

* Random
* WindowMA
* WMAGroups
* BackToFront
* FrontToBack
* SteffenOptimal
* SteffenModified
* SimulationOptimal

# Benchmarking
Benchmarking a method is really easy:

```
BenchmarkTools.benchmark("Random", 100)
```

will bench Random boarding 100 times.

# Animating a boarding process

If you want to see an animation of the boarding, start with:

```
BenchmarkTools.write("Random", "random.txt")
```
This will create text file that you can run through [AsciiAnimator](https://github.com/ThatcherDev/AsciiAnimator)
to visualize.

# Creating your own boarding methods
Refer to BoardingMethods.py to create your own boarding methods.
