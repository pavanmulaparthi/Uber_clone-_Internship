import time

class SessionManager:
    def __init__(self, expiry_seconds: int):
        """
        Initialize the session manager.
        :param expiry_seconds: Duration in seconds a session remains active.
        """
        self.expiry_seconds = expiry_seconds
        self.sessions = {}  # {session_id: creation_time}

    def create_session(self, session_id: str) -> None:
        """
        Create a new session.
        :param session_id: Unique session identifier.
        """
        self.sessions[session_id] = time.time()

    def is_session_active(self, session_id: str) -> bool:
        """
        Check if a session is active.
        If expired, delete it automatically.
        :param session_id: Unique session identifier.
        :return: True if active, False otherwise.
        """
        if session_id not in self.sessions:
            return False

        created_at = self.sessions[session_id]
        if time.time() - created_at < self.expiry_seconds:
            return True
        else:
            # Session expired → auto-delete
            del self.sessions[session_id]
            return False

    def delete_session(self, session_id: str) -> str:
        """
        Delete a session manually.
        :param session_id: Unique session identifier.
        :return: "Deleted" if found, else "Not Found".
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            return "Deleted"
        return "Not Found"


if __name__ == "__main__":
    manager = SessionManager(expiry_seconds=5)

    # Create a session
    manager.create_session("driver123")
    print("Created session for driver123")

    # Check immediately
    print("Active?", manager.is_session_active("driver123"))  # True

    # Wait 6 seconds to force expiry
    time.sleep(6)
    print("Active after 6s?", manager.is_session_active("driver123"))  # False

    # Manually delete (already expired, so "Not Found")
    print(manager.delete_session("driver123"))
