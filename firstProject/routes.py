from pydantic import BaseModel


class Router(BaseModel):
    Home: str = '/'
    About: str = '/about'


router = Router()
