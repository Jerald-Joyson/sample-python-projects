class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def normalize(self):
        extra_minutes, self.seconds = divmod(self.seconds, 60)
        self.minutes += extra_minutes
        extra_hours, self.minutes = divmod(self.minutes, 60)
        self.hours += extra_hours

    def __add__(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        total_seconds = self.seconds + other.seconds

        result_time = Time(total_hours, total_minutes, total_seconds)
        result_time.normalize()
        return result_time

# Example usage
time1 = Time(1, 30, 45)
time2 = Time(2, 15, 20)

result_time = time1 + time2
print("Result:", result_time)
