import sys         
# sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')
sys.path.append('/home/Back-End-XenophonIT/Budgetizi-BackEnd-Server/Servers')

from ServerMain import *

#This request POST for calculate the step one of offre for totality
@app.post("/company/checkCompleteOffre")
async def checkCompleteOffre(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunction = checkCompleteOffreDB(idOffreSend,phoneNumber)

    return {
        "resutFunction" : resutFunction
    }

