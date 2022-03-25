
#---------------------------------------------------------------
# This file is generated! Dont make any changes in this file.
#---------------------------------------------------------------
from .base import *
from .cached_property import cached_property



class SessionInfoHandler(BaseGetHandler):
	'''Session Infos

	Methods
	-------
		createEntry()
			Creates a new SessionInfo entry object.
	
	Inherited Methods
	-----------------
		get (BaseGetHandler)
	'''
	

	def createEntry(self):
		'''Creates a new SessionInfo entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return SessionInfo(self)
	

class SessionInfo(BaseEntry):
	'''Model with login session infos

	Attributes [writable]
	---------------------
		RootGroupId : integer
			Root group REST ID
		RootGroupName : string
			Root group name
		Rights : array from {ParamType}
			Rights
		ExpiresIn : integer
			Expires In
		SemVersion : string
			SEM Version
		SemBuildNr : string
			SEM Build Nr.
	'''

	def __init__(self, getHandler):
		BaseEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"RootGroupId" : 0,
			"RootGroupName" : "",
			"Rights" : [],
			"ExpiresIn" : 0,
			"SemVersion" : "",
			"SemBuildNr" : "",
		}
	
	@cached_property
	def RootGroupId(self):
		return self.__getattr__("RootGroupId")
	
	@cached_property
	def RootGroupName(self):
		return self.__getattr__("RootGroupName")
	
	@cached_property
	def Rights(self):
		return self.__getattr__("Rights")
	
	@cached_property
	def ExpiresIn(self):
		return self.__getattr__("ExpiresIn")
	
	@cached_property
	def SemVersion(self):
		return self.__getattr__("SemVersion")
	
	@cached_property
	def SemBuildNr(self):
		return self.__getattr__("SemBuildNr")
	

class SemInfoHandler(BaseGetHandler):
	'''System Information

	Methods
	-------
		createEntry()
			Creates a new SemInfo entry object.
	
	Inherited Methods
	-----------------
		get (BaseGetHandler)
	'''
	

	def createEntry(self):
		'''Creates a new SemInfo entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return SemInfo(self)
	

class SemInfo(BaseEntry):
	'''Info from Management Server 

	Attributes [read-only]
	----------------------
		StartTime : time
			Start Time from SEM
		LicensedManagedUnits : integer
			Licensed Managed Units
			Enum Values: 4294967295=unlimited
		UsedManagedUnits : integer
			Used Managed Units
		IsLicenseValid : boolean
			Is License Valid
		SerialNumber : string
			License Serial Number
		LicensedVersion : string
			Licensed Version
		SoftwareVersion : string
			Software Version
		BuildNr : string
			Build Nr
		CommitID : string
			Commit ID
		DBDriverVersion : string
			DB Driver Version
	'''

	def __init__(self, getHandler):
		BaseEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"StartTime" : "",
			"LicensedManagedUnits" : 0,
			"UsedManagedUnits" : 0,
			"IsLicenseValid" : False,
			"SerialNumber" : "",
			"LicensedVersion" : "",
			"SoftwareVersion" : "",
			"BuildNr" : "",
			"CommitID" : "",
			"DBDriverVersion" : "",
		}
	
	@cached_property
	def StartTime(self):
		return self.__getattr__("StartTime")
	
	@cached_property
	def LicensedManagedUnits(self):
		return self.__getattr__("LicensedManagedUnits")
	
	@cached_property
	def UsedManagedUnits(self):
		return self.__getattr__("UsedManagedUnits")
	
	@cached_property
	def IsLicenseValid(self):
		return self.__getattr__("IsLicenseValid")
	
	@cached_property
	def SerialNumber(self):
		return self.__getattr__("SerialNumber")
	
	@cached_property
	def LicensedVersion(self):
		return self.__getattr__("LicensedVersion")
	
	@cached_property
	def SoftwareVersion(self):
		return self.__getattr__("SoftwareVersion")
	
	@cached_property
	def BuildNr(self):
		return self.__getattr__("BuildNr")
	
	@cached_property
	def CommitID(self):
		return self.__getattr__("CommitID")
	
	@cached_property
	def DBDriverVersion(self):
		return self.__getattr__("DBDriverVersion")
	

