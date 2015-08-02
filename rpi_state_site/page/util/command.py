import subprocess


def run_shell_command(arg):
    process = subprocess.Popen(arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = process.communicate()

    if err is not None:
        err = err.decode('unicode_escape')

    if out is not None:
        out = out.decode('unicode_escape')

    return out, err
