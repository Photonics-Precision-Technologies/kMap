import os
import matplotlib.pyplot as plt
from kmap.library.sliceddata import SlicedData
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# Import the sliced data class from the model folder

# Get path to the directory this file is in
# ATTENTION FILE DOES NOT EXIT ANYMORE
file_path = os.path.dirname(os.path.realpath(__file__)) + '/../data/6584.hdf5'

# Loading from file (Initialisation methods are usually class members)
sliced_data = SlicedData.init_from_hdf5(file_path)
print(dir(sliced_data))

# Get a PlotData object consisting of the 10th slice and its axes
plot_data = sliced_data.slice_from_index(10)


# Plot
__, axes = plt.subplots()
axes.imshow(plot_data.data)
plt.show()