class SemSettingsHandler(BaseListGetHandler, BaseListUpdateHandler):
	'''SEM System Settings

	Methods
	-------
		createEntry()
			Creates a new SemSettingEntry entry object.
	
	Inherited Methods
	-----------------
		get (BaseListGetHandler)
		list (BaseListHandler)
		update (BaseListUpdateHandler)
	'''
	

	def createEntry(self):
		'''Creates a new SemSettingEntry entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return SemSettingEntry(self)
	

class SemSettingEntry(LazyModifiableListEntry):
	'''General settings of Management Server 

	Attributes [read-only]
	----------------------
		Id : integer
			Id
		Name : string
			Name
		Type : integer
			Type
			Enum Values: 1=int, 2=str, 3=bool, 4=encstr
		GroupName : string
			Group Name
		ReadOnly : integer
			Read only

	Attributes [writable]
	---------------------
		Value : string
			Value
	'''

	def __init__(self, getHandler):
		LazyModifiableListEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Id" : 0,
			"Name" : "",
			"Type" : 0,
			"GroupName" : "",
			"Value" : "",
			"ReadOnly" : 0,
		}
	
	@cached_property
	def Id(self):
		return self.__getattr__("Id")
	
	@cached_property
	def Name(self):
		return self.__getattr__("Name")
	
	@cached_property
	def Type(self):
		return self.__getattr__("Type")
	
	@cached_property
	def GroupName(self):
		return self.__getattr__("GroupName")
	
	@cached_property
	def Value(self):
		return self.__getattr__("Value")
	
	@cached_property
	def ReadOnly(self):
		return self.__getattr__("ReadOnly")
	

class SemLicenseHandler(BaseUpdateHandler, BaseGetHandler):
	'''SEM License

	Methods
	-------
		createEntry()
			Creates a new SemLicense entry object.
	
	Inherited Methods
	-----------------
		get (BaseGetHandler)
		update (BaseUpdateHandler)
	'''
	

	def createEntry(self):
		'''Creates a new SemLicense entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return SemLicense(self)
	

class SemLicense(LazyEntry):
	'''License Setting of Management Server 

	Attributes [read-only]
	----------------------
		IsLicenseValid : boolean
			Is License Valid
		LicensedVersion : string
			Licensed Version
		LicensedManagedUnits : integer
			Licensed Managed Units
			Enum Values: 4294967295=unlimited
		LicensedServerType : integer
			Licensed Server Type
			Enum Values: 0=Primary Server, 2=Backup Server
		MultiFactorAuthLicense : boolean
			Multi-factor Authentication License
		TimeLeftTestVersion : integer
			Time Left Test Version
		SoftwareVersion : string
			Software Version
		BuildNr : string
			Build Nr

	Attributes [writable]
	---------------------
		SerialNumber : string
			Serial Number
		ActivationKey : string
			Activation Key
	'''

	def __init__(self, getHandler):
		LazyEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"SerialNumber" : "",
			"ActivationKey" : "",
			"IsLicenseValid" : False,
			"LicensedVersion" : "",
			"LicensedManagedUnits" : 0,
			"LicensedServerType" : 0,
			"MultiFactorAuthLicense" : False,
			"TimeLeftTestVersion" : 0,
			"SoftwareVersion" : "",
			"BuildNr" : "",
		}
	
	@cached_property
	def SerialNumber(self):
		return self.__getattr__("SerialNumber")
	
	@cached_property
	def ActivationKey(self):
		return self.__getattr__("ActivationKey")
	
	@cached_property
	def IsLicenseValid(self):
		return self.__getattr__("IsLicenseValid")
	
	@cached_property
	def LicensedVersion(self):
		return self.__getattr__("LicensedVersion")
	
	@cached_property
	def LicensedManagedUnits(self):
		return self.__getattr__("LicensedManagedUnits")
	
	@cached_property
	def LicensedServerType(self):
		return self.__getattr__("LicensedServerType")
	
	@cached_property
	def MultiFactorAuthLicense(self):
		return self.__getattr__("MultiFactorAuthLicense")
	
	@cached_property
	def TimeLeftTestVersion(self):
		return self.__getattr__("TimeLeftTestVersion")
	
	@cached_property
	def SoftwareVersion(self):
		return self.__getattr__("SoftwareVersion")
	
	@cached_property
	def BuildNr(self):
		return self.__getattr__("BuildNr")
	

