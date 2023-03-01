from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library) -> [str, None]:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library) -> [str, None]:
        if user not in library.user_records:
            return f"We could not find such user to remove!"

        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        try:
            curr_user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if new_username == curr_user.username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        for username, books in library.rented_books.items():
            if username == curr_user.username:
                del library.rented_books[username]
                library.rented_books[new_username] = books

        curr_user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
