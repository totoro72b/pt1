# use subprocess to manage child processes
import subprocess
import os
import random
from time import time

# simple child process using Popen
proc = subprocess.Popen(['echo', 'hello from the child!'], stdout=subprocess.PIPE)
out, err = proc.communicate()  # this get the output from the process
assert out.decode('utf-8') == 'hello from the child!\n'


##################
# child process works independently from the parent.
# can use poll to poll status

# NOTE setting studout below allows out, err=proc.communicate(), otherwise out=None
proc = subprocess.Popen(['sleep', '0.1'], stdout=subprocess.PIPE)
# NOTE if the following, then after communicate() returns, proc.poll() is NOT None.
# print('communicating...')
# out, err = proc.communicate()
# print('communicate out={} error={}'.format(out.decode('utf-8'), err))
while proc.poll() is None:
    print('still working...')
    # do_something_else()

print('exit status', proc.poll())


##################
# can run many child processes independently

def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

start = time()
procs = []
# start 10 process
for i in range(10):
    p = run_sleep(0.1)
    procs.append(p)

# wait for each to finish
for proc in procs:
    proc.communicate()

end = time()
print('finished in %.3f seconds' %  (end - start))
# NOTE total time ~ 0.1 seconds. i don't have 10 CPUS, so where does the 10x speed up come from?


##################
# pipe input from python program into the subprocess and then retrieve the results
def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Q13S\x11'
    proc = subprocess.Popen(
        # try what if pass password in direclty?
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()  # make sure the child gets the input
    return proc

# pipe random data into openssl
procs = []
for i in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

for p in procs:
    out, err = p.communicate()
    print('encrypted = {} err={}'.format(out, err))

########################3
# pipe output of one child process to the input of another
def run_md5(stdin_input):
    """run md5 on the input of another child process"""
    proc = subprocess.Popen(
        ['md5'],
        stdin=stdin_input,
        stdout=subprocess.PIPE)
    return proc


ssl_proc = []
md5_proc = []
for i in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    ssl_proc.append(proc)
    proc = run_md5(proc.stdout)
    md5_proc.append(proc)

# start them? or are they already started?
for p in ssl_proc:
    p.communicate()

for p in md5_proc:
    out, err = p.communicate()
    print('md5 result: %s' % out)


####################
# use timeout to terminate misbehaving child

proc = run_sleep(2)

try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('exit status:', proc.poll())
