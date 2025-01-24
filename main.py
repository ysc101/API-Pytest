import subprocess
scripts=["test_get_token.py","test_ecs_push.py","test_updatepayeedata.py"]

for script in scripts:
    subprocess.run(["python",script ])