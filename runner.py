import subprocess
import os
from datetime import datetime

keyword = 'CHATGPT'

cmd = ['git', 'log', '-1', '--pretty=%B']
result = subprocess.run(cmd,
                        text=True, shell=False, capture_output=True)
commit_message_for_keyword = result.stdout

cmd = ['git', 'log', '-1', '--format=format:', '--name-only']
result = subprocess.run(cmd,
                        text=True, shell=False, capture_output=True)
commit_message_filename = result.stdout

if keyword in commit_message_for_keyword:
    full_path = commit_message_filename
    # commit_message_for_keyword.split(' ', maxsplit=1)[-1]
    path_head,filename = os.path.split(full_path)
    result_filename, _ = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    result_filename = f'{result_filename}_feedback_{timestamp}'
    result_filename = result_filename.upper() + '.md'
    result_path = os.path.join(path_head,result_filename)

    with open(result_path, 'w') as file:
        file.write('HAHAHHA')


# print(commit_message_for_keyword)
print(result_path)
print(result_filename)
