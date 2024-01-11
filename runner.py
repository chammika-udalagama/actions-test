import subprocess
import os
from datetime import datetime

keyword = 'CHATGPT_FEEDBACK'

cmd = ['git', 'log', '-1', '--pretty=%B']
result = subprocess.run(cmd,
                        text=True, shell=False, capture_output=True)
commit_message = result.stdout

if keyword in commit_message:
    filename = commit_message.split(' ', maxsplit=1)[-1]

    cmd = ['export', f'chatgpt_filename={filename}']
    subprocess.run(cmd)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    result_filename, _ = os.path.splitext(filename)
    result_filename = f'{result_filename}_feedback_{timestamp}'
    result_filename = result_filename.upper() + '.md'

    with open(result_filename, 'w') as file:
        file.write('HAHAHHA')