class AdminsHandler(BaseListFindHandler, BaseListUpdateHandler, BaseListInsertHandler, BaseListDeleteHandler):
	'''Management of SEM administrators

	Methods
	-------
		createEntry()
			Creates a new Admin entry object.
	
	Inherited Methods
	-----------------
		delete (BaseListDeleteHandler)
		find (BaseListFindHandler)
		get (BaseListGetHandler)
		insert (BasListInsertHandler)
		list (BaseListHandler)
		update (BaseListUpdateHandler)
	'''
	
	def __init__(self, api, groupid):
		url = "sem-mgm/{groupid}/admins".format(**vars())
		BaseHandler.__init__(self, api, url)
		self._groupid = groupid

	def createEntry(self):
		'''Creates a new Admin entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return Admin(self, self._groupid)
	

class Admin(LazyModifiableListEntry):
	'''Parameters of SEM administror

	Attributes [read-only]
	----------------------
		LastSerialNumber : string
			Last incoming certificate serial number 
		LastLogin : time
			Last login
		LastLogout : time
			Last logout
		LoginErrors : integer
			Number of login errors
		ModifiedOn : time
			Modified on
		ModifiedBy : string
			Modified by

	Attributes [writable]
	---------------------
		Name : string
			Name
		Description : string
			Description
		Password : string
			Password
		State : integer
			State
			Enum Values: 0=denied, 1=granted, 2=locked
		AdminGroup : string or integer from {Controller}
			Administrator Group
		ForceTLS : boolean
			Force TLS connection
		ForceCert : boolean
			Force TLS with certificate
		CertificateSerialNumber : string
			Certificate serial number 
		ManagementIPAddrs : string
			Management IP addresses
	'''

	def __init__(self, getHandler, groupid):
		LazyModifiableListEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Name" : "",
			"Description" : "",
			"Password" : "",
			"State" : "granted",
			"AdminGroup" : "",
			"ForceTLS" : False,
			"ForceCert" : False,
			"CertificateSerialNumber" : "",
			"ManagementIPAddrs" : "",
			"LastSerialNumber" : "",
			"LastLogin" : "",
			"LastLogout" : "",
			"LoginErrors" : 0,
			"ModifiedOn" : "",
			"ModifiedBy" : "",
		}
	
	@cached_property
	def Name(self):
		return self.__getattr__("Name")
	
	@cached_property
	def Description(self):
		return self.__getattr__("Description")
	
	@cached_property
	def Password(self):
		return self.__getattr__("Password")
	
	@cached_property
	def State(self):
		return self.__getattr__("State")
	
	@cached_property
	def AdminGroup(self):
		return self.__getattr__("AdminGroup")
	
	@cached_property
	def ForceTLS(self):
		return self.__getattr__("ForceTLS")
	
	@cached_property
	def ForceCert(self):
		return self.__getattr__("ForceCert")
	
	@cached_property
	def CertificateSerialNumber(self):
		return self.__getattr__("CertificateSerialNumber")
	
	@cached_property
	def ManagementIPAddrs(self):
		return self.__getattr__("ManagementIPAddrs")
	
	@cached_property
	def LastSerialNumber(self):
		return self.__getattr__("LastSerialNumber")
	
	@cached_property
	def LastLogin(self):
		return self.__getattr__("LastLogin")
	
	@cached_property
	def LastLogout(self):
		return self.__getattr__("LastLogout")
	
	@cached_property
	def LoginErrors(self):
		return self.__getattr__("LoginErrors")
	
	@cached_property
	def ModifiedOn(self):
		return self.__getattr__("ModifiedOn")
	
	@cached_property
	def ModifiedBy(self):
		return self.__getattr__("ModifiedBy")
	

class AdminGroupsHandler(BaseListFindHandler):
	'''Management of administrator groups

	Methods
	-------
		createEntry()
			Creates a new AdminGroup entry object.
	
	Inherited Methods
	-----------------
		find (BaseListFindHandler)
		get (BaseListGetHandler)
		list (BaseListHandler)
	'''
	
	def __init__(self, api, groupid):
		url = "sem-mgm/{groupid}/admin-groups".format(**vars())
		BaseHandler.__init__(self, api, url)
		self._groupid = groupid

	def createEntry(self):
		'''Creates a new AdminGroup entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return AdminGroup(self, self._groupid)
	

