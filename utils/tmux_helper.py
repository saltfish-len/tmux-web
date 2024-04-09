import libtmux


class TmuxHelper:
    def __init__(self):
        self.server = libtmux.Server()

    def get_session(self, session_name_or_id: str | int) -> libtmux.session.Session | None:
        """
        Get a tmux session by name or id
        :param session_name_or_id: name or id of session
        :return: the session if found, None if not found
        """
        # Get all session
        sessions = self.server.sessions
        if isinstance(session_name_or_id, int):
            for session in sessions:
                if session.id == session_name_or_id:
                    return session
        else:
            for session in sessions:
                if session_name_or_id == session.name:
                    return session
        return None

    def create_session(self, session_name: str) -> libtmux.Session | None:
        """
        create a new tmux session, if the session already exists, return None
        :param session_name: name of session
        :return: the session if created, None if the session already exists
        """
        if self.server.has_session(session_name):
            return None
        return self.server.new_session(session_name)

    def kill_session(self, session_name: str) -> bool:
        """
        kill a tmux session, if the session does not exist, return False
        :param session_name: name of the session
        :return: True if the session is killed, False if the session does not exist
        """
        if not self.server.has_session(session_name):
            return False
        self.server.kill_session(session_name)
        return True

    def set_environment(self, session_name: str, key: str, value: str) -> bool:
        """
        set an environment variable in a tmux session
        :param session_name: name of the session
        :param key: key of the environment variable
        :param value: value of the environment variable
        :return: True if the environment variable is set, False if the session does not exist
        """
        session = self.get_session(session_name)
        if session is None:
            return False
        session.set_environment(key, value)
        return True

    def run_command(self, session_name: str, command: [str]):
        """
        run a command in a tmux session
        :param session_name: name of the session
        :param command: command to run
        :return: the output of the command
        """
        session = self.get_session(session_name)
        if session is None:
            return False
        return session.cmd(*command)

    def get_stdout(self, session_name: str):
        """
        get the stdout of a tmux session
        :param session_name: name of the session
        :return: the stdout of the session
        """
        session = self.get_session(session_name)
        if session is None:
            return False
        return session.cmd("capture-pane", "-p")
