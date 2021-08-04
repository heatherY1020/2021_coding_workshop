#LECTURE4 폴더에서 실행시켰다고 가정하고 만들었습니다.

import os
present_path = os.getcwd()
for i in os.listdir(present_path):
    print(i)

for i in os.listdir(os.path.join(present_path, '4-1.py')):
    print(i)
