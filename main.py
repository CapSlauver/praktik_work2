import time
import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __str__(self):
        return f"User({self.nickname})"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        return False


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return f"Video('{self.title}')"


class UrTube:
    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = None

    def register(self, nickname, password, age):
        existing_user = next((user for user in self.users if user.nickname == nickname), None)
        if existing_user:
            print(f"Пользователь {nickname} уже существует.")
            return False  # Return False if user already exists

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(nickname, hashed_password, age)
        self.users.append(new_user)
        print(f"Пользователь {nickname} успешно зарегистрирован.")
        return True


    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if user.password == hashed_password:
                    self.current_user = user
                    print(f"Пользователь {nickname} успешно вошёл.")
                    return True
                else:
                    print("Неверный пароль.")
                    return False
        print(f"Пользователь {nickname} не найден.")
        return False


    def log_out(self):
        self.current_user = None
        print("Вы вышли из системы.")


    def add(self, *videos):
        self.videos.extend(videos)

    def get_videos(self, query):
        results = [video.title for video in self.videos if query.lower() in video.title.lower()]
        return results

    def watch_video(self, title):
        video_found = False
        for video in self.videos:
            if video.title.lower() == title.lower():
                video_found = True
                if self.current_user is None:
                    print("Пожалуйста, войдите в систему для просмотра.")
                    return
                elif video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    return
                else:
                    for _ in range(video.duration):
                        time.sleep(0.1)  # Adjust delay as needed
                        video.time_now += 1
                        print(video.time_now, end=" ")
                    print("\nВидео окончено.")
                    video.time_now = 0
                break

        if not video_found:
            print(f"Видео '{title}' не найдено.")


# Example Usage
ur = UrTube()
video1 = Video('Лучший язык программирования 2024 года', 5)
video2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(video1, video2)

print(ur.get_videos('лучший'))
print(ur.get_videos('программист'))

ur.register('vasya_pupkin', '12345', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'qwerty', 25)
ur.watch_video('Для чего девушкам парень программист?')


ur.register('vasya_pupkin', 'new_password', 55)
print(ur.current_user)

ur.log_in("vasya_pupkin", "new_password")
ur.watch_video('Для чего девушкам парень программист?')

ur.log_out()
