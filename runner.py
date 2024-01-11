import subprocess

keyword = 'CHATGPT_FEEDBACK'

cmd = ['git', 'log', '-1', '--pretty=%B']
result = subprocess.run(cmd,
                        text=True, shell=False, capture_output=True)
commit_message = result.stdout

if keyword in commit_message:
    filename = commit_message.split(' ')[-1]