class AdminGroup(LazyListEntry):
	'''Parameters of SEM administror group

	Attributes [read-only]
	----------------------
		ConfiguredIn : string
			Configured in
		ModifiedOn : time
			Modified on
		ModifiedBy : string
			Modified by

	Attributes [writable]
	---------------------
		Name : string
			Name
		Description : string
			Description
	'''

	def __init__(self, getHandler, groupid):
		LazyListEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Name" : "",
			"Description" : "",
			"ConfiguredIn" : "",
			"ModifiedOn" : "",
			"ModifiedBy" : "",
		}
	
	@cached_property
	def Name(self):
		return self.__getattr__("Name")
	
	@cached_property
	def Description(self):
		return self.__getattr__("Description")
	
	@cached_property
	def ConfiguredIn(self):
		return self.__getattr__("ConfiguredIn")
	
	@cached_property
	def ModifiedOn(self):
		return self.__getattr__("ModifiedOn")
	
	@cached_property
	def ModifiedBy(self):
		return self.__getattr__("ModifiedBy")
	

class SoftwareUpdateListsHandler(BaseListFindHandler):
	'''Management of software update lists

	Methods
	-------
		createEntry()
			Creates a new GetIdNameList entry object.
	
	Inherited Methods
	-----------------
		find (BaseListFindHandler)
		get (BaseListGetHandler)
		list (BaseListHandler)
	'''
	
	def __init__(self, api, groupid):
		url = "sem-mgm/sw-update-lists/{groupid}".format(**vars())
		BaseHandler.__init__(self, api, url)
		self._groupid = groupid

	def createEntry(self):
		'''Creates a new GetIdNameList entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return GetIdNameList(self, self._groupid)
	

class GetIdNameList(ListEntry):
	'''Model GetIdNameList

	Attributes [writable]
	---------------------
		Id : integer
			ID of the entry
		Name : string
			Name of the entry
	'''

	def __init__(self, getHandler, groupid):
		ListEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Id" : 0,
			"Name" : "",
		}
	
	@cached_property
	def Id(self):
		return self.__getattr__("Id")
	
	@cached_property
	def Name(self):
		return self.__getattr__("Name")
	

class StateDBReplicationHandler(BaseGetHandler):
	'''State Replication Management

	Methods
	-------
		createEntry()
			Creates a new StateDBReplication entry object.
	
	Inherited Methods
	-----------------
		get (BaseGetHandler)
	'''
	

	def createEntry(self):
		'''Creates a new StateDBReplication entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return StateDBReplication(self)
	

class StateDBReplication(BaseEntry):
	'''State Database Replication

	Attributes [read-only]
	----------------------
		State : integer
			State
			Enum Values: 0=off, 1=disconnected, 2=init, 3=update, 4=init-update, 5=work, 6=delete, 7=db-error
		ReplicatedRecords : integer
			Replicated Records
	'''

	def __init__(self, getHandler):
		BaseEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"State" : 0,
			"ReplicatedRecords" : 0,
		}
	
	@cached_property
	def State(self):
		return self.__getattr__("State")
	
	@cached_property
	def ReplicatedRecords(self):
		return self.__getattr__("ReplicatedRecords")
	

