import timeit
import numpy
normal_time=timeit.timeit('sum(x*x for x in range(1000))',number=10000)
naive_time=timeit.timeit('sum(na*na)',setup="import numpy as np; na=np.arange(1000)",number=10000)
good_time = timeit.timeit('na.dot(na)',setup="import numpy as np; na=np.arange(1000)",number=10000)

print("Normal Python: %f sec"%normal_time)
print("Naive Numpy: %f sec"%naive_time)
print("Good Numpy: %f sec"%good_time)
