"""Examples of Object-oriented Programming."""


class Profile:
    """An example of a simple social media profile model."""
    handle: str
    followrs: int
    is_private: bool

    def __init__(self, handle: str):
        """Initalizes all atributes of an object."""
        self.handle  = handle
        self.followers = 0
        self.is_private = False

    def tweet(self, message: str) -> None:
        print(f"@{self.handle} tweets {message}")


my_profile: Profile = Profile("KeeganB")
my_profile.tweet("Hello, world.")