class BackupServersHandler(BaseListHandler):
	'''Backup Servers

	Methods
	-------
		createEntry()
			Creates a new BackupServerListEntry entry object.
	
	Inherited Methods
	-----------------
		list (BaseListHandler)
	'''
	

	def createEntry(self):
		'''Creates a new BackupServerListEntry entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return BackupServerListEntry(self)
	

class BackupServerListEntry(ListEntry):
	'''Parameters of a backup server

	Attributes [read-only]
	----------------------
		OnlineState : integer
			Online State
			Enum Values: 0=Offline, 1=Online
		LastReceiveTime : time
			Last receive time
		ReplState : integer
			Replication State
			Enum Values: 0=Offline, 1=Replication Accounting, 11=Replication Groups, 12=Replication Logs, 13=Replication VPN/GWs, 14=Replication RADIUS Configuration, 15=Replication RADIUS Users, 16=Replication Accounting, 17=Replication Error Counters, 18=Replication RADIUS Group Settings, 19=Replication Certificates, 20=Replication CA Certificates, 21=Replication CRLs, 22=Replication Policy Rules, 23=Replication Policy Parameters, 24=Replication RADIUS Dictionary Attributes, 25=Replication RADIUS Dictionaries, 26=Replication CMP Data, 27=Replication User Templates, 28=Replication Drafts, 29=Replication Packages, 30=Replication Package Access, 31=Replication Software Download Infos, 32=Replication Authentication Codes, 33=Replication Users, 34=Replication Scripts, 35=Replication Profiles, 36=Replication Messages to Primary, 37=Replication Package Files, 38=Replication PKCS#12 Files, 39=Replication Configuration Files, 40=Replication Client Files, 41=Replication File Configuration, 42=Replication Console Profiles, 47=Replication Licenses, 48=Replication Subscriptions, 49=Replication Client Audit Logs, 50=Up-To-Date, 60=Disconnected, 101=Error: Time different greater than one hour between Backup and Primary Server, 102=Error: Duplicate Serial Number, 103=Error: Authentication failed, 104=Error: Backup Licensed Units < Primary Licensed Units, 105=Error: Primary Version < Backup Version, 106=Error: Backup license without NCP Multi-Factor Authentication option

	Attributes [writable]
	---------------------
		Id : integer
			Id of the entry
		Name : string
			Name
		IPAddress : string
			IP Address
	'''

	def __init__(self, getHandler):
		ListEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Id" : 0,
			"Name" : "",
			"IPAddress" : "",
			"OnlineState" : 0,
			"LastReceiveTime" : "",
			"ReplState" : 0,
		}
	
	@cached_property
	def Id(self):
		return self.__getattr__("Id")
	
	@cached_property
	def Name(self):
		return self.__getattr__("Name")
	
	@cached_property
	def IPAddress(self):
		return self.__getattr__("IPAddress")
	
	@cached_property
	def OnlineState(self):
		return self.__getattr__("OnlineState")
	
	@cached_property
	def LastReceiveTime(self):
		return self.__getattr__("LastReceiveTime")
	
	@cached_property
	def ReplState(self):
		return self.__getattr__("ReplState")
	

class NotificationsHandler(BaseListHandler):
	'''Management of Notifications

	Methods
	-------
		createEntry()
			Creates a new Notification entry object.
	
	Inherited Methods
	-----------------
		list (BaseListHandler)
	'''
	
	def __init__(self, api, groupid):
		url = "sem-mgm/{groupid}/notifications".format(**vars())
		BaseHandler.__init__(self, api, url)
		self._groupid = groupid

	def createEntry(self):
		'''Creates a new Notification entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return Notification(self, self._groupid)
	

