#Search for:
import uiScriptLocale

#Add below:
import os
from _winreg import *


#Search for:
ime.AddExceptKey(93)

#Add below:
self.CheckAccount()


#Search for:
self.loginExitButton		= GetObject("LoginExitButton")

Add below:
self.saveAccount1Button		= GetObject("SaveAccount1Button")
self.loadAccount1Button		= GetObject("LoadAccount1Button")
self.account1Text			= self.GetChild("NameAccount1")
self.saveAccount2Button		= GetObject("SaveAccount2Button")
self.loadAccount2Button		= GetObject("LoadAccount2Button")
self.account2Text			= self.GetChild("NameAccount2")
self.saveAccount3Button		= GetObject("SaveAccount3Button")
self.loadAccount3Button		= GetObject("LoadAccount3Button")
self.account3Text			= self.GetChild("NameAccount3")
self.saveAccount4Button		= GetObject("SaveAccount4Button")
self.loadAccount4Button		= GetObject("LoadAccount4Button")
self.account4Text			= self.GetChild("NameAccount4")
self.saveAccount5Button		= GetObject("SaveAccount5Button")
self.loadAccount5Button		= GetObject("LoadAccount5Button")
self.account5Text			= self.GetChild("NameAccount5")
self.saveAccount6Button		= GetObject("SaveAccount6Button")
self.loadAccount6Button		= GetObject("LoadAccount6Button")
self.account6Text			= self.GetChild("NameAccount6")


#Search for:
self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))

#Add below:
self.saveAccount1Button.SetEvent(ui.__mem_func__(self.__OnClickSaveAccount1Button))
self.loadAccount1Button.SetEvent(ui.__mem_func__(self.__OnClickLoadAccount1Button))
self.saveAccount2Button.SetEvent(ui.__mem_func__(self.__OnClickSaveAccount2Button))
self.loadAccount2Button.SetEvent(ui.__mem_func__(self.__OnClickLoadAccount2Button))
self.saveAccount3Button.SetEvent(ui.__mem_func__(self.__OnClickSaveAccount3Button))
self.loadAccount3Button.SetEvent(ui.__mem_func__(self.__OnClickLoadAccount3Button))
self.saveAccount4Button.SetEvent(ui.__mem_func__(self.__OnClickSaveAccount4Button))
self.loadAccount4Button.SetEvent(ui.__mem_func__(self.__OnClickLoadAccount4Button))
self.saveAccount5Button.SetEvent(ui.__mem_func__(self.__OnClickSaveAccount5Button))
self.loadAccount5Button.SetEvent(ui.__mem_func__(self.__OnClickLoadAccount5Button))
self.saveAccount6Button.SetEvent(ui.__mem_func__(self.__OnClickSaveAccount6Button))
self.loadAccount6Button.SetEvent(ui.__mem_func__(self.__OnClickLoadAccount6Button))


#Search for:
self.stream.popupWindow.Open(localeInfo.LOGIN_FAILURE_SAMELOGIN, 0, localeInfo.UI_OK)

#Add below:
	def EDENWORK_ENCRYPT(self,data):
		Data = ''
		for l in data:
			Data = Data+str(int(ord(l) + 33) * 15 * 4)+' '
		return Data

	def EDENWORK_DECRYPT(self,data):
		Data = ''
		data = data.split()
		for l in data:
			Data = Data+chr((int(l) / 15 / 4) - 33)
		return Data

	def SaveAccountChoose(self, choose):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()
		idchoose = "account"+str(choose)+"id"
		pwdchoose = "account"+str(choose)+"pwd"
		if not os.path.exists("SOFTWARE\EDENWORK\Accounts"):
			key = CreateKey(HKEY_CURRENT_USER,"SOFTWARE\EDENWORK\Accounts")
		SetValueEx(key, idchoose, 0, REG_SZ, self.EDENWORK_ENCRYPT(id))
		SetValueEx(key, pwdchoose, 0, REG_SZ, self.EDENWORK_ENCRYPT(pwd))
		CloseKey(key)
		self.PopupNotifyMessage("Data saved!",self.SetIDEditLineFocus)
		self.CheckAccount()

	def LoadAccountChoose(self, choose):
		try:
			idchoose = "account"+str(choose)+"id"
			pwdchoose = "account"+str(choose)+"pwd"
			key = OpenKey(HKEY_CURRENT_USER, "SOFTWARE\EDENWORK\Accounts", 0, KEY_ALL_ACCESS)
			accountloadid = self.EDENWORK_DECRYPT(QueryValueEx(key,idchoose)[0])
			accountloadpwd = self.EDENWORK_DECRYPT(QueryValueEx(key,pwdchoose)[0])
			self.idEditLine.SetText(str(accountloadid))
			self.pwdEditLine.SetText(str(accountloadpwd))
			CloseKey(key)
		except:
			self.PopupNotifyMessage("No data saved!",self.SetIDEditLineFocus)
		self.CheckAccount()

	def CheckAccount(self):
		key = OpenKey(HKEY_CURRENT_USER, "SOFTWARE\EDENWORK\Accounts", 0, KEY_ALL_ACCESS)
		try:
			self.account1Text.SetText(str(self.EDENWORK_DECRYPT(QueryValueEx(key,"account1id")[0])))
		except:
			self.account1Text.SetText("Not saved!")
		try:
			self.account2Text.SetText(str(self.EDENWORK_DECRYPT(QueryValueEx(key,"account2id")[0])))
		except:
			self.account2Text.SetText("Not saved!")
		try:
			self.account3Text.SetText(str(self.EDENWORK_DECRYPT(QueryValueEx(key,"account3id")[0])))
		except:
			self.account3Text.SetText("Not saved!")
		try:
			self.account4Text.SetText(str(self.EDENWORK_DECRYPT(QueryValueEx(key,"account4id")[0])))
		except:
			self.account4Text.SetText("Not saved!")
		try:
			self.account5Text.SetText(str(self.EDENWORK_DECRYPT(QueryValueEx(key,"account5id")[0])))
		except:
			self.account5Text.SetText("Not saved!")
		try:
			self.account6Text.SetText(str(self.EDENWORK_DECRYPT(QueryValueEx(key,"account6id")[0])))
		except:
			self.account6Text.SetText("Not saved!")

	#####     ACCOUNT1     #####
	def __OnClickSaveAccount1Button(self):
		self.SaveAccountChoose(1)

	def __OnClickLoadAccount1Button(self):
		self.LoadAccountChoose(1)

	#####     ACCOUNT2     #####
	def __OnClickSaveAccount2Button(self):
		self.SaveAccountChoose(2)

	def __OnClickLoadAccount2Button(self):
		self.LoadAccountChoose(2)

	#####     ACCOUNT3     #####
	def __OnClickSaveAccount3Button(self):
		self.SaveAccountChoose(3)

	def __OnClickLoadAccount3Button(self):
		self.LoadAccountChoose(3)

	#####     ACCOUNT4     #####
	def __OnClickSaveAccount4Button(self):
		self.SaveAccountChoose(4)

	def __OnClickLoadAccount4Button(self):
		self.LoadAccountChoose(4)

	#####     ACCOUNT5     #####
	def __OnClickSaveAccount5Button(self):
		self.SaveAccountChoose(5)

	def __OnClickLoadAccount5Button(self):
		self.LoadAccountChoose(5)

	#####     ACCOUNT6     #####
	def __OnClickSaveAccount6Button(self):
		self.SaveAccountChoose(6)

	def __OnClickLoadAccount6Button(self):
		self.LoadAccountChoose(6)