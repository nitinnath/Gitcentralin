from connection import connection
import datetime

global data_dic
last_inserted_id = ""

class ConsultantClass:

    def __init__(self, UserId, Steps, Plan, Title, JobCategory, SubCategory, Description, FileName, FileLocation,
                 FileData, ProjectType,
                 Describes, WorkType, ApiToIntegrate, ProjectStage, ImpSkills, LookingSkills, JobCanSeenBy, PayBy,
                 ProjectDuration,
                 TimeRequirement, SpecificBudget, Urgency, Feature, sevenbutton, consultantID):

        # self.type = type
        self.UserId = UserId
        self.Steps = Steps
        self.Plan = Plan
        self.Title = Title
        self.JobCategory = JobCategory
        self.SubCategory = SubCategory
        self.Description = Description
        self.FileName = FileName
        self.FileLocation = FileLocation
        self.FileData = FileData
        self.ProjectType = ProjectType
        self.Describes = Describes
        self.WorkType = WorkType
        self.ApiToIntegrate = ApiToIntegrate
        self.ProjectStage = ProjectStage
        self.ImpSkills = ImpSkills
        self.LookingSkills = LookingSkills
        self.JobCanSeenBy = JobCanSeenBy
        self.PayBy = PayBy
        self.ProjectDuration = ProjectDuration
        self.TimeRequirement = TimeRequirement
        self.SpecificBudget = SpecificBudget
        self.Urgency = Urgency
        self.Feature = Feature
        self.sevenbutton = sevenbutton
        self.consultantID = consultantID
        # self.SaveExit=SaveExit

    def getAllData(self):
        with connection.cursor() as cur:
            cur.execute("select * from personallink")
            data = cur.fetchall()
            cur.close()
            return data

    def getConsultantById(self):
        print("into getConsultantById which is ", str(self.UserId))
        global last_inserted_id
        print(last_inserted_id)
        print("into getConsultantById last_inserted_id  and self.consultantID is ", str(last_inserted_id), str(self.consultantID))
        try:
            with connection.cursor() as cur:
                cur.execute("select * from consultant where UserId = '" + str(self.UserId) + "' and Id='"+str(last_inserted_id)+"'")
                data = cur.fetchone()
                global data_dic
                data_dic = data
                print("data retrieved from getConsultantById: ", data)
                cur.close()
                # return data
                return data_dic
        except:
            print("SQL Error in getConsultantById")

    def insertFirstStepConsultantLink(self):
        try:
            print("data is: ", self.Plan, self.UserId, self.Steps, datetime.datetime.now(), datetime.datetime.now())
            with connection.cursor() as cursor:
                sql = "INSERT INTO consultant (Plan, UserId, LastStep, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql,
                               (self.Plan, self.UserId, self.Steps, datetime.datetime.now(), datetime.datetime.now()))
                connection.commit()
                cursor.close()
        finally:
            with connection.cursor() as cur:
                cur.execute("select MAX(id) from consultant where UserId = '" + str(self.UserId) + "'")
                data = cur.fetchone()
                print("last ID from insertFirstStepConsultantLink: ", data)
                global last_inserted_id
                last_inserted_id = str(data['MAX(id)'])
                self.consultantID = str(data['MAX(id)'])
                cur.close()
            return ""

    def updateFirstStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Plan = %s, LastStep=%s, updated_at=%s Where UserId = %s and Id='"+last_inserted_id+"'"
                cursor.execute(sql, (self.Plan, self.Steps, datetime.datetime.now(), self.UserId))
                connection.commit()
                print("record from plan selection page")
                cursor.close()
        finally:
            return ""

    def updateSecondStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Title = %s, LastStep=%s, updated_at=%s, JobCategory=%s, SubCategory=%s Where UserId = %s and Id='"+last_inserted_id+"' "
                cursor.execute(sql, (
                self.Title, self.Steps, datetime.datetime.now(), self.JobCategory, self.SubCategory, self.UserId))
                connection.commit()
                print("record from 1st step title job ctgry and all")
                cursor.close()
        finally:
            return ""

    def updateThirdStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Description=%s, LastStep=%s,  FileName = %s,  FileLocation = %s,  FileData = %s, updated_at=%s Where UserId = %s and Id='"+last_inserted_id+"'"
                cursor.execute(sql, (
                self.Description, self.Steps, self.FileName, self.FileLocation, self.FileData, datetime.datetime.now(),
                self.UserId))
                connection.commit()
                print("record from 2nd step descrption last step and etc")
                cursor.close()
        finally:
            return ""

    def updateFourStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set ProjectType = %s, LastStep=%s,  Describes = %s, WorkType = %s, ApiToIntegrate = %s, ProjectStage = %s, updated_at=%s Where UserId = %s and Id='"+last_inserted_id+"'"
                cursor.execute(sql, (
                self.ProjectType, self.Steps, self.Describes, self.WorkType, self.ApiToIntegrate, self.ProjectStage,
                datetime.datetime.now(), self.UserId))
                connection.commit()
                print("record from 3rd steps project type and all")
                cursor.close()
        finally:
            return ""

    def updateFiveStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set ImpSkills = %s, LastStep=%s, LookingSkills = %s, updated_at=%s  Where UserId = %s and Id='"+last_inserted_id+"'"
                cursor.execute(sql,
                               (self.ImpSkills, self.Steps, self.LookingSkills, datetime.datetime.now(), self.UserId))
                connection.commit()
                print("record from 4th looking skills and etc")
                cursor.close()
        finally:
            return ""

    def updateSixStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set JobCanSeenBy = %s, LastStep=%s, updated_at=%s Where UserId = %s and Id='"+last_inserted_id+"'"
                cursor.execute(sql, (self.JobCanSeenBy, self.Steps, datetime.datetime.now(), self.UserId))
                connection.commit()
                print("record from 5th step saved job can seen")
                cursor.close()
        except:
                print("Execption in SQL at updateSixStepConsultantLink.")
        finally:
            return ""

    def updateSevenStepConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set PayBy = %s, LastStep=%s, ProjectDuration = %s, TimeRequirement = %s, SpecificBudget = %s, Urgency = %s, updated_at=%s Where UserId = %s and Id='"+last_inserted_id+"'"
                cursor.execute(sql, (self.PayBy, self.Steps, self.ProjectDuration, self.TimeRequirement, self.SpecificBudget,
                                     self.Urgency,datetime.datetime.now(), self.UserId))
                connection.commit()
                print("record saved 6 steps Pay projct duration and all")
                cursor.close()
        except:
            print("SQL Error at updateSevenStepConsultantLink")
        finally:
            # with connection.cursor() as cur:
            #     cur.execute("select * from consultant where UserId = '" + str(self.UserId) + "'")
            #     data = cur.fetchone()
            #     global data_dic
            #     data_dic = data
            #     cur.close()
            return ""

    def updateOnReviewConsultantLink(self):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Feature = %s, LastStep=%s, updated_at=%s Where UserId = %s and Id='"+last_inserted_id+"'"
                cursor.execute(sql, (self.Feature, self.Steps, datetime.datetime.now(), self.UserId))
                connection.commit()
                print("record on 7th step Updated a featured or not")
                cursor.close()
        finally:
            return ""

    def FromSevenPostJob(self, steps, userid):
        Feature = self.Feature
        print("FromSevenPostJob Feature: ", Feature)
        print("FromSevenPostJob function")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Feature = %s, PostJob = %s, LastStep=%s, updated_at=%s Where UserId = %s  and Id='"+last_inserted_id+"'"
                cursor.execute(sql, (Feature, '1', steps, datetime.datetime.now(), userid))
                connection.commit()
                print("record Posted a Job")
                cursor.close()
        finally:
            return ""

    def FromSevenSaveExit(self, steps, userid):
        Feature = self.Feature
        print("FromSevenSaveExit Feature: ", Feature)
        print("FromSevenSaveExit function")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE consultant set Feature = %s, SaveExit = %s, LastStep=%s, updated_at=%s Where UserId = %s and Id='"+last_inserted_id+"'"
                cursor.execute(sql, (Feature, '1', steps, datetime.datetime.now(), userid))
                connection.commit()
                print("record SAVE and exit")
                cursor.close()
        finally:
            return ""

    def SaveConsultant(self, consultantID):
        consultantRecords = ConsultantClass.getConsultantById(self)
        print("from SaveConsultant steps is : ", self.Steps)
        if self.Steps == 'step1':
            if consultantID=="None":
                ConsultantClass.insertFirstStepConsultantLink(self)
                print("found None going to insert ")
            else:
                print("consultantID found "+str(consultantID)+" and now going to update")
                ConsultantClass.updateFirstStepConsultantLink(self)
            # if consultantRecords is not None:
            #     ConsultantClass.updateFirstStepConsultantLink(self)
            # else:
            #     print("for new ", self.consultantID)
            #     ConsultantClass.insertFirstStepConsultantLink(self)

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

        if self.Steps == 'step7':  # this would b run from 6 step on "next step" button
            if consultantRecords is not None:
                ConsultantClass.updateSevenStepConsultantLink(self)

        if self.Steps == 'step8':
            if consultantRecords is not None:
                ConsultantClass.updateOnReviewConsultantLink(self)

        '''if self.Steps == 'SaveExit':
            if consultantRecords is not None:
                ConsultantClass.updateOnReviewConsultantLink(self)'''


class ConsultantData:

    def getPostJobsById(uid, uname):
        with connection.cursor() as cur:
            cur.execute(
                "select Title, created_at, Description, LookingSkills, SpecificBudget from consultant where PostJob='1' and UserId='"+str(uid)+"'")
            data = cur.fetchall()
            if data:
                global data_dic
                data_dic = data
                cur.close()
                print("Consultant > getPostJobsById > data_dic: ", data_dic)
            return data

            # global data_dic
            # data_dic = data
            # cur.close()
            # print("data retrieved from getConsultantById data_dic: ", data_dic)
            # return data

    def getSavedJobsById(uid, uname):
        with connection.cursor() as cur:
            cur.execute(
                # "select c.Id, c.Plan, c.Title, u.fullname from consultant c, user u where c.SaveExit='1' and c.UserId=u.Id  ")
                "select c.Id, c.Plan, c.Title, u.fullname from consultant c, user u where c.SaveExit='1' and c.UserId='"+str(uid)+"' and c.UserId=u.Id ")
            data = cur.fetchall()
            if data:
                global data_dic
                data_dic = data
                cur.close()
                print("from consultant - getSavedJobsById / data_dic: ", data_dic)
            return data
