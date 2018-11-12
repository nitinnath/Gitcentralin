from connection import connection
import datetime


class ConsultantClass:

    def __init__(self, Steps, UserId, Plan, Title, Description, ProjectType, Describes, ConsultantDoing, API,
                 ProjectStage, Skill, SkillList,
                 SeeYourJob, PayPlan, ExpertiseLevel, HowLongNeed, TimeRequirement, SpecificBudget, UrgentProject):
        self.Steps = Steps
        self.Plan = Plan
        self.Title = Title
        self.Description = Description
        #self.UserId = UserId
        self.UserId = '112'
        self.ProjectType = ProjectType
        self.Describes = Describes
        self.ConsultantDoing = ConsultantDoing
        self.type = type
        self.API = API
        self.ProjectStage = ProjectStage
        self.Skill = Skill
        self.SkillList = SkillList
        self.SeeYourJob = SeeYourJob
        self.PayPlan = PayPlan
        self.ExpertiseLevel = ExpertiseLevel
        self.HowLongNeed = HowLongNeed
        self.TimeRequirement = TimeRequirement
        self.SpecificBudget = SpecificBudget
        self.UrgentProject = UrgentProject

    def getAllData(self):
        with connection.cursor() as cur:
            cur.execute("select * from personallink")
            data = cur.fetchall()
            cur.close()
            return data

    def getConsultantById(self):
        with connection.cursor() as cur:
            cur.execute("select * from consultant where UserId = '" + str(self.UserId) + "'")
            data = cur.fetchone()
            cur.close()
            return data

    def insertFirstStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO consultant (Plan,UserId) VALUES (%s, %s)"
                cursor.execute(sql, (self.Plan, self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateFirstStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Plan = %s Where UserId = %s"
                cursor.execute(sql, (self.Plan, self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateSecondStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Title = %s Where UserId = %s"
                cursor.execute(sql, (self.Title, self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateThirdStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Description = %s Where UserId = %s"
                cursor.execute(sql, (self.Description, self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateFourStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set ProjectType = %s,Describes = %s,ConsultantDoing = %s,API = %s,ProjectStage = %s Where UserId = %s"
                cursor.execute(sql, (
                self.ProjectType, self.Describes, self.ConsultantDoing, self.API, self.ProjectStage, self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def SaveConsultant(self):
        consultantRecords = ConsultantClass.getConsultantById(self)
        if self.Steps == 'step1':
            if consultantRecords is not None:
                ConsultantClass.updateFirstStepConsultantLink(self)
            else:
                ConsultantClass.insertFirstStepConsultantLink(self)

        if self.Steps == 'step2':
            if consultantRecords is not None:
                ConsultantClass.updateSecondStepConsultantLink(self)

        if self.Steps == 'step3':
            if consultantRecords is not None:
                ConsultantClass.updateThirdStepConsultantLink(self)

        if self.Steps == 'step4':
            if consultantRecords is not None:
                ConsultantClass.updateFourStepConsultantLink(self)
