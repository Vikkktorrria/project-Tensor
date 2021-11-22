class PatientProfile:
    """Класс для работы с профилем пациента"""
    def __init__(self, fullName, passport, anamnesis):
        self.fullName = fullName
        self.passport = passport
        self.anamnesis = anamnesis


class DoctorProfile:
    """Класс для работы с профилем врача"""
    def __init__(self, fullName, qualification):
        self.fullName = fullName
        self.qualification = qualification


class Diagnosis:
    """Класс диагнозов"""
    def __init__(self, infAboutDiagnos):
        self.infAboutDiagnos = infAboutDiagnos


class Recipe:
    """Класс рецептов"""
    def __init__(self, infAboutRecipe):
        self.infAboutRecipe = infAboutRecipe


class Note(Diagnosis, Recipe):
    """Класс для работы записями на приём"""
    def __init__(self, date, information):
        self.date = date
        self.information = information


class Patient:
    """Класс для работы с пациентом"""
    profile = PatientProfile()  # записали классы как атрибуты
    notes = []

    def addNote(self, Note):
        self.notes.append(Note)


class Doctor:
    """Класс для работы с врачом"""
    profile = DoctorProfile()
    note = Note()

    def addNote(patient, Note):
        patient.notes.append(Note)
