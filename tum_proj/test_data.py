from datetime import datetime

from pydantic import BaseModel

class PullRequestModel(BaseModel):
    labNumber: int
    studentName: str
    date: datetime
    group: str
    numOfPassedLabs: int
    numOfRepasses: int
    prId: str
    studentId: str
    prLink: str

class PullRequestData:
    def __init__(self):
        self.data = [
            PullRequestModel(labNumber=1, studentName="test", date=datetime(2024, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
            PullRequestModel(labNumber=2, studentName="test", date=datetime(2023, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
            PullRequestModel(labNumber=3, studentName="БАГАУТДИНОВ Даниил", date=datetime(2023, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
            PullRequestModel(labNumber=4, studentName="Бугаенко Иван", date=datetime(2023, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
            PullRequestModel(labNumber=5, studentName="Фадеев Павел", date=datetime(2023, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=2, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
            PullRequestModel(labNumber=6, studentName="ЗОТОВ Никита", date=datetime(2023, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
            PullRequestModel(labNumber=7, studentName="ЗОТОВ Никита", date=datetime(2023, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
            PullRequestModel(labNumber=8, studentName="ШИРОКОВСКИЙ Данил", date=datetime(2023, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
            PullRequestModel(labNumber=9, studentName="САФРОНОВ Александр", date=datetime(2023, 12, 31), group="ФИТ-212", numOfPassedLabs=0, numOfRepasses=0, prId="1", studentId="2", prLink="https://github.com/Aleshua/OMSTU-lubs5/pull/11"),
        ]