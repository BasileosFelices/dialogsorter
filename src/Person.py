class Person:
    def __init__(self, name, email, schoolclass, time, preferences):
        self.mName = name
        self.mEmail = email
        self.mSchoolClass = schoolclass
        self.mTime = time
        self.mPreferences = preferences
    def __str__(self):
        return " ".join([self.mName, self.mEmail, self.mSchoolClass, str(self.mTime), str(self.mPreferences)])