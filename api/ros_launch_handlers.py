from roslaunch import parent as launch_parent, rlutil


class LaunchFile:
    def __init__(self, filename: str, args: dict = None):
        self.__uuid = rlutil.get_or_generate_uuid(None, False)
        self.filename = filename

        if args is not None:
            self.args = [f"{key}:={val}" for key, val in args.items()]
        else:
            self.args = None

        self.launch_proc = launch_parent.ROSLaunchParent(self.__uuid, [(self.filename, self.args)])

    def start(self):
        self.launch_proc.start()

    def stop(self):
        self.launch_proc.shutdown()
