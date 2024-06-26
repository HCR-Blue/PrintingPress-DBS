

with sqlite3.connect("DataBaseDir/PressDb.db") as db:
	cur = db.cursor()
	cur.execute("""
	CREATE TABLE IF NOT EXISTS EmployeeTable(
	ETID INTEGER PRIMARY KEY AUTOINCREMENT,
	ENAME TEXT NOT NULL,
	EFNAME TEXT NOT NULL,
	EPHONENO INTEGER NOT NULL,
	EEMAIL TEXT NOT NULL,
	EADDRESS TEXT NOT NULL,
	EIDCARDNO INTEGER NOT NULL,
	EGENDER TEXT NOT NULL,
	EPOSITION TEXT NOT NULL,
	EEDUCATION TEXT NOT NULL,
	EJOINDATE DATE,
	EENDDATE DATE,
	EACTIVETIME TEXT NOT NULL,
	ESALARY INTEGER NOT NULL);
	""")


	cur.execute("""
	CREATE TABLE IF NOT EXISTS CustomerTable(
	CMRTID INTEGER PRIMARY KEY AUTOINCREMENT,
	CMRNAME TEXT NOT NULL,
	CMRWIDTH INTEGER NOT NULL,
	CMRQUNTITY INTEGER NOT NULL,
	CMRMATERIALTYPE TEXT NOT NULL,
	CMRTEXT TEXT NOT NULL,
	CMRNOTE TEXT NOT NULL);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS LaserTable(
	OTID INTEGER PRIMARY KEY AUTOINCREMENT,
	OLENGTH INTEGER NOT NULL,
	OWIDTH INTEGER NOT NULL,
	OQUNTITY INTEGER NOT NULL,
	OMATERIALTYPE TEXT NOT NULL,
	OTEXT TEXT NOT NULL,
	OCURRENTTIME DATE,
	OFINISHTIME DATE,
	OPRICE INTEGER NOT NULL,
	OPREPAY INTEGER NOT NULL,
	OCUSTOMERNAME TEXT NOT NULL,
	OCUSTOMERPHONE INTEGER NOT NULL,
	OCUSTADDRESS TEXT NOT NULL,
	ODELIVERYPRICE INTEGER NOT NULL,
	ONOTE TEXT NOT NULL);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS DititalTable(
	DTID INTEGER PRIMARY KEY AUTOINCREMENT,
	DLENGTH INTEGER NOT NULL,
	DWIDTH INTEGER NOT NULL,
	DQUNTITY INTEGER NOT NULL,
	DMATERIALTYPE TEXT NOT NULL,
	DTEXT TEXT NOT NULL,
	DCURRENTTIME DATE,
	DFINISHTIME DATE,
	DPRICE INTEGER NOT NULL,
	DPREPAY INTEGER NOT NULL,
	DCUSTOMERNAME TEXT NOT NULL,
	DCUSTOMERPHONE INTEGER NOT NULL,
	DCUSTADDRESS TEXT NOT NULL,
	DDELIVERYPRICE INTEGER NOT NULL,
	DNOTE TEXT NOT NULL);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS PlaterTable(
	PLTTID INTEGER PRIMARY KEY AUTOINCREMENT,
	PLTSIZE TEXT NOT NULL,
	PLTQUNTITY INTEGER NOT NULL,
	PLTTEXT TEXT NOT NULL,
	PLTNOTE TEXT NOT NULL,
	PLTDATE DATE);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS BoojiTable(
	BJTTID INTEGER PRIMARY KEY AUTOINCREMENT,
	BJTSIZE TEXT NOT NULL,
	BJTQUNTITY INTEGER NOT NULL,
	BJTCOLOR TEXT NOT NULL,
	BJTTEXT TEXT NOT NULL,
	BJTDATE DATE);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS PlasticTable(
	PSTTID INTEGER PRIMARY KEY AUTOINCREMENT,
	PSTSIZE TEXT NOT NULL,
	PSTQUNTITY INTEGER NOT NULL,
	PSTCOLOR TEXT NOT NULL,
	PSTTEXT TEXT NOT NULL,
	PSTDATE DATE);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS PenTable(
	PENTID INTEGER PRIMARY KEY AUTOINCREMENT,
	PENSIZE TEXT NOT NULL,
	PENQUNTITY INTEGER NOT NULL,
	PENCOLOR TEXT NOT NULL,
	PENTEXT TEXT NOT NULL,
	PENDATE DATE);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS PlateTable(
	PLATETID INTEGER PRIMARY KEY AUTOINCREMENT,
	PLATEQUNTITY INTEGER NOT NULL,
	PLATECOLOR TEXT NOT NULL,
	PLATETEXT TEXT NOT NULL,
	PLATEDATE DATE);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS FlagTable(
	FLGTID INTEGER PRIMARY KEY AUTOINCREMENT,
	FLGSIZE TEXT NOT NULL,
	FLGQUNTITY INTEGER NOT NULL,
	FLGCOLOR TEXT NOT NULL,
	FLGTEXT TEXT NOT NULL,
	FLGDATE DATE);
	""")

	cur.execute("""
	CREATE TABLE IF NOT EXISTS ClothTable(
	CLTTID INTEGER PRIMARY KEY AUTOINCREMENT,
	CLTSIZE TEXT NOT NULL,
	CLTQUNTITY INTEGER NOT NULL,
	CLTCOLOR TEXT NOT NULL,
	CLTTEXT TEXT NOT NULL,
	CLTDATE DATE);
	""")



	cur.execute("""
	CREATE TABLE IF NOT EXISTS FinanceTable(
	FTID INTEGER PRIMARY KEY AUTOINCREMENT,
	FAPARTRENT INTEGER NOT NULL,
	FELECBILL INTEGER NOT NULL,
	FTAX INTEGER NOT NULL,
	FEMPSALARY INTEGER NOT NULL,
	FINGREDIENTS INTEGER NOT NULL,
	FMARKETPRICE INTEGER NOT NULL,
	FPREMATERPRICE INTEGER NOT NULL);
	""")