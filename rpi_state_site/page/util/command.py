import subprocess


def run_shell_command(args):
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = process.communicate()

    if err is not None:
        import page
        err = err.decode('unicode_escape')
        page.app.logger.warning(err)

    if out is not None:
        out = out.decode('unicode_escape')

    return out, err