class Notification(ListEntry):
	'''Parameters of the notifications

	Attributes [read-only]
	----------------------
		Id : integer
			Id
		Priority : integer
			Priority
			Enum Values: 3=error, 1=info, 2=warning
		Subject : string
			Subject
		StartTime : time
			Start time
	'''

	def __init__(self, getHandler, groupid):
		ListEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Id" : 0,
			"Priority" : 0,
			"Subject" : "",
			"StartTime" : "",
		}
	
	@cached_property
	def Id(self):
		return self.__getattr__("Id")
	
	@cached_property
	def Priority(self):
		return self.__getattr__("Priority")
	
	@cached_property
	def Subject(self):
		return self.__getattr__("Subject")
	
	@cached_property
	def StartTime(self):
		return self.__getattr__("StartTime")
	

class SemLogsHandler(BaseListHandler):
	'''SEM Logs

	Methods
	-------
		createEntry()
			Creates a new SemLogEntry entry object.
	
	Inherited Methods
	-----------------
		list (BaseListHandler)
	'''
	
	def __init__(self, api, groupid):
		url = "sem-mgm/{groupid}/logs".format(**vars())
		BaseHandler.__init__(self, api, url)
		self._groupid = groupid

	def createEntry(self):
		'''Creates a new SemLogEntry entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return SemLogEntry(self, self._groupid)
	

class SemLogEntry(ListEntry):
	'''Parameters of a SEM log entry

	Attributes [read-only]
	----------------------
		Id : integer
			Id
		Message : string
			Message
		Time : time
			Log Time
		ErrorNr : integer
			Error number
		LogType : integer
			Log Type
		Server : string
			Server
	'''

	def __init__(self, getHandler, groupid):
		ListEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Id" : 0,
			"Message" : "",
			"Time" : "",
			"ErrorNr" : 0,
			"LogType" : 0,
			"Server" : "",
		}
	
	@cached_property
	def Id(self):
		return self.__getattr__("Id")
	
	@cached_property
	def Message(self):
		return self.__getattr__("Message")
	
	@cached_property
	def Time(self):
		return self.__getattr__("Time")
	
	@cached_property
	def ErrorNr(self):
		return self.__getattr__("ErrorNr")
	
	@cached_property
	def LogType(self):
		return self.__getattr__("LogType")
	
	@cached_property
	def Server(self):
		return self.__getattr__("Server")
	

class SemTraceLogsHandler(BaseListHandler):
	'''SEM Trace Logs

	Methods
	-------
		createEntry()
			Creates a new SemTraceLogEntry entry object.
	
	Inherited Methods
	-----------------
		list (BaseListHandler)
	'''
	

	def createEntry(self):
		'''Creates a new SemTraceLogEntry entry object.
			Call createEntry to get an empty object for insert() or update().
			createEntry is called by get()'''
		return SemTraceLogEntry(self)
	

class SemTraceLogEntry(ListEntry):
	'''Parameters of a SEM trace log entry

	Attributes [read-only]
	----------------------
		Id : integer
			Id
		Message : string
			Message
		Time : time
			Log Time
		LogType : integer
			Log Type
	'''

	def __init__(self, getHandler):
		ListEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Id" : 0,
			"Message" : "",
			"Time" : "",
			"LogType" : 0,
		}
	
	@cached_property
	def Id(self):
		return self.__getattr__("Id")
	
	@cached_property
	def Message(self):
		return self.__getattr__("Message")
	
	@cached_property
	def Time(self):
		return self.__getattr__("Time")
	
	@cached_property
	def LogType(self):
		return self.__getattr__("LogType")
	

class SemTraceLoggerUpdate(BaseEntry):
	'''Parameters for settings SEM trace loggers

	Attributes [writable]
	---------------------
		Loggers : array from model {Model}
			Loggers
	'''

	def __init__(self, getHandler):
		BaseEntry.__init__(self, getHandler)		# Default values
		self._defaultValues = {
			"Loggers" : [],
		}
	
	@cached_property
	def Loggers(self):
		return self.__getattr__("Loggers")
	
