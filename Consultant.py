from connection import connection
import datetime


class ConsultantClass:

    def __init__(self, UserId, Steps, Plan, Title, JobCategory, SubCategory, Description, FileName, FileLocation, FileData, ProjectType,
                 Describes, WorkType, ApiToIntegrate, ProjectStage, ImpSkills, LookingSkills, JobCanSeenBy, PayBy, ProjectDuration,
                 TimeRequirement, SpecificBudget, Urgency, Feature, Done):

        #self.type = type
        self.UserId=UserId
        self.Steps=Steps
        self.Plan=Plan
        self.Title=Title
        self.JobCategory=JobCategory
        self.SubCategory=SubCategory
        self.Description=Description
        self.FileName=FileName
        self.FileLocation=FileLocation
        self.FileData=FileData
        self.ProjectType=ProjectType
        self.Describes=Describes
        self.WorkType=WorkType
        self.ApiToIntegrate=ApiToIntegrate
        self.ProjectStage=ProjectStage
        self.ImpSkills=ImpSkills
        self.LookingSkills=LookingSkills
        self.JobCanSeenBy=JobCanSeenBy
        self.PayBy=PayBy
        self.ProjectDuration=ProjectDuration
        self.TimeRequirement=TimeRequirement
        self.SpecificBudget=SpecificBudget
        self.Urgency=Urgency
        self.Feature=Feature
        self.Done=Done

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
            print("data retrieved from getConsultantById: ", data)
            return data

    def insertFirstStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO consultant (Plan, UserId, LastStep=%s, created_at, updated_at) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (self.Plan, self.UserId, self.Steps, datetime.datetime.now(), datetime.datetime.now()))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateFirstStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Plan = %s, LastStep=%s, updated_at=%s Where UserId = %s"
                cursor.execute(sql, (self.Plan, self.Steps, datetime.datetime.now(), self.UserId ))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateSecondStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Title = %s, LastStep=%s, updated_at=%s, JobCategory=%s, SubCategory=%s  Where UserId = %s"
                cursor.execute(sql, (self.Title, self.Steps, datetime.datetime.now(), self.JobCategory, self.SubCategory, self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateThirdStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Description=%s, LastStep=%s,  FileName = %s,  FileLocation = %s,  FileData = %s, updated_at=%s   Where UserId = %s"
                cursor.execute(sql, (self.Description, self.Steps, self.FileName, self.FileLocation, self.FileData, datetime.datetime.now(), self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateFourStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set ProjectType = %s, LastStep=%s,  Describes = %s, WorkType = %s, ApiToIntegrate = %s, ProjectStage = %s, updated_at=%s Where UserId = %s"
                cursor.execute(sql, (self.ProjectType, self.Steps, self.Describes, self.WorkType, self.ApiToIntegrate, self.ProjectStage, datetime.datetime.now(), self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateFiveStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set ImpSkills = %s, LastStep=%s, LookingSkills = %s, updated_at=%s  Where UserId = %s"
                cursor.execute(sql, (self.ImpSkills, self.Steps, self.LookingSkills, datetime.datetime.now(), self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateSixStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set ProjectType = %s, LastStep=%s, Describes = %s, WorkType = %s, ApiToIntegrate = %s, ProjectStage = %s, updated_at=%s Where UserId = %s"
                cursor.execute(sql, (self.ProjectType, self.Steps, self.Describes, self.WorkType, self.ApiToIntegrate, self.ProjectStage, datetime.datetime.now(), self.UserId))
                connection.commit()
                cursor.close()
        finally:
            return ""

    def updateSevenStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set ProjectType = %s, LastStep=%s, Describes = %s, WorkType = %s, ApiToIntegrate = %s, ProjectStage = %s, updated_at=%s Where UserId = %s"
                cursor.execute(sql, (self.ProjectType, self.Steps, self.Describes, self.WorkType, self.ApiToIntegrate, self.ProjectStage, datetime.datetime.now(), self.UserId))
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

        if self.Steps == 'step5':
            if consultantRecords is not None:
                ConsultantClass.updateFiveStepConsultantLink(self)

        if self.Steps == 'step6':
            if consultantRecords is not None:
                ConsultantClass.updateSixStepConsultantLink(self)

        if self.Steps == 'step7':
            if consultantRecords is not None:
                ConsultantClass.updateSevenStepConsultantLink(self)
