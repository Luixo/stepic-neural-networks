# debug code
import numpy as np
import random
mat = np.array(random.sample(range(1000), 12)) # ���������� ������ �� 12 ��������� ����� �� 1 �� 1000
mat = mat.reshape((2,2,3)) # ��������� w � ��������� �������
print(mat)
# production code
import numpy as np
mat = mat.reshape((12,1))
print(mat)
