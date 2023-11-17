from .db.dao import PaisDao, MunicipioDao, FuerzaDao , PuntosIDao, UsuarioDao
from .api.apisService import getAllPaisesApi, getAllMunicipiosApi, getAllFuerzaApi, getAllPuntosIApi, verifyUserApi

def getAllPaisesUC():
    PaisDao.deleteAll()
    PaisDao.insert(getAllPaisesApi())
    pass

def getAllMunicipiosUC():
    MunicipioDao.deleteAll()
    MunicipioDao.insert(getAllMunicipiosApi())

def getAllFuerzaUC():
    FuerzaDao.deleteAll()
    FuerzaDao.insert(getAllFuerzaApi())

def getAllPuntosIUC():
    PuntosIDao.deleteAll()
    PuntosIDao.insert(getAllPuntosIApi())

def verifyUser(datos):
    user = verifyUserApi(datos)

    if user.password == "ok":
        user.password = datos.password
        UsuarioDao.update(user)
        return True
    else:
        return False
    
def updateUser():
    userI = UsuarioDao.getById(1)
    user = verifyUserApi(userI)

    if user.password == "ok":
        return True
    else:
        return False