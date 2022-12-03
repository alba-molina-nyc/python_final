import holidays

north_america = holidays.CA() + holidays.US() + holidays.MX()
south_america = holidays.AR() + holidays.BO() + holidays.BR() + holidays.CL() + holidays.CO() + holidays.PY() + holidays.PE() + holidays.UY() + holidays.VE()
northern_europe = holidays.DK() + holidays.EE() + holidays.FI() + holidays.IS() + holidays.IE() + holidays.LV() + holidays.LT() + holidays.NO() + holidays.SE() + holidays.GB()
eastern_europe = holidays.BG() + holidays.HU() + holidays.MD() + holidays.PL() + holidays.RO() + holidays.RU() + holidays.SK() + holidays.UA()
southern_europe = holidays.BA() + holidays.HR() + holidays.CY() + holidays.GR() + holidays.IT() + holidays.MT() + holidays.MK() + holidays.PT() + holidays.RS() + holidays.SI() + holidays.ES() + holidays.TR() 
western_europe = holidays.AT() + holidays.BE() + holidays.FR() + holidays.DE() + holidays.LI() + holidays.LU() + holidays.NL()
europe = southern_europe + northern_europe + eastern_europe + western_europe




print('europe: ', europe)







# print('--------------')
# print('southern_europe: ', southern_europe)
# print('--------------')
# print('eastern_europe: ', eastern_europe)
# print('--------------')
# print('northern_europe: ', northern_europe)
# print('--------------')
# print('south_america: ', south_america)
# print('--------------')
# print('north_america: ', north_america)


# holidays.HolidayBase(years=[], expand=True, observed=True, prov=None, state=None)