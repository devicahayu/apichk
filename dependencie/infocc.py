class info: 
    ccnum = None
    expm = None
    expy = None
    cv2 = None
    brand = None
    def __init__(self):
        pass
    def checkMoth(self, mes, tipo):
        date = str()
        if len(tipo) == 2:
            if len(mes) == 2:
                date = mes
            elif len(mes) == 1:
                if mes == '1':
                    date = '01'
                elif mes == '2':
                    date = '02'
                elif mes == '3':
                    date = '03'
                elif mes == '4':
                    date = '04'
                elif mes == '5':
                    date = '05'
                elif mes == '6':
                    date = '06'
                elif mes == '7':
                    date == '07'
                elif mes == '8':
                    date = '08'
                elif mes == '9':
                    date = '09'
            return date
            
        elif len(tipo) == 1:
            if len(mes) == 1:
                date = mes
            elif len(mes) == 2:
                if mes == '01':
                    date = '1'
                elif mes == '02':
                    date = '2'
                elif mes == '03':
                    date = '3'
                elif mes == '04':
                    date = '4'
                elif mes == '05':
                    date = '5'
                elif mes == '06':
                    date = '6'
                elif mes == '07':
                    date = '7'
                elif mes == '08':
                    date = '8'
                elif mes == '09':
                    date = '9'
                elif mes == '10':
                    date = '10'
                elif mes == '11':
                    date = '11'
                elif mes == '12':
                    date = '12'
            return date
        else:
            return False
    def checkYear(self,year, tipo):
        date = str()
        if len(tipo) == 2:
            if len(year) == 2:
                date = year
            elif len(year) == 4:
                date = year[2:]
            return date
        elif len(tipo) == 4:
            if len(year) == 4:
                date = year
            elif len(year) == 2:
                date = '20'+year
            return date
        else:
            return False
    def info(self,cc,tipo):
        ccnew = cc.replace(' ','')
        linecc = ccnew.split('|')
        tipoFormat = tipo.split(' ')
        mesTipo  = tipoFormat[0]
        yearTipo = tipoFormat[1]
        
        visa = 'visa'
        mc = 'mc'
        amex = 'amex'
        discovery = 'discovery'
        if len(linecc) == 4:
            # bloque 1 cc
            if len(linecc[0]) >= 15 and  len(linecc[0]) <= 16:
                if len(linecc[0]) == 15:
                    self.ccnum = linecc[0]
                    self.brand = amex
                elif len(linecc[0]) == 16:
                    cc = linecc[0]
                    if  cc[0:1] == '4':
                        self.ccnum = linecc[0]
                        self.brand = visa
                    elif cc[0:1] == '5':
                        self.ccnum = linecc[0]
                        self.brand = mc
                    elif cc[0:1] == '6':
                        self.ccnum = linecc[0]
                        self.brand = discovery
                    else:
                        return False
            else:
                return False
            #bloque 2 mes
            if len(linecc[1]) >= 1 and len(linecc[1]) <= 2:
                valuemont = self.checkMoth(linecc[1],'x')
                valuemont = int(valuemont)
                if valuemont >= 1 and valuemont <= 12:
                    self.expm = self.checkMoth(linecc[1],mesTipo)
                else:
                    return False
            else:
                return False
            #bloque 3 año
            if len(linecc[2]) == 2 or len(linecc[2]) == 4:
                yearx = int(self.checkYear(linecc[2],'xxxx'))
                if yearx >= 2020 and yearx <= 2030:
                    self.expy = self.checkYear(linecc[2],yearTipo)
                else:
                    return False 
            #bloque 4 cv2
            if  len(linecc[3]) == 3 or len(linecc[3]) == 4:
                if not (self.brand == 'amex') and len(linecc[3]) == 3:
                    self.cv2 = linecc[3]
                else:
                    if self.brand == 'amex' and len(linecc[3]) == 4:
                        self.cv2 = linecc[3]
                    else:
                        return False
        else:
            return False